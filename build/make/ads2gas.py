#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2010 The WebM Authors
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
import re
import sys
import thumb

if __name__ == '__main__':
    parser = ArgumentParser(description='Convert ARM Developer Suite 1.0.1 syntax assembly source to GNU as format')
    parser.add_argument('-thumb', action='store_true')
    parser.add_argument('-noelf', dest='elf', action='store_false')

    args = parser.parse_args()

    print('@ This file was created from a .asm file')
    print('@  using the ads2gas.pl script.')
    print('.syntax unified')

    if args.thumb:
        print('\t.thumb')

    # Stack of procedure names.
    proc_stack: list[str] = []

    f = iter(sys.stdin.readlines())
    for line in f:
        # Python edit to make sure we don't duplicate newlines
        l = line.rstrip()

        # Load and store alignment
        l = re.sub(r'@', ',:', l)

        # Comment character
        l = re.sub(r';', r'@', l)

        # Convert ELSE to .else
        l = re.sub(r'\bELSE\b', r'.else', l)

        # Convert ENDIF to .endif
        l = re.sub(r'\bENDIF\b', r'.endif', l)

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
        if args.elf:
            l = re.sub(r'(\s*)EXPORT\s+\|([\$\w]*)\|', r'\1.global \2\n\1.type \2, function', l)
        else:
            l = re.sub(r'(\s*)EXPORT\s+\|([\$\w]*)\|', r'\1.global \2', l)

        # No vertical bars on function names
        l = re.sub(r'^\|(\$?\w+)\|', r'\1', l)

        # Labels need trailing colon
        if not re.search('EQU', l):
            l = re.sub(r'^([a-zA-Z_0-9\$]+)', r'\1:', l)

        # ALIGN directive
        l = re.sub(r'\bALIGN\b', r'.balign', l)

        if args.thumb:
            # ARM code - we force everything to thumb with the declaration in the
            # header
            l = re.sub(r'\bARM\b', r'', l)
        else:
            # ARM code
            l = re.sub(r'\bARM\b', r'.arm', l)

        # push/pop
        l = re.sub(r'(push\s+)(r\d+)', r'stmdb sp!, {\2}', l)
        l = re.sub(r'(pop\s+)(r\d+)', r'ldmia sp!, {\2}', l)

        if args.thumb:
            l = thumb.FixThumbInstructions(l)

        # eabi_attributes numerical equivalents can be found in the
        # "ARM IHI 0045C" document.

        if args.elf:
            # REQUIRE8 Stack is required to be 8-byte aligned
            l = re.sub(r'\bREQUIRE8\b', r'.eabi_attribute 24, 1 @Tag_ABI_align_needed', l)

            # PRESERVE8 Stack 8-byte align is preserved
            l = re.sub(r'\bPRESERVE8\b', r'.eabi_attribute 25, 1 @Tag_ABI_align_preserved', l)
        else:
            l = re.sub(r'\bREQUIRE8\b', r'', l)
            l = re.sub(r'\bPRESERVE8\b', r'', l)

        # Use PROC and ENDP to give the symbols a .size directive.
        # This makes them show up properly in debugging tools like gdb and valgrind.
        if re.search(r'\bPROC\b', l):
            # Match the function name so it can be stored in $proc
            proc = re.search(r'^([\.0-9A-Z_a-z]\w+)\b', l)
            if proc:
                proc_stack.append(proc.group(1))
            l = re.sub(r'\bPROC\b', r'@ \g<0>', l)

        if re.search(r'\bENDP\b', l):
            l = re.sub(r'\bENDP\b', r'@ \g<0>', l)
            proc = None if len(proc_stack) == 0 else proc_stack.pop()
            if proc and args.elf:
                l = f'.size {proc}, .-{proc}{l}'

        # EQU directive
        l = re.sub(r'(\S+\s+)EQU(\s+\S+)', r'.equ \1, \2', l)

        # Begin macro definition
        if re.search(r'\bMACRO\b', l):
            # Process next line down, which will be the macro definition
            l = next(f)
            l = re.sub(r'^', r'.macro', l)
            l = l.replace(r'$', r'')             # Remove $ from the variables in the declaration

        l = l.replace(r'$', '\\')               # Use \ to reference formal parameters
        # End macro definition

        l = re.sub(r'\bMEND\b', r'.endm', l)       # No need to tell it where to stop assembling
        if re.search(r'^\s*END\s*$', l):
            continue

        l = re.sub(r'[ \t]+$', '', l)
        print(l)

    # Mark that this object doesn't need an executable stack.
    if args.elf:
        print(r'    .section .note.GNU-stack,"",%progbits')
