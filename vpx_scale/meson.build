# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vp8_common.mk

#### --- GENERATED --- ####

scale_sources = files(
	'generic/yv12config.c',
	'generic/yv12extend.c',
	'vpx_scale_rtcd.c',
)

scale_optional_sources = {
	'dspr2' : files(
		'mips/dspr2/yv12extend_dspr2.c'
	),
	'spatial_resampling' : files(
		'generic/vpx_scale.c',
		'generic/gen_scalers.c'
	),
}

scale_headers_sources = files(
	'yv12config.h',
)

scale_headers_optional_sources = {
	'spatial_resampling' : files(
		'vpx_scale.h'
	),
}

#### --- END GENERATED --- ####

codec_srcs += scale_sources
optional_sources = get_variable('scale_optional_sources', {})
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

codec_headers += scale_headers_sources
optional_sources = get_variable('scale_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	elif ARCH_EXT_LIST.contains(comp_name)
		codec_arch_headers += {
			comp_name: codec_arch_headers.get(comp_name, []) + comp_sources
		}
	else
		codec_headers += comp_sources
	endif
endforeach

vpx_scale_rtcd_defs = meson.current_source_dir() / 'vpx_scale_rtcd.py'

codec_rtcds += {
	'vpx_scale_rtcd': vpx_scale_rtcd_defs
}
codec_headers += files(vpx_scale_rtcd_defs)
