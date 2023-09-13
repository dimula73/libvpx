#!/usr/bin/env python3

# SPDX-FileNotice: This file is based on the FFmpeg Meson build version
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType
from pathlib import Path
import re
from warnings import warn

try:
	from hashlib import file_digest
except ImportError:
	import hashlib
	from io import BufferedReader
	def file_digest(f: BufferedReader, algorithm: str):
		return hashlib.new(algorithm, f.read())

if __name__ == '__main__':
	parser = ArgumentParser(description='Validate a list of files')
	parser.add_argument('manifest', type=FileType('r', encoding='utf-8'), help='Path to the SHA-1 hash manifest')

	args = parser.parse_args()

	sha_map = {}

	for line in args.manifest:
		if option := re.match(r'([a-fA-F0-9]+)\s+\*?(.+)', line.strip()):
			sha_map[option.group(1)] = option.group(2)

	print('Checking test data:\n')
	for file, hash in sha_map.items():
		with Path(file) as f:
			if not f.exists():
				warn(f'{f} does not exist, skipping...')
				continue
			digest = file_digest(f.open('rb'), 'sha1').hexdigest()
			if digest != hash:
				raise ValueError(f'Hash mismatch for {f}: expected {hash}, got {hash}')
			else:
				print(f'{f}: OK\n')

	print('Test data OK\n')
