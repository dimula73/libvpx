# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vpx_util.mk

#### --- GENERATED --- ####

util_sources = files(
	'vpx_thread.c',
	'vpx_write_yuv_frame.c',
)

util_optional_sources = {
	'mismatch_debug' : files(
		# 'vpx_debug_util.c' # MANUAL
	),
}

util_headers_sources = files(
	'vpx_atomics.h',
	'vpx_thread.h',
	'endian_inl.h',
	'vpx_write_yuv_frame.h',
	'vpx_timestamp.h',
)

util_headers_optional_sources = {
	'mismatch_debug' : files(
		# 'vpx_debug_util.h' # MANUAL
	),
}

if features.get('bitstream_debug', false) or features.get('mismatch_debug', false)
	util_sources += files(
		'vpx_debug_util.c'
	)

	util_headers_sources += files(
		'vpx_debug_util.h'
	)
endif

#### --- END GENERATED --- ####

optional_sources = get_variable('util_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		util_sources += comp_sources
	endif
endforeach

codec_srcs += util_sources

optional_sources = get_variable('util_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		util_headers_sources += comp_sources
	endif
endforeach

codec_headers += util_headers_sources
