# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vpx_dsp.mk

#### --- GENERATED --- ####

dsp_sources = files(
	'prob.c',
	# 'bitwriter.c', # MANUAL
	# 'bitwriter_buffer.c', # MANUAL
	# 'psnr.c', # MANUAL
	# 'bitreader.c', # MANUAL
	# 'bitreader_buffer.c', # MANUAL
	'intrapred.c',
	# 'add_noise.c', # MANUAL
	# 'deblock.c', # MANUAL
	# 'vpx_convolve.c', # MANUAL
	# 'arm/vpx_convolve_copy_neon_asm.asm', # MANUAL
	# 'arm/vpx_convolve8_horiz_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_vert_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_horiz_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_vert_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_horiz_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_vert_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_horiz_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_vert_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve_avg_neon_asm.asm', # MANUAL
	# 'arm/vpx_convolve8_neon_asm.c', # MANUAL
	# 'arm/vpx_convolve_neon.c', # MANUAL
	# 'arm/vpx_convolve_copy_neon.c', # MANUAL
	# 'arm/vpx_convolve8_neon.c', # MANUAL
	# 'arm/vpx_convolve_avg_neon.c', # MANUAL
	# 'arm/vpx_convolve_neon.c', # MANUAL
	# 'loopfilter.c', # MANUAL
	# 'arm/loopfilter_16_neon.asm', # MANUAL
	# 'arm/loopfilter_8_neon.asm', # MANUAL
	# 'arm/loopfilter_4_neon.asm', # MANUAL
	# 'fwd_txfm.c', # MANUAL
	# 'inv_txfm.c', # MANUAL
	# 'arm/idct_neon.asm', # MANUAL
	# 'arm/idct4x4_1_add_neon.asm', # MANUAL
	# 'arm/idct4x4_add_neon.asm', # MANUAL
	# 'quantize.c', # MANUAL
	# 'avg.c', # MANUAL
	'skin_detection.c',
	# 'sad.c', # MANUAL
	# 'subtract.c', # MANUAL
	# 'sum_squares.c', # MANUAL
	# 'variance.c', # MANUAL
	'vpx_dsp_rtcd.c',
)

dsp_optional_sources = {
	'avx' : files(
		# 'x86/quantize_avx.c' # MANUAL
	),
	'avx2' : files(
		# 'x86/vpx_subpixel_8t_intrin_avx2.c', # MANUAL
		# 'x86/highbd_convolve_avx2.c', # MANUAL
		# 'x86/loopfilter_avx2.c', # MANUAL
		# 'x86/fwd_txfm_avx2.c', # MANUAL
		# 'x86/quantize_avx2.c', # MANUAL
		# 'x86/highbd_quantize_intrin_avx2.c', # MANUAL
		# 'x86/avg_intrin_avx2.c', # MANUAL
		# 'x86/sad4d_avx2.c', # MANUAL
		# 'x86/sad_avx2.c', # MANUAL
		# 'x86/subtract_avx2.c', # MANUAL
		# 'x86/highbd_sad4d_avx2.c', # MANUAL
		# 'x86/highbd_sad_avx2.c', # MANUAL
		# 'x86/variance_avx2.c' # MANUAl
	),
	'avx512' : files(
		# 'x86/sad4d_avx512.c' # MANUAL
	),
	'dspr2' : files(
		'mips/intrapred4_dspr2.c',
		'mips/intrapred8_dspr2.c',
		'mips/intrapred16_dspr2.c',
		'mips/common_dspr2.c',
		# 'mips/convolve2_avg_dspr2.c', # MANUAL
		# 'mips/convolve2_avg_horiz_dspr2.c', # MANUAL
		# 'mips/convolve2_dspr2.c', # MANUAL
		# 'mips/convolve2_horiz_dspr2.c', # MANUAL
		# 'mips/convolve2_vert_dspr2.c', # MANUAL
		# 'mips/convolve8_avg_dspr2.c', # MANUAL
		# 'mips/convolve8_avg_horiz_dspr2.c', # MANUAL
		# 'mips/convolve8_dspr2.c', # MANUAL
		# 'mips/convolve8_horiz_dspr2.c', # MANUAL
		# 'mips/convolve8_vert_dspr2.c', # MANUAL
		# 'mips/loopfilter_filters_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_horiz_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_vert_dspr2.c', # MANUAL
		# 'mips/itrans4_dspr2.c', # MANUAL
		# 'mips/itrans8_dspr2.c', # MANUAL
		# 'mips/itrans16_dspr2.c', # MANUAL
		# 'mips/itrans32_dspr2.c', # MANUAL
		# 'mips/itrans32_cols_dspr2.c' # MANUAL
	),
	'internal_stats' : files(
		# 'ssim.c', # MANUAL
		# 'psnrhvs.c', # MANUAL
		# 'fastssim.c' # MANUAL
	),
	'lsx' : files(
		'loongarch/intrapred_lsx.c',
		# 'loongarch/vpx_convolve8_avg_horiz_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_avg_vert_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_horiz_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_vert_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_avg_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve_avg_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve_copy_lsx.c', # MANUAL
		# 'loongarch/loopfilter_16_lsx.c', # MANUAL
		# 'loongarch/loopfilter_8_lsx.c', # MANUAL
		# 'loongarch/loopfilter_4_lsx.c', # MANUAL
		# 'loongarch/fwd_txfm_lsx.c', # MANUAL
		# 'loongarch/fwd_dct32x32_lsx.c', # MANUAL
		# 'loongarch/idct32x32_lsx.c', # MANUAL
		# 'loongarch/quantize_lsx.c', # MANUAL
		# 'loongarch/avg_lsx.c', # MANUAL
		# 'loongarch/sad_lsx.c', # MANUAL
		# 'loongarch/subtract_lsx.c', # MANUAL
		# 'loongarch/variance_lsx.c', # MANUAL
		# 'loongarch/sub_pixel_variance_lsx.c', # MANUAL
		# 'loongarch/avg_pred_lsx.c' # MANUAl
	),
	'mmi' : files(
		# 'mips/vpx_convolve8_mmi.c', # MANUAL
		# 'mips/sad_mmi.c', # MANUAL
		# 'mips/subtract_mmi.c', # MANUAL
		# 'mips/variance_mmi.c' # MANUAl
	),
	'msa' : files(
		# 'mips/add_noise_msa.c', # MANUAL
		# 'mips/deblock_msa.c', # MANUAL
		'mips/intrapred_msa.c',
		# 'mips/vpx_convolve8_avg_horiz_msa.c', # MANUAL
		# 'mips/vpx_convolve8_avg_msa.c', # MANUAL
		# 'mips/vpx_convolve8_avg_vert_msa.c', # MANUAL
		# 'mips/vpx_convolve8_horiz_msa.c', # MANUAL
		# 'mips/vpx_convolve8_msa.c', # MANUAL
		# 'mips/vpx_convolve8_vert_msa.c', # MANUAL
		# 'mips/vpx_convolve_avg_msa.c', # MANUAL
		# 'mips/vpx_convolve_copy_msa.c', # MANUAL
		# 'mips/loopfilter_16_msa.c', # MANUAL
		# 'mips/loopfilter_8_msa.c', # MANUAL
		# 'mips/loopfilter_4_msa.c', # MANUAL
		# 'mips/fwd_txfm_msa.c', # MANUAL
		# 'mips/fwd_dct32x32_msa.c', # MANUAL
		# 'mips/idct4x4_msa.c', # MANUAL
		# 'mips/idct8x8_msa.c', # MANUAL
		# 'mips/idct16x16_msa.c', # MANUAL
		# 'mips/idct32x32_msa.c', # MANUAL
		# 'mips/avg_msa.c', # MANUAL
		# 'mips/sum_squares_msa.c', # MANUAL
		# 'mips/sad_msa.c', # MANUAL
		# 'mips/subtract_msa.c', # MANUAL
		# 'mips/variance_msa.c', # MANUAL
		# 'mips/sub_pixel_variance_msa.c' # MANUAL
	),
	'neon' : files(
		# 'arm/highbd_intrapred_neon.c', # MANUAL
		# 'arm/deblock_neon.c', # MANUAL
		'arm/intrapred_neon.c',
		# 'arm/highbd_vpx_convolve_copy_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve_avg_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve8_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve_neon.c', # MANUAL
		# 'arm/vpx_scaled_convolve8_neon.c', # MANUAL
		# 'arm/loopfilter_neon.c', # MANUAL
		# 'arm/highbd_loopfilter_neon.c', # MANUAL
		# 'arm/fdct4x4_neon.c', # MANUAL
		# 'arm/fdct8x8_neon.c', # MANUAL
		# 'arm/fdct16x16_neon.c', # MANUAL
		# 'arm/fdct32x32_neon.c', # MANUAL
		# 'arm/fdct_partial_neon.c', # MANUAL
		# 'arm/highbd_idct4x4_add_neon.c', # MANUAL
		# 'arm/highbd_idct8x8_add_neon.c', # MANUAL
		# 'arm/highbd_idct16x16_add_neon.c', # MANUAL
		# 'arm/highbd_idct32x32_add_neon.c', # MANUAL
		# 'arm/highbd_idct32x32_34_add_neon.c', # MANUAL
		# 'arm/highbd_idct32x32_135_add_neon.c', # MANUAL
		# 'arm/highbd_idct32x32_1024_add_neon.c', # MANUAL
		# 'arm/idct4x4_1_add_neon.c', # MANUAL
		# 'arm/idct4x4_add_neon.c', # MANUAL
		# 'arm/idct8x8_1_add_neon.c', # MANUAL
		# 'arm/idct8x8_add_neon.c', # MANUAL
		# 'arm/idct16x16_1_add_neon.c', # MANUAL
		# 'arm/idct16x16_add_neon.c', # MANUAL
		# 'arm/idct32x32_1_add_neon.c', # MANUAL
		# 'arm/idct32x32_34_add_neon.c', # MANUAL
		# 'arm/idct32x32_135_add_neon.c', # MANUAL
		# 'arm/idct32x32_add_neon.c', # MANUAL
		# 'arm/quantize_neon.c', # MANUAL
		# 'arm/highbd_quantize_neon.c', # MANUAL
		# 'arm/avg_neon.c', # MANUAL
		# 'arm/hadamard_neon.c', # MANUAL
		# 'arm/sum_squares_neon.c', # MANUAL
		# 'arm/sad4d_neon.c', # MANUAL
		# 'arm/sad_neon.c', # MANUAL
		# 'arm/subtract_neon.c', # MANUAL
		# 'arm/highbd_sad_neon.c', # MANUAL
		# 'arm/avg_pred_neon.c', # MANUAL
		# 'arm/subpel_variance_neon.c', # MANUAL
		# 'arm/variance_neon.c', # MANUAL
		# 'arm/highbd_variance_neon.c' # MANUAL
	),
	'neon_asm' : files(
		# 'arm/intrapred_neon_asm.asm', # MANUAL
		# 'arm/save_reg_neon.asm' # MANUAL
	),
	'sse2' : files(
		# 'x86/highbd_intrapred_intrin_sse2.c', # MANUAL
		# 'x86/post_proc_sse2.c', # MANUAL
		# 'x86/vpx_subpixel_4t_intrin_sse2.c', # MANUAL
		# 'x86/loopfilter_sse2.c', # MANUAL
		# 'x86/highbd_loopfilter_sse2.c', # MANUAL
		# 'x86/fwd_txfm_sse2.c', # MANUAL
		# 'x86/inv_txfm_sse2.c', # MANUAL
		# 'x86/highbd_idct4x4_add_sse2.c', # MANUAL
		# 'x86/highbd_idct8x8_add_sse2.c', # MANUAL
		# 'x86/highbd_idct16x16_add_sse2.c', # MANUAL
		# 'x86/highbd_idct32x32_add_sse2.c', # MANUAL
		# 'x86/quantize_sse2.c', # MANUAL
		# 'x86/highbd_quantize_intrin_sse2.c', # MANUAL
		# 'x86/avg_intrin_sse2.c', # MANUAL
		# 'x86/sum_squares_sse2.c', # MANUAL
		# 'x86/avg_pred_sse2.c', # MANUAL
		# 'x86/variance_sse2.c', # MANUAL
		# 'x86/highbd_variance_sse2.c' # MANUAL
	),
	'sse4_1' : files(
		# 'x86/highbd_idct4x4_add_sse4.c', # MANUAL
		# 'x86/highbd_idct8x8_add_sse4.c', # MANUAL
		# 'x86/highbd_idct16x16_add_sse4.c', # MANUAL
		# 'x86/highbd_idct32x32_add_sse4.c' # MANUAL
	),
	'ssse3' : files(
		# 'x86/highbd_intrapred_intrin_ssse3.c', # MANUAL
		# 'x86/vpx_subpixel_8t_intrin_ssse3.c', # MANUAL
		# 'x86/inv_txfm_ssse3.c', # MANUAL
		# 'x86/quantize_ssse3.c' # MANUAL
	),
	'vsx' : files(
		'ppc/intrapred_vsx.c',
		# 'ppc/deblock_vsx.c', # MANUAL
		# 'ppc/vpx_convolve_vsx.c', # MANUAL
		# 'ppc/fdct32x32_vsx.c', # MANUAL
		# 'ppc/inv_txfm_vsx.c', # MANUAL
		# 'ppc/quantize_vsx.c', # MANUAL
		# 'ppc/hadamard_vsx.c', # MANUAL
		# 'ppc/sad_vsx.c', # MANUAL
		# 'ppc/subtract_vsx.c', # MANUAl
		# 'ppc/variance_vsx.c' # MANUAl
	),
}

dsp_headers_sources = files(
	'vpx_dsp_common.h',
	'prob.h',
	# 'bitwriter.h', # MANUAL
	# 'bitwriter_buffer.h', # MANUAL
	# 'psnr.h', # MANUAL
	# 'bitreader.h', # MANUAL
	# 'bitreader_buffer.h', # MANUAL
	# 'postproc.h', # MANUAL
	'vpx_filter.h',
	# 'vpx_convolve.h', # MANUAL
	# 'arm/vpx_convolve8_neon_asm.h', # MANUAL
	'txfm_common.h',
	# 'fwd_txfm.h', # MANUAL
	# 'inv_txfm.h', # MANUAL
	# 'quantize.h', # MANUAL
	'skin_detection.h',
	# 'variance.h', # MANUAL
)

dsp_headers_optional_sources = {
	'avx2' : files(
		'x86/bitdepth_conversion_avx2.h',
		# 'x86/convolve_avx2.h', # MANUAL
		# 'x86/fwd_dct32x32_impl_avx2.h' # MANUAL
	),
	'dspr2' : files(
		'mips/common_dspr2.h',
		# 'mips/convolve_common_dspr2.h', # MANUAL
		# 'mips/loopfilter_filters_dspr2.h', # MANUAL
		# 'mips/loopfilter_macros_dspr2.h', # MANUAL
		# 'mips/loopfilter_masks_dspr2.h', # MANUAL
		# 'mips/inv_txfm_dspr2.h' # MANUAL
	),
	'internal_stats' : files(
		# 'ssim.h' # MANUAL
	),
	'lsx' : files(
		# 'loongarch/vpx_convolve_lsx.h', # MANUAL
		# 'loongarch/loopfilter_lsx.h', # MANUAL
		'loongarch/txfm_macros_lsx.h',
		# 'loongarch/fwd_txfm_lsx.h', # MANUAL
		# 'loongarch/variance_lsx.h', # MANUAL
		'loongarch/bitdepth_conversion_lsx.h'
	),
	'msa' : files(
		'mips/macros_msa.h',
		# 'mips/vpx_convolve_msa.h', # MANUAL
		# 'mips/loopfilter_msa.h', # MANUAL
		'mips/txfm_macros_msa.h',
		# 'mips/fwd_txfm_msa.h', # MANUAL
		# 'mips/inv_txfm_msa.h' # MANUAL
	),
	'neon' : files(
		# 'arm/highbd_idct_neon.h', # MANUAL
		'arm/idct_neon.h',
		'arm/mem_neon.h',
		'arm/sum_neon.h',
		'arm/transpose_neon.h',
		'arm/vpx_convolve8_neon.h'
	),
	'sse2' : files(
		'x86/bitdepth_conversion_sse2.h',
		# 'x86/convolve_sse2.h', # MANUAL
		'x86/txfm_common_sse2.h',
		# 'x86/fwd_txfm_sse2.h', # MANUAL
		# 'x86/fwd_txfm_impl_sse2.h', # MANUAL
		# 'x86/fwd_dct32x32_impl_sse2.h', # MANUAL
		# 'x86/inv_txfm_sse2.h', # MANUAL
		# 'x86/highbd_inv_txfm_sse2.h', # MANUAL
		# 'x86/quantize_sse2.h', # MANUAL
		'x86/mem_sse2.h',
		'x86/transpose_sse2.h'
	),
	'sse4_1' : files(
		# 'x86/highbd_inv_txfm_sse4.h' # MANUAL
	),
	'ssse3' : files(
		# 'x86/convolve_ssse3.h', # MANUAL
		# 'x86/inv_txfm_ssse3.h', # MANUAL
		# 'x86/quantize_ssse3.h' # MANUAL
	),
	'vsx' : files(
		'ppc/types_vsx.h',
		'ppc/txfm_common_vsx.h',
		'ppc/transpose_vsx.h',
		'ppc/bitdepth_conversion_vsx.h'
	),
}

dsp_asm_optional_sources = {
	'sse2' : files(
		'x86/intrapred_sse2.asm',
		# 'x86/highbd_intrapred_sse2.asm', # MANUAL
		# 'x86/add_noise_sse2.asm', # MANUAL
		# 'x86/deblock_sse2.asm', # MANUAL
		# 'x86/vpx_subpixel_8t_sse2.asm', # MANUAL
		# 'x86/vpx_subpixel_bilinear_sse2.asm', # MANUAL
		# 'x86/vpx_high_subpixel_8t_sse2.asm', # MANUAL
		# 'x86/vpx_high_subpixel_bilinear_sse2.asm', # MANUAL
		# 'x86/vpx_convolve_copy_sse2.asm', # MANUAL
		# 'x86/inv_wht_sse2.asm', # MANUAL
		# 'x86/sad4d_sse2.asm', # MANUAL
		# 'x86/sad_sse2.asm', # MANUAL
		# 'x86/subtract_sse2.asm', # MANUAL
		# 'x86/highbd_sad4d_sse2.asm', # MANUAL
		# 'x86/highbd_sad_sse2.asm', # MANUAL
		# 'x86/ssim_opt_x86_64.asm', # MANUAL
		# 'x86/subpel_variance_sse2.asm', # MANUAL
		# 'x86/highbd_variance_impl_sse2.asm', # MANUAL
		# 'x86/highbd_subpel_variance_impl_sse2.asm' # MANUAL
	),
	'ssse3' : files(
		'x86/intrapred_ssse3.asm',
		# 'x86/vpx_subpixel_8t_ssse3.asm', # MANUAL
		# 'x86/vpx_subpixel_bilinear_ssse3.asm', # MANUAL
		# 'x86/fwd_txfm_ssse3_x86_64.asm', # MANUAL
		# 'x86/avg_ssse3_x86_64.asm' # MANUAL
	),
}


if features.get('encoders', false) # MANUAL
	dsp_sources += files(
		'bitwriter.c',
		'bitwriter_buffer.c',
		'psnr.c',
	)

	dsp_headers_sources += files(
		'bitwriter.h',
		'bitwriter_buffer.h',
		'psnr.h',
	)

	dsp_optional_sources += {
		'internal_stats' : dsp_optional_sources['internal_stats'] + files(
			'ssim.c',
			'psnrhvs.c',
			'fastssim.c'
		),
	}

	dsp_headers_optional_sources += {
		'internal_stats' : dsp_headers_optional_sources['internal_stats'] + files(
			'ssim.h'
		),
	}
endif

if features.get('encoders', false) # MANUAL
	dsp_sources += files(
		'bitreader.c',
		'bitreader_buffer.c',
	)

	dsp_headers_sources += files(
		'bitreader.h',
		'bitreader_buffer.h',
	)
endif

# intra predictions
if features.get('vp9_highbitdepth', false) # MANUAL
	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/highbd_intrapred_sse2.asm',
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/highbd_intrapred_intrin_sse2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/highbd_intrapred_intrin_ssse3.c',
		),
		'neon' : dsp_optional_sources['ssse3'] + files(
			'arm/highbd_intrapred_neon.c',
		),
	}
endif

# intra predictions
if not features.get('postproc', false) or not features.get('vp9_postproc', false) # MANUAL
	dsp_sources += files(
		'add_noise.c',
		'deblock.c',
	)

	dsp_headers_sources += files(
		'postproc.h',
	)

	dsp_optional_sources += {
		'msa' : dsp_optional_sources['msa'] + files(
			'mips/add_noise_msa.c',
			'mips/deblock_msa.c',
		),
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/deblock_neon.c',
		),
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/post_proc_sse2.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/deblock_vsx.c',
		),
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/add_noise_sse2.asm',
			'x86/deblock_sse2.asm',
		),
		'ssse3' : dsp_asm_optional_sources['ssse3'] + files(
			'x86/vpx_subpixel_8t_ssse3.asm',
			'x86/vpx_subpixel_bilinear_ssse3.asm',
		)
	}
endif

if features.get('neon_asm', false) # MANUAL
	dsp_sources += asm_transformer.process(
		files(
			'arm/intrapred_neon_asm.asm',
		)
	)
endif

if features.get('vp9', false) # MANUAL
	# interpolation filters

	dsp_sources += files(
		'vpx_convolve.c',
		# loop filters
		'loopfilter.c',
	)

	dsp_headers_sources += files(
		'vpx_convolve.h',
	)

	dsp_headers_optional_sources += {
		'x86' : files(
			'x86/convolve.h',
		),
		'x86_64' : files(
			'x86/convolve.h',
		),
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/convolve_sse2.h',
		),
		'ssse3' : dsp_headers_optional_sources['ssse3'] + files(
			'x86/convolve_ssse3.h',
		),
		'avx2' : dsp_headers_optional_sources['avx2'] + files(
			'x86/convolve_avx2.h',
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			# common (msa)
			'mips/vpx_convolve_msa.h',
			# loop filters
			'mips/loopfilter_msa.h',
		),
		'dspr2' : dsp_headers_optional_sources['dspr2'] + files(
			# common (dspr2)
			'mips/convolve_common_dspr2.h',
			# loop filters
			'mips/loopfilter_filters_dspr2.h',
			'mips/loopfilter_macros_dspr2.h',
			'mips/loopfilter_masks_dspr2.h',
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			# common (lsx)
			'loongarch/vpx_convolve_lsx.h',
			# loop filters
			'loongarch/loopfilter_lsx.h',
		)
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/vpx_subpixel_8t_sse2.asm',
			'x86/vpx_subpixel_bilinear_sse2.asm',
			'x86/vpx_convolve_copy_sse2.asm',
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/vpx_subpixel_4t_intrin_sse2.c',
			# loop filters
			'x86/loopfilter_sse2.c',
		),
		'avx2' : dsp_optional_sources['avx2'] + files(
			'x86/vpx_subpixel_8t_intrin_avx2.c',
			# loop filters
			'x86/loopfilter_avx2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/vpx_subpixel_8t_intrin_ssse3.c',
		),
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/vpx_scaled_convolve8_neon.c',
		),
		'msa' : dsp_optional_sources['msa'] + files(
			# common (msa)
			'mips/vpx_convolve8_avg_horiz_msa.c',
			'mips/vpx_convolve8_avg_msa.c',
			'mips/vpx_convolve8_avg_vert_msa.c',
			'mips/vpx_convolve8_horiz_msa.c',
			'mips/vpx_convolve8_msa.c',
			'mips/vpx_convolve8_vert_msa.c',
			'mips/vpx_convolve_avg_msa.c',
			'mips/vpx_convolve_copy_msa.c',
			# loop filters
			'mips/loopfilter_16_msa.c',
			'mips/loopfilter_8_msa.c',
			'mips/loopfilter_4_msa.c',
		),
		'mmi' : dsp_optional_sources['mmi'] + files(
			'mips/vpx_convolve8_mmi.c',
		),
		'dspr2' : dsp_optional_sources['dspr2'] + files(
			# common (dspr2)
			'mips/convolve2_avg_dspr2.c',
			'mips/convolve2_avg_horiz_dspr2.c',
			'mips/convolve2_dspr2.c',
			'mips/convolve2_horiz_dspr2.c',
			'mips/convolve2_vert_dspr2.c',
			'mips/convolve8_avg_dspr2.c',
			'mips/convolve8_avg_horiz_dspr2.c',
			'mips/convolve8_dspr2.c',
			'mips/convolve8_horiz_dspr2.c',
			'mips/convolve8_vert_dspr2.c',
			# loop filters
			'mips/loopfilter_filters_dspr2.c',
			'mips/loopfilter_mb_dspr2.c',
			'mips/loopfilter_mb_horiz_dspr2.c',
			'mips/loopfilter_mb_vert_dspr2.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/vpx_convolve_vsx.c',
		),
		'lsx' : dsp_optional_sources['lsx'] + files(
			# common (lsx)
			'loongarch/vpx_convolve8_avg_horiz_lsx.c',
			'loongarch/vpx_convolve8_avg_vert_lsx.c',
			'loongarch/vpx_convolve8_horiz_lsx.c',
			'loongarch/vpx_convolve8_vert_lsx.c',
			'loongarch/vpx_convolve8_lsx.c',
			'loongarch/vpx_convolve8_avg_lsx.c',
			'loongarch/vpx_convolve_avg_lsx.c',
			'loongarch/vpx_convolve_copy_lsx.c',
			# loop filters
			'loongarch/loopfilter_16_lsx.c',
			'loongarch/loopfilter_8_lsx.c',
			'loongarch/loopfilter_4_lsx.c',
		)
	}

	if features.get('vp9_highbitdepth', false)
		dsp_asm_optional_sources += {
			'sse2' : dsp_asm_optional_sources['sse2'] + files(
				'x86/vpx_high_subpixel_8t_sse2.asm',
				'x86/vpx_high_subpixel_bilinear_sse2.asm',
			)
		}

		dsp_optional_sources += {
			'avx2' : dsp_optional_sources['avx2'] + files(
				'x86/highbd_convolve_avx2.c'
			),
			'sse2' : dsp_optional_sources['sse2'] + files(
				# loop filters
				'x86/highbd_loopfilter_sse2.c'
			),
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_vpx_convolve_copy_neon.c',
				'arm/highbd_vpx_convolve_avg_neon.c',
				'arm/highbd_vpx_convolve8_neon.c',
				'arm/highbd_vpx_convolve_neon.c',
				# loop filters
				'arm/highbd_loopfilter_neon.c',
			)
		}
	endif

	if features.get('neon_asm', false)
		dsp_sources += asm_transformer.process(
			files(
				'arm/vpx_convolve_copy_neon_asm.asm',
				'arm/vpx_convolve8_horiz_filter_type2_neon.asm',
				'arm/vpx_convolve8_vert_filter_type2_neon.asm',
				'arm/vpx_convolve8_horiz_filter_type1_neon.asm',
				'arm/vpx_convolve8_vert_filter_type1_neon.asm',
				'arm/vpx_convolve8_avg_horiz_filter_type2_neon.asm',
				'arm/vpx_convolve8_avg_vert_filter_type2_neon.asm',
				'arm/vpx_convolve8_avg_horiz_filter_type1_neon.asm',
				'arm/vpx_convolve8_avg_vert_filter_type1_neon.asm',
				'arm/vpx_convolve_avg_neon_asm.asm',
				# loop filters
				'arm/loopfilter_16_neon.asm',
				'arm/loopfilter_8_neon.asm',
				'arm/loopfilter_4_neon.asm',
			)
		)

		dsp_sources += files(
			'arm/vpx_convolve8_neon_asm.c',
			'arm/vpx_convolve_neon.c',
		)

		dsp_headers_sources += files(
			'arm/vpx_convolve8_neon_asm.h',
		)
	elif features.get('neon', false)
		dsp_sources += files(
			'arm/vpx_convolve_copy_neon.c',
			'arm/vpx_convolve8_neon.c',
			'arm/vpx_convolve_avg_neon.c',
			'arm/vpx_convolve_neon.c',
			# loop filters
			'arm/loopfilter_neon.c',
		)
	endif
endif

# forward transform
if features.get('vp9_encoder', false)
	dsp_sources += files(
		'fwd_txfm.c',
	)

	dsp_headers_sources += files(
		'fwd_txfm.h',
	)

	dsp_headers_optional_sources += {
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/fwd_txfm_sse2.h',
			'x86/fwd_txfm_impl_sse2.h',
			'x86/fwd_dct32x32_impl_sse2.h',
		),
		'avx2' : dsp_headers_optional_sources['avx2'] + files(
			'x86/fwd_dct32x32_impl_avx2.h'
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			'mips/fwd_txfm_msa.h'
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			'loongarch/fwd_txfm_lsx.h'
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/fwd_txfm_sse2.c',
		),
		'neon': dsp_optional_sources['neon'] + files(
			'arm/fdct4x4_neon.c',
			'arm/fdct8x8_neon.c',
			'arm/fdct16x16_neon.c',
			'arm/fdct32x32_neon.c',
			'arm/fdct_partial_neon.c',
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			'mips/fwd_txfm_msa.c',
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			'loongarch/fwd_txfm_lsx.c',
		),
		'vsx' : dsp_headers_optional_sources['vsx'] + files(
			'ppc/fdct32x32_vsx.c',
		),
	}

	if features.get('x86_64', false)
		dsp_asm_optional_sources += {
			'ssse3' : dsp_asm_optional_sources['ssse3'] + files(
				'x86/fwd_txfm_ssse3_x86_64.asm',
			)
		}
	endif

	if not features.get('vp9_highbitdepth', false)
		dsp_optional_sources += {
			'avx2' : dsp_optional_sources['avx2'] + files(
				'x86/fwd_txfm_avx2.c'
			),
			'msa' : dsp_optional_sources['msa'] + files(
				# loop filters
				'mips/fwd_dct32x32_msa.c'
			),
			'lsx' : dsp_optional_sources['lsx'] + files(
				# loop filters
				'loongarch/fwd_dct32x32_lsx.c',
			)
		}
	endif
endif

# inverse transform
if features.get('vp9', true) # MANUAL
	dsp_sources += files(
		'inv_txfm.c',
	)

	dsp_headers_sources += files(
		'inv_txfm.h',
	)

	dsp_headers_optional_sources += {
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/inv_txfm_sse2.h',
		),
		'ssse3' : dsp_headers_optional_sources['ssse3'] + files(
			'x86/inv_txfm_ssse3.h',
		),
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/inv_txfm_sse2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/inv_txfm_ssse3.c',
		),
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/fdct4x4_neon.c',
			'arm/fdct8x8_neon.c',
			'arm/fdct16x16_neon.c',
			'arm/fdct32x32_neon.c',
			'arm/fdct_partial_neon.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/inv_txfm_vsx.c',
		)
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/inv_wht_sse2.asm',
		),
	}

	if features.get('neon_asm', false)
		dsp_sources += asm_transformer.process(
			files(
				'arm/save_reg_neon.asm',
			)
		)
	endif

	if not features.get('vp9_highbitdepth', false)
		dsp_headers_optional_sources += {
			'msa' : dsp_headers_optional_sources['msa'] + files(
				'mips/inv_txfm_msa.h',
			),
			'dspr2' : dsp_headers_optional_sources['dspr2'] + files(
				'mips/inv_txfm_dspr2.h',
			)
		}

		dsp_optional_sources += {
			'msa' : dsp_optional_sources['msa'] + files(
				'mips/idct4x4_msa.c',
				'mips/idct8x8_msa.c',
				'mips/idct16x16_msa.c',
				'mips/idct32x32_msa.c',
			),
			'dspr2' : dsp_optional_sources['dspr2'] + files(
				'mips/itrans4_dspr2.c',
				'mips/itrans8_dspr2.c',
				'mips/itrans16_dspr2.c',
				'mips/itrans32_dspr2.c',
				'mips/itrans32_cols_dspr2.c',
			),
			'lsx' : dsp_optional_sources['lsx'] + files(
				'loongarch/idct32x32_lsx.c',
			)
		}
	else
		dsp_headers_optional_sources += {
			'neon' : dsp_headers_optional_sources['neon'] + files(
				'arm/highbd_idct_neon.h',
			),
			'sse2' : dsp_headers_optional_sources['sse2'] + files(
				'x86/highbd_inv_txfm_sse2.h',
			),
			'sse4_1' : dsp_headers_optional_sources['sse4_1'] + files(
				'x86/highbd_inv_txfm_sse4.h',
			)
		}

		dsp_optional_sources += {
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_idct4x4_add_neon.c',
				'arm/highbd_idct8x8_add_neon.c',
				'arm/highbd_idct16x16_add_neon.c',
				'arm/highbd_idct32x32_add_neon.c',
				'arm/highbd_idct32x32_34_add_neon.c',
				'arm/highbd_idct32x32_135_add_neon.c',
				'arm/highbd_idct32x32_1024_add_neon.c',
			),
			'sse2' : dsp_optional_sources['sse2'] + files(
				'x86/highbd_idct4x4_add_sse2.c',
				'x86/highbd_idct8x8_add_sse2.c',
				'x86/highbd_idct16x16_add_sse2.c',
				'x86/highbd_idct32x32_add_sse2.c',
			),
			'lsx' : dsp_optional_sources['lsx'] + files(
				'x86/highbd_idct4x4_add_sse4.c',
				'x86/highbd_idct8x8_add_sse4.c',
				'x86/highbd_idct16x16_add_sse4.c',
				'x86/highbd_idct32x32_add_sse4.c',
			)
		}
	endif

	if features.get('neon_asm', false)
		dsp_sources += asm_transformer.process(
			files(
				'arm/idct4x4_1_add_neon.asm',
				'arm/idct4x4_add_neon.asm',
			)
		)
	else
		dsp_optional_sources += {
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/idct4x4_1_add_neon.c',
				'arm/idct4x4_add_neon.c',
			)
		}
	endif

	dsp_optional_sources += {
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/idct8x8_1_add_neon.c',
			'arm/idct8x8_add_neon.c',
			'arm/idct16x16_1_add_neon.c',
			'arm/idct16x16_add_neon.c',
			'arm/idct32x32_1_add_neon.c',
			'arm/idct32x32_34_add_neon.c',
			'arm/idct32x32_135_add_neon.c',
			'arm/idct32x32_add_neon.c',
		)
	}
endif

# quantization
if features.get('vp9_encoder', false) # MANUAL
	dsp_sources += files(
		'quantize.c',
		# avg
		'avg.c',
	)

	dsp_headers_sources += files(
		'quantize.h',
	)

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/quantize_sse2.c',
			# avg
			'x86/avg_intrin_sse2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/quantize_ssse3.c',
		),
		'avx' : dsp_optional_sources['avx'] + files(
			'x86/quantize_avx.c',
		),
		'avx2' : dsp_optional_sources['avx2'] + files(
			'x86/quantize_avx2.c',
			# avg
			'x86/avg_intrin_avx2.c',
		),
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/quantize_neon.c',
			# avg
			'arm/avg_neon.c',
			'arm/hadamard_neon.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/quantize_vsx.c',
			# avg
			'ppc/hadamard_vsx.c',
		),
		'lsx' : dsp_optional_sources['lsx'] + files(
			'loongarch/quantize_lsx.c',
			# avg
			'loongarch/avg_lsx.c',
		),
		'msa' : dsp_optional_sources['msa'] + files(
			# avg
			'mips/avg_msa.c',
		),
	}

	dsp_headers_optional_sources += {
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/quantize_sse2.h',
		),
		'ssse3' : dsp_headers_optional_sources['ssse3'] + files(
			'x86/quantize_ssse3.h',
		)
	}

	if features.get('vp9_highbitdepth', false)
		dsp_optional_sources += {
			'sse2' : dsp_optional_sources['sse2'] + files(
				'x86/highbd_quantize_intrin_sse2.c',
			),
			'avx2' : dsp_optional_sources['avx'] + files(
				'x86/highbd_quantize_intrin_avx2.c',
			),
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_quantize_neon.c',
			),
		}
	endif

	# avg
	if features.get('x86_64', false)
		dsp_asm_optional_sources += {
			'ssse3' : dsp_asm_optional_sources['ssse3'] + files(
				'x86/avg_ssse3_x86_64.asm',
			)
		}
	endif
endif

if features.get('encoders', false) # MANUAL
	dsp_sources += files(
		'sad.c',
		'subtract.c',
		'sum_squares.c',
	)

	dsp_optional_sources += {
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/sum_squares_neon.c',
			'arm/sad4d_neon.c',
			'arm/sad_neon.c',
			'arm/subtract_neon.c',
		),
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/sum_squares_sse2.c',
		),
		'msa' : dsp_optional_sources['msa'] + files(
			'mips/sum_squares_msa.c',
			'mips/sad_msa.c',
			'mips/subtract_msa.c',
		),
		'lsx' : dsp_optional_sources['lsx'] + files(
			'loongarch/sad_lsx.c',
			'loongarch/subtract_lsx.c',
		),
		'mmi' : dsp_optional_sources['mmi'] + files(
			'mips/sad_mmi.c',
			'mips/subtract_mmi.c',
		),
		'avx2' : dsp_optional_sources['avx2'] + files(
			'x86/sad4d_avx2.c',
			'x86/sad_avx2.c',
			'x86/subtract_avx2.c',
		),
		'avx512' : dsp_optional_sources['avx512'] + files(
			'x86/sad4d_avx512.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/sad_vsx.c',
			'ppc/subtract_vsx.c',
		),
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/sad4d_sse2.asm',
			'x86/sad_sse2.asm',
			'x86/subtract_sse2.asm',
		)
	}

	if features.get('vp9_highbitdepth', false)
		dsp_asm_optional_sources += {
			'sse2' : dsp_asm_optional_sources['sse2'] + files(
				'x86/highbd_sad4d_sse2.asm',
				'x86/highbd_sad_sse2.asm',
			)
		}

		dsp_optional_sources += {
			'avx2' : dsp_optional_sources['avx2'] + files(
				'x86/highbd_sad4d_avx2.c',
				'x86/highbd_sad_avx2.c',
			),
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_sad_neon.c',
			)
		}
	endif
endif


if not features.get('encoders', false) or not features.get('postproc', false) or not features.get('vp9_postproc', false) # MANUAL
	dsp_sources += files(
		'variance.c',
	)

	dsp_headers_sources += files(
		'variance.h',
	)

	dsp_optional_sources += {
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/avg_pred_neon.c',
			'arm/subpel_variance_neon.c',
			'arm/variance_neon.c',
		),
		'msa' : dsp_optional_sources['msa'] + files(
			'mips/variance_msa.c',
			'mips/sub_pixel_variance_msa.c',
		),
		'lsx' : dsp_optional_sources['lsx'] + files(
			'loongarch/variance_lsx.c',
			'loongarch/sub_pixel_variance_lsx.c',
			'loongarch/avg_pred_lsx.c',
		),
		'mmi' : dsp_optional_sources['mmi'] + files(
			'mips/variance_mmi.c',
		),
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/avg_pred_sse2.c',
			'x86/variance_sse2.c', # Contains SSE2 and SSSE3
		),
		'avx2' : dsp_optional_sources['avx2'] + files(
			'x86/variance_avx2.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/variance_vsx.c',
		),

	}

	dsp_headers_optional_sources += {
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			'loongarch/variance_lsx.h',
		)
	}

	if features.get('x86_64', false)
		dsp_asm_optional_sources += {
			'sse2' : dsp_asm_optional_sources['sse2'] + files(
				'x86/ssim_opt_x86_64.asm',
			),
		}
	endif

	# Contains SSE2 and SSSE3
	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/subpel_variance_sse2.asm',
		)
	}

	if features.get('vp9_highbitdepth', false)
		dsp_asm_optional_sources += {
			'sse2' : dsp_asm_optional_sources['sse2'] + files(
				'x86/highbd_variance_impl_sse2.asm',
				'x86/highbd_subpel_variance_impl_sse2.asm',
			)
		}

		dsp_optional_sources += {
			'sse2' : dsp_optional_sources['sse2'] + files(
				'x86/highbd_variance_sse2.c',
			),
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_variance_neon.c',
			)
		}
	endif
endif

#### --- END GENERATED --- ####

subdir('arm')

codec_srcs += dsp_sources
optional_sources = get_variable('dsp_optional_sources', {})
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

optional_sources = get_variable('dsp_asm_optional_sources', {})
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

codec_headers += dsp_headers_sources
optional_sources = get_variable('dsp_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	elif ARCH_EXT_LIST.contains(comp_name)
		codec_arch_srcs += {
			comp_name: codec_arch_srcs.get(comp_name, []) + comp_sources
		}
	else
		codec_headers += comp_sources
	endif
endforeach

vpx_dsp_rtcd_defs = files(
	'vpx_dsp_rtcd_defs.pl',
)

codec_rtcds += {
	'vpx_dsp_rtcd': vpx_dsp_rtcd_defs[0]
}

codec_headers += vpx_dsp_rtcd_defs
