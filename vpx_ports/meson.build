# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vpx_ports.mk

#### --- GENERATED --- ####

ports_sources = files(
)

ports_optional_sources = {
	'mmx' : files(
		# 'emms_mmx.c' # MANUAL
	),
	'arm' : files(
		'arm_cpudetect.c',
	),
	'ppc' : files(
		'ppc_cpudetect.c',
	),
	'mips' : files(
		'mips_cpudetect.c',
	),
	'loongarch' : files(
		'loongarch_cpudetect.c',
	),
}

ports_headers_sources = files(
	'bitops.h',
	'compiler_attributes.h',
	'mem.h',
	'msvc.h',
	'static_assert.h',
	'system_state.h',
	'vpx_timer.h',
	# 'x86.h', # MANUAL
	# 'asmdefs_mmi.h', # MANUAL
)

ports_headers_optional_sources = {
	'arm' : files(
		'arm.h',
	),
	'ppc' : files(
		'ppc.h',
	),
	'mips' : files(
		'mips.h',
	),
	'loongarch' : files(
		'loongarch.h',
	),
}

ports_asm_sources = files(
	# 'x86_abi_support.asm', # MANUAL
)

ports_asm_optional_sources = {
	'mmx' : files(
		# 'emms_mmx.asm' # MANUAL
	),
	'msvs' : files(
		# 'float_control_word.asm' # MANUAL
	),
}

ports_headers_sources += files( # MANUAL
	'emmintrin_compat.h',
	'mem_ops.h',
	'mem_ops_aligned.h',
	'vpx_once.h',
)

if features.get('x86', false) # MANUAL
	ports_optional_sources += {
		'mmx' : ports_optional_sources['mmx'] + files(
			'emms_mmx.c'
		),
	}
endif

if features.get('x86_64', false) # MANUAL
	# Visual Studio x64 does not support the _mm_empty() intrinsic.
	ports_asm_optional_sources += {
		'mmx' : ports_asm_optional_sources['mmx'] + files(
			'emms_mmx.asm'
		),
	}

	ports_asm_optional_sources += {
		'msvs' : ports_asm_optional_sources['msvs'] +files(
			'float_control_word.asm'
		),
	}
endif

# Do NOT compile these ASM files with MSVC! It will cause a linker deadlock
# because the PDBs are empty:
# https://developercommunity.visualstudio.com/t/MSVC-deadlockscrashes-when-linking-a-Me/10336032
# The original configure script doesn't fail because they're ignored
# in the ASM_INCLUDES variable.
ports_headers_optional_sources += { # MANUAL
	'x86': files(
		'x86.h',
		'x86_abi_support.asm',
	),
	'x86_64': files(
		'x86.h',
		'x86_abi_support.asm',
	),
	'mips': files(
		'asmdefs_mmi.h'
	)
}

#### --- END GENERATED --- ####

codec_srcs += ports_sources
optional_sources = get_variable('ports_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	elif ARCH_EXT_LIST.contains(comp_name)
		codec_arch_srcs += {
			comp_name: codec_arch_srcs.get(comp_name, []) + comp_sources
		}
	else
		codec_srcs += comp_sources
	endif
endforeach

optional_sources = get_variable('ports_asm_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	elif ARCH_EXT_LIST.contains(comp_name)
		transformed_sources = comp_sources
		if asm_conversion_exe.found()
			transformed_sources = asm_transformer.process(comp_sources)
		endif
		codec_arch_srcs += {
			comp_name: codec_arch_srcs.get(comp_name, []) + transformed_sources
		}
	else
		codec_srcs += comp_sources
	endif
endforeach

codec_headers += ports_headers_sources
optional_sources = get_variable('ports_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		codec_headers += comp_sources
	endif
endforeach
