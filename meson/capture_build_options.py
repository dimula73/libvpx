#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
import re
import os

if __name__ == '__main__':
	with open(f'{os.environ["MESON_BUILD_ROOT"]}/meson-logs/meson-log.txt', encoding="utf-8", mode='r') as f:
		lines = [line for line in f if 'Build Options' in line]

		options = re.match(r'Build Options:\s+(.+)$', lines[-1])

		if options is not None:
			print(options.group(1))

