# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

libyuv_includes = files(
	'include/libyuv/convert.h',
	'include/libyuv/convert_argb.h',
	'include/libyuv/convert_from.h',
	'include/libyuv/cpu_id.h',
	'include/libyuv/planar_functions.h',
	'include/libyuv/rotate.h',
	'include/libyuv/row.h',
	'include/libyuv/scale.h',
	'include/libyuv/scale_row.h',
)

libyuv_include_directories = include_directories('include')

libyuv_srcs = files(
	'source/cpu_id.cc',
	'source/planar_functions.cc',
	'source/row_any.cc',
	'source/row_common.cc',
	'source/row_gcc.cc',
	'source/row_msa.cc',
	'source/row_neon.cc',
	'source/row_neon64.cc',
	'source/row_win.cc',
	'source/scale.cc',
	'source/scale_any.cc',
	'source/scale_common.cc',
	'source/scale_gcc.cc',
	'source/scale_msa.cc',
	'source/scale_neon.cc',
	'source/scale_neon64.cc',
	'source/scale_win.cc',
)

libyuv = static_library(
	'vpx_yuv',
	libyuv_srcs,
	cpp_args: libyuv_cpp_args,
	extra_files: libyuv_includes,
	include_directories: libyuv_include_directories,
)

libyuv_dep = declare_dependency(
	link_with: libyuv,
	include_directories: libyuv_include_directories,
)
