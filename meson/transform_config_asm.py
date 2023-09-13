#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser
from pathlib import Path
import re

def parse_all_options(lines: list[str]) -> dict[str, str]:
	options = {}
	for line in lines:
		if option := re.match(r'#define\s+(VPX_ARCH|HAVE|CONFIG)(_[A-Z0-9_]+)\s+([01])', line):
			options[f'{option.group(1)}{option.group(2)}'] = option.group(3)
	return options

def create_config_asm_file(options: dict[str, str], output: Path, format='yasm'):
	with open(output, 'w', encoding='utf-8') as f:
		if format == 'yasm':
			lines = [f'{k} equ {v}\n' for k, v in options.items()]
		elif format == 'ads':
			lines = [f'{k} EQU {v}\n' for k, v in options.items()]
			lines += ['END\n']
		else:
			lines = [f'{k} .equ {v}\n' for k, v in options.items()]
		f.writelines(lines)

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('input', type=Path, help='Path to configuration header')
	parser.add_argument('--format', choices=['yasm', 'ads', 'gas'], default='ads', help='Format of the assembly file')
	parser.add_argument('output', type=Path, help='Path to config.asm')
	args = parser.parse_args()
	with open(args.input, 'r', encoding='utf-8') as f:
		options = parse_all_options(f.readlines())
		create_config_asm_file(options, args.output, format=args.format)
