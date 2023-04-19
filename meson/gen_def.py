#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType, REMAINDER
from io import TextIOWrapper
import re
from sys import stdout

SYMBOL = r'^(text|data)\s+(.+)$'
COMMENT = r'^#(.+)'

# Unlike the stock generator script, this one does not accept 'name'
# as that tells LINK.EXE to change the library export file name.
def collate_windows_exports(files: list[TextIOWrapper], needs_underscore: bool) -> list[str]:
	lines = ['EXPORTS']
	underscore = '_' if needs_underscore else ''

	for file in files:
		for symbol in file.readlines():
			symbol = symbol.strip()
			option = re.match(SYMBOL, symbol)
			if option:
				suffix = '\tDATA' if option.group(1) == 'data' else ''
				lines.append(f"\t{underscore}{option.group(2)}{suffix}")
			elif re.match(COMMENT, symbol):
				continue
			else:
				raise RuntimeError(f'Unknown line: {symbol}')

	return lines

def collate_linux_ver(files: list[TextIOWrapper], needs_underscore: bool) -> list[str]:
	lines = ['{ global:']
	underscore = '_' if needs_underscore else ''

	for file in files:
		for symbol in file.readlines():
			symbol = symbol.strip()
			option = re.match(SYMBOL, symbol)
			if option:
				lines.append(f"{underscore}{option.group(2)};")
			elif re.match(COMMENT, symbol):
				continue
			else:
				raise RuntimeError(f'Unknown line: {symbol}')

	lines += ['local: *; };']

	return lines

def collate_macos_sym(files: list[TextIOWrapper], needs_underscore: bool) -> list[str]:
	lines = []
	underscore = '_' if needs_underscore else ''

	for file in files:
		for symbol in file.readlines():
			symbol = symbol.strip()
			option = re.match(SYMBOL, symbol)
			if option:
				lines.append(f"{underscore}{option.group(2)}")
			elif re.match(COMMENT, symbol):
				continue
			else:
				raise RuntimeError(f'Unknown line: {symbol}')

	return lines

def collate_exports(files: list[TextIOWrapper], format='win', needs_underscore=False) -> list[str]:
	if format == 'mac':
		return collate_macos_sym(files, needs_underscore)
	elif format == 'linux':
		return collate_linux_ver(files, needs_underscore)
	else:
		return collate_windows_exports(files, needs_underscore)

if __name__ == '__main__':
	parser = ArgumentParser(description='''
		This script generates a module definition file containing a list of symbols
		to export from a library. Source files are technically bash scripts (and thus may
		use #comment syntax) but in general, take the form of a list of symbols:

		  <kind> symbol1 [symbol2, symbol3, ...]

		where <kind> is either 'text' or 'data'
		''')
	parser.add_argument('--out', type=FileType('w', encoding='utf-8'), default=stdout, help='Write output to a file')
	parser.add_argument('--name', type=str, help='Name of the library (required)')
	parser.add_argument('--format', type=str, choices=['win', 'mac', 'linux'], default='win', help='Format of the module definition file')
	parser.add_argument('--underscore', action='store_true', help='The symbols need an underscore for exporting')
	parser.add_argument('files', nargs=REMAINDER, type=FileType('r', encoding='utf-8'))
	args = parser.parse_args()

	lines = collate_exports(args.files, format=args.format, needs_underscore=args.underscore)

	for line in lines:
		args.out.write(line)
		args.out.write('\n')
