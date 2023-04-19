#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType
from pathlib import Path
from io import TextIOWrapper

if __name__ == '__main__':
	parser = ArgumentParser(description='Create a section Doxyfile')
	parser.add_argument('--sections', nargs='+', required=True, help='Doxyfile template')
	parser.add_argument('--include', type=Path, help='Add this folder to the include path')
	parser.add_argument('--output', type=FileType('w', encoding='utf-8'), required=True, help='Write to this file')
	parser.add_argument('files', nargs='+', type=Path, help='Inputs to the Doxyfile')
	args = parser.parse_args()

	f: TextIOWrapper = args.output

	inputs = ' '.join([f.as_posix() for f in args.files])
	include: str | None = args.include
	sections = ' '.join(args.sections)

	f.write(f'INPUT += {inputs}\n')
	if include is not None:
		args.output.write(f'INCLUDE_PATH += {include.as_posix()}\n')
	f.write(f'ENABLED_SECTIONS += {sections}\n')
