# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vp9_common.mk

#### --- GENERATED --- ####

vp9_common_sources = files(
	'vp9_iface_common.c',
	'common/vp9_alloccommon.c',
	'common/vp9_blockd.c',
	'common/vp9_entropy.c',
	'common/vp9_entropymode.c',
	'common/vp9_entropymv.c',
	'common/vp9_frame_buffers.c',
	'common/vp9_idct.c',
	'common/vp9_filter.c',
	'common/vp9_pred_common.c',
	'common/vp9_rtcd.c',
	'common/vp9_scale.c',
	'common/vp9_seg_common.c',
	'common/vp9_tile_common.c',
	'common/vp9_loopfilter.c',
	'common/vp9_thread_common.c',
	'common/vp9_mvref_common.c',
	'common/vp9_quant_common.c',
	'common/vp9_reconinter.c',
	'common/vp9_reconintra.c',
	'common/vp9_common_data.c',
	'common/vp9_scan.c',
)

vp9_common_optional_sources = {
	'dspr2' : files(
		# 'common/mips/dspr2/vp9_itrans4_dspr2.c', # MANUAL
		# 'common/mips/dspr2/vp9_itrans8_dspr2.c', # MANUAL
		# 'common/mips/dspr2/vp9_itrans16_dspr2.c' # MANUAL
	),
	'msa' : files(
		# 'common/mips/msa/vp9_idct4x4_msa.c', # MANUAL
		# 'common/mips/msa/vp9_idct8x8_msa.c', # MANUAL
		# 'common/mips/msa/vp9_idct16x16_msa.c', # MANUAL
		# 'common/mips/msa/vp9_mfqe_msa.c' # MANUAL
	),
	'neon' : files(
		'common/arm/neon/vp9_iht4x4_add_neon.c',
		'common/arm/neon/vp9_iht8x8_add_neon.c',
		'common/arm/neon/vp9_iht16x16_add_neon.c',
		# 'common/arm/neon/vp9_highbd_iht4x4_add_neon.c', # MANUAL
		# 'common/arm/neon/vp9_highbd_iht8x8_add_neon.c', # MANUAL
		# 'common/arm/neon/vp9_highbd_iht16x16_add_neon.c' # MANUAL
	),
	'sse2' : files(
		'common/x86/vp9_idct_intrin_sse2.c'
	),
	'sse4_1' : files(
		# 'common/x86/vp9_highbd_iht4x4_add_sse4.c', # MANUAL
		# 'common/x86/vp9_highbd_iht8x8_add_sse4.c', # MANUAL
		# 'common/x86/vp9_highbd_iht16x16_add_sse4.c' # MANUAL
	),
	'vp9_postproc' : files(
		'common/vp9_postproc.c',
		'common/vp9_mfqe.c'
	),
	'vsx' : files(
		'common/ppc/vp9_idct_vsx.c'
	),
}

if not features.get('vp9_highbitdepth', false) # MANUAL
	vp9_common_optional_sources += {
		'msa': vp9_common_optional_sources['msa'] + files(
			'common/mips/msa/vp9_idct4x4_msa.c',
			'common/mips/msa/vp9_idct8x8_msa.c',
			'common/mips/msa/vp9_idct16x16_msa.c',
		),
		'dspr2': vp9_common_optional_sources['dspr2'] + files(
			'common/mips/dspr2/vp9_itrans4_dspr2.c',
			'common/mips/dspr2/vp9_itrans8_dspr2.c',
			'common/mips/dspr2/vp9_itrans16_dspr2.c'
		)
	}
else
	vp9_common_optional_sources += {
		'neon': vp9_common_optional_sources['neon'] + files(
			'common/arm/neon/vp9_highbd_iht4x4_add_neon.c',
			'common/arm/neon/vp9_highbd_iht8x8_add_neon.c',
			'common/arm/neon/vp9_highbd_iht16x16_add_neon.c'
		),
		'sse4_1': vp9_common_optional_sources['sse4_1'] + files(
			'common/x86/vp9_highbd_iht4x4_add_sse4.c',
			'common/x86/vp9_highbd_iht8x8_add_sse4.c',
			'common/x86/vp9_highbd_iht16x16_add_sse4.c'
		)
	}
endif

if features.get('vp9_postproc', false) # MANUAL
	vp9_common_optional_sources += {
		'msa': vp9_common_optional_sources['msa'] + files(
			'common/mips/msa/vp9_mfqe_msa.c'
		)
	}
endif

vp9_cx_sources = files(
	'vp9_cx_iface.c',
	'encoder/vp9_bitstream.c',
	'encoder/vp9_context_tree.c',
	'encoder/vp9_cost.c',
	'encoder/vp9_dct.c',
	'encoder/vp9_encodeframe.c',
	'encoder/vp9_encodemb.c',
	'encoder/vp9_encodemv.c',
	'encoder/vp9_ethread.c',
	'encoder/vp9_extend.c',
	# 'encoder/vp9_firstpass.c', # MANUAL
	'encoder/vp9_frame_scale.c',
	'encoder/vp9_lookahead.c',
	'encoder/vp9_multi_thread.c',
	'encoder/vp9_mcomp.c',
	'encoder/vp9_encoder.c',
	'encoder/vp9_picklpf.c',
	'encoder/vp9_quantize.c',
	'encoder/vp9_ratectrl.c',
	'encoder/vp9_rd.c',
	'encoder/vp9_rdopt.c',
	'encoder/vp9_pickmode.c',
	'encoder/vp9_segmentation.c',
	'encoder/vp9_speed_features.c',
	'encoder/vp9_subexp.c',
	'encoder/vp9_svc_layercontext.c',
	'encoder/vp9_resize.c',
	'encoder/vp9_tokenize.c',
	'encoder/vp9_treewriter.c',
	# 'encoder/vp9_aq_variance.c', # MANUAL
	# 'encoder/vp9_aq_360.c', # MANUAL
	'encoder/vp9_aq_cyclicrefresh.c',
	# 'encoder/vp9_aq_complexity.c', # MANUAL
	# 'encoder/vp9_alt_ref_aq.c', # MANUAL
	'encoder/vp9_skin_detection.c',
	'encoder/vp9_noise_estimate.c',
	'encoder/vp9_ext_ratectrl.c',
	# 'encoder/vp9_temporal_filter.c', # MANUAL
	# 'encoder/vp9_mbgraph.c', # MANUAL
)

vp9_cx_optional_sources = {
	'avx' : files(
		'encoder/x86/vp9_diamond_search_sad_avx.c'
	),
	'avx2' : files(
		'encoder/x86/vp9_quantize_avx2.c',
		'encoder/x86/vp9_error_avx2.c'
	),
	'internal_stats' : files(
		'encoder/vp9_blockiness.c',
		'common/vp9_postproc.c'
	),
	'msa' : files(
		'encoder/mips/msa/vp9_error_msa.c',
		# 'encoder/mips/msa/vp9_fdct4x4_msa.c', # MANUAL
		# 'encoder/mips/msa/vp9_fdct8x8_msa.c', # MANUAL
		# 'encoder/mips/msa/vp9_fdct16x16_msa.c' # MANUAL
	),
	'neon' : files(
		'encoder/arm/neon/vp9_diamond_search_sad_neon.c',
		'encoder/arm/neon/vp9_dct_neon.c',
		# 'encoder/arm/neon/vp9_denoiser_neon.c', # MANUAL
		# 'encoder/arm/neon/vp9_error_neon.c', # MANUAL
		'encoder/arm/neon/vp9_frame_scale_neon.c',
		'encoder/arm/neon/vp9_quantize_neon.c'
	),
	'non_greedy_mv' : files(
		'encoder/vp9_non_greedy_mv.c'
	),
	'sse2' : files(
		'encoder/x86/vp9_quantize_sse2.c',
		# 'encoder/x86/vp9_highbd_block_error_intrin_sse2.c', # MANUAL
		'encoder/x86/vp9_dct_intrin_sse2.c',
		# 'encoder/x86/vp9_denoiser_sse2.c' # MANUAL
	),
	'sse4_1' : files(
		# 'encoder/x86/temporal_filter_sse4.c', # MANUAL
		# 'encoder/x86/highbd_temporal_filter_sse4.c', # MANUAL
	),
	'ssse3' : files(
		'encoder/x86/vp9_quantize_ssse3.c',
		'encoder/x86/vp9_frame_scale_ssse3.c'
	),
	'vp9_temporal_denoising' : files(
		'encoder/vp9_denoiser.c'
	),
	'vsx' : files(
		'encoder/ppc/vp9_quantize_vsx.c'
	),
}

vp9_dx_sources = files(
	'vp9_dx_iface.c',
	'decoder/vp9_decodemv.c',
	'decoder/vp9_decodeframe.c',
	'decoder/vp9_detokenize.c',
	'decoder/vp9_decoder.c',
	'decoder/vp9_dsubexp.c',
	'decoder/vp9_job_queue.c',
)

vp9_dx_optional_sources = {
}

vp9_common_headers_sources = files(
	'vp9_iface_common.h',
	'common/vp9_ppflags.h',
	'common/vp9_frame_buffers.h',
	'common/vp9_alloccommon.h',
	'common/vp9_blockd.h',
	'common/vp9_common.h',
	'common/vp9_entropy.h',
	'common/vp9_entropymode.h',
	'common/vp9_entropymv.h',
	'common/vp9_enums.h',
	'common/vp9_filter.h',
	'common/vp9_idct.h',
	'common/vp9_loopfilter.h',
	'common/vp9_thread_common.h',
	'common/vp9_mv.h',
	'common/vp9_onyxc_int.h',
	'common/vp9_pred_common.h',
	'common/vp9_quant_common.h',
	'common/vp9_reconinter.h',
	'common/vp9_reconintra.h',
	'common/vp9_scale.h',
	'common/vp9_seg_common.h',
	'common/vp9_tile_common.h',
	'common/vp9_mvref_common.h',
	'common/vp9_common_data.h',
	'common/vp9_scan.h',
)

vp9_common_headers_optional_sources = {
	'neon' : files(
		'common/arm/neon/vp9_iht_neon.h'
	),
	'vp9_postproc' : files(
		'common/vp9_postproc.h',
		'common/vp9_mfqe.h'
	),
}

vp9_cx_headers_sources = files(
	'vp9_cx_iface.h',
	'encoder/vp9_context_tree.h',
	'encoder/vp9_cost.h',
	'encoder/vp9_encodeframe.h',
	'encoder/vp9_ethread.h',
	'encoder/vp9_block.h',
	'encoder/vp9_bitstream.h',
	'encoder/vp9_encodemb.h',
	'encoder/vp9_encodemv.h',
	'encoder/vp9_extend.h',
	'encoder/vp9_firstpass.h',
	'encoder/vp9_job_queue.h',
	'encoder/vp9_lookahead.h',
	'encoder/vp9_mcomp.h',
	'encoder/vp9_multi_thread.h',
	'encoder/vp9_encoder.h',
	'encoder/vp9_quantize.h',
	'encoder/vp9_ratectrl.h',
	'encoder/vp9_rd.h',
	'encoder/vp9_rdopt.h',
	'encoder/vp9_pickmode.h',
	'encoder/vp9_svc_layercontext.h',
	'encoder/vp9_tokenize.h',
	'encoder/vp9_treewriter.h',
	'encoder/vp9_picklpf.h',
	'encoder/vp9_partition_models.h',
	'encoder/vp9_segmentation.h',
	'encoder/vp9_speed_features.h',
	'encoder/vp9_subexp.h',
	'encoder/vp9_resize.h',
	# 'encoder/vp9_aq_variance.h', # MANUAL
	# 'encoder/vp9_aq_360.h', # MANUAL
	'encoder/vp9_aq_cyclicrefresh.h', # MANUAL
	# 'encoder/vp9_aq_complexity.h', # MANUAL
	# 'encoder/vp9_alt_ref_aq.h', # MANUAL
	'encoder/vp9_skin_detection.h',
	'encoder/vp9_noise_estimate.h',
	'encoder/vp9_ext_ratectrl.h',
	'encoder/vp9_temporal_filter.h',
	'encoder/vp9_mbgraph.h',
)

vp9_cx_headers_optional_sources = {
	'internal_stats' : files(
		'encoder/vp9_blockiness.h',
		'common/vp9_postproc.h'
	),
	'msa' : files(
		# 'encoder/mips/msa/vp9_fdct_msa.h' # MANUAL
	),
	'non_greedy_mv' : files(
		'encoder/vp9_non_greedy_mv.h'
	),
	'sse4_1' : files(
		# 'encoder/x86/temporal_filter_constants.h' # MANUAL
	),
	'vp9_temporal_denoising' : files(
		'encoder/vp9_denoiser.h'
	),
}

vp9_cx_remove_headers_optional_sources = {
	'realtime_only' : files(
		'encoder/x86/temporal_filter_constants.h',
		'encoder/vp9_alt_ref_aq.h',
		'encoder/vp9_aq_variance.h',
		'encoder/vp9_aq_360.h',
		'encoder/vp9_aq_complexity.h'
	),
}

vp9_dx_headers_sources = files(
	'vp9_dx_iface.h',
	'decoder/vp9_decodeframe.h',
	'decoder/vp9_decodemv.h',
	'decoder/vp9_detokenize.h',
	'decoder/vp9_decoder.h',
	'decoder/vp9_dsubexp.h',
	'decoder/vp9_job_queue.h',
)

vp9_dx_headers_optional_sources = {
}

vp9_common_asm_optional_sources = {
	'sse2' : files(
		# 'common/x86/vp9_mfqe_sse2.asm' # MANUAL
	),
}

if features.get('vp9_postproc', false) # MANUAL
	vp9_common_optional_sources += {
		'sse2': vp9_common_asm_optional_sources['sse2'] + files(
			'common/x86/vp9_mfqe_sse2.asm'
		)
	}
endif

vp9_cx_asm_optional_sources = {
	'sse2' : files(
		'encoder/x86/vp9_dct_sse2.asm',
		'encoder/x86/vp9_error_sse2.asm'
	),
}

if features.get('vp9_temporal_denoising', false)
	vp9_cx_optional_sources += {
		'sse2' : vp9_cx_optional_sources['sse2'] + files(
			'encoder/x86/vp9_denoiser_sse2.c',
		),
		'neon' : vp9_cx_optional_sources['neon'] + files(
			'encoder/arm/neon/vp9_denoiser_neon.c',
		),
	}
endif

if features.get('vp9_highbitdepth', false)
	vp9_cx_optional_sources += {
		'sse2' : vp9_cx_optional_sources['sse2'] + files(
			'encoder/x86/vp9_highbd_block_error_intrin_sse2.c',
		),
	}
else
	vp9_cx_optional_sources += {
		'neon' : vp9_cx_optional_sources['neon'] + files(
			'encoder/arm/neon/vp9_error_neon.c',
		),
		'msa' : vp9_cx_optional_sources['msa'] + files(
			'encoder/mips/msa/vp9_fdct4x4_msa.c',
			'encoder/mips/msa/vp9_fdct8x8_msa.c',
			'encoder/mips/msa/vp9_fdct16x16_msa.c'
		),
	}

	vp9_cx_headers_optional_sources += {
		'msa' : vp9_cx_headers_optional_sources['msa'] + files(
			'encoder/mips/msa/vp9_fdct_msa.h'
		),
	}
endif

if not features.get('realtime_only', false)
	vp9_cx_sources += files(
		'encoder/vp9_firstpass.c',
		'encoder/vp9_mbgraph.c',
		'encoder/vp9_temporal_filter.c',
		'encoder/vp9_alt_ref_aq.c',
		'encoder/vp9_aq_variance.c',
		'encoder/vp9_aq_360.c',
		'encoder/vp9_aq_complexity.c'
	)

	vp9_cx_headers_sources += files(
		'encoder/vp9_alt_ref_aq.h',
		'encoder/vp9_aq_variance.h',
		'encoder/vp9_aq_360.h',
		'encoder/vp9_aq_complexity.h'
	)

	vp9_cx_optional_sources += {
		'sse4_1' : vp9_cx_optional_sources['sse4_1'] + files(
			'encoder/x86/temporal_filter_sse4.c',
		),
	}

	vp9_cx_headers_optional_sources += {
		'sse4_1' : vp9_cx_headers_optional_sources['sse4_1'] + files(
			'encoder/x86/temporal_filter_constants.h'
		),
	}

	if not features.get('vp9_highbitdepth', true)
		vp9_cx_optional_sources += {
			'sse4_1' : vp9_cx_optional_sources['sse4_1'] + files(
				'encoder/x86/highbd_temporal_filter_sse4.c',
			),
		}
	endif
endif

#### --- END GENERATED --- ####

codec_srcs += vp9_common_sources
optional_sources = get_variable('vp9_common_optional_sources', {})
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


optional_sources = get_variable('vp9_common_asm_optional_sources', {})
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

codec_headers += vp9_common_headers_sources
optional_sources = get_variable('vp9_common_headers_optional_sources', {})
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

if features.get('vp9_encoder', false)
	codec_srcs += vp9_cx_sources
	codec_headers += vp9_cx_headers_sources

	optional_sources = get_variable('vp9_cx_optional_sources', {})
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

	optional_sources = get_variable('vp9_cx_asm_optional_sources', {})
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

	optional_sources = get_variable('vp9_cx_headers_optional_sources', {})
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
endif

if features.get('vp9_encoder', false)
	codec_srcs += vp9_dx_sources
	codec_headers += vp9_dx_headers_sources

	optional_sources = get_variable('vp9_dx_optional_sources', {})
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

	optional_sources = get_variable('vp9_dx_asm_optional_sources', {})
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

	optional_sources = get_variable('vp9_dx_headers_optional_sources', {})
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
endif

vp9_rtcd_defs = meson.current_source_dir() / 'common/vp9_rtcd_defs.py'

codec_rtcds += {
	'vp9_rtcd': vp9_rtcd_defs
}

codec_headers += files(vp9_rtcd_defs)

if features.get('vp9_encoder', false)
	codec_exports += files(
		'exports_enc',
	)
endif

if features.get('vp9_decoder', false)
	codec_exports += files(
		'exports_dec',
	)
endif
