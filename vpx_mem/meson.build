# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vp8_common.mk

#### --- GENERATED --- ####

mem_sources = files(
	'vpx_mem.c',
)

mem_optional_sources = {
}

mem_headers_sources = files(
	'vpx_mem.h',
	'include/vpx_mem_intrnl.h',
)

mem_headers_optional_sources = {
}

#### --- END GENERATED --- ####

optional_sources = get_variable('mem_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		mem_sources += comp_sources
	endif
endforeach

codec_srcs += mem_sources

optional_sources = get_variable('mem_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		mem_headers_sources += comp_sources
	endif
endforeach

codec_headers += mem_headers_sources
