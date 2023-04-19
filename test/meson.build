# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

# test.mk

#### --- GENERATED --- ####

libvpx_test_sources = files(
	'bench.cc',
	'test_libvpx.cc',
	'../md5_utils.c', # MANUAL
	'../y4minput.c', # MANUAL
	'test_vectors.cc',
	'decode_test_driver.cc',
	# 'decode_perf_test.cc', # MANUAL
	# 'encode_perf_test.cc', # MANUAL
	# 'invalid_file_test.cc', # MANUAL
	# 'vp8_boolcoder_test.cc', # MANUAL
	# 'vp8_fragments_test.cc', # MANUAL
	# 'idct_test.cc', # MANUAL
	# 'predict_test.cc', # MANUAL
	# 'vpx_scale_test.cc', # MANUAL
	# 'idct8x8_test.cc', # MANUAL
	# 'partial_idct_test.cc', # MANUAL
	# 'superframe_test.cc', # MANUAL
	# 'tile_independence_test.cc', # MANUAL
	# 'vp9_boolcoder_test.cc', # MANUAL
	# 'vp9_encoder_parms_get_to_decoder.cc', # MANUAL
	# 'vp9_roi_test.cc', # MANUAL
	# 'convolve_test.cc', # MANUAL
	# 'lpf_test.cc', # MANUAL
	# 'vp9_intrapred_test.cc', # MANUAL
	# 'vp9_denoiser_test.cc', # MANUAL
)

libvpx_test_optional_sources = {
	'decoders' : files(
		# '../webmdec.cc', # MANUAL
		'decode_api_test.cc',
		'test_vector_test.cc'
	),
	'encoders' : files(
		'altref_test.cc',
		'aq_segment_test.cc',
		'alt_ref_aq_segment_test.cc',
		'vp8_datarate_test.cc',
		'vp9_datarate_test.cc',
		'encode_api_test.cc',
		'error_resilience_test.cc',
		'realtime_test.cc',
		'resize_test.cc',
		'encode_test_driver.cc',
		# 'sad_test.cc',, # MANUAL
		# 'sum_squares_test.cc', # MANUAL
	),
	'internal_stats' : files(
		# 'blockiness_test.cc', # MANUAL
		# 'consistency_test.cc' # MANUAL
	),
	'non_greedy_mv' : files(
		# 'non_greedy_mv_test.cc' # MANUAL
	),
	'postproc' : files(
		# 'add_noise_test.cc', # MANUAL
		# 'pp_filter_test.cc' # MANUAL
	),
	'sse2' : files(
		# 'vp8_denoiser_sse2_test.cc' # MANUAL
	),
	'vp8_decoder' : files(
		# 'vp8_decrypt_test.cc' # MANUAL
	),
	'vp8_encoder' : files(
		'config_test.cc',
		'cq_test.cc',
		'keyframe_test.cc',
		# 'quantize_test.cc', # MANUAL
		# 'set_roi.cc', # MANUAL
		# 'variance_test.cc', # MANUAL
		# 'vp8_fdct4x4_test.cc' # MANUAL
	),
	'vp9_decoder' : files(
		'byte_alignment_test.cc',
		'decode_svc_test.cc',
		'external_frame_buffer_test.cc',
		'user_priv_test.cc',
		# 'vp9_skip_loopfilter_test.cc', # MANUAL
		# 'vp9_decrypt_test.cc', # MANUAL
		# 'vp9_thread_test.cc' # MANUAL
	),
	'vp9_encoder' : files(
		'active_map_refresh_test.cc',
		'active_map_test.cc',
		'borders_test.cc',
		'cpu_speed_test.cc',
		'frame_size_tests.cc',
		'vp9_lossless_test.cc',
		'vp9_end_to_end_test.cc',
		'decode_corrupted.cc',
		'vp9_ethread_test.cc',
		'vp9_motion_vector_test.cc',
		'level_test.cc',
		'svc_datarate_test.cc',
		'svc_test.cc',
		'svc_end_to_end_test.cc',
		'timestamp_test.cc',
		'vp9_ext_ratectrl_test.cc',
		# 'avg_test.cc', # MANUAL
		# 'comp_avg_pred_test.cc', # MANUAL
		# 'dct16x16_test.cc', # MANUAL
		# 'dct32x32_test.cc', # MANUAL
		# 'dct_partial_test.cc', # MANUAL
		# 'dct_test.cc', # MANUAL
		# 'fdct8x8_test.cc', # MANUAL
		# 'hadamard_test.cc', # MANUAL
		# 'minmax_test.cc', # MANUAL
		# 'vp9_scale_test.cc', # MANUAL
		# 'yuv_temporal_filter_test.cc', # MANUAL
		# 'variance_test.cc', # MANUAL
		# 'vp9_block_error_test.cc', # MANUAL
		# 'vp9_quantize_test.cc', # MANUAL
		# 'vp9_subtract_test.cc', # MANUAL
		# 'vp9_arf_freq_test.cc' # MANUAL
	),
}

libwebm_parser_sources = files(
	# '../third_party/libwebm/mkvparser/mkvparser.cc', # MANUAL
	# '../third_party/libwebm/mkvparser/mkvreader.cc', # MANUAL
)

libwebm_parser_optional_sources = {
}

simple_encode_test_sources = files(
)

simple_encode_test_optional_sources = {
	'rate_ctrl' : files(
		# 'simple_encode_test.cc' # MANUAL
	),
}

test_intra_pred_speed_sources = files(
	# 'test_intra_pred_speed.cc', # MANUAL
)

test_intra_pred_speed_optional_sources = {
}

rc_interface_test_sources = files(
	# 'test_rc_interface.cc', # MANUAL
	# 'decode_test_driver.cc', # MANUAL
)

rc_interface_test_optional_sources = {
	'encoders' : files(
		# 'encode_test_driver.cc' # MANUAL
	),
	'vp8_encoder' : files(
		# 'vp8_ratectrl_rtc_test.cc' # MANUAL
	),
	'vp9_encoder' : files(
		# 'vp9_ratectrl_rtc_test.cc' # MANUAL
	),
}

libvpx_test_headers_sources = files(
	'acm_random.h',
	'bench.h',
	'buffer.h',
	'clear_system_state.h',
	'codec_factory.h',
	'md5_helper.h',
	'register_state_check.h',
	'test_vectors.h',
	'util.h',
	'video_source.h',
	'../md5_utils.h', # MANUAL
	'../y4minput.h', # MANUAL
	'decode_test_driver.h',
	'encode_test_driver.h',
	'vpx_scale_test.h',
)

libvpx_test_headers_optional_sources = {
	'decoders' : files(
		'ivf_video_source.h',
		'../tools_common.h',
		# '../webmdec.h', # MANUAL
		# 'webm_video_source.h' # MANUAL
	),
	'encoders' : files(
		'i420_video_source.h',
		'y4m_video_source.h',
		'yuv_video_source.h'
	),
	'vp9_encoder' : files(
		'svc_test.h',
		'../vp9/simple_encode.h'
	),
}

libwebm_parser_headers_sources = files(
	# '../third_party/libwebm/mkvparser/mkvparser.h', # MANUAL
	# '../third_party/libwebm/mkvparser/mkvreader.h', # MANUAL
	# '../third_party/libwebm/common/webmids.h', # MANUAL
)

libwebm_parser_headers_optional_sources = {
}

rc_interface_test_headers_sources = files(
	# 'decode_test_driver.h', # MANUAL
	# 'codec_factory.h', # MANUAL
)

rc_interface_test_headers_optional_sources = {
	'encoders' : files(
		'encode_test_driver.h'
	),
}

libvpx_test_data_data_sources = [
]

libvpx_test_data_data_optional_sources = {
	'encoders' : [
		'hantro_collage_w352h288.yuv',
		'hantro_collage_w352h288_nv12.yuv',
		'hantro_odd.yuv',
		'desktop_office1.1280_720-020.yuv',
		'slides_code_term_web_plot.1920_1080.yuv',
		'desktopqvga.320_240.yuv',
		'park_joy_90p_10_420_20f.y4m',
		'park_joy_90p_10_422_20f.y4m',
		'park_joy_90p_10_444_20f.y4m',
		'park_joy_90p_10_440.yuv',
		'park_joy_90p_12_420_20f.y4m',
		'park_joy_90p_12_422_20f.y4m',
		'park_joy_90p_12_444_20f.y4m',
		'park_joy_90p_12_440.yuv',
		'park_joy_90p_8_420_a10-1.y4m',
		'park_joy_90p_8_420.y4m',
		'park_joy_90p_8_422.y4m',
		'park_joy_90p_8_444.y4m',
		'park_joy_90p_8_440.yuv'
	],
	'vp8_decoder' : [
		'vp80-00-comprehensive-001.ivf',
		'vp80-00-comprehensive-001.ivf.md5',
		'vp80-00-comprehensive-002.ivf',
		'vp80-00-comprehensive-002.ivf.md5',
		'vp80-00-comprehensive-003.ivf',
		'vp80-00-comprehensive-003.ivf.md5',
		'vp80-00-comprehensive-004.ivf',
		'vp80-00-comprehensive-004.ivf.md5',
		'vp80-00-comprehensive-005.ivf',
		'vp80-00-comprehensive-005.ivf.md5',
		'vp80-00-comprehensive-006.ivf',
		'vp80-00-comprehensive-006.ivf.md5',
		'vp80-00-comprehensive-007.ivf',
		'vp80-00-comprehensive-007.ivf.md5',
		'vp80-00-comprehensive-008.ivf',
		'vp80-00-comprehensive-008.ivf.md5',
		'vp80-00-comprehensive-009.ivf',
		'vp80-00-comprehensive-009.ivf.md5',
		'vp80-00-comprehensive-010.ivf',
		'vp80-00-comprehensive-010.ivf.md5',
		'vp80-00-comprehensive-011.ivf',
		'vp80-00-comprehensive-011.ivf.md5',
		'vp80-00-comprehensive-012.ivf',
		'vp80-00-comprehensive-012.ivf.md5',
		'vp80-00-comprehensive-013.ivf',
		'vp80-00-comprehensive-013.ivf.md5',
		'vp80-00-comprehensive-014.ivf',
		'vp80-00-comprehensive-014.ivf.md5',
		'vp80-00-comprehensive-015.ivf',
		'vp80-00-comprehensive-015.ivf.md5',
		'vp80-00-comprehensive-016.ivf',
		'vp80-00-comprehensive-016.ivf.md5',
		'vp80-00-comprehensive-017.ivf',
		'vp80-00-comprehensive-017.ivf.md5',
		'vp80-00-comprehensive-018.ivf',
		'vp80-00-comprehensive-018.ivf.md5',
		'vp80-01-intra-1400.ivf',
		'vp80-01-intra-1400.ivf.md5',
		'vp80-01-intra-1411.ivf',
		'vp80-01-intra-1411.ivf.md5',
		'vp80-01-intra-1416.ivf',
		'vp80-01-intra-1416.ivf.md5',
		'vp80-01-intra-1417.ivf',
		'vp80-01-intra-1417.ivf.md5',
		'vp80-02-inter-1402.ivf',
		'vp80-02-inter-1402.ivf.md5',
		'vp80-02-inter-1412.ivf',
		'vp80-02-inter-1412.ivf.md5',
		'vp80-02-inter-1418.ivf',
		'vp80-02-inter-1418.ivf.md5',
		'vp80-02-inter-1424.ivf',
		'vp80-02-inter-1424.ivf.md5',
		'vp80-03-segmentation-01.ivf',
		'vp80-03-segmentation-01.ivf.md5',
		'vp80-03-segmentation-02.ivf',
		'vp80-03-segmentation-02.ivf.md5',
		'vp80-03-segmentation-03.ivf',
		'vp80-03-segmentation-03.ivf.md5',
		'vp80-03-segmentation-04.ivf',
		'vp80-03-segmentation-04.ivf.md5',
		'vp80-03-segmentation-1401.ivf',
		'vp80-03-segmentation-1401.ivf.md5',
		'vp80-03-segmentation-1403.ivf',
		'vp80-03-segmentation-1403.ivf.md5',
		'vp80-03-segmentation-1407.ivf',
		'vp80-03-segmentation-1407.ivf.md5',
		'vp80-03-segmentation-1408.ivf',
		'vp80-03-segmentation-1408.ivf.md5',
		'vp80-03-segmentation-1409.ivf',
		'vp80-03-segmentation-1409.ivf.md5',
		'vp80-03-segmentation-1410.ivf',
		'vp80-03-segmentation-1410.ivf.md5',
		'vp80-03-segmentation-1413.ivf',
		'vp80-03-segmentation-1413.ivf.md5',
		'vp80-03-segmentation-1414.ivf',
		'vp80-03-segmentation-1414.ivf.md5',
		'vp80-03-segmentation-1415.ivf',
		'vp80-03-segmentation-1415.ivf.md5',
		'vp80-03-segmentation-1425.ivf',
		'vp80-03-segmentation-1425.ivf.md5',
		'vp80-03-segmentation-1426.ivf',
		'vp80-03-segmentation-1426.ivf.md5',
		'vp80-03-segmentation-1427.ivf',
		'vp80-03-segmentation-1427.ivf.md5',
		'vp80-03-segmentation-1432.ivf',
		'vp80-03-segmentation-1432.ivf.md5',
		'vp80-03-segmentation-1435.ivf',
		'vp80-03-segmentation-1435.ivf.md5',
		'vp80-03-segmentation-1436.ivf',
		'vp80-03-segmentation-1436.ivf.md5',
		'vp80-03-segmentation-1437.ivf',
		'vp80-03-segmentation-1437.ivf.md5',
		'vp80-03-segmentation-1441.ivf',
		'vp80-03-segmentation-1441.ivf.md5',
		'vp80-03-segmentation-1442.ivf',
		'vp80-03-segmentation-1442.ivf.md5',
		'vp80-04-partitions-1404.ivf',
		'vp80-04-partitions-1404.ivf.md5',
		'vp80-04-partitions-1405.ivf',
		'vp80-04-partitions-1405.ivf.md5',
		'vp80-04-partitions-1406.ivf',
		'vp80-04-partitions-1406.ivf.md5',
		'vp80-05-sharpness-1428.ivf',
		'vp80-05-sharpness-1428.ivf.md5',
		'vp80-05-sharpness-1429.ivf',
		'vp80-05-sharpness-1429.ivf.md5',
		'vp80-05-sharpness-1430.ivf',
		'vp80-05-sharpness-1430.ivf.md5',
		'vp80-05-sharpness-1431.ivf',
		'vp80-05-sharpness-1431.ivf.md5',
		'vp80-05-sharpness-1433.ivf',
		'vp80-05-sharpness-1433.ivf.md5',
		'vp80-05-sharpness-1434.ivf',
		'vp80-05-sharpness-1434.ivf.md5',
		'vp80-05-sharpness-1438.ivf',
		'vp80-05-sharpness-1438.ivf.md5',
		'vp80-05-sharpness-1439.ivf',
		'vp80-05-sharpness-1439.ivf.md5',
		'vp80-05-sharpness-1440.ivf',
		'vp80-05-sharpness-1440.ivf.md5',
		'vp80-05-sharpness-1443.ivf',
		'vp80-05-sharpness-1443.ivf.md5',
		'vp80-06-smallsize.ivf',
		'vp80-06-smallsize.ivf.md5',
		'invalid-bug-1443.ivf',
		'invalid-bug-1443.ivf.res',
		'invalid-bug-148271109.ivf',
		'invalid-bug-148271109.ivf.res',
		'invalid-token-partition.ivf',
		'invalid-token-partition.ivf.res',
		'invalid-vp80-00-comprehensive-018.ivf.2kf_0x6.ivf',
		'invalid-vp80-00-comprehensive-018.ivf.2kf_0x6.ivf.res',
		'invalid-vp80-00-comprehensive-s17661_r01-05_b6-.ivf',
		'invalid-vp80-00-comprehensive-s17661_r01-05_b6-.ivf.res'
	],
	'vp9_decoder' : [
		'vp90-2-00-quantizer-00.webm',
		'vp90-2-00-quantizer-00.webm.md5',
		'vp90-2-00-quantizer-01.webm',
		'vp90-2-00-quantizer-01.webm.md5',
		'vp90-2-00-quantizer-02.webm',
		'vp90-2-00-quantizer-02.webm.md5',
		'vp90-2-00-quantizer-03.webm',
		'vp90-2-00-quantizer-03.webm.md5',
		'vp90-2-00-quantizer-04.webm',
		'vp90-2-00-quantizer-04.webm.md5',
		'vp90-2-00-quantizer-05.webm',
		'vp90-2-00-quantizer-05.webm.md5',
		'vp90-2-00-quantizer-06.webm',
		'vp90-2-00-quantizer-06.webm.md5',
		'vp90-2-00-quantizer-07.webm',
		'vp90-2-00-quantizer-07.webm.md5',
		'vp90-2-00-quantizer-08.webm',
		'vp90-2-00-quantizer-08.webm.md5',
		'vp90-2-00-quantizer-09.webm',
		'vp90-2-00-quantizer-09.webm.md5',
		'vp90-2-00-quantizer-10.webm',
		'vp90-2-00-quantizer-10.webm.md5',
		'vp90-2-00-quantizer-11.webm',
		'vp90-2-00-quantizer-11.webm.md5',
		'vp90-2-00-quantizer-12.webm',
		'vp90-2-00-quantizer-12.webm.md5',
		'vp90-2-00-quantizer-13.webm',
		'vp90-2-00-quantizer-13.webm.md5',
		'vp90-2-00-quantizer-14.webm',
		'vp90-2-00-quantizer-14.webm.md5',
		'vp90-2-00-quantizer-15.webm',
		'vp90-2-00-quantizer-15.webm.md5',
		'vp90-2-00-quantizer-16.webm',
		'vp90-2-00-quantizer-16.webm.md5',
		'vp90-2-00-quantizer-17.webm',
		'vp90-2-00-quantizer-17.webm.md5',
		'vp90-2-00-quantizer-18.webm',
		'vp90-2-00-quantizer-18.webm.md5',
		'vp90-2-00-quantizer-19.webm',
		'vp90-2-00-quantizer-19.webm.md5',
		'vp90-2-00-quantizer-20.webm',
		'vp90-2-00-quantizer-20.webm.md5',
		'vp90-2-00-quantizer-21.webm',
		'vp90-2-00-quantizer-21.webm.md5',
		'vp90-2-00-quantizer-22.webm',
		'vp90-2-00-quantizer-22.webm.md5',
		'vp90-2-00-quantizer-23.webm',
		'vp90-2-00-quantizer-23.webm.md5',
		'vp90-2-00-quantizer-24.webm',
		'vp90-2-00-quantizer-24.webm.md5',
		'vp90-2-00-quantizer-25.webm',
		'vp90-2-00-quantizer-25.webm.md5',
		'vp90-2-00-quantizer-26.webm',
		'vp90-2-00-quantizer-26.webm.md5',
		'vp90-2-00-quantizer-27.webm',
		'vp90-2-00-quantizer-27.webm.md5',
		'vp90-2-00-quantizer-28.webm',
		'vp90-2-00-quantizer-28.webm.md5',
		'vp90-2-00-quantizer-29.webm',
		'vp90-2-00-quantizer-29.webm.md5',
		'vp90-2-00-quantizer-30.webm',
		'vp90-2-00-quantizer-30.webm.md5',
		'vp90-2-00-quantizer-31.webm',
		'vp90-2-00-quantizer-31.webm.md5',
		'vp90-2-00-quantizer-32.webm',
		'vp90-2-00-quantizer-32.webm.md5',
		'vp90-2-00-quantizer-33.webm',
		'vp90-2-00-quantizer-33.webm.md5',
		'vp90-2-00-quantizer-34.webm',
		'vp90-2-00-quantizer-34.webm.md5',
		'vp90-2-00-quantizer-35.webm',
		'vp90-2-00-quantizer-35.webm.md5',
		'vp90-2-00-quantizer-36.webm',
		'vp90-2-00-quantizer-36.webm.md5',
		'vp90-2-00-quantizer-37.webm',
		'vp90-2-00-quantizer-37.webm.md5',
		'vp90-2-00-quantizer-38.webm',
		'vp90-2-00-quantizer-38.webm.md5',
		'vp90-2-00-quantizer-39.webm',
		'vp90-2-00-quantizer-39.webm.md5',
		'vp90-2-00-quantizer-40.webm',
		'vp90-2-00-quantizer-40.webm.md5',
		'vp90-2-00-quantizer-41.webm',
		'vp90-2-00-quantizer-41.webm.md5',
		'vp90-2-00-quantizer-42.webm',
		'vp90-2-00-quantizer-42.webm.md5',
		'vp90-2-00-quantizer-43.webm',
		'vp90-2-00-quantizer-43.webm.md5',
		'vp90-2-00-quantizer-44.webm',
		'vp90-2-00-quantizer-44.webm.md5',
		'vp90-2-00-quantizer-45.webm',
		'vp90-2-00-quantizer-45.webm.md5',
		'vp90-2-00-quantizer-46.webm',
		'vp90-2-00-quantizer-46.webm.md5',
		'vp90-2-00-quantizer-47.webm',
		'vp90-2-00-quantizer-47.webm.md5',
		'vp90-2-00-quantizer-48.webm',
		'vp90-2-00-quantizer-48.webm.md5',
		'vp90-2-00-quantizer-49.webm',
		'vp90-2-00-quantizer-49.webm.md5',
		'vp90-2-00-quantizer-50.webm',
		'vp90-2-00-quantizer-50.webm.md5',
		'vp90-2-00-quantizer-51.webm',
		'vp90-2-00-quantizer-51.webm.md5',
		'vp90-2-00-quantizer-52.webm',
		'vp90-2-00-quantizer-52.webm.md5',
		'vp90-2-00-quantizer-53.webm',
		'vp90-2-00-quantizer-53.webm.md5',
		'vp90-2-00-quantizer-54.webm',
		'vp90-2-00-quantizer-54.webm.md5',
		'vp90-2-00-quantizer-55.webm',
		'vp90-2-00-quantizer-55.webm.md5',
		'vp90-2-00-quantizer-56.webm',
		'vp90-2-00-quantizer-56.webm.md5',
		'vp90-2-00-quantizer-57.webm',
		'vp90-2-00-quantizer-57.webm.md5',
		'vp90-2-00-quantizer-58.webm',
		'vp90-2-00-quantizer-58.webm.md5',
		'vp90-2-00-quantizer-59.webm',
		'vp90-2-00-quantizer-59.webm.md5',
		'vp90-2-00-quantizer-60.webm',
		'vp90-2-00-quantizer-60.webm.md5',
		'vp90-2-00-quantizer-61.webm',
		'vp90-2-00-quantizer-61.webm.md5',
		'vp90-2-00-quantizer-62.webm',
		'vp90-2-00-quantizer-62.webm.md5',
		'vp90-2-00-quantizer-63.webm',
		'vp90-2-00-quantizer-63.webm.md5',
		'vp90-2-01-sharpness-1.webm',
		'vp90-2-01-sharpness-1.webm.md5',
		'vp90-2-01-sharpness-2.webm',
		'vp90-2-01-sharpness-2.webm.md5',
		'vp90-2-01-sharpness-3.webm',
		'vp90-2-01-sharpness-3.webm.md5',
		'vp90-2-01-sharpness-4.webm',
		'vp90-2-01-sharpness-4.webm.md5',
		'vp90-2-01-sharpness-5.webm',
		'vp90-2-01-sharpness-5.webm.md5',
		'vp90-2-01-sharpness-6.webm',
		'vp90-2-01-sharpness-6.webm.md5',
		'vp90-2-01-sharpness-7.webm',
		'vp90-2-01-sharpness-7.webm.md5',
		'vp90-2-02-size-08x08.webm',
		'vp90-2-02-size-08x08.webm.md5',
		'vp90-2-02-size-08x10.webm',
		'vp90-2-02-size-08x10.webm.md5',
		'vp90-2-02-size-08x16.webm',
		'vp90-2-02-size-08x16.webm.md5',
		'vp90-2-02-size-08x18.webm',
		'vp90-2-02-size-08x18.webm.md5',
		'vp90-2-02-size-08x32.webm',
		'vp90-2-02-size-08x32.webm.md5',
		'vp90-2-02-size-08x34.webm',
		'vp90-2-02-size-08x34.webm.md5',
		'vp90-2-02-size-08x64.webm',
		'vp90-2-02-size-08x64.webm.md5',
		'vp90-2-02-size-08x66.webm',
		'vp90-2-02-size-08x66.webm.md5',
		'vp90-2-02-size-10x08.webm',
		'vp90-2-02-size-10x08.webm.md5',
		'vp90-2-02-size-10x10.webm',
		'vp90-2-02-size-10x10.webm.md5',
		'vp90-2-02-size-10x16.webm',
		'vp90-2-02-size-10x16.webm.md5',
		'vp90-2-02-size-10x18.webm',
		'vp90-2-02-size-10x18.webm.md5',
		'vp90-2-02-size-10x32.webm',
		'vp90-2-02-size-10x32.webm.md5',
		'vp90-2-02-size-10x34.webm',
		'vp90-2-02-size-10x34.webm.md5',
		'vp90-2-02-size-10x64.webm',
		'vp90-2-02-size-10x64.webm.md5',
		'vp90-2-02-size-10x66.webm',
		'vp90-2-02-size-10x66.webm.md5',
		'vp90-2-02-size-16x08.webm',
		'vp90-2-02-size-16x08.webm.md5',
		'vp90-2-02-size-16x10.webm',
		'vp90-2-02-size-16x10.webm.md5',
		'vp90-2-02-size-16x16.webm',
		'vp90-2-02-size-16x16.webm.md5',
		'vp90-2-02-size-16x18.webm',
		'vp90-2-02-size-16x18.webm.md5',
		'vp90-2-02-size-16x32.webm',
		'vp90-2-02-size-16x32.webm.md5',
		'vp90-2-02-size-16x34.webm',
		'vp90-2-02-size-16x34.webm.md5',
		'vp90-2-02-size-16x64.webm',
		'vp90-2-02-size-16x64.webm.md5',
		'vp90-2-02-size-16x66.webm',
		'vp90-2-02-size-16x66.webm.md5',
		'vp90-2-02-size-18x08.webm',
		'vp90-2-02-size-18x08.webm.md5',
		'vp90-2-02-size-18x10.webm',
		'vp90-2-02-size-18x10.webm.md5',
		'vp90-2-02-size-18x16.webm',
		'vp90-2-02-size-18x16.webm.md5',
		'vp90-2-02-size-18x18.webm',
		'vp90-2-02-size-18x18.webm.md5',
		'vp90-2-02-size-18x32.webm',
		'vp90-2-02-size-18x32.webm.md5',
		'vp90-2-02-size-18x34.webm',
		'vp90-2-02-size-18x34.webm.md5',
		'vp90-2-02-size-18x64.webm',
		'vp90-2-02-size-18x64.webm.md5',
		'vp90-2-02-size-18x66.webm',
		'vp90-2-02-size-18x66.webm.md5',
		'vp90-2-02-size-32x08.webm',
		'vp90-2-02-size-32x08.webm.md5',
		'vp90-2-02-size-32x10.webm',
		'vp90-2-02-size-32x10.webm.md5',
		'vp90-2-02-size-32x16.webm',
		'vp90-2-02-size-32x16.webm.md5',
		'vp90-2-02-size-32x18.webm',
		'vp90-2-02-size-32x18.webm.md5',
		'vp90-2-02-size-32x32.webm',
		'vp90-2-02-size-32x32.webm.md5',
		'vp90-2-02-size-32x34.webm',
		'vp90-2-02-size-32x34.webm.md5',
		'vp90-2-02-size-32x64.webm',
		'vp90-2-02-size-32x64.webm.md5',
		'vp90-2-02-size-32x66.webm',
		'vp90-2-02-size-32x66.webm.md5',
		'vp90-2-02-size-34x08.webm',
		'vp90-2-02-size-34x08.webm.md5',
		'vp90-2-02-size-34x10.webm',
		'vp90-2-02-size-34x10.webm.md5',
		'vp90-2-02-size-34x16.webm',
		'vp90-2-02-size-34x16.webm.md5',
		'vp90-2-02-size-34x18.webm',
		'vp90-2-02-size-34x18.webm.md5',
		'vp90-2-02-size-34x32.webm',
		'vp90-2-02-size-34x32.webm.md5',
		'vp90-2-02-size-34x34.webm',
		'vp90-2-02-size-34x34.webm.md5',
		'vp90-2-02-size-34x64.webm',
		'vp90-2-02-size-34x64.webm.md5',
		'vp90-2-02-size-34x66.webm',
		'vp90-2-02-size-34x66.webm.md5',
		'vp90-2-02-size-64x08.webm',
		'vp90-2-02-size-64x08.webm.md5',
		'vp90-2-02-size-64x10.webm',
		'vp90-2-02-size-64x10.webm.md5',
		'vp90-2-02-size-64x16.webm',
		'vp90-2-02-size-64x16.webm.md5',
		'vp90-2-02-size-64x18.webm',
		'vp90-2-02-size-64x18.webm.md5',
		'vp90-2-02-size-64x32.webm',
		'vp90-2-02-size-64x32.webm.md5',
		'vp90-2-02-size-64x34.webm',
		'vp90-2-02-size-64x34.webm.md5',
		'vp90-2-02-size-64x64.webm',
		'vp90-2-02-size-64x64.webm.md5',
		'vp90-2-02-size-64x66.webm',
		'vp90-2-02-size-64x66.webm.md5',
		'vp90-2-02-size-66x08.webm',
		'vp90-2-02-size-66x08.webm.md5',
		'vp90-2-02-size-66x10.webm',
		'vp90-2-02-size-66x10.webm.md5',
		'vp90-2-02-size-66x16.webm',
		'vp90-2-02-size-66x16.webm.md5',
		'vp90-2-02-size-66x18.webm',
		'vp90-2-02-size-66x18.webm.md5',
		'vp90-2-02-size-66x32.webm',
		'vp90-2-02-size-66x32.webm.md5',
		'vp90-2-02-size-66x34.webm',
		'vp90-2-02-size-66x34.webm.md5',
		'vp90-2-02-size-66x64.webm',
		'vp90-2-02-size-66x64.webm.md5',
		'vp90-2-02-size-66x66.webm',
		'vp90-2-02-size-66x66.webm.md5',
		'vp90-2-02-size-130x132.webm',
		'vp90-2-02-size-130x132.webm.md5',
		'vp90-2-02-size-132x130.webm',
		'vp90-2-02-size-132x130.webm.md5',
		'vp90-2-02-size-132x132.webm',
		'vp90-2-02-size-132x132.webm.md5',
		'vp90-2-02-size-178x180.webm',
		'vp90-2-02-size-178x180.webm.md5',
		'vp90-2-02-size-180x178.webm',
		'vp90-2-02-size-180x178.webm.md5',
		'vp90-2-02-size-180x180.webm',
		'vp90-2-02-size-180x180.webm.md5',
		'vp90-2-02-size-lf-1920x1080.webm',
		'vp90-2-02-size-lf-1920x1080.webm.md5',
		'vp90-2-03-deltaq.webm',
		'vp90-2-03-deltaq.webm.md5',
		'vp90-2-03-size-196x196.webm',
		'vp90-2-03-size-196x196.webm.md5',
		'vp90-2-03-size-196x198.webm',
		'vp90-2-03-size-196x198.webm.md5',
		'vp90-2-03-size-196x200.webm',
		'vp90-2-03-size-196x200.webm.md5',
		'vp90-2-03-size-196x202.webm',
		'vp90-2-03-size-196x202.webm.md5',
		'vp90-2-03-size-196x208.webm',
		'vp90-2-03-size-196x208.webm.md5',
		'vp90-2-03-size-196x210.webm',
		'vp90-2-03-size-196x210.webm.md5',
		'vp90-2-03-size-196x224.webm',
		'vp90-2-03-size-196x224.webm.md5',
		'vp90-2-03-size-196x226.webm',
		'vp90-2-03-size-196x226.webm.md5',
		'vp90-2-03-size-198x196.webm',
		'vp90-2-03-size-198x196.webm.md5',
		'vp90-2-03-size-198x198.webm',
		'vp90-2-03-size-198x198.webm.md5',
		'vp90-2-03-size-198x200.webm',
		'vp90-2-03-size-198x200.webm.md5',
		'vp90-2-03-size-198x202.webm',
		'vp90-2-03-size-198x202.webm.md5',
		'vp90-2-03-size-198x208.webm',
		'vp90-2-03-size-198x208.webm.md5',
		'vp90-2-03-size-198x210.webm',
		'vp90-2-03-size-198x210.webm.md5',
		'vp90-2-03-size-198x224.webm',
		'vp90-2-03-size-198x224.webm.md5',
		'vp90-2-03-size-198x226.webm',
		'vp90-2-03-size-198x226.webm.md5',
		'vp90-2-03-size-200x196.webm',
		'vp90-2-03-size-200x196.webm.md5',
		'vp90-2-03-size-200x198.webm',
		'vp90-2-03-size-200x198.webm.md5',
		'vp90-2-03-size-200x200.webm',
		'vp90-2-03-size-200x200.webm.md5',
		'vp90-2-03-size-200x202.webm',
		'vp90-2-03-size-200x202.webm.md5',
		'vp90-2-03-size-200x208.webm',
		'vp90-2-03-size-200x208.webm.md5',
		'vp90-2-03-size-200x210.webm',
		'vp90-2-03-size-200x210.webm.md5',
		'vp90-2-03-size-200x224.webm',
		'vp90-2-03-size-200x224.webm.md5',
		'vp90-2-03-size-200x226.webm',
		'vp90-2-03-size-200x226.webm.md5',
		'vp90-2-03-size-202x196.webm',
		'vp90-2-03-size-202x196.webm.md5',
		'vp90-2-03-size-202x198.webm',
		'vp90-2-03-size-202x198.webm.md5',
		'vp90-2-03-size-202x200.webm',
		'vp90-2-03-size-202x200.webm.md5',
		'vp90-2-03-size-202x202.webm',
		'vp90-2-03-size-202x202.webm.md5',
		'vp90-2-03-size-202x208.webm',
		'vp90-2-03-size-202x208.webm.md5',
		'vp90-2-03-size-202x210.webm',
		'vp90-2-03-size-202x210.webm.md5',
		'vp90-2-03-size-202x224.webm',
		'vp90-2-03-size-202x224.webm.md5',
		'vp90-2-03-size-202x226.webm',
		'vp90-2-03-size-202x226.webm.md5',
		'vp90-2-03-size-208x196.webm',
		'vp90-2-03-size-208x196.webm.md5',
		'vp90-2-03-size-208x198.webm',
		'vp90-2-03-size-208x198.webm.md5',
		'vp90-2-03-size-208x200.webm',
		'vp90-2-03-size-208x200.webm.md5',
		'vp90-2-03-size-208x202.webm',
		'vp90-2-03-size-208x202.webm.md5',
		'vp90-2-03-size-208x208.webm',
		'vp90-2-03-size-208x208.webm.md5',
		'vp90-2-03-size-208x210.webm',
		'vp90-2-03-size-208x210.webm.md5',
		'vp90-2-03-size-208x224.webm',
		'vp90-2-03-size-208x224.webm.md5',
		'vp90-2-03-size-208x226.webm',
		'vp90-2-03-size-208x226.webm.md5',
		'vp90-2-03-size-210x196.webm',
		'vp90-2-03-size-210x196.webm.md5',
		'vp90-2-03-size-210x198.webm',
		'vp90-2-03-size-210x198.webm.md5',
		'vp90-2-03-size-210x200.webm',
		'vp90-2-03-size-210x200.webm.md5',
		'vp90-2-03-size-210x202.webm',
		'vp90-2-03-size-210x202.webm.md5',
		'vp90-2-03-size-210x208.webm',
		'vp90-2-03-size-210x208.webm.md5',
		'vp90-2-03-size-210x210.webm',
		'vp90-2-03-size-210x210.webm.md5',
		'vp90-2-03-size-210x224.webm',
		'vp90-2-03-size-210x224.webm.md5',
		'vp90-2-03-size-210x226.webm',
		'vp90-2-03-size-210x226.webm.md5',
		'vp90-2-03-size-224x196.webm',
		'vp90-2-03-size-224x196.webm.md5',
		'vp90-2-03-size-224x198.webm',
		'vp90-2-03-size-224x198.webm.md5',
		'vp90-2-03-size-224x200.webm',
		'vp90-2-03-size-224x200.webm.md5',
		'vp90-2-03-size-224x202.webm',
		'vp90-2-03-size-224x202.webm.md5',
		'vp90-2-03-size-224x208.webm',
		'vp90-2-03-size-224x208.webm.md5',
		'vp90-2-03-size-224x210.webm',
		'vp90-2-03-size-224x210.webm.md5',
		'vp90-2-03-size-224x224.webm',
		'vp90-2-03-size-224x224.webm.md5',
		'vp90-2-03-size-224x226.webm',
		'vp90-2-03-size-224x226.webm.md5',
		'vp90-2-03-size-226x196.webm',
		'vp90-2-03-size-226x196.webm.md5',
		'vp90-2-03-size-226x198.webm',
		'vp90-2-03-size-226x198.webm.md5',
		'vp90-2-03-size-226x200.webm',
		'vp90-2-03-size-226x200.webm.md5',
		'vp90-2-03-size-226x202.webm',
		'vp90-2-03-size-226x202.webm.md5',
		'vp90-2-03-size-226x208.webm',
		'vp90-2-03-size-226x208.webm.md5',
		'vp90-2-03-size-226x210.webm',
		'vp90-2-03-size-226x210.webm.md5',
		'vp90-2-03-size-226x224.webm',
		'vp90-2-03-size-226x224.webm.md5',
		'vp90-2-03-size-226x226.webm',
		'vp90-2-03-size-226x226.webm.md5',
		'vp90-2-03-size-352x288.webm',
		'vp90-2-03-size-352x288.webm.md5',
		'vp90-2-05-resize.ivf',
		'vp90-2-05-resize.ivf.md5',
		'vp90-2-06-bilinear.webm',
		'vp90-2-06-bilinear.webm.md5',
		'vp90-2-07-frame_parallel.webm',
		'vp90-2-07-frame_parallel.webm.md5',
		'vp90-2-07-frame_parallel-1.webm',
		'vp90-2-07-frame_parallel-1.webm.md5',
		'vp90-2-08-tile-4x1.webm',
		'vp90-2-08-tile-4x1.webm.md5',
		'vp90-2-08-tile-4x4.webm',
		'vp90-2-08-tile-4x4.webm.md5',
		'vp90-2-08-tile_1x2.webm',
		'vp90-2-08-tile_1x2.webm.md5',
		'vp90-2-08-tile_1x2_frame_parallel.webm',
		'vp90-2-08-tile_1x2_frame_parallel.webm.md5',
		'vp90-2-08-tile_1x4.webm',
		'vp90-2-08-tile_1x4.webm.md5',
		'vp90-2-08-tile_1x4_frame_parallel.webm',
		'vp90-2-08-tile_1x4_frame_parallel.webm.md5',
		'vp90-2-08-tile_1x8.webm',
		'vp90-2-08-tile_1x8.webm.md5',
		'vp90-2-08-tile_1x8_frame_parallel.webm',
		'vp90-2-08-tile_1x8_frame_parallel.webm.md5',
		'vp90-2-09-aq2.webm',
		'vp90-2-09-aq2.webm.md5',
		'vp90-2-09-lf_deltas.webm',
		'vp90-2-09-lf_deltas.webm.md5',
		'vp90-2-09-subpixel-00.ivf',
		'vp90-2-09-subpixel-00.ivf.md5',
		'vp90-2-10-show-existing-frame.webm',
		'vp90-2-10-show-existing-frame.webm.md5',
		'vp90-2-10-show-existing-frame2.webm',
		'vp90-2-10-show-existing-frame2.webm.md5',
		'vp90-2-11-size-351x287.webm',
		'vp90-2-11-size-351x287.webm.md5',
		'vp90-2-11-size-351x288.webm',
		'vp90-2-11-size-351x288.webm.md5',
		'vp90-2-11-size-352x287.webm',
		'vp90-2-11-size-352x287.webm.md5',
		'vp90-2-12-droppable_1.ivf',
		'vp90-2-12-droppable_1.ivf.md5',
		'vp90-2-12-droppable_2.ivf',
		'vp90-2-12-droppable_2.ivf.md5',
		'vp90-2-12-droppable_3.ivf',
		'vp90-2-12-droppable_3.ivf.md5',
		'vp90-2-13-largescaling.webm',
		'vp90-2-13-largescaling.webm.md5',
		'vp90-2-14-resize-fp-tiles-1-16.webm',
		'vp90-2-14-resize-fp-tiles-1-16.webm.md5',
		'vp90-2-14-resize-fp-tiles-1-2-4-8-16.webm',
		'vp90-2-14-resize-fp-tiles-1-2-4-8-16.webm.md5',
		'vp90-2-14-resize-fp-tiles-1-2.webm',
		'vp90-2-14-resize-fp-tiles-1-2.webm.md5',
		'vp90-2-14-resize-fp-tiles-1-4.webm',
		'vp90-2-14-resize-fp-tiles-1-4.webm.md5',
		'vp90-2-14-resize-fp-tiles-1-8.webm',
		'vp90-2-14-resize-fp-tiles-1-8.webm.md5',
		'vp90-2-14-resize-fp-tiles-16-1.webm',
		'vp90-2-14-resize-fp-tiles-16-1.webm.md5',
		'vp90-2-14-resize-fp-tiles-16-2.webm',
		'vp90-2-14-resize-fp-tiles-16-2.webm.md5',
		'vp90-2-14-resize-fp-tiles-16-4.webm',
		'vp90-2-14-resize-fp-tiles-16-4.webm.md5',
		'vp90-2-14-resize-fp-tiles-16-8-4-2-1.webm',
		'vp90-2-14-resize-fp-tiles-16-8-4-2-1.webm.md5',
		'vp90-2-14-resize-fp-tiles-16-8.webm',
		'vp90-2-14-resize-fp-tiles-16-8.webm.md5',
		'vp90-2-14-resize-fp-tiles-2-1.webm',
		'vp90-2-14-resize-fp-tiles-2-1.webm.md5',
		'vp90-2-14-resize-fp-tiles-2-16.webm',
		'vp90-2-14-resize-fp-tiles-2-16.webm.md5',
		'vp90-2-14-resize-fp-tiles-2-4.webm',
		'vp90-2-14-resize-fp-tiles-2-4.webm.md5',
		'vp90-2-14-resize-fp-tiles-2-8.webm',
		'vp90-2-14-resize-fp-tiles-2-8.webm.md5',
		'vp90-2-14-resize-fp-tiles-4-1.webm',
		'vp90-2-14-resize-fp-tiles-4-1.webm.md5',
		'vp90-2-14-resize-fp-tiles-4-16.webm',
		'vp90-2-14-resize-fp-tiles-4-16.webm.md5',
		'vp90-2-14-resize-fp-tiles-4-2.webm',
		'vp90-2-14-resize-fp-tiles-4-2.webm.md5',
		'vp90-2-14-resize-fp-tiles-4-8.webm',
		'vp90-2-14-resize-fp-tiles-4-8.webm.md5',
		'vp90-2-14-resize-fp-tiles-8-1.webm',
		'vp90-2-14-resize-fp-tiles-8-1.webm.md5',
		'vp90-2-14-resize-fp-tiles-8-16.webm',
		'vp90-2-14-resize-fp-tiles-8-16.webm.md5',
		'vp90-2-14-resize-fp-tiles-8-2.webm',
		'vp90-2-14-resize-fp-tiles-8-2.webm.md5',
		'vp90-2-14-resize-fp-tiles-8-4.webm',
		'vp90-2-14-resize-fp-tiles-8-4.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-1-2-4-8.webm',
		'vp90-2-14-resize-10frames-fp-tiles-1-2-4-8.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-1-2.webm',
		'vp90-2-14-resize-10frames-fp-tiles-1-2.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-1-4.webm',
		'vp90-2-14-resize-10frames-fp-tiles-1-4.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-1-8.webm',
		'vp90-2-14-resize-10frames-fp-tiles-1-8.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-2-1.webm',
		'vp90-2-14-resize-10frames-fp-tiles-2-1.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-2-4.webm',
		'vp90-2-14-resize-10frames-fp-tiles-2-4.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-2-8.webm',
		'vp90-2-14-resize-10frames-fp-tiles-2-8.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-4-1.webm',
		'vp90-2-14-resize-10frames-fp-tiles-4-1.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-4-2.webm',
		'vp90-2-14-resize-10frames-fp-tiles-4-2.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-4-8.webm',
		'vp90-2-14-resize-10frames-fp-tiles-4-8.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-8-1.webm',
		'vp90-2-14-resize-10frames-fp-tiles-8-1.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-8-2.webm',
		'vp90-2-14-resize-10frames-fp-tiles-8-2.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-8-4-2-1.webm',
		'vp90-2-14-resize-10frames-fp-tiles-8-4-2-1.webm.md5',
		'vp90-2-14-resize-10frames-fp-tiles-8-4.webm',
		'vp90-2-14-resize-10frames-fp-tiles-8-4.webm.md5',
		'vp90-2-15-segkey.webm',
		'vp90-2-15-segkey.webm.md5',
		'vp90-2-15-segkey_adpq.webm',
		'vp90-2-15-segkey_adpq.webm.md5',
		'vp90-2-16-intra-only.webm',
		'vp90-2-16-intra-only.webm.md5',
		'vp90-2-17-show-existing-frame.webm',
		'vp90-2-17-show-existing-frame.webm.md5',
		'vp90-2-18-resize.ivf',
		'vp90-2-18-resize.ivf.md5',
		'vp90-2-19-skip.webm',
		'vp90-2-19-skip.webm.md5',
		'vp90-2-19-skip-01.webm',
		'vp90-2-19-skip-01.webm.md5',
		'vp90-2-19-skip-02.webm',
		'vp90-2-19-skip-02.webm.md5',
		'vp91-2-04-yuv422.webm',
		'vp91-2-04-yuv422.webm.md5',
		'vp91-2-04-yuv440.webm',
		'vp91-2-04-yuv440.webm.md5',
		'vp91-2-04-yuv444.webm',
		'vp91-2-04-yuv444.webm.md5',
		'vp90-2-20-big_superframe-01.webm',
		'vp90-2-20-big_superframe-01.webm.md5',
		'vp90-2-20-big_superframe-02.webm',
		'vp90-2-20-big_superframe-02.webm.md5',
		# 'vp92-2-20-10bit-yuv420.webm', # MANUAL
		# 'vp92-2-20-10bit-yuv420.webm.md5', # MANUAL
		# 'vp92-2-20-12bit-yuv420.webm', # MANUAL
		# 'vp92-2-20-12bit-yuv420.webm.md5', # MANUAL
		# 'vp93-2-20-10bit-yuv422.webm', # MANUAL
		# 'vp93-2-20-10bit-yuv422.webm.md5', # MANUAL
		# 'vp93-2-20-12bit-yuv422.webm', # MANUAL
		# 'vp93-2-20-12bit-yuv422.webm.md5', # MANUAL
		# 'vp93-2-20-10bit-yuv440.webm', # MANUAL
		# 'vp93-2-20-10bit-yuv440.webm.md5', # MANUAL
		# 'vp93-2-20-12bit-yuv440.webm', # MANUAL
		# 'vp93-2-20-12bit-yuv440.webm.md5', # MANUAL
		# 'vp93-2-20-10bit-yuv444.webm', # MANUAL
		# 'vp93-2-20-10bit-yuv444.webm.md5', # MANUAL
		# 'vp93-2-20-12bit-yuv444.webm', # MANUAL
		# 'vp93-2-20-12bit-yuv444.webm.md5', # MANUAL
		'invalid-vp90-01-v3.webm',
		'invalid-vp90-01-v3.webm.res',
		'invalid-vp90-02-v2.webm',
		'invalid-vp90-02-v2.webm.res',
		'invalid-vp90-03-v3.webm',
		'invalid-vp90-03-v3.webm.res',
		'invalid-vp90-2-00-quantizer-00.webm.ivf.s5861_r01-05_b6-.v2.ivf',
		'invalid-vp90-2-00-quantizer-00.webm.ivf.s5861_r01-05_b6-.v2.ivf.res',
		'invalid-vp90-2-00-quantizer-11.webm.ivf.s52984_r01-05_b6-.ivf',
		'invalid-vp90-2-00-quantizer-11.webm.ivf.s52984_r01-05_b6-.ivf.res',
		'invalid-vp90-2-00-quantizer-11.webm.ivf.s52984_r01-05_b6-z.ivf',
		'invalid-vp90-2-00-quantizer-11.webm.ivf.s52984_r01-05_b6-z.ivf.res',
		'invalid-vp90-2-00-quantizer-63.ivf.kf_65527x61446.ivf',
		'invalid-vp90-2-00-quantizer-63.ivf.kf_65527x61446.ivf.res',
		'invalid-vp90-2-03-size-202x210.webm.ivf.s113306_r01-05_b6-.ivf',
		'invalid-vp90-2-03-size-202x210.webm.ivf.s113306_r01-05_b6-.ivf.res',
		'invalid-vp90-2-03-size-224x196.webm.ivf.s44156_r01-05_b6-.ivf',
		'invalid-vp90-2-03-size-224x196.webm.ivf.s44156_r01-05_b6-.ivf.res',
		'invalid-vp90-2-05-resize.ivf.s59293_r01-05_b6-.ivf',
		'invalid-vp90-2-05-resize.ivf.s59293_r01-05_b6-.ivf.res',
		'invalid-vp90-2-08-tile_1x2_frame_parallel.webm.ivf.s47039_r01-05_b6-.ivf',
		'invalid-vp90-2-08-tile_1x2_frame_parallel.webm.ivf.s47039_r01-05_b6-.ivf.res',
		'invalid-vp90-2-08-tile_1x8_frame_parallel.webm.ivf.s288_r01-05_b6-.ivf',
		'invalid-vp90-2-08-tile_1x8_frame_parallel.webm.ivf.s288_r01-05_b6-.ivf.res',
		'invalid-vp90-2-08-tile_1x4_frame_parallel_all_key.webm',
		'invalid-vp90-2-08-tile_1x4_frame_parallel_all_key.webm.res',
		'invalid-vp90-2-09-aq2.webm.ivf.s3984_r01-05_b6-.v2.ivf',
		'invalid-vp90-2-09-aq2.webm.ivf.s3984_r01-05_b6-.v2.ivf.res',
		'invalid-vp90-2-09-subpixel-00.ivf.s19552_r01-05_b6-.v2.ivf',
		'invalid-vp90-2-09-subpixel-00.ivf.s19552_r01-05_b6-.v2.ivf.res',
		'invalid-vp90-2-09-subpixel-00.ivf.s20492_r01-05_b6-.v2.ivf',
		'invalid-vp90-2-09-subpixel-00.ivf.s20492_r01-05_b6-.v2.ivf.res',
		'invalid-vp90-2-10-show-existing-frame.webm.ivf.s180315_r01-05_b6-.ivf',
		'invalid-vp90-2-10-show-existing-frame.webm.ivf.s180315_r01-05_b6-.ivf.res',
		'invalid-vp90-2-12-droppable_1.ivf.s3676_r01-05_b6-.ivf',
		'invalid-vp90-2-12-droppable_1.ivf.s3676_r01-05_b6-.ivf.res',
		'invalid-vp90-2-12-droppable_1.ivf.s73804_r01-05_b6-.ivf',
		'invalid-vp90-2-12-droppable_1.ivf.s73804_r01-05_b6-.ivf.res',
		'invalid-vp90-2-21-resize_inter_320x180_5_3-4.webm.ivf.s45551_r01-05_b6-.ivf',
		'invalid-vp90-2-21-resize_inter_320x180_5_3-4.webm.ivf.s45551_r01-05_b6-.ivf.res',
		'invalid-vp91-2-mixedrefcsp-444to420.ivf',
		'invalid-vp91-2-mixedrefcsp-444to420.ivf.res',
		'invalid-vp90-2-07-frame_parallel-1.webm',
		'invalid-vp90-2-07-frame_parallel-2.webm',
		'invalid-vp90-2-07-frame_parallel-3.webm',
		'invalid-crbug-629481.webm',
		'invalid-crbug-629481.webm.res',
		'invalid-crbug-1558.ivf',
		'invalid-crbug-1558.ivf.res',
		'invalid-crbug-1562.ivf',
		'invalid-crbug-1562.ivf.res',
		'invalid-crbug-667044.webm',
		'invalid-crbug-667044.webm.res',
		'crbug-1539.rawfile',
		# 'vp90-2-bbb_426x240_tile_1x1_180kbps.webm', # MANUAL
		# 'vp90-2-bbb_640x360_tile_1x2_337kbps.webm', # MANUAL
		# 'vp90-2-bbb_854x480_tile_1x2_651kbps.webm', # MANUAL
		# 'vp90-2-bbb_1280x720_tile_1x4_1310kbps.webm', # MANUAL
		# 'vp90-2-bbb_1920x1080_tile_1x1_2581kbps.webm', # MANUAL
		# 'vp90-2-bbb_1920x1080_tile_1x4_2586kbps.webm', # MANUAL
		# 'vp90-2-bbb_1920x1080_tile_1x4_fpm_2304kbps.webm', # MANUAL
		# 'vp90-2-sintel_426x182_tile_1x1_171kbps.webm', # MANUAL
		# 'vp90-2-sintel_640x272_tile_1x2_318kbps.webm', # MANUAL
		# 'vp90-2-sintel_854x364_tile_1x2_621kbps.webm', # MANUAL
		# 'vp90-2-sintel_1280x546_tile_1x4_1257kbps.webm', # MANUAL
		# 'vp90-2-sintel_1920x818_tile_1x4_fpm_2279kbps.webm', # MANUAL
		# 'vp90-2-tos_426x178_tile_1x1_181kbps.webm', # MANUAL
		# 'vp90-2-tos_640x266_tile_1x2_336kbps.webm', # MANUAL
		# 'vp90-2-tos_854x356_tile_1x2_656kbps.webm', # MANUAL
		# 'vp90-2-tos_854x356_tile_1x2_fpm_546kbps.webm', # MANUAL
		# 'vp90-2-tos_1280x534_tile_1x4_1306kbps.webm', # MANUAL
		# 'vp90-2-tos_1280x534_tile_1x4_fpm_952kbps.webm', # MANUAL
		# 'vp90-2-tos_1920x800_tile_1x4_fpm_2335kbps.webm', # MANUAL
		'vp90-2-21-resize_inter_320x180_5_1-2.webm',
		'vp90-2-21-resize_inter_320x180_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_320x180_5_3-4.webm',
		'vp90-2-21-resize_inter_320x180_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_320x180_7_1-2.webm',
		'vp90-2-21-resize_inter_320x180_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_320x180_7_3-4.webm',
		'vp90-2-21-resize_inter_320x180_7_3-4.webm.md5',
		'vp90-2-21-resize_inter_320x240_5_1-2.webm',
		'vp90-2-21-resize_inter_320x240_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_320x240_5_3-4.webm',
		'vp90-2-21-resize_inter_320x240_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_320x240_7_1-2.webm',
		'vp90-2-21-resize_inter_320x240_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_320x240_7_3-4.webm',
		'vp90-2-21-resize_inter_320x240_7_3-4.webm.md5',
		'vp90-2-21-resize_inter_640x360_5_1-2.webm',
		'vp90-2-21-resize_inter_640x360_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_640x360_5_3-4.webm',
		'vp90-2-21-resize_inter_640x360_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_640x360_7_1-2.webm',
		'vp90-2-21-resize_inter_640x360_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_640x360_7_3-4.webm',
		'vp90-2-21-resize_inter_640x360_7_3-4.webm.md5',
		'vp90-2-21-resize_inter_640x480_5_1-2.webm',
		'vp90-2-21-resize_inter_640x480_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_640x480_5_3-4.webm',
		'vp90-2-21-resize_inter_640x480_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_640x480_7_1-2.webm',
		'vp90-2-21-resize_inter_640x480_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_640x480_7_3-4.webm',
		'vp90-2-21-resize_inter_640x480_7_3-4.webm.md5',
		'vp90-2-21-resize_inter_1280x720_5_1-2.webm',
		'vp90-2-21-resize_inter_1280x720_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_1280x720_5_3-4.webm',
		'vp90-2-21-resize_inter_1280x720_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_1280x720_7_1-2.webm',
		'vp90-2-21-resize_inter_1280x720_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_1280x720_7_3-4.webm',
		'vp90-2-21-resize_inter_1280x720_7_3-4.webm.md5',
		'vp90-2-21-resize_inter_1920x1080_5_1-2.webm',
		'vp90-2-21-resize_inter_1920x1080_5_1-2.webm.md5',
		'vp90-2-21-resize_inter_1920x1080_5_3-4.webm',
		'vp90-2-21-resize_inter_1920x1080_5_3-4.webm.md5',
		'vp90-2-21-resize_inter_1920x1080_7_1-2.webm',
		'vp90-2-21-resize_inter_1920x1080_7_1-2.webm.md5',
		'vp90-2-21-resize_inter_1920x1080_7_3-4.webm',
		'vp90-2-21-resize_inter_1920x1080_7_3-4.webm.md5',
		'vp90-2-22-svc_1280x720_3.ivf',
		'vp90-2-22-svc_1280x720_3.ivf.md5',
		'vp90-2-22-svc_1280x720_1.webm',
		'vp90-2-22-svc_1280x720_1.webm.md5'
	],
	'vp9_encoder' : [
		'desktop_credits.y4m',
		'niklas_1280_720_30.y4m',
		'noisy_clip_640_360.y4m',
		'rush_hour_444.y4m',
		'screendata.y4m',
		'niklas_640_480_30.yuv',
		'bus_352x288_420_f20_b8.yuv',
		'niklas_1280_720_30.yuv',
		'desktop_640_360_30.yuv',
		'kirland_640_480_30.yuv',
		'macmarcomoving_640_480_30.yuv',
		'macmarcostationary_640_480_30.yuv',
		'niklas_1280_720_30.yuv',
		'tacomanarrows_640_480_30.yuv',
		'tacomasmallcameramovement_640_480_30.yuv',
		'thaloundeskmtg_640_480_30.yuv'
	],
}

if features.get('webm_io', false) # MANUAL
	libvpx_test_optional_sources += {
		'decoders' : libvpx_test_optional_sources['decoders'] + files(
			# '../third_party/libwebm/mkvparser/mkvparser.cc',
			# '../third_party/libwebm/mkvparser/mkvreader.cc',
			'../webmdec.cc',
			'vp9_skip_loopfilter_test.cc',
		)
	}

	libvpx_test_headers_optional_sources += {
		'decoders' : libvpx_test_headers_optional_sources['decoders'] + files(
			# '../third_party/libwebm/mkvparser/mkvparser.h',
			# '../third_party/libwebm/mkvparser/mkvreader.h',
			# '../third_party/libwebm/common/webmids.h',
			'../webmdec.h',
			'webm_video_source.h',
		)
	}
endif

# Currently we only support decoder perf tests for vp9. Also they read from WebM
# files, so WebM IO is required.
if features.get('decode_perf_tests', false) and features.get('vp9_decoder', false) and features.get('webm_io', false) # MANUAL
	libvpx_test_sources += files(
		'decode_perf_test.cc',
	)
endif

# encode perf tests are vp9 only
if features.get('encode_perf_tests', false) and features.get('vp9_encoder', false) # MANUAL
	libvpx_test_sources += files(
		'encode_perf_test.cc',
	)
endif

## Multi-codec blackbox tests.
if features.get('vp8_encoder', false) or features.get('vp9_encoder', false) # MANUAL
	libvpx_test_sources += files(
		'invalid_file_test.cc',
	)
endif

##
## WHITE BOX TESTS
##
## Whitebox tests invoke functions not exposed via the public API. Certain
## shared library builds don't make these functions accessible.
##
# (note from Amy)
# Those shared library builds are actually linkers that follow
# the module definitions. Alternatively, this implies that they are
# either MSVC or a compiler with -fvisibility=hidden by default.
if not features.get('shared', false) # MANUAL
	## VP8
	if features.get('vp8', false)
		# These tests require both the encoder and decoder to be built.
		if features.get('vp8_encoder', false) and features.get('vp8_decoder', false)
			libvpx_test_sources += files(
				'vp8_boolcoder_test.cc',
				'vp8_fragments_test.cc',
			)
		endif

		libvpx_test_optional_sources += {
			'postproc' : libvpx_test_optional_sources['postproc'] + files(
				'add_noise_test.cc',
				'pp_filter_test.cc',
			),
			'vp8_decoder' : libvpx_test_optional_sources['vp8_decoder'] + files(
				'vp8_decrypt_test.cc',
				'set_roi.cc',
				'variance_test.cc',
				'vp8_fdct4x4_test.cc',
			)
		}

		quantize_test_allowed_architectures = [
			'sse2', 'ssse3', 'sse4_1', 'neon', 'msa', 'mmi'
		]

		quantize_test_allowed = false
		foreach arch : quantize_test_allowed_architectures
			if features.get(arch, false)
				quantize_test_allowed = true
				break
			endif
		endforeach

		if quantize_test_allowed
			libvpx_test_optional_sources += {
				'vp8_decoder' : libvpx_test_optional_sources['vp8_decoder'] + files(
					'quantize_test.cc',
				)
			}
		endif

		libvpx_test_sources += files(
			'idct_test.cc',
			'predict_test.cc',
			'vpx_scale_test.cc',
		)

		libvpx_test_headers_sources += files(
			'vpx_scale_test.h',
		)

		if features.get('vp8_encoder', false) and features.get('temporal_denoising', false)
			libvpx_test_optional_sources += {
				'sse2' : libvpx_test_optional_sources['sse2'] + files(
					'vp8_denoiser_sse2_test.cc',
				)
			}
		endif
	endif

	## VP9
	if features.get('vp9', false)
		# These tests require both the encoder and decoder to be built.
		if features.get('vp9_encoder', false) and features.get('vp9_decoder', false)
			# IDCT test currently depends on FDCT function
			libvpx_test_sources += files(
				'idct8x8_test.cc',
				'partial_idct_test.cc',
				'superframe_test.cc',
				'tile_independence_test.cc',
				'vp9_boolcoder_test.cc',
				'vp9_encoder_parms_get_to_decoder.cc',
				'vp9_roi_test.cc',
			)
		endif

		libvpx_test_sources += files(
			'convolve_test.cc',
			'lpf_test.cc',
			'vp9_intrapred_test.cc',
		)

		libvpx_test_optional_sources += {
			'vp9_decoder' : libvpx_test_optional_sources['vp9_decoder'] + files(
				'vp9_decrypt_test.cc',
				'vp9_thread_test.cc',
			),
			'vp9_encoder' : libvpx_test_optional_sources['vp9_encoder'] + files(
				'avg_test.cc',
				'comp_avg_pred_test.cc',
				'dct16x16_test.cc',
				'dct32x32_test.cc',
				'dct_partial_test.cc',
				'dct_test.cc',
				'fdct8x8_test.cc',
				'hadamard_test.cc',
				'minmax_test.cc',
				'vp9_scale_test.cc',
				'variance_test.cc',
				'vp9_quantize_test.cc',
				'vp9_subtract_test.cc',
			)
		}

		if not features.get('realtime_only', false)
			libvpx_test_optional_sources += {
				'vp9_encoder' : libvpx_test_optional_sources['vp9_encoder'] + files(
					'yuv_temporal_filter_test.cc',
				)
			}
		endif

		if features.get('sse2', false) or features.get('avx2', false)
			libvpx_test_optional_sources += {
				'vp9_encoder' : libvpx_test_optional_sources['vp9_encoder'] + files(
					'vp9_block_error_test.cc',
				)
			}
		endif

		if features.get('vp9_encoder', false)
			libvpx_test_optional_sources += {
				'internal_stats' : libvpx_test_optional_sources['internal_stats'] + files(
					'blockiness_test.cc',
					'consistency_test.cc',
					'non_greedy_mv_test.cc',
				)
			}
		endif

		if features.get('vp9_encoder', false) and features.get('vp9_temporal_denoising', false)
			libvpx_test_sources += files(
				'vp9_denoiser_test.cc',
			)
		endif

		libvpx_test_optional_sources += {
			'vp9_encoder' : libvpx_test_optional_sources['vp9_encoder'] + files(
				'vp9_arf_freq_test.cc',
			)
		}

		if features.get('vp9_encoder', false)
			simple_encode_test_optional_sources += {
				'rate_ctrl' : simple_encode_test_optional_sources['rate_ctrl']+ files(
					'simple_encode_test.cc',
				)
			}
		endif
	endif

	## Multi-codec / unconditional whitebox tests.
	libvpx_test_optional_sources += {
		'encoders' : libvpx_test_optional_sources['encoders'] + files(
			'sad_test.cc'
		)
	}

	if features.get('neon', false) or features.get('sse2', false) or features.get('msa', false)
		libvpx_test_optional_sources += {
			'encoders' : libvpx_test_optional_sources['encoders'] + files(
				'sum_squares_test.cc'
			)
		}
	endif

	test_intra_pred_speed_sources += files(
		'test_intra_pred_speed.cc',
		'../md5_utils.c',
	)

	test_intra_pred_speed_headers_sources = files(
		'../md5_utils.h',
	)

	rc_interface_test_optional_sources += {
		'encoders' : rc_interface_test_optional_sources['encoders'] + files(
			'encode_test_driver.cc'
		),
		'vp8_encoder' : rc_interface_test_optional_sources['encoders'] + files(
			'vp8_ratectrl_rtc_test.cc'
		),
		'vp9_encoder' : rc_interface_test_optional_sources['encoders'] + files(
			'vp9_ratectrl_rtc_test.cc'
		),
	}

	rc_interface_test_sources = files(
		'test_rc_interface.cc',
		'decode_test_driver.cc',
	)

	rc_interface_test_headers_sources += files(
		'decode_test_driver.h',
		'codec_factory.h',
	)
endif

if features.get('vp9_highbitdepth', false)
	libvpx_test_data_data_optional_sources += {
		'vp9_decoder' : libvpx_test_data_data_optional_sources['vp9_decoder'] + [
			'vp92-2-20-10bit-yuv420.webm',
			'vp92-2-20-10bit-yuv420.webm.md5',
			'vp92-2-20-12bit-yuv420.webm',
			'vp92-2-20-12bit-yuv420.webm.md5',
			'vp93-2-20-10bit-yuv422.webm',
			'vp93-2-20-10bit-yuv422.webm.md5',
			'vp93-2-20-12bit-yuv422.webm',
			'vp93-2-20-12bit-yuv422.webm.md5',
			'vp93-2-20-10bit-yuv440.webm',
			'vp93-2-20-10bit-yuv440.webm.md5',
			'vp93-2-20-12bit-yuv440.webm',
			'vp93-2-20-12bit-yuv440.webm.md5',
			'vp93-2-20-10bit-yuv444.webm',
			'vp93-2-20-10bit-yuv444.webm.md5',
			'vp93-2-20-12bit-yuv444.webm',
			'vp93-2-20-12bit-yuv444.webm.md5',
		]
	}
endif

if features.get('decode_perf_tests', false)
	libvpx_test_data_data_optional_sources += {
		'vp9_encoder' : libvpx_test_data_data_optional_sources['vp9_encoder'] + [
			# Encode / Decode test
			'niklas_1280_720_30.yuv',
		],
		'vp9_decoder' : libvpx_test_data_data_optional_sources['vp9_decoder'] + [
			# BBB VP9 streams
			'vp90-2-bbb_426x240_tile_1x1_180kbps.webm',
			'vp90-2-bbb_640x360_tile_1x2_337kbps.webm',
			'vp90-2-bbb_854x480_tile_1x2_651kbps.webm',
			'vp90-2-bbb_1280x720_tile_1x4_1310kbps.webm',
			'vp90-2-bbb_1920x1080_tile_1x1_2581kbps.webm',
			'vp90-2-bbb_1920x1080_tile_1x4_2586kbps.webm',
			'vp90-2-bbb_1920x1080_tile_1x4_fpm_2304kbps.webm',
			# Sintel VP9 streams
			'vp90-2-sintel_426x182_tile_1x1_171kbps.webm',
			'vp90-2-sintel_640x272_tile_1x2_318kbps.webm',
			'vp90-2-sintel_854x364_tile_1x2_621kbps.webm',
			'vp90-2-sintel_1280x546_tile_1x4_1257kbps.webm',
			'vp90-2-sintel_1920x818_tile_1x4_fpm_2279kbps.webm',
			# TOS VP9 streams
			'vp90-2-tos_426x178_tile_1x1_181kbps.webm',
			'vp90-2-tos_640x266_tile_1x2_336kbps.webm',
			'vp90-2-tos_854x356_tile_1x2_656kbps.webm',
			'vp90-2-tos_854x356_tile_1x2_fpm_546kbps.webm',
			'vp90-2-tos_1280x534_tile_1x4_1306kbps.webm',
			'vp90-2-tos_1280x534_tile_1x4_fpm_952kbps.webm',
			'vp90-2-tos_1920x800_tile_1x4_fpm_2335kbps.webm',
		]
	}
endif

if features.get('encode_perf_tests', false)
	libvpx_test_data_data_optional_sources += {
		'vp9_encoder' : libvpx_test_data_data_optional_sources['vp9_encoder'] + [
			'desktop_640_360_30.yuv',
			'kirland_640_480_30.yuv',
			'macmarcomoving_640_480_30.yuv',
			'macmarcostationary_640_480_30.yuv',
			'niklas_1280_720_30.yuv',
			'tacomanarrows_640_480_30.yuv',
			'tacomasmallcameramovement_640_480_30.yuv',
			'thaloundeskmtg_640_480_30.yuv',
		]
	}
endif

#### --- END GENERATED --- ####

optional_sources = get_variable('libvpx_test_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		libvpx_test_sources += comp_sources
	endif
endforeach

optional_sources = get_variable('libvpx_test_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		libvpx_test_headers_sources += comp_sources
	endif
endforeach

optional_sources = get_variable('rc_interface_test_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		rc_interface_test_sources += comp_sources
	endif
endforeach

optional_sources = get_variable('simple_encode_test_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		simple_encode_test_sources += comp_sources
	endif
endforeach

optional_sources = get_variable('libvpx_test_data_data_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		libvpx_test_data_data_sources += comp_sources
	endif
endforeach

##
## libvpx test directives
##

libvpx_test_deps = [libvpx_dep, gtest_dep]

if features.get('webm_io', false)
	libvpx_test_deps += libwebm_dep
endif

LIBVPX_TEST_BIN = executable(
	'test_libvpx',
	libvpx_test_sources,
	extra_files: libvpx_test_headers_sources,
	dependencies: libvpx_test_deps
)

libvpx_test_data_url = 'https://storage.googleapis.com/downloads.webmproject.org/test_data/libvpx/@0@'

libvpx_test_data = []
libvpx_test_data_dedup = configuration_data()

foreach f : libvpx_test_data_data_sources
	if not libvpx_test_data_dedup.get(f, false)
		libvpx_test_data += custom_target(
			f,
			command: [curl_exe, '-S', '-s', '--retry', '1', '-L', '-o', '@OUTPUT@', libvpx_test_data_url.format(f)],
			output: f
		)
		libvpx_test_data_dedup.set(f, true)
	endif
endforeach

test_data_manifest = files(
	'test-data.sha1'
)

testdata = custom_target(
	'testdata',
	command: [check_test_data, '@INPUT@'],
	output: 'testdata.txt',
	input: test_data_manifest,
	depends: libvpx_test_data,
	capture: true
)

if test_intra_pred_speed_sources.length() > 0
	TEST_INTRA_PRED_SPEED_BIN = executable(
		'test_intra_pred_speed',
		test_intra_pred_speed_sources,
		extra_files: test_intra_pred_speed_headers_sources,
		dependencies: [libvpx_dep, gtest_dep]
	)
	test('test_intra_pred_speed', TEST_INTRA_PRED_SPEED_BIN)
endif

if features.get('encoders', false) and rc_interface_test_sources.length() > 0
	RC_INTERFACE_TEST_BIN = executable(
		'test_rc_interface',
		rc_interface_test_sources,
		extra_files: rc_interface_test_headers_sources,
		link_with: vpxrc_lib,
		dependencies: [libvpx_dep, gtest_dep]
	)

	test(
		'test_rc_interface',
		RC_INTERFACE_TEST_BIN,
		depends: testdata,
	)
endif

if simple_encode_test_sources.length() > 0
	SIMPLE_ENCODE_TEST_BIN = executable(
		'test_simple_encode',
		simple_encode_test_sources,
		link_with: simple_encode_lib,
		dependencies: [libvpx_dep, gtest_dep]
	)
	test(
		'test_simple_encode',
		SIMPLE_ENCODE_TEST_BIN,
		depends: testdata,
	)
endif

NUM_SHARDS = 10

foreach i : range(0, NUM_SHARDS)
	test('test_shard.@0@'.format(i), LIBVPX_TEST_BIN,
		env: {
			'GTEST_SHARD_INDEX': '@0@'.format(i),
			'GTEST_TOTAL_SHARDS': '@0'.format(NUM_SHARDS),
		}
	)
endforeach

##
## vpxdec/vpxenc tests.
##
test(
	'utiltest_vpxdec',
	vpxdec_sh,
	args: ['--test-data-path', meson.current_build_dir(), '--bin-path', meson.current_build_dir()],
	depends: testdata,
)
test(
	'utiltest_vpxenc',
	vpxenc_sh,
	args: ['--test-data-path', meson.current_build_dir(), '--bin-path', meson.current_build_dir()],
	depends: testdata,
)

##
## Example tests.
##
test(
	'exampletest',
	examples_sh,
	args: ['--test-data-path', meson.current_build_dir(), '--bin-path', meson.current_build_dir()],
	depends: testdata,
)
