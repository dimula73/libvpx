project('nasm', 'c', license: 'BSD-2-Clause')

if host_machine.system() == 'windows'
	nasm_exe = find_program('nasm', required: true)
	meson.override_find_program('nasm_windows_exe', nasm_exe)
elif host_machine.system() == 'darwin'
	python_exe = find_program('patch_nasm.py')
	run_command(python_exe, meson.current_source_dir(), check: true)
	nasm_exe = find_program('nasm', required: true)
	meson.override_find_program('nasm_macos_exe', nasm_exe)
else
	error('This wrap only supports Windows or macOS')
endif
