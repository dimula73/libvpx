# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

examples_subpages = {}
utils_subpages = {}

examples_deps = [libvpx_dep]

# List of examples to build. UTILS are tools meant for distribution
# while EXAMPLES demonstrate specific portions of the API.

# Unlike the original, I'm putting all the common files in a
# single library to save on up to 16 copies of the same translation unit
# (y4minput.c and tools_common.c, for instance).

vpx_examples_common_headers = []

vpx_examples_common_sources = []

if features.get('decoders', false) or features.get('encoders', false)
	vpx_examples_common_headers += files(
		'../vpx_ports/mem_ops.h',
		'../vpx_ports/mem_ops_aligned.h',
		'../vpx_ports/msvc.h',
		'../args.h',
		'../ivfdec.h',
		'../y4minput.h',
		'../tools_common.h',
		'../ivfenc.h', # encoders or decoders or vp8|9_encoder or (decoders and vp9_encoder)
		'../vpx_ports/vpx_timer.h',
		'../video_common.h',
	)

	vpx_examples_common_sources += files(
		'../args.c',
		'../ivfdec.c',
		'../y4minput.c',
		'../tools_common.c',
		'../ivfenc.c', # encoders or decoders or vp8|9_encoder or (decoders and vp9_encoder)
	)
endif

if features.get('decoders', false)
	vpx_examples_common_headers += files(
		'../vpx_ports/compiler_attributes.h',
		'../md5_utils.h',
		'../video_reader.h',
	)

	vpx_examples_common_sources += files(
		'../md5_utils.c',
		'../video_reader.c',
	)
endif

if features.get('encoders', false) or features.get('vp9_encoder', false)
	vpx_examples_common_headers += files(
		'../vpxstats.h',
	)

	vpx_examples_common_sources += files(
		'../vpxstats.c',
	)
endif

if features.get('encoders', false) or (features.get('decoders', false) and features.get('vp9_encoder', false))
	vpx_examples_common_headers += files(
		'../video_writer.h',
	)

	vpx_examples_common_sources += files(
		'../video_writer.c',
	)
endif

vpx_examples_common = static_library(
	'vpx_examples_common',
	vpx_examples_common_sources,
	extra_files: vpx_examples_common_headers,
	dependencies: examples_deps,
)

examples_deps += declare_dependency(
	link_with: vpx_examples_common,
	include_directories: include_directories('.'),
)

vpxdec_headers = files(
	'../vpx/vpx_integer.h',
	'../y4menc.h',
)

vpxdec_srcs = files(
	'../vpxdec.c',
	'../y4menc.c',
)

vpxenc_headers = files(
	'../vpxenc.h',
	'../rate_hist.h',
	'../warnings.h',
)

vpxenc_srcs = files(
	'../vpxenc.c',
	'../rate_hist.c',
	'../warnings.c',
)

vp9_spatial_svc_encoder_headers = files(
	'svc_context.h',
)

vp9_spatial_svc_encoder_srcs = files(
	'vp9_spatial_svc_encoder.c',
	'svc_encodeframe.c',
)

vpx_temporal_svc_encoder_headers = files(
)

vpx_temporal_svc_encoder_srcs = files(
	'vpx_temporal_svc_encoder.c',
)

simple_decoder_headers = files(
)

simple_decoder_srcs  = files(
	'simple_decoder.c',
)

postproc_headers = files(
)

postproc_srcs  = files(
	'postproc.c',
)

decode_to_md5_srcs = files(
	'decode_to_md5.c'
)

decode_to_md5_headers = files(
)

simple_encoder_headers = files(
)

simple_encoder_srcs = files(
	'simple_encoder.c',
)

simple_encoder_headers = files(
)

vp9_lossless_encoder_srcs = files(
	'vp9_lossless_encoder.c',
)

vp9_lossless_encoder_headers = files(
)

twopass_encoder_srcs = files(
	'twopass_encoder.c',
)

twopass_encoder_headers = files(
)

decode_with_drops_srcs = files(
	'decode_with_drops.c',
)

decode_with_drops_headers = files(
)

set_maps_srcs = files(
	'set_maps.c',
)

set_maps_headers = files(
)

vp8cx_set_ref_srcs = files(
	'vp8cx_set_ref.c',
)

vp8cx_set_ref_headers = files(
)

vp9cx_set_ref_srcs = files(
	'vp9cx_set_ref.c',
)

vp9cx_set_ref_headers = files(
)

vp8_multi_resolution_encoder_srcs = files(
	'vp8_multi_resolution_encoder.c',
)

vp9cx_set_ref_headers = files(
)

# Add compile flags and include path for libwebm sources.
if features.get('webm_io', false)
	examples_deps += libwebm_dep

	vpxdec_headers += files(
		'../webmdec.h',
	)
	vpxdec_srcs += files(
		'../webmdec.cc'
	)

	vpxenc_headers += files(
		'../webmenc.h',
	)
	vpxenc_srcs += files(
		'../webmenc.cc'
	)
endif

if features.get('decoders', false)
	vpxdec_deps = examples_deps

	if features.get('libyuv', false)
		vpxdec_deps += libyuv_dep
	endif

	vpxdec = executable(
		'vpxdec',
		vpxdec_srcs,
		extra_files: vpxdec_headers,
		dependencies: vpxdec_deps,
		install: features.get('install_bins', false),
	)

	utils_subpages += {
		'vpxdec': 'Full featured decoder'
	}
endif

if features.get('encoders', false)
	vpxenc_deps = examples_deps

	if features.get('libyuv', false)
		vpxenc_deps += libyuv_dep
	endif

	vpxenc = executable(
		'vpxenc',
		vpxenc_srcs,
		extra_files: vpxenc_headers,
		dependencies: vpxenc_deps,
		install: features.get('install_bins', false),
	)

	utils_subpages += {
		'vpxenc': 'Full featured encoder'
	}
endif

if features.get('vp9_encoder', false)
	vp9_spatial_svc_encoder = executable(
		'vp9_spatial_svc_encoder',
		vp9_spatial_svc_encoder_srcs,
		extra_files: vp9_spatial_svc_encoder_headers,
		dependencies: examples_deps,
	)

	examples_subpages += {
		'vp9_spatial_svc_encoder': 'VP9 Spatial SVC Encoder'
	}
endif

if not features.get('shared', false)
	resize_util = executable(
		'resize_util',
		files(
			'resize_util.c'
		),
		dependencies: examples_deps,
	)
endif

if features.get('encoders', false)
	vpx_temporal_svc_encoder = executable(
		'vpx_temporal_svc_encoder',
		vpx_temporal_svc_encoder_srcs,
		extra_files: vpx_temporal_svc_encoder_headers,
		dependencies: examples_deps,
	)

	decode_to_md5 = executable(
		'decode_to_md5',
		decode_to_md5_srcs,
		extra_files: decode_to_md5_headers,
		dependencies: examples_deps,
	)

	simple_encoder = executable(
		'simple_encoder',
		simple_encoder_srcs,
		extra_files: simple_encoder_headers,
		dependencies: examples_deps,
	)

	vp9_lossless_encoder = executable(
		'vp9_lossless_encoder',
		vp9_lossless_encoder_srcs,
		extra_files: vp9_lossless_encoder_headers,
		dependencies: examples_deps,
	)

	twopass_encoder = executable(
		'twopass_encoder',
		twopass_encoder_srcs,
		extra_files: twopass_encoder_headers,
		dependencies: examples_deps,
	)

	set_maps = executable(
		'set_maps',
		set_maps_srcs,
		extra_files: set_maps_headers,
		dependencies: examples_deps,
	)

	examples_subpages += {
		'vpx_temporal_svc_encoder': 'Temporal SVC Encoder',
		'decode_to_md5': 'Frame by frame MD5 checksum',
		'simple_encoder': 'Simplified encoder loop',
		'vp9_lossless_encoder': 'Simplified lossless VP9 encoder',
		'twopass_encoder': 'Two-pass encoder loop',
		'set_maps': 'Set active and ROI maps',
	}
endif

if features.get('decoders', false)
	simple_decoder = executable(
		'simple_decoder',
		simple_decoder_srcs,
		extra_files: simple_decoder_headers,
		dependencies: examples_deps,
	)

	postproc = executable(
		'postproc',
		postproc_srcs,
		extra_files: postproc_headers,
		dependencies: examples_deps,
	)

	decode_with_drops = executable(
		'decode_with_drops',
		decode_with_drops_srcs,
		extra_files: postproc_headers,
		dependencies: examples_deps,
	)

	examples_subpages += {
		'simple_decoder': 'Simplified decoder loop',
		'postproc': 'Decoder postprocessor control',
		'decode_with_drops': 'Drops frames while decoding',
	}
endif

if features.get('vp8_encoder', false)
	vp8cx_set_ref = executable(
		'vp8cx_set_ref',
		vp8cx_set_ref_srcs,
		extra_files: vp8cx_set_ref_headers,
		dependencies: examples_deps,
	)

	examples_subpages += {
		'vp8cx_set_ref': 'VP8 set encoder reference frame',
	}
endif

if features.get('vp9_encoder', false) and features.get('decoders', false)
	vp9cx_set_ref = executable(
		'vp9cx_set_ref',
		vp9cx_set_ref_srcs,
		extra_files: vp9cx_set_ref_headers,
		dependencies: examples_deps,
	)

	examples_subpages += {
		'vp9cx_set_ref': 'VP9 set encoder reference frame',
	}
endif

if features.get('multi_res_encoding', false) and features.get('libyuv', false)
	vp8_multi_resolution_encoder = executable(
		'vp8_multi_resolution_encoder',
		vp8_multi_resolution_encoder_srcs,
		extra_files: vp8_multi_resolution_encoder_headers,
		dependencies: examples_deps + libyuv_dep,
	)

	examples_subpages += {
		'vp8_multi_resolution_encoder': 'VP8 Multiple-resolution Encoding',
	}
endif

#
# Documentation Rules
#

if features.get('install_docs', false)
	doxfiles = []
	examples_subpages_entries = []
	utils_subpages_entries = []

	foreach page, description: examples_subpages
		doxfiles += configure_file(
			command: [generate_component_dox, '--component', 'example', '--output', '@OUTPUT@', '@INPUT@'],
			input: get_variable('@0@_srcs'.format(page))[0],
			output: '@0@.dox'.format(page),
		)

		examples_subpages_entries += '    - \subpage example_@0@ @1@'.format(page, description)
	endforeach

	foreach page, description: utils_subpages
		doxfiles += configure_file(
			command: [generate_component_dox, '--component', 'example', '--output', '@OUTPUT@', '@INPUT@'],
			input: get_variable('@0@_srcs'.format(page))[0],
			output: '@0@.dox'.format(page),
		)

		utils_subpages_entries += '    - \subpage example_@0@ @1@'.format(page, description)
	endforeach

	samples_dox = configure_file(
		input: 'samples.dox.in',
		output: 'samples.dox',
		configuration: {
			'examples_subpages': '\n'.join(examples_subpages_entries),
			'utils_subpages': '\n'.join(utils_subpages_entries),
		}
	)

	examples_doxy = configure_file(
		command: [doxy_template, '--sections', 'samples', '--output', '@OUTPUT@', '@INPUT@'],
		input: [samples_dox] + doxfiles,
		output: 'examples.doxy',
	)
endif
