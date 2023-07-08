#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2017 The WebM Authors
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
import re
from pathlib import Path
from typing import Any, Dict, List

ALL_FUNCS: Dict[str, List[str]] = {}
ALL_ARCHS: List[str] = []
ALL_FORWARD_DECLS: List[str] = []
REQUIRES: List[str] = []

opts: Dict[str, Any] = {}
disabled: List[str] = []
required: List[str] = []

config: Dict[str, str] = {}

def qw(s: str) -> List[str]:
    return s.split()

#
# Routines for the RTCD DSL to call
#
def vpx_config(s: str) -> str:
    return config[s] if s in config else ''

def specialize(*args: str):
    fn = args[0]
    for opt in args[1:]:
        exec(f"{fn}_{opt}='{fn}_{opt}'", globals())

def add_proto(*args: str):
    _args = list(args)
    fn = _args.pop(-2)
    ALL_FUNCS[fn] = _args
    specialize(fn, "c")

def require(*args: str):
    for fn in ALL_FUNCS.keys():
        for opt in args:
            try:
                ofn = eval(f"{fn}_{opt}")
            except NameError:
                continue

            # if we already have a default, then we can disable it, as we know
            # we can do better.
            try:
                best = eval(f"{fn}_default")
                best_ofn = eval(f"{best}")
                if best_ofn != ofn:
                    exec(f"{best}_link = False", globals())
            except NameError:
                pass

            exec(f"{fn}_default='{fn}_{opt}'", globals())
            exec(f"{fn}_{opt}_link=True", globals())

def forward_decls(*args: str):
    ALL_FORWARD_DECLS.extend(args)

#
# Process the directives according to the command line
#
def process_forward_decls():
  for f in ALL_FORWARD_DECLS:
    exec(f'{f}()', globals())

def determine_indirection(*params: str):
    if vpx_config("CONFIG_RUNTIME_CPU_DETECT") != "yes":
        require(*ALL_ARCHS)
    for fn in ALL_FUNCS.keys():
        n = ""
        val = list(ALL_FUNCS[fn])
        args = val.pop()
        rtyp = ' '.join(val)
        dfn = eval(f"{fn}_default")
        dfn = eval(f"{dfn}")
        for opt in params:
            try:
                ofn = eval(f"{fn}_{opt}")
            except:
                continue
            try:
                link = eval(f"{fn}_{opt}_link")
                if link == False:
                    continue
            except:
                pass
            n += "x"
        exec(f'{fn}_indirect = {n != "x"}', globals())

def declare_function_pointers(*params: str):
    for fn in sorted(ALL_FUNCS.keys()):
        val = list(ALL_FUNCS[fn])
        args = val.pop()
        rtyp = ' '.join(val)
        dfn = eval(f"{fn}_default")
        dfn = eval(f"{dfn}")
        for opt in params:
            try:
                ofn = eval(f"{fn}_{opt}")
            except:
                continue
            print(f"{rtyp} {ofn}({args});")
        if not eval(f"{fn}_indirect"):
            print(f"#define {fn} {dfn}")
        else:
            print(f"RTCD_EXTERN {rtyp} (*{fn})({args});")
        print("")

def set_function_pointers(*params: str):
    for fn in sorted(ALL_FUNCS.keys()):
        val = list(ALL_FUNCS[fn])
        args = val.pop()
        rtyp = ' '.join(val)
        dfn = eval(f"{fn}_default")
        dfn = eval(f"{dfn}")
        if eval(f"{fn}_indirect"):
            print(f"    {fn} = {dfn};")
            for opt in params:
                try:
                    ofn = eval(f"{fn}_{opt}")
                except:
                    continue
                if ofn == dfn:
                    continue
                try:
                    link = eval(f"{fn}_{opt}_link")
                    if link == False:
                        continue
                except:
                    pass
                cond = eval(f"have_{opt}")
                print(f"    if ({cond}) {fn} = {ofn};")

def filter(*args: str) -> List[str]:
    filtered = []
    for arg in args:
        if not arg in disabled:
            filtered.append(arg)
    return filtered

#
# Helper functions for generating the arch specific RTCD files
#
def common_top():
    include_guard = str(opts['sym']).upper() + "_H_"
    print(f'''// This file is generated. Do not edit.
#ifndef {include_guard}
#define {include_guard}

#ifdef RTCD_C
#define RTCD_EXTERN
#else
#define RTCD_EXTERN extern
#endif
''')

    process_forward_decls()
    print('''#ifdef __cplusplus
extern "C" {
#endif
''')
    declare_function_pointers("c", *ALL_ARCHS)

    print(f'''void {opts['sym']}(void);
''')

def common_bottom():
  print('''
#ifdef __cplusplus
}  // extern "C"
#endif

#endif''')

def x86():
    determine_indirection("c", *ALL_ARCHS)

    # Assign the helper variable for each enabled extension
    for opt in ALL_ARCHS:
        opt_uc = opt.upper()
        exec(f"have_{opt}=\"flags & HAS_{opt_uc}\"", globals())

    common_top()
    print('''#ifdef RTCD_C
#include "vpx_ports/x86.h"
static void setup_rtcd_internal(void)
{
    int flags = x86_simd_caps();

    (void)flags;
''')

    set_function_pointers("c", *ALL_ARCHS)

    print('''}
#endif''')
    common_bottom()

def arm():
    determine_indirection("c", *ALL_ARCHS)

    # Assign the helper variable for each enabled extension
    for opt in ALL_ARCHS:
        opt_uc = opt.upper()
        # Enable neon assembly based on HAVE_NEON logic instead of adding new
        # HAVE_NEON_ASM logic
        if opt == 'neon_asm': opt_uc = 'NEON'
        exec(f"have_{opt}=\"flags & HAS_{opt_uc}\"", globals())

    common_top()
    print('''#include "vpx_config.h"

#ifdef RTCD_C
#include "vpx_ports/arm.h"
static void setup_rtcd_internal(void)
{
    int flags = arm_cpu_caps();

    (void)flags;
''')

    set_function_pointers("c", *ALL_ARCHS)

    print('''}
#endif''')
    common_bottom()

def mips():
    determine_indirection("c", *ALL_ARCHS)

    # Assign the helper variable for each enabled extension
    for opt in ALL_ARCHS:
        opt_uc = opt.upper()
        exec(f"have_{opt}=\"flags & HAS_{opt_uc}\"", globals())

    common_top()

    print('''#include "vpx_config.h"

#ifdef RTCD_C
#include "vpx_ports/mips.h"
static void setup_rtcd_internal(void)
{
    int flags = mips_cpu_caps();

    (void)flags;
''')

    set_function_pointers("c", *ALL_ARCHS)

    print('''
#if HAVE_DSPR2
void vpx_dsputil_static_init();
#if CONFIG_VP8
void dsputil_static_init();
#endif

vpx_dsputil_static_init();
#if CONFIG_VP8
dsputil_static_init();
#endif
#endif
}
#endif''')
    common_bottom()

def ppc():
    determine_indirection("c", *ALL_ARCHS)

    # Assign the helper variable for each enabled extension
    for opt in ALL_ARCHS:
        opt_uc = opt.upper()
        exec(f"have_{opt}=\"flags & HAS_{opt_uc}\"", globals())

    common_top()
    print('''#include "vpx_config.h"

#ifdef RTCD_C
#include "vpx_ports/ppc.h"
static void setup_rtcd_internal(void)
{
    int flags = ppc_simd_caps();
    (void)flags;
''')

    set_function_pointers("c", *ALL_ARCHS)

    print('''}
#endif''')
    common_bottom()

def loongarch():
    determine_indirection("c", *ALL_ARCHS)

    # Assign the helper variable for each enabled extension
    for opt in ALL_ARCHS:
        opt_uc = opt.upper()
        exec(f"have_{opt}=\"flags & HAS_{opt_uc}\"", globals())

    common_top()
    print('''#include "vpx_config.h"

#ifdef RTCD_C
#include "vpx_ports/loongarch.h"
static void setup_rtcd_internal(void)
{
    int flags = loongarch_cpu_caps();

    (void)flags;
''')

    set_function_pointers("c", *ALL_ARCHS)

    print('''}
#endif''')
    common_bottom()

def unoptimized():
    determine_indirection("c")
    common_top()
    print('''#include "vpx_config.h"

#ifdef RTCD_C
static void setup_rtcd_internal(void)
{
''')

    set_function_pointers("c")

    print('''}
#endif''')
    common_bottom()

#
# Main Driver
#

if __name__ == '__main__':
    parser = ArgumentParser(description='Reads the Run Time CPU Detections definitions from FILE and generates a C header file on stdout.')
    parser.add_argument('--arch', help='Architecture to generate defs for', required=True)
    parser.add_argument('--disable', metavar='EXT', action='append', default=[], help='Disable support for EXT extension')
    parser.add_argument('--require', metavar='EXT', action='append', default=[], help='Require support for EXT extension')
    parser.add_argument('--sym', metavar='SYMBOL', help='Unique symbol to use for RTCD initialization function')
    parser.add_argument('--config', metavar='FILE', type=Path, help='File with CONFIG_FOO=yes lines to parse', required=True)
    parser.add_argument('file', metavar='FILE', nargs='+', type=Path)

    args = parser.parse_known_args()

    opts = vars(args[0])

    for ext in opts['disable']:
        disabled.append(ext)
    for ext in opts['require']:
        required.append(ext)
    for ext in args[1]:
        match = re.match('--disable-(.+)', ext)
        if match:
            disabled.append(match.group(1))
            continue
        match = re.match('--enable-(.+)', ext)
        if match:
            required.append(match.group(1))
            continue

    with Path(opts['config']).open('r', encoding='utf-8') as f:
        for line in f:
            if not re.search(r'^(?:CONFIG_|HAVE_)', line):
                continue
            pair = line.strip().split('=')
            config[pair[0]] = pair[1]

    #
    # Include the user's directives
    #
    for file in args[0].file:
        with file.open('r', encoding='utf-8') as f:
            try:
                exec(f.read(), globals())
            except BaseException as e:
                raise RuntimeWarning(f'exec failed: {e}')


    require(*qw("c"))
    require(*required)
    if opts['arch'] == 'x86':
        ALL_ARCHS = filter(*qw('mmx sse sse2 sse3 ssse3 sse4_1 avx avx2 avx512'))
        x86()
    elif opts['arch'] == 'x86_64':
        ALL_ARCHS = filter(*qw('mmx sse sse2 sse3 ssse3 sse4_1 avx avx2 avx512'))
        REQUIRES = filter(*qw('mmx sse sse2'))
        require(*REQUIRES)
        x86()
    elif opts['arch'] == 'mips32' or opts['arch'] == 'mips64':
        have_dspr2 = False
        have_msa = False
        have_mmi = False
        ALL_ARCHS = filter(*opts["arch"])
        CONFIG_FILE: Path = opts['config']
        for line in CONFIG_FILE.open('r', encoding='utf-8'):
            have_dspr2 = re.search(r'HAVE_DSPR2=yes', line) is not None
            have_msa = re.search(r'HAVE_MSA=yes', line) is not None
            have_mmi = re.search(r'HAVE_MMI=yes', line) is not None
        if have_dspr2:
            ALL_ARCHS = filter(*opts['arch'], *qw('dspr2'))
        elif have_msa and have_mmi:
            ALL_ARCHS = filter(*opts['arch'], *qw('mmi msa'))
        elif have_msa:
            ALL_ARCHS = filter(*opts['arch'], *qw('msa'))
        elif have_mmi:
            ALL_ARCHS = filter(*opts['arch'], *qw('mmi'))
        else:
            unoptimized()
        mips()
    elif re.search(r'armv7\w?', opts['arch']):
        ALL_ARCHS = filter(*qw('neon_asm neon'))
        arm()
    elif opts['arch'] == 'armv8' or opts['arch'] == 'arm64':
        ALL_ARCHS = filter(*qw('neon'))
        REQUIRES = filter(*qw('neon'))
        require(*REQUIRES)
        arm()
    elif re.search(r'^ppc', opts['arch']):
        ALL_ARCHS = filter(*qw('vsx'))
        ppc()
    elif re.search(r'loongarch', opts['arch']):
        ALL_ARCHS = filter(*qw('lsx lasx'))
        loongarch()
    else:
        unoptimized()
