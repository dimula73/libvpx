# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

doxfiles = []

tiny_ssim_srcs = files(
	'tiny_ssim.c',
	'../y4minput.c',
	'../vpx/src/vpx_image.c',
	'../vpx_mem/vpx_mem.c',
)

tiny_ssim_headers = files(
	'../vpx/vpx_integer.h',
	'../y4minput.h',
	'../vpx/vpx_codec.h',
	'../vpx_mem/vpx_mem.h',
	'../vpx_dsp/ssim.h',
	'../vpx_scale/yv12config.h',
	'../vpx_ports/mem.h',
	'../vpx_mem/include/vpx_mem_intrnl.h',
)

tiny_ssim = executable(
	'tiny_ssim',
	tiny_ssim_srcs,
	link_args: link_args,
	extra_files: tiny_ssim_headers,
	dependencies: libvpx_dep,
	install: get_option('install_bins'),
)

tools_subpages = {
	'tiny_ssim': 'Generate SSIM/PSNR from raw .yuv files'
}

tools_subpages_entries = []

#
# Documentation Rules
#

if features.get('install_docs', false)
	foreach page, description: tools_subpages
		doxfiles += configure_file(
			command: [generate_component_dox, '--component', 'tools', '--output', '@OUTPUT@', '@INPUT@'],
			input: get_variable('@0@_srcs'.format(page))[0],
			output: '@0@.dox'.format(page),
		)

		tools_subpages_entries += '    - \subpage tools_@0@ @1@'.format(page, description)
	endforeach

	tools_dox = configure_file(
		input: 'tools.dox.in',
		output: 'tools.dox',
		configuration: {
			'tools_subpages': '\n'.join(tools_subpages_entries),
		}
	)

	tools_doxy = configure_file(
		command: [doxy_template, '--sections', 'tools', '--output', '@OUTPUT@', '@INPUT@'],
		input: [tools_dox] + doxfiles,
		output: 'tools.doxy',
	)
endif
