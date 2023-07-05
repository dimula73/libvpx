#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2013 The WebM Authors
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

import re

def FixThumbInstructions(l: str) -> str:
    # Write additions with shifts, such as "add r10, r11, lsl #8",
    # in three operand form, "add r10, r10, r11, lsl #8".
    l = re.sub(r'(add\s+)(r\d+),\s*(r\d+),\s*(lsl #\d+)', r'\1\2, \2, \3, \4', l)

    # Convert additions with a non-constant shift into a sequence
    # with left shift, addition and a right shift (to restore the
    # register to the original value). Currently the right shift
    # isn't necessary in the code base since the values in these
    # registers aren't used, but doing the shift for consistency.
    # This converts instructions such as "add r12, r12, r5, lsl r4"
    # into the sequence "lsl r5, r4", "add r12, r12, r5", "lsr r5, r4".
    l = re.sub(r'^(\s*)(add)(\s+)(r\d+),\s*(r\d+),\s*(r\d+),\s*lsl (r\d+)', r'\1lsl\3\6, \7\n\1\2\3\4, \5, \6\n\1lsr\3\6, \7', l)

    # Convert loads with right shifts in the indexing into a
    # sequence of an add, load and sub. This converts
    # "ldrb r4, [r9, lr, asr #1]" into "add r9, r9, lr, asr #1",
    # "ldrb r9, [r9]", "sub r9, r9, lr, asr #1".
    l = re.sub(r'^(\s*)(ldrb)(\s+)(r\d+),\s*\[(\w+),\s*(\w+),\s*(asr #\d+)\]', r'\1add \3\5, \5, \6, \7\n\1\2\3\4, [\5]\n\1sub \3\5, \5, \6, \7', l)

    # Convert register indexing with writeback into a separate add
    # instruction. This converts "ldrb r12, [r1, r2]!" into
    # "ldrb r12, [r1, r2]", "add r1, r1, r2".
    l = re.sub(r'^(\s*)(ldrb)(\s+)(r\d+),\s*\[(\w+),\s*(\w+)\]!', r'\1\2\3\4, [\5, \6]\n\1add \3\5, \6', l)

    # Convert negative register indexing into separate sub/add instructions.
    # This converts "ldrne r4, [src, -pstep, lsl #1]" into
    # "subne src, src, pstep, lsl #1", "ldrne r4, [src]",
    # "addne src, src, pstep, lsl #1". In a couple of cases where
    # this is used, it's used for two subsequent load instructions,
    # where a hand-written version of it could merge two subsequent
    # add and sub instructions.
    l = re.sub(r'^(\s*)((ldr|str|pld)(ne)?)(\s+)(r\d+,\s*)?\[(\w+), -([^\]]+)\]', r'\1sub\4\5\7, \7, \8\n\1\2\5\6\[\7\]\n\1add\4\5\7, \7, \8', l)

    # Convert register post indexing to a separate add instruction.
    # This converts "ldrneb r9, [r0], r2" into "ldrneb r9, [r0]",
    # "addne r0, r0, r2".
    l = re.sub(r'^(\s*)((ldr|str)(ne)?[bhd]?)(\s+)(\w+),(\s*\w+,)?\s*\[(\w+)\],\s*(\w+)', r'\1\2\5\6,\7 [\8]\n\1add\4\5\8, \8, \9', l)

    # Convert "mov pc, lr" into "bx lr", since the former only works
    # for switching from arm to thumb (and only in armv7), but not
    # from thumb to arm.
    l = re.sub(r'mov(\s*)pc\s*,\s*lr', r'bx\1lr', l)

    return l
