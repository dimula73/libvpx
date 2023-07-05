#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2013 The WebM Authors
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

import re
import sys
import thumb

if __name__ == '__main__':
    print('; This file was created from a .asm file')
    print('; using the ads2armasm_ms.py script.')

    f = sys.stdin.readlines()
    for line in f:
        # Python edit to make sure we don't duplicate newlines
        l = line.rstrip()

        l = l.replace(r'REQUIRE8', 'r') \
            .replace(r'PRESERVE8', r'')
        l = re.sub(r'^\s*ARM\s*$', r'', l)

        l = re.sub(r'AREA\s+\|\|(.*)\|\|', r'AREA |\1|', l)
        l = l.replace(r'qsubaddx', r'qsax')
        l = l.replace(r'qaddsubx', r'qasx')

        l = thumb.FixThumbInstructions(l)

        l = l.replace(r'ldrneb', r'ldrbne') \
            .replace(r'ldrneh', r'ldrhne')
        l = re.sub(r'^(\s*)ENDP.*', r'\g<0>\n\1ALIGN 4', l)

        print(l)
