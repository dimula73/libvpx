#### --- MANUAL --- ####

# inverse transform
if features.get('vp9', true) # MANUAL
	if features.get('neon_asm', false)
		dsp_sources += configure_file(
			command: [stdinout_wrapper_exe, '--input', '@INPUT@', '--output', '@OUTPUT@', asm_conversion_exe.full_path()] + asm_conversion_cmd,
			input: 'idct_neon.asm',
			output: 'idct_neon.asm.S'
		)
	endif
endif
