#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
import re
from warnings import warn

def parse_options(lines: list[str]) -> dict:
	current_options: dict = {}
	boolean_regexp = r'--(enable|disable)-([^\s]+)\s+(.+)'
	combo_regexp = r'^--([a-z0-9_\-]+)=\{?([A-Za-z]+\|[A-Za-z|]+)\}?\s+(.+)$'
	stock_regexp = r'^--([a-z0-9_\-]+)(?:=[A-Za-z]+)?\s+(.+)$'
	codec_regexp = r'^([a-z0-9_\-]+):\s+(encoder|decoder)(?:\s+)?(encoder|decoder)?$'

	for line in lines:
		line = line.strip()
		option = re.match(boolean_regexp, line)
		if option:
			current_options[option.group(2).lower().replace('-', '_')] = {
				'type': 'boolean',
				'value': 'enabled' if option.group(1) == 'disable' else 'unset',
				'description': option.group(3).strip()
			}
			continue
		option = re.match(combo_regexp, line)
		if option:
			current_options[option.group(1).lower().replace('-', '_')] = {
				'type': 'combo',
				'choices': option.group(2).split('|'),
				'description': option.group(3)
			}
			continue
		option = re.match(codec_regexp, line)
		if option:
			feature = option.group(2).strip()
			current_options[f'{option.group(1)}_{feature}'.lower().replace('-', '_')] = {
				'type': 'boolean',
				'value': 'enabled' if option.group(1) == 'disable' else 'unset',
				'description': f'Enable the {option.group(1).upper()} {feature} only'
			}
			if option.group(3):
				additional_feature = option.group(3).strip()
				current_options[f'{option.group(1)}_{additional_feature}'.lower().replace('-', '_')] = {
					'type': 'boolean',
					'value': 'enabled' if option.group(1) == 'disable' else 'unset',
					'description': f'Enable the {option.group(1).upper()} {additional_feature} only'
				}
				current_options[f'{option.group(1)}'.lower().replace('-', '_')] = {
					'type': 'boolean',
					'value': 'enabled' if option.group(1) == 'disable' else 'unset',
					'description': f'Enable the {option.group(1).upper()} codec'
				}
			else:
				current_options[f'{option.group(1)}'.lower().replace('-', '_')] = {
					'type': 'boolean',
					'value': 'enabled' if option.group(1) == 'disable' else 'unset',
					'description': f'Enable the {option.group(1).upper()} {feature}'
				}
			continue
		option = re.match(stock_regexp, line)
		if option:
			current_options[option.group(1).lower().replace('-', '_')] = {
				'type': 'string',
				'description': option.group(2)
			}
		elif line.startswith('--') and not re.match(r'.+\<[a-z]+\>.*', line):
			warn(f"Unhandled option: {line}, did you apply meson/patch-configure.diff?", FutureWarning)

	return current_options

MESON_HANDLED_OPTIONS = [
	'help',
	'log',
	'target',
	'extra_cflags',
	'extra_cxxflags',
	'extra_warnings',
	'werror',
	'optimizations',
	'pic',
	'ccache',
	'debug',
	'gcov',
	'dependency_tracking',
	'libc',
	'as',
	'shared',
	'static',
	'small',
	'static_msvcrt',
	'debug_libs',
	'install_srcs',
]

def filter_meson_handled_options(pair) -> bool:
	k, _v = pair
	return k not in MESON_HANDLED_OPTIONS

def update_meson_options(options: dict):
	has_generated = False
	lines = []
	with open('meson_options.txt', 'r', encoding='utf-8') as meson_file:
		opening = '#### --- GENERATED EXTERN OPTIONS --- ####\n'
		closing = opening.replace('GENERATED', 'END GENERATED')
		for l in meson_file.readlines():
			if l == opening:
				has_generated = True
				lines.append(l)
				for key, kv in options.items():
					if kv['type'] == 'combo':
						choices = ', '.join([f"'{i}'" for i in kv['choices']])
						lines.append(f"option('{key}', type: 'combo', choices: [{choices}], description: '{kv['description']}')\n")
					elif kv['type'] == 'boolean':
						if kv['value'] != 'unset':
							value = f"value: '{kv['value']}', "
						else:
							value = ''
						lines.append(f"option('{key}', type: 'feature', {value}description: '{kv['description']}')\n")
					else:
						if kv.get('value') and len(kv['value']) != 0:
							value = f"value: '{kv['value']}', "
						else:
							value = ''
						lines.append(f"option('{key}', type: 'string', {value}description: '{kv['description']}')\n")
			elif l == closing:
				lines.append(l)
				has_generated = False
			elif not has_generated:
				lines.append(l)

	with open('meson_options.txt', 'w') as meson_file:
		meson_file.write(''.join(lines))

def update_meson_build(options: dict):
	has_generated = False
	lines = []
	booleans = [i for i in options.keys() if options.get(i)['type'] == 'boolean']
	with open('meson.build', 'r', encoding='utf-8') as meson_file:
		opening = '#### --- GENERATED EXTERN OPTIONS --- ####\n'
		closing = opening.replace('GENERATED', 'END GENERATED')
		for l in meson_file.readlines():
			if l == opening:
				has_generated = True
				lines.append(l)
				lines.append('IGNORE_MESON_BUILTINS = [\n')
				for i in MESON_HANDLED_OPTIONS:
					lines.append(f"\t'{i}',\n")
				lines.append(']\n')
				lines.append('\n')
				lines.append('MESON_OPTIONS = [\n')
				for i in booleans:
					lines.append(f"\t'{i}',\n")
				lines.append(']\n')
			elif l == closing:
				lines.append(l)
				has_generated = False
			elif not has_generated:
				lines.append(l)

	with open('meson.build', 'w') as meson_file:
		meson_file.write(''.join(lines))

if __name__=='__main__':
	# ./configure --help > tmp_meson_options.txt
	with open('tmp_meson_options.txt', 'r', encoding='utf-8') as f:
		options = parse_options(f.readlines())
		options = dict(filter(filter_meson_handled_options, options.items()))
		update_meson_options(options)
		update_meson_build(options)
