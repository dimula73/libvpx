# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

libwebm_common_srcs = files(
	'common/hdr_util.cc',
)

libwebm_common_includes = files(
	'common/hdr_util.h',
	'common/webmids.h',
)

libwebm_muxer_srcs = files(
	'mkvmuxer/mkvmuxer.cc',
	'mkvmuxer/mkvmuxerutil.cc',
	'mkvmuxer/mkvwriter.cc',
)

libwebm_muxer_headers = files(
	'mkvmuxer/mkvmuxer.h',
	'mkvmuxer/mkvmuxertypes.h',
	'mkvmuxer/mkvmuxerutil.h',
	'mkvparser/mkvparser.h',
	'mkvmuxer/mkvwriter.h',
)

libwebm_parser_srcs = files(
	'mkvparser/mkvparser.cc',
	'mkvparser/mkvreader.cc',
)

libwebm_parser_headers = files(
	'mkvparser/mkvparser.h',
	'mkvparser/mkvreader.h',
)

libwebm = static_library(
	'vpx_webm',
	libwebm_common_srcs + libwebm_muxer_srcs + libwebm_parser_srcs,
	extra_files: libwebm_common_includes + libwebm_muxer_headers + libwebm_parser_headers,
	include_directories: include_directories('.'),
	cpp_args: [
		'-D__STDC_CONSTANT_MACROS',
		'-D__STDC_FORMAT_MACROS',
		'-D__STDC_LIMIT_MACROS'
	]
)

libwebm_dep = declare_dependency(
	link_with: libwebm,
	include_directories: include_directories('.'),
)
