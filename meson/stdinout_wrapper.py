#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType, REMAINDER
import subprocess

if __name__ == '__main__':
	parser = ArgumentParser(description='Redirect I/O streams from/to the given files')
	parser.add_argument('--input', type=FileType('rb'), help='Pipe this file to STDIN')
	parser.add_argument('--output', type=FileType('w', encoding='utf-8'), help='Pipe STDOUT to this file')
	parser.add_argument('executable', help='Executable to run')
	parser.add_argument('args', nargs=REMAINDER, help='Arguments')

	args = parser.parse_args()

	subprocess.run([args.executable] + args.args, input=args.input.read(), stdout=args.output, check=True)
