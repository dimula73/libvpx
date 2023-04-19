#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType
from io import StringIO
from pathlib import Path
import os

def with_trailing(p: Path) -> str:
	return f"{p.as_posix()}{'/' if p.is_dir() else ''}"

if __name__ == '__main__':
	parser = ArgumentParser(description='Create a Doxyfile for the whole project')
	parser.add_argument('--prelude', nargs='+', type=Path, help='Templates that will be copied to the file')
	parser.add_argument('--strip', nargs='+', type=Path, help='Make paths inside this directory relative')
	parser.add_argument('--example-path', nargs='+', type=Path, help='Directory that contains example code fragments')
	parser.add_argument('--output', type=FileType('w', encoding='utf-8'), required=True, help='Write to this file')
	parser.add_argument('inputs', nargs='+', type=Path, help='Inputs for the Doxygen documentation')
	args = parser.parse_args()

	f = StringIO()

	files: list[Path] = args.prelude

	for file in files:
		with file.open(encoding='utf-8') as input:
			f.write(input.read())
	f.write('# MESON override OUTPUT_DIR\n')
	f.write('OUTPUT_DIRECTORY       = \n')
	if args.strip is not None:
		paths_to_strip: str = ' '.join([f.as_posix() for f in args.strip])
		f.write(f'STRIP_FROM_PATH += {paths_to_strip}\n')
	if len(args.inputs) > 0:
		inputs = ' '.join([f.as_posix() for f in args.inputs])
		f.write(f'INPUT += {inputs}\n')
	if len(args.example_path) > 0:
		example_paths = ' '.join(map(with_trailing, args.example_path))
		f.write(f'EXAMPLE_PATH += {example_paths}\n')

	with args.output as output:
		output.write(f.getvalue())
