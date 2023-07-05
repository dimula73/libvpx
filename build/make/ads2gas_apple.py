#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2013 The WebM Authors
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
import re
import sys

if __name__ == '__main__':
    parser = ArgumentParser(description='Convert ARM Developer Suite 1.0.1 syntax assembly source to GNU as format')

    parser.parse_args()

    print('@ This file was created from a .asm file')
    print('@  using the ads2gas_apple.py script.\n')
    print('.syntax unified')

    f = iter(sys.stdin.readlines())
    for line in f:
        # Python edit to make sure we don't duplicate newlines
        l = line.rstrip()

        # Load and store alignment
        l = re.sub(r'@', r',:', l)

        # Comment character
        l = re.sub(r';', r'@', l)

        # Convert ELSE to .else
        l = re.sub(r'\bELSE\b', r'.else', l)

        # Convert ENDIF to .endif
        l = re.sub(r'\bENDIF\b', r'.else', l)

        # Convert IF to .if
        if re.search(r'\bIF\b', l):
            l = re.sub(r'\bIF\b', r'.if', l)
            l = l.replace('=+', '==')

        # Convert INCLUDE to .INCLUDE "file"
        l = re.sub(r'INCLUDE\s?(.*)$', r'.include "\1"', l)

        # No AREA required
        # But ALIGNs in AREA must be obeyed
        l = re.sub(r'^(\s*)\bAREA\b.*ALIGN=([0-9])$', r'\1.text\n\1.p2align \2', l)
        # If no ALIGN, strip the AREA and align to 4 bytes
        l = re.sub(r'^(\s*)\bAREA\b.*$', r'\1.text\n\1.p2align 2', l)

        # Make function visible to linker.
        l = re.sub(r'EXPORT\s+\|([\$\w]*)\|', r'.globl _\1', l)

        # No vertical bars on function names
        l = re.sub(r'^\|(\$?\w+)\|', r'\1', l)

        # Labels and functions need a leading underscore and trailing colon
        if not re.search(r'EQU', l):
            print(l)
            l = re.sub(r'^([a-zA-Z_0-9\$]+)', r'_\1:', l)

        # Branches need to call the correct, underscored, function
        if not re.search('EQU', l):
            l = re.sub(r'^(\s+b[egln]?[teq]?\s+)([a-zA-Z_0-9\$]+)', r'\1 _\2', l)

        # ALIGN directive
        l = re.sub(r'\bALIGN\b', r'.balign', l)

        # Strip ARM
        l = re.sub(r'\s+ARM', '', l)

        # Strip REQUIRE8
        l = re.sub(r'\s+REQUIRE8', r'', l)

        # Strip PRESERVE8
        l = re.sub(r'\s+PRESERVE8', r'', l)

        # Strip PROC and ENDPROC
        l = re.sub(r'\bPROC\b', r'', l)
        l = re.sub(r'\bENDP\b', r'', l)

        # EQU directive
        l = re.sub(r'(\S+\s+)EQU(\s+\S+)', r'.equ \1, \2', l)

        # Begin macro definition
        if re.search(r'\bMACRO\b', l):
            # Process next line down, which will be the macro definition
            l = next(f)
            l = l.replace(r'^', r'.macro')
            l = l.replace(r'$', r'')             # Remove $ from the variables in the declaration

        l = l.replace(r'$', r'\\')               # Use \ to reference formal parameters
        # End macro definition

        l = re.sub(r'\bMEND\b', r'.endm', l)       # No need to tell it where to stop assembling
        if re.search(r'^\s*END\s*$', l):
            continue
        l = re.sub(r'[ \t]+$', '', l)
        print(l)
