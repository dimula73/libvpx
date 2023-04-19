project('strawberryperl', 'c', license: ' Artistic-1.0-Perl OR GPL-1.0-or-later')

perl_exe = find_program('perl',
	dirs: [meson.current_source_dir() / 'perl' / 'bin'],
	required: true
)

meson.override_find_program('perl_windows_exe', perl_exe)
