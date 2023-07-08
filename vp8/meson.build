# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# vp8_common.mk

#### --- GENERATED --- ####

vp8_common_sources = files(
	'common/alloccommon.c',
	'common/blockd.c',
	'common/dequantize.c',
	'common/entropy.c',
	'common/entropymode.c',
	'common/entropymv.c',
	'common/extend.c',
	'common/filter.c',
	'common/findnearmv.c',
	'common/generic/systemdependent.c',
	'common/idct_blk.c',
	'common/idctllm.c',
	'common/rtcd.c',
	'common/vp8_loopfilter.c',
	'common/loopfilter_filters.c',
	'common/mbpitch.c',
	'common/modecont.c',
	'common/quant_common.c',
	'common/reconinter.c',
	'common/reconintra.c',
	'common/reconintra4x4.c',
	'common/setupintrarecon.c',
	'common/swapyv12buffer.c',
	'common/treecoder.c',
)

vp8_common_optional_sources = {
	'x86': files( # MANUAL
		'common/x86/vp8_asm_stubs.c',
		'common/x86/loopfilter_x86.c',
	),
	'x86_64': files( # MANUAL
		'common/x86/vp8_asm_stubs.c',
		'common/x86/loopfilter_x86.c',
	),
	'dspr2' : files(
		'common/mips/dspr2/idctllm_dspr2.c',
		'common/mips/dspr2/filter_dspr2.c',
		'common/mips/dspr2/vp8_loopfilter_filters_dspr2.c',
		'common/mips/dspr2/reconinter_dspr2.c',
		'common/mips/dspr2/idct_blk_dspr2.c',
		'common/mips/dspr2/dequantize_dspr2.c'
	),
	'lsx' : files(
		'common/loongarch/loopfilter_filters_lsx.c',
		'common/loongarch/sixtap_filter_lsx.c',
		'common/loongarch/idct_lsx.c'
	),
	'mmi' : files(
		'common/mips/mmi/sixtap_filter_mmi.c',
		'common/mips/mmi/loopfilter_filters_mmi.c',
		'common/mips/mmi/idctllm_mmi.c',
		'common/mips/mmi/dequantize_mmi.c',
		'common/mips/mmi/copymem_mmi.c',
		'common/mips/mmi/idct_blk_mmi.c'
	),
	'mmx' : files(
		'common/x86/idct_blk_mmx.c'
	),
	'msa' : files(
		'common/mips/msa/bilinear_filter_msa.c',
		'common/mips/msa/copymem_msa.c',
		'common/mips/msa/idct_msa.c',
		'common/mips/msa/loopfilter_filters_msa.c',
		'common/mips/msa/sixtap_filter_msa.c',
		# 'common/mips/msa/mfqe_msa.c' # MANUAL
	),
	'neon' : files(
		'common/arm/loopfilter_arm.c',
		'common/arm/neon/bilinearpredict_neon.c',
		'common/arm/neon/copymem_neon.c',
		'common/arm/neon/dc_only_idct_add_neon.c',
		'common/arm/neon/dequant_idct_neon.c',
		'common/arm/neon/dequantizeb_neon.c',
		'common/arm/neon/idct_blk_neon.c',
		'common/arm/neon/iwalsh_neon.c',
		'common/arm/neon/vp8_loopfilter_neon.c',
		'common/arm/neon/loopfiltersimplehorizontaledge_neon.c',
		'common/arm/neon/loopfiltersimpleverticaledge_neon.c',
		'common/arm/neon/mbloopfilter_neon.c',
		'common/arm/neon/shortidct4x4llm_neon.c',
		'common/arm/neon/sixtappredict_neon.c'
	),
	'postproc' : files(
		'common/mfqe.c',
		'common/postproc.c'
	),
	'sse2' : files(
		'common/x86/idct_blk_sse2.c',
		'common/x86/bilinear_filter_sse2.c'
	),
}

vp8_cx_sources = files(
	'vp8_cx_iface.c',
	'encoder/bitstream.c',
	'encoder/boolhuff.c',
	'encoder/copy_c.c',
	'encoder/dct.c',
	'encoder/encodeframe.c',
	'encoder/encodeintra.c',
	'encoder/encodemb.c',
	'encoder/encodemv.c',
	# 'encoder/firstpass.c', # MANUAL
	'encoder/lookahead.c',
	'encoder/mcomp.c',
	'encoder/modecosts.c',
	'encoder/onyx_if.c',
	'encoder/pickinter.c',
	'encoder/picklpf.c',
	'encoder/vp8_quantize.c',
	'encoder/ratectrl.c',
	'encoder/rdopt.c',
	'encoder/segmentation.c',
	'common/vp8_skin_detection.c',
	'encoder/tokenize.c',
	'encoder/treewriter.c',
	# 'encoder/temporal_filter.c', # MANUAL
)

vp8_cx_optional_sources = {
	'internal_stats' : files(
		'common/postproc.c'
	),
	'lsx' : files(
		'encoder/loongarch/dct_lsx.c',
		'encoder/loongarch/encodeopt_lsx.c',
		'encoder/loongarch/vp8_quantize_lsx.c'
	),
	'mmi' : files(
		'encoder/mips/mmi/vp8_quantize_mmi.c',
		'encoder/mips/mmi/dct_mmi.c'
	),
	'msa' : files(
		'encoder/mips/msa/dct_msa.c',
		'encoder/mips/msa/encodeopt_msa.c',
		'encoder/mips/msa/quantize_msa.c',
		# 'encoder/mips/msa/temporal_filter_msa.c', # MANUAL
		# 'encoder/mips/msa/denoising_msa.c' # MANUAL
	),
	'multithread' : files(
		'encoder/ethreading.c'
	),
	'multi_res_encoding' : files(
		'encoder/mr_dissim.c'
	),
	'neon' : files(
		'encoder/arm/neon/denoising_neon.c',
		'encoder/arm/neon/fastquantizeb_neon.c',
		'encoder/arm/neon/shortfdct_neon.c',
		'encoder/arm/neon/vp8_shortwalsh4x4_neon.c'
	),
	'sse2' : files(
		'encoder/x86/vp8_quantize_sse2.c',
		# 'encoder/x86/denoising_sse2.c', # MANUAL
		'encoder/x86/vp8_enc_stubs_sse2.c'
	),
	'sse4_1' : files(
		'encoder/x86/quantize_sse4.c'
	),
	'ssse3' : files(
		'encoder/x86/vp8_quantize_ssse3.c'
	),
	'temporal_denoising' : files(
		'encoder/denoising.c'
	),
}

if not features.get('realtime_only', false)
	vp8_cx_sources += files(
		'encoder/firstpass.c',
		'encoder/temporal_filter.c',
	)
	vp8_cx_optional_sources += {
		'msa': vp8_cx_optional_sources['msa'] + files(
			'encoder/mips/msa/temporal_filter_msa.c',
		)
	}
endif

if features.get('temporal_denoising', true)
	vp8_cx_optional_sources += {
		'sse2': vp8_cx_optional_sources['sse2'] + files(
			'encoder/x86/denoising_sse2.c'
		)
	}
	vp8_cx_optional_sources += {
		'msa': vp8_cx_optional_sources['msa'] + files(
			'encoder/mips/msa/denoising_msa.c'
		)
	}
endif

vp8_dx_sources = files(
	'vp8_dx_iface.c',
	'decoder/dboolhuff.c',
	'decoder/decodemv.c',
	'decoder/decodeframe.c',
	'decoder/detokenize.c',
	'decoder/onyxd_if.c',
)

vp8_dx_optional_sources = {
	'error_concealment' : files(
		'decoder/error_concealment.c'
	),
	'multithread' : files(
		'decoder/threading.c'
	),
}

vp8_common_headers_sources = files(
	'common/ppflags.h',
	'common/onyx.h',
	'common/onyxd.h',
	'common/coefupdateprobs.h',
	'common/default_coef_probs.h',
	'common/filter.h',
	'common/alloccommon.h',
	'common/blockd.h',
	'common/common.h',
	'common/entropy.h',
	'common/entropymode.h',
	'common/entropymv.h',
	'common/extend.h',
	'common/findnearmv.h',
	'common/header.h',
	'common/invtrans.h',
	'common/loopfilter.h',
	'common/modecont.h',
	'common/mv.h',
	'common/onyxc_int.h',
	'common/quant_common.h',
	'common/reconinter.h',
	'common/reconintra.h',
	'common/reconintra4x4.h',
	'common/setupintrarecon.h',
	'common/swapyv12buffer.h',
	'common/systemdependent.h',
	'common/threading.h',
	'common/treecoder.h',
	'common/vp8_entropymodedata.h',
)

vp8_common_headers_optional_sources = {
	'msa' : files(
		'common/mips/msa/vp8_macros_msa.h'
	),
	'neon' : files(
		'common/arm/loopfilter_arm.h'
	),
	'postproc' : files(
		'common/postproc.h'
	),
}

vp8_cx_headers_sources = files(
	'encoder/defaultcoefcounts.h',
	'encoder/encodeframe.h',
	'encoder/block.h',
	'encoder/boolhuff.h',
	'encoder/bitstream.h',
	'encoder/encodeintra.h',
	'encoder/encodemb.h',
	'encoder/encodemv.h',
	'encoder/firstpass.h',
	'encoder/lookahead.h',
	'encoder/mcomp.h',
	'encoder/modecosts.h',
	'encoder/onyx_int.h',
	'encoder/pickinter.h',
	'encoder/quantize.h',
	'encoder/ratectrl.h',
	'encoder/rdopt.h',
	'encoder/tokenize.h',
	'encoder/treewriter.h',
	'encoder/picklpf.h',
	'encoder/segmentation.h',
	'common/vp8_skin_detection.h',
	'encoder/dct_value_cost.h',
	'encoder/dct_value_tokens.h',
	# 'encoder/temporal_filter.h', # MANUAL
)

vp8_cx_headers_optional_sources = {
	'internal_stats' : files(
		'common/postproc.h'
	),
	'multithread' : files(
		'encoder/ethreading.h'
	),
	'multi_res_encoding' : files(
		'encoder/mr_dissim.h'
	),
	'temporal_denoising' : files(
		'encoder/denoising.h'
	),
}

if not features.get('realtime_only', false)
	vp8_cx_headers_sources += files(
		'encoder/temporal_filter.h',
	)
endif

vp8_dx_headers_sources = files(
	'decoder/dboolhuff.h',
	'decoder/decodemv.h',
	'decoder/decoderthreading.h',
	'decoder/detokenize.h',
	'decoder/onyxd_int.h',
	'decoder/treereader.h',
)

vp8_dx_headers_optional_sources = {
	'error_concealment' : files(
		'decoder/ec_types.h',
		'decoder/error_concealment.h'
	),
}

vp8_common_asm_optional_sources = {
	'mmx' : files(
		'common/x86/dequantize_mmx.asm',
		'common/x86/idctllm_mmx.asm',
		'common/x86/recon_mmx.asm',
		'common/x86/subpixel_mmx.asm'
	),
	'sse2' : files(
		'common/x86/idctllm_sse2.asm',
		'common/x86/recon_sse2.asm',
		'common/x86/subpixel_sse2.asm',
		'common/x86/loopfilter_sse2.asm',
		'common/x86/iwalsh_sse2.asm',
		# 'common/x86/mfqe_sse2.asm', # MANUAL
		# 'common/x86/loopfilter_block_sse2_x86_64.asm', # MANUAL
	),
	'ssse3' : files(
		'common/x86/subpixel_ssse3.asm'
	),
}

if features.get('postproc', false) # MANUAL
	vp8_common_asm_optional_sources += {
		'sse2': vp8_common_asm_optional_sources['sse2'] + files(
			'common/x86/mfqe_sse2.asm',
		),
	}
	vp8_common_optional_sources += {
		'msa': vp8_common_optional_sources['msa'] + files(
			'common/mips/msa/mfqe_msa.c',
		)
	}
endif

if features.get('x86_64', false) # MANUAL
	vp8_common_asm_optional_sources += {
		'sse2': vp8_common_asm_optional_sources['sse2'] + files(
			'common/x86/loopfilter_block_sse2_x86_64.asm',
		),
	}
endif

vp8_cx_asm_optional_sources = {
	'sse2' : files(
		'encoder/x86/copy_sse2.asm',
		'encoder/x86/copy_sse3.asm',
		'encoder/x86/dct_sse2.asm',
		'encoder/x86/fwalsh_sse2.asm',
		'encoder/x86/block_error_sse2.asm',
		# 'encoder/x86/temporal_filter_apply_sse2.asm' # MANUAL
	),
}

if not features.get('realtime_only', false)
	vp8_common_asm_optional_sources += {
		'sse2': vp8_common_asm_optional_sources['sse2'] + files(
			'encoder/x86/temporal_filter_apply_sse2.asm',
		),
	}
endif

#### --- END GENERATED --- ####

codec_srcs += vp8_common_sources
optional_sources = get_variable('vp8_common_optional_sources', {})
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

optional_sources = get_variable('vp8_common_asm_optional_sources', {})
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

codec_headers += vp8_common_headers_sources
optional_sources = get_variable('vp8_common_headers_optional_sources', {})
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

if features.get('vp8_encoder', false)
	codec_srcs += vp8_cx_sources
	codec_headers += vp8_cx_headers_sources

	optional_sources = get_variable('vp8_cx_optional_sources', {})
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

	optional_sources = get_variable('vp8_cx_asm_optional_sources', {})
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

	optional_sources = get_variable('vp8_cx_headers_optional_sources', {})
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

if features.get('vp8_encoder', false)
	codec_srcs += vp8_dx_sources
	codec_headers += vp8_dx_headers_sources

	optional_sources = get_variable('vp8_dx_optional_sources', {})
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

	optional_sources = get_variable('vp8_dx_asm_optional_sources', {})
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

	optional_sources = get_variable('vp8_dx_headers_optional_sources', {})
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

vp8_rtcd_defs = meson.current_source_dir() / 'common/rtcd_defs.py'

codec_rtcds += {
	'vp8_rtcd': vp8_rtcd_defs
}

codec_headers += files(vp8_rtcd_defs)

if features.get('vp8_encoder', false)
	codec_exports += files(
		'exports_enc',
	)
endif

if features.get('vp8_decoder', false)
	codec_exports += files(
		'exports_dec',
	)
endif
