# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

project(
	'libvpx',
	'c', 'cpp',
	version: '1.13.0',
	default_options: [
		# Enforce c89 for c files. Don't be too strict about it though. Allow
		# gnu extensions like "//" for comments.
		'c_std=gnu89',
		# Uncomment when Meson can handle this one for MSVC.
		# 'cpp_std=gnu++11',
		'warning_level=2',
		'default_library=static',
		'buildtype=debugoptimized',
	],
	license: 'BSD-3-Clause',
	meson_version: '>=0.64',
)

features = configuration_data()

asm_conversion_exe = disabler()
asm_conversion_cmd = []
as_sfx = '.asm'
asm_args = []
tune_cflags = ''
rtcd_options = []
link_args = []
extra_libs = []

libyuv_cpp_args = []

#######################
###### configure ######
#######################

# all_targets is a list of all targets that can be configured
# note that these should be in dependency order for now.
all_targets = [
	'libs',
	'examples',
	'tools',
	'docs',
]

# all targets available are enabled, by default.
foreach t : all_targets
	features.set(t, true)
endforeach

# we don't use diff in Meson.
perl_executables = ['perl']
# Adding Meson overrides manually.
if host_machine.system() == 'windows'
	perl_executables += ['perl_windows_exe']
endif
perl_exe = find_program(perl_executables, required: true)

doxygen = find_program('doxygen', required: false, disabler: true)

if doxygen.found()
	doxygen_version = doxygen.version()

	if doxygen_version.version_compare('>= 1.5.5.3')
		features.set('doxygen', true)
	endif
endif

# We don't disable codecs when their source directory does not exist
# because it's Git and they all exist.

# install everything except the sources, by default. sources will have
# to be enabled when doing dist builds, since that's no longer a common
# case.
if features.get('doxygen', false)
	features.set('install_docs', true)
endif
features.set('install_bins', true)
features.set('install_libs', true)

features.set('static', get_option('default_library') != 'shared')
features.set('shared', get_option('default_library') != 'static')
features.set('optimizations', true)
features.set('dependency_tracking', true)
features.set('spatial_resampling', true)
features.set('multithread', true)
features.set('os_support', true)
features.set('temporal_denoising', true)

CODECS = [
	'vp8_encoder',
	'vp8_decoder',
	'vp9_encoder',
	'vp9_decoder',
]

CODEC_FAMILIES = [
	'vp8',
	'vp9',
]

ARCH_LIST = [
	'arm',
	'mips',
	'x86',
	'x86_64',
	'ppc',
	'loongarch',
]

ARCH_EXT_LIST_X86 = [
	'mmx',
	'sse',
	'sse2',
	'sse3',
	'ssse3',
	'sse4_1',
	'avx',
	'avx2',
	'avx512',
]

ARCH_EXT_LIST_LOONGSON = [
	'mmi',
	'lsx',
	'lasx',
]

ARCH_EXT_LIST = [
	'neon',
	'neon_asm',

	'mips32',
	'dspr2',
	'msa',
	'mips64',
] + ARCH_EXT_LIST_X86 + [
	'vsx',
] + ARCH_EXT_LIST_LOONGSON

HAVE_LIST = ARCH_EXT_LIST + [
	'vpx_ports',
	'pthread_h',
	'unistd_h',
]

EXPERIMENT_LIST = [
	'fp_mb_stats',
	'emulate_hardware',
	'non_greedy_mv',
	'rate_ctrl',
	'collect_component_timing',
]

CONFIG_LIST = [
	'dependency_tracking',
	'external_build',
	'install_docs',
	'install_bins',
	'install_libs',
	'install_srcs',
	'debug',
	'gprof',
	'gcov',
	'rvct',
	'gcc',
	'msvs',
	'pic',
	'big_endian',

	'codec_srcs',
	'debug_libs',

	'dequant_tokens',
	'dc_recon',
	'runtime_cpu_detect',
	'postproc',
	'vp9_postproc',
	'multithread',
	'internal_stats',
] + CODECS + CODEC_FAMILIES + [
	'encoders',
	'decoders',
	'static_msvcrt',
	'spatial_resampling',
	'realtime_only',
	'onthefly_bitpacking',
	'error_concealment',
	'shared',
	'static',
	'small',
	'postproc_visualizer',
	'os_support',
	'unit_tests',
	'webm_io',
	'libyuv',
	'decode_perf_tests',
	'encode_perf_tests',
	'multi_res_encoding',
	'temporal_denoising',
	'vp9_temporal_denoising',
	'consistent_recode',
	'coefficient_range_checking',
	'vp9_highbitdepth',
	'better_hw_compatibility',
	'experimental',
	'size_limit',
	'always_adjust_bpm',
	'bitstream_debug',
	'mismatch_debug',
] + EXPERIMENT_LIST

# this is the list of toggleable options in meson_options.txt
# EXCEPT for a couple that I've separated because they're
# derived from the Meson configuration.
CMDLINE_SELECT = [
	'dependency_tracking',
	'external_build',
	'extra_warnings',
	'werror',
	'install_docs',
	'install_bins',
	'install_libs',
	'install_srcs',
	'debug',
	'gprof',
	'gcov',
	'pic',
	'optimizations',
	'ccache',
	'runtime_cpu_detect',
	'thumb',

	'libs',
	'examples',
	'tools',
	'docs',
	'libc',
	'as',
	'size_limit',
	'codec_srcs',
	'debug_libs',

	'dequant_tokens',
	'dc_recon',
	'postproc',
	'vp9_postproc',
	'multithread',
	'internal_stats',
] + CODECS + CODEC_FAMILIES + [
	'static_msvcrt',
	'spatial_resampling',
	'realtime_only',
	'onthefly_bitpacking',
	'error_concealment',
	'shared',
	'static',
	'small',
	'postproc_visualizer',
	'unit_tests',
	'webm_io',
	'libyuv',
	'decode_perf_tests',
	'encode_perf_tests',
	'multi_res_encoding',
	'temporal_denoising',
	'vp9_temporal_denoising',
	'consistent_recode',
	'coefficient_range_checking',
	'better_hw_compatibility',
	'vp9_highbitdepth',
	'experimental',
	'always_adjust_bpm',
	'bitstream_debug',
	'mismatch_debug',
]

# These options are either provided or handled by Meson
#### --- GENERATED EXTERN OPTIONS --- ####
IGNORE_MESON_BUILTINS = [
	'help',
	'log',
	'target',
	'extra_cflags',
	'extra_cxxflags',
	'extra_warnings',
	'werror',
	'optimizations',
	'pic',
	'ccache',
	'debug',
	'gcov',
	'dependency_tracking',
	'libc',
	'as',
	'shared',
	'static',
	'small',
	'static_msvcrt',
	'debug_libs',
	'install_srcs',
]

MESON_OPTIONS = [
	'gprof',
	'thumb',
	'install_docs',
	'install_bins',
	'install_libs',
	'decode_perf_tests',
	'encode_perf_tests',
	'codec_srcs',
	'vp9_highbitdepth',
	'better_hw_compatibility',
	'internal_stats',
	'postproc',
	'vp9_postproc',
	'multithread',
	'spatial_resampling',
	'realtime_only',
	'onthefly_bitpacking',
	'error_concealment',
	'coefficient_range_checking',
	'runtime_cpu_detect',
	'postproc_visualizer',
	'multi_res_encoding',
	'temporal_denoising',
	'vp9_temporal_denoising',
	'webm_io',
	'libyuv',
]

MESON_FEATURES = [
	'libs',
	'examples',
	'tools',
	'docs',
	'unit_tests',
	'vp8',
	'vp9',
	'vp8_encoder',
	'vp8_decoder',
	'vp9_encoder',
	'vp9_decoder',
]
#### --- END GENERATED EXTERN OPTIONS --- ####

VAR_LIST = []

# process #

## process_cmdline ##

features.set('extra_warnings', not ['0', '1'].contains(get_option('warning_level')))
features.set('werror', get_option('werror'))
features.set('debug', ['debug', 'debugoptimized'].contains(get_option('buildtype')))
features.set('gcov', get_option('b_coverage'))
features.set('static_msvcrt', ['static_from_buildtype', 'mt'].contains(get_option('b_vscrt')))
features.set('debug_libs', features.get('debug', false))

tune_cpu = ''

foreach flag: CMDLINE_SELECT
	if IGNORE_MESON_BUILTINS.contains(flag)
		continue
	elif MESON_FEATURES.contains(flag)
		value = get_option(flag)
		if not value.auto()
			features.set(flag, value.enabled())
		endif
	elif MESON_OPTIONS.contains(flag)
		value = get_option(flag)
		if value != 'auto'
			features.set(flag, value == 'enabled')
		endif
	elif flag == 'size_limit'
		size_limit_value = get_option('size_limit')
		if size_limit_value == ''
			continue
		endif

		size_limit_value = size_limit_value.split('x')

		if size_limit_value.length() != 2
			error('Invalid size-limit: must be of the form WIDTHxHEIGHT')
		endif

		w = size_limit_value[0].to_int()
		h = size_limit_value[1].to_int()
		if w <= 0 or h <= 0
			error('Invalid size-limit: too small.')
		elif w >= 65536 or h >= 65536
			error('Invalid size-limit: too big.')
		else
			var_list += ['DECODE_WIDTH_LIMIT', 'DECODE_HEIGHT_LIMIT']
			features.set('DECODE_WIDTH_LIMIT', w)
			features.set('DECODE_HEIGHT_LIMIT', h)
			features.set('size_limit', true)
		endif
	elif flag == 'cpu'
		tune_cpu = get_option(flag)
	else
		continue
	endif
endforeach

enable_features = get_option('enable_features')
disable_features = get_option('disable_features')
force_disable_features = get_option('force_disable_features')
force_enable_features = get_option('force_enable_features')

if enable_features.contains('help') or disable_features.contains('help') or force_disable_features.contains('help') or force_enable_features.contains('help')
	error('''
		These are the list of available features:
		Experiments: @0@
		Codecs:
		Codec families:
		Architectures:
		Toggles:
	'''.format(EXPERIMENT_LIST, CODECS, CODEC_FAMILIES, ARCH_EXT_LIST, CMDLINE_SELECT))
endif

foreach feature: enable_features
	if EXPERIMENT_LIST.contains(feature)
		if features.get('experimental', false)
			features.set(feature, true)
		else
			warning('Ignoring @0@ -- not in experimental mode.'.format(feature))
		endif
	elif CODECS.contains(feature) or CODEC_FAMILIES.contains(feature)
		message('\tenabling @0@'.format(feature))
		features.set(feature, true)
		if CODECS.contains(feature)
			features.set('@0@_encoder'.format(feature), true)
			features.set('@0@_decoder'.format(feature), true)
		endif
	elif ARCH_EXT_LIST.contains(feature)
		continue
	elif not features.get(feature, false) # action == 'enable and not enabled
		if not CMDLINE_SELECT.contains(feature)
			error('Unknown option @0@'.format(feature))
		endif
		message('\tenabling @0@'.format(feature))
	endif
	features.set(feature, true)
endforeach
foreach feature: disable_features
	if EXPERIMENT_LIST.contains(feature)
		if features.get('experimental', false)
			features.set(feature, false)
		else
			warning('Ignoring @0@ -- not in experimental mode.'.format(feature))
		endif
	elif CODECS.contains(feature) or CODEC_FAMILIES.contains(feature)
		message('\tdisabling @0@'.format(feature))
		features.set(feature, true)
		if CODECS.contains(feature)
			features.set('@0@_encoder'.format(feature), false)
			features.set('@0@_decoder'.format(feature), false)
		endif
	elif ARCH_EXT_LIST.contains(feature)
		rtcd_options += ['--disable-@0@'.format(feature)]
	elif features.get(feature, true) # action == disable and not disabled
		if not CMDLINE_SELECT.contains(feature)
			error('Unknown option @0@'.format(feature))
		endif
		message('\tdisabling @0@'.format(feature))
	endif
	features.set(feature, false)
endforeach

foreach feature: force_disable_features
	features.set(feature, false)
endforeach
foreach feature: force_enable_features
	features.set(feature, true)
endforeach

## post_process_common_cmdline ##

## post_process_cmdline ##

if features.get('coefficient_range_checking', false)
	warn('coefficient-range-checking is for decoders only, disabling encoders')
	encoders_features = ['vp8_encoder', 'vp9_encoder']
	foreach feature: encoders_features # soft_disable
		if not features.get(feature, false) # ! enabled
			if not features.has(feature) # disabled
				message('\tdisabling @0@'.format(feature))
			endif
			features.set(feature, false)
		endif
	endforeach
endif

# Enable all detected codecs, if they haven't been disabled
foreach feature: CODECS
	if features.get(feature, true) # soft_enabled
		if not features.has(feature)
			message('\tenabling @0@'.format(feature))
		endif
		features.set(feature, true)
	endif
endforeach

# Enable the codec family if any component of that family is enabled
foreach feature: CODECS
	if features.get(feature, true)
		features.set(feature.split('_')[0], true)
	endif
endforeach

# Set the {en,de}coders variable if any algorithm in that class is enabled
# Grep help: CONFIG_DECODERS, decoders, encoders
foreach feature: CODECS
	if features.get(feature, true)
		features.set('@0@s'.format(feature.split('_')[1]), true)
	endif
endforeach

### process_toolchain ###
#### process_common_toolchain ####

c = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')
asm = meson.get_compiler('c') # asm == GCC

tgt_isa = target_machine.cpu_family()
tgt_os = target_machine.system()
tgt_cc = c.get_id()

if tgt_isa == 'arm'
	# The __SOFTFP__ macro is unreliable, clang defines it
	# as __SOFT_FP__. The other one matches the configure script better.
	if c.get_define('__ARM_PCS_VFP') != ''
		float_abi = 'hard'
	else
		float_abi = 'softfp'
	endif
endif

if tgt_os == 'windows' or tgt_os == 'cygwin'
	tgt_os = 'windows'
elif ['darwin', 'ios', 'tvos'].contains(tgt_os)
	# The gcc -dumpmachine bit is used to force -mmacosx-version-min/max
	warning('Apple target detected, please supply the --m(macos|ios)-version-* and -isysroot flags through -Dc_flags or a native file')

	if tgt_os == 'darwin'
		# Detect if iOS, tvOS...
		xcrun_exe = find_program('xcrun', required: true)

		# The only one actually used is the iPhone simulator-- see later
		# is_ios = c.get_define('TARGET_OS_MAC', prefix: '#include <TargetConditionals.h>')
		# is_tvos = c.get_define('TARGET_OS_TV', prefix: '#include <TargetConditionals.h>')
		is_simulator = c.get_define('TARGET_OS_SIMULATOR', prefix: '#include <TargetConditionals.h>')

		# if is_ios.to_int() == 1
		# 	tgt_os = 'ios'
		# elif is_tvos.to_int() == 1
		# 	tgt_os = 'tvos'
		# el
		if is_simulator.to_int() == 1
			tgt_os = 'iphonesimulator'
		endif
	endif
elif tgt_os == 'linux' or tgt_os.endswith('bsd')
	tgt_os = 'linux'
elif tgt_os == 'sunos'
	tgt_os = 'solaris'
endif

#
# Set up toolchain variables
#

# Mark the specific ISA requested as enabled
if tgt_isa == 'aarch64'
	tgt_isa = 'arm64'
elif tgt_isa == 'arm'
	arm_arch = c.get_define('__ARM_ARCH')
	if arm_arch == ''
		arm_arch = c.get_define('_M_ARM')
	endif
	if arm_arch == ''
		warning('Unknown 32-bit Arm architecture version, assuming v7-a')
		arm_arch = '7'
	endif
	tgt_isa = 'armv@0@'.format(arm_arch)
elif tgt_isa.startswith('sparc')
	tgt_isa = 'sparc'
elif tgt_isa == 'ppc64' and target_machine.endian() == 'little'
	tgt_isa = 'ppc64le'
elif tgt_isa == 'mips'
	tgt_isa = 'mips32'
elif not tgt_isa.startswith('x86')
	tgt_isa = 'generic'
endif
if features.get(tgt_isa, true) # soft_enabled
	if not features.has(tgt_isa)
		message('\tenabling @0@'.format(tgt_isa))
	endif
	features.set(tgt_isa, true)
endif
if c.get_argument_syntax() == 'msvc'
	tgt_cc = 'msvs' # Upstream uses "vs@0@".format(vs_major_version_number)
elif c.get_id() == 'icc'
	tgt_cc = 'icc'
elif ['gcc', 'clang'].contains(c.get_id())
	tgt_cc = 'gcc'
else
	tgt_cc = 'gnu'
endif
features.set(tgt_cc, true)

# Enable the architecture family
if tgt_isa.startswith('arm')
	features.set('arm', true)
elif tgt_isa.startswith('mips')
	features.set('mips', true)
elif tgt_isa.startswith('ppc')
	features.set('ppc', true)
elif tgt_isa == 'loongarch64'
	features.set('loongarch', true)
	loongson_features = ['lsx', 'lasx']
	foreach feature : loongson_features
		if features.get(feature, true)
			if not feature.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
endif

# Handle Solaris variants. Solaris 10 needs -lposix4
if tgt_os == 'solaris'
	extra_libs += c.find_library('posix4', required: true)
endif

if tgt_isa.startswith('arm')
	feature = 'neon'
	if features.get(feature, true)
		if not features.has(feature)
			message('\tenabling @0@'.format(feature))
		endif
		features.set(feature, true)
	endif

	if tgt_isa == 'armv7'
		# Only enable neon_asm when neon is also enabled.
		if features.get('neon', false)
			feature = 'neon_asm'
			if features.get(feature, true)
				if not features.has(feature)
					message('\tenabling @0@'.format(feature))
				endif
				features.set(feature, true)
			endif
		endif
		# If someone tries to force it through, die.
		if not features.get('neon', true) and features.get('neon_asm', false)
			error('Disabling neon while keeping neon-asm is not supported')
		endif
	endif

	if tgt_cc == 'gcc'
		tune_cflags = '-mtune=@0@'

		if tgt_isa == 'armv7'
			if features.get('neon', false) or features.get('neon_asm', false)
				gcc_flags = ['-mfpu=neon']
				add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c') #-ftree-vectorize
				add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
			endif
		endif

		asm_conversion_exe = find_program('build/make/ads2gas.pl', required: true)
		asm_conversion_cmd = []
		as_sfx = '.S'

		if tgt_os == 'windows'
			asm_conversion_cmd += ['-noelf']
			features.set('thumb', true)
		endif

		if features.get('thumb', false)
			asm_conversion_cmd += ['-thumb']
			gcc_flags = ['-mthumb', '-Wa,-mimplicit-it=always']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c') #-ftree-vectorize
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
		endif
	elif tgt_cc == 'msvs'
		# A number of ARM-based Windows platforms are constrained by their
		# respective SDKs' limitations. Fortunately, these are all 32-bit ABIs
		# and so can be selected as 'win32'.

		if tgt_isa == 'armv7'
			asm_conversion_exe = find_program('build/make/ads2armasm_ms.py', required: true)
			asm_conversion_cmd = []
			as_sfx = '.masm'
			features.set('multithread', false)
			features.set('unit_tests', false)
			# We drive MSVC through Ninja here, so don't disable examples nor tools.
		else
			# Windows 10 on ARM, on the other hand, has full Windows SDK support
			# for building Win32 ARM64 applications in addition to ARM64
			# Windows Store apps. It is the only 64-bit ARM ABI that
			# Windows supports, so it is the default definition of 'win64'.
			# ARM64 build support officially shipped in Visual Studio 15.9.0.

			# Because the ARM64 Windows SDK's arm_neon.h is ARM32-specific
			# while LLVM's is not, probe its validity.
			if features.get('neon', false)
				if not c.compiles('''
						#include <arm_neon.h>
						int z;
					''',
					name: 'has a valid arm_neon.h file for the architecture'
				)
					features.set('win_arm64_neon_h_workaround', c.has_header('arm64_neon.h'))
				endif
			endif
		endif
	endif

	if tgt_os == 'android'
		message('Assuming standalone build with NDK toolchain.')
		# See later for why we allow shared builds.
		# features.set('static', true)
		feature = 'unit_tests'
		if features.get(feature, true)
			if not feature.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	elif tgt_os == 'darwin'
		if tgt_isa.startswith('arm')
			as_sfx = '.S'
			xcodebuild = find_program('xcodebuild', required: false)
			if xcodebuild.found()
				xcode_version = run_command(xcodebuild, '-version',
					capture: true,
					check: true
				).stdout().strip().split('\n').get(0, '').split()

				if features.get('neon', false) and xcode_version.get(1, '').version_compare('>=6.3')
					feature = 'neon'
					if not features.get(feature, false)
						if not features.has(feature)
							message('\tdisabling @0@'.format(feature))
						endif
						features.set(feature, false)
					endif
					warning('\tneon disabled: upgrade Xcode (need v6.3+)')
					if features.get('neon_asm', false)
						feature = 'neon_asm'
						if not features.get(feature, false)
							if not features.has(feature)
								message('\tdisabling @0@'.format(feature))
							endif
							features.set(feature, false)
						endif
						warning('\tneon disabled: upgrade Xcode (need v6.3+)')
					endif
				endif
			endif
		endif

		# Darwin toolchain and embed-bitcode options are Meson handled.
		asm_conversion_exe = find_program('build/make/ads2gas_apple.pl', required: true)
		asm_conversion_cmd = []
	elif tgt_os == 'linux'
		features.set('linux', true)
	endif
elif tgt_isa.startswith('mips')
	tune_cflags = '-mtune=@0@'

	if features.get('dspr2', false)
		add_project_arguments(c.get_supported_arguments('-mips2r32', '-mdspr2'), language: 'cpp')
		add_project_arguments(cpp.get_supported_arguments('-mips2r32', '-mdspr2'), language: 'cpp')
	endif

	if features.get('runtime_cpu_detect', false)
		features.set('runtime_cpu_detect', false)
	endif

	if tune_cpu != ''
		if tune_cpu == 'p5600'
			gcc_flags = ['-mips32r5', '-mload-store-pairs', '-msched-weight', '-mhard-float', '-mfp64']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
		elif ['i6400', 'p6600'].contains(tune_cpu)
			gcc_flags = ['-mips64r6', '-mabi=64', '-msched-weight', '-mload-store-pairs', '-mhard-float', '-mfp64']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
			add_project_link_arguments(c.get_supported_link_arguments(gcc_flags), language: 'c')
			add_project_link_arguments(cpp.get_supported_link_arguments(gcc_flags), language: 'cpp')
		elif tune_cpu.startswith('loongson3')
			if c.has_argument('-march=loongson3a')
				feature = 'mmi'
				if features.get(feature, true)
					if not feature.has(feature)
						message('\tenabling @0@'.format(feature))
					endif
					features.set(feature, true)
				endif
			else
				features.set('mmi', false)
			endif

			if c.has_argument('-mmsa')
				feature = 'msa'
				if features.get(feature, true)
					if not feature.has(feature)
						message('\tenabling @0@'.format(feature))
					endif
					features.set(feature, true)
				endif
			else
				features.set('msa', false)
			endif

			tgt_isa = 'loongson3a'
		endif

		if features.get('mmi', false) or features.get('msa', false)
			feature = 'runtime_cpu_detect'
			if features.get(feature, true)
				if not feature.has(feature)
					message('\tenabling @0@'.format(feature))
				endif
				features.set(feature, true)
			endif
		endif

		if features.get('msa', false)
			# TODO(libyuv:793)
			# The new mips functions in libyuv do not build
			# with the toolchains we currently use for testing.
			feature = 'libyuv'
			if not features.get(feature, false) # ! enabled
				if not features.has(feature) # disabled
					message('\tdisabling @0@'.format(feature))
				endif
				features.set(feature, false)
			endif
		endif
	endif

	add_project_arguments(c.get_supported_arguments('-march=@0@'.format(tgt_isa)), language: 'c')
	# KPIC is a flag that is valid only for SunCC.
	# As such, we'll use the Meson derived version.
elif tgt_isa == 'ppc64' and target_machine.endian() == 'little'
	# Do not enable vsx by default.
	# https://bugs.chromium.org/p/webm/issues/detail?id=1522
	if not features.get('vsx', false)
		rtcd_options += ['--disable-vsx']
	endif

	if tune_cpu.startswith('power')
		tune_cflags = '-mcpu=@0@'
	endif
elif tgt_isa.startswith('x86')
	if tgt_os == 'android'
		feature = 'realtime_only'
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	elif tgt_os == 'windows'
		if features.get('gcc', false)
			gcc_flags = ['-fno-common']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
		endif
	# Solaris is Meson handled, and OS/2 is unsupported by Meson.
	endif

	as = 'auto'

	if tgt_cc == 'icc'
		gcc_flags = ['-use-msasm']
		add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
		add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
		# add -no-intel-extensions to suppress warning #10237
		# refer to http://software.intel.com/en-us/forums/topic/280199
		# Meson: -i-static is deprecated
		# See https://www.cita.utoronto.ca/~merz/intel_c10b/main_cls/mergedProjects/copts_cls/common_options/option_i_static.htm
		gcc_flags = ['-static-intel', '-no-intel-extensions']
		add_project_link_arguments(c.get_supported_link_arguments(gcc_flags), language: 'c')
		add_project_link_arguments(cpp.get_supported_link_arguments(gcc_flags), language: 'cpp')

		if tgt_isa == 'x86_64'
			# -ipo is LTO, -static and -O3 all are Meson handled
			gcc_flags = ['-no-prec-div']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
			# xiar is also Meson handled
			if tune_cpu.startswith('atom')
				tune_cflags = '-x'
				tune_cpu = 'SSE3_ATOM'
			else
				tune_cflags = '-march=@0@'
			endif
		endif
	elif tgt_cc == 'gcc'
		tune_cflags = '-march='
		# #for 32 bit x86 builds, -O3 did not turn on this flag
		if features.get('optimizations', false) and not features.get('gprof', true)
			gcc_flags = ['-fomit-frame-pointer']
			add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
			add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
		endif
	elif tgt_cc == 'msvs'
		# Based on the Gerrit review, it seems the author intended to ban
		# VS 2017 and earlier.
		# See https://chromium-review.googlesource.com/c/webm/libvpx/+/751863
		if c.version().version_compare('< 19.20.27508')
			warning('This version of Visual Studio does not support avx512, disabling.....')
			rtcd_options += ['--disable-avx512']
			feature = 'avx512'
			if not features.get(feature, false) # ! enabled
				if not features.has(feature) # disabled
					message('\tdisabling @0@'.format(feature))
				endif
				features.set(feature, false)
			endif
		endif
	endif

	x86_bits = 32
	if target_machine.cpu_family() == 'x86_64'
		x86_bits = 64
	endif

	feature = 'runtime_cpu_detect'
	if features.get(tgt_isa, true) # soft_enabled
		if not features.has(tgt_isa)
			message('\tenabling @0@'.format(tgt_isa))
		endif
		features.set(tgt_isa, true)
	endif

	# Unline the original, we do can test cflags here :)
	disable_exts = false
	foreach ext : ARCH_EXT_LIST_X86
		# disable higher order extensions to simplify asm dependencies
		if disable_exts
			if features.get(ext, true)
				rtcd_options += ['--disable-@0@'.format(ext)]
				message('\tdisabling @0@'.format(ext))
				features.set(ext, false)
			endif
		elif not features.get(ext, true)
			disable_exts = true
		else
			if ext == 'avx512'
				exts = ['avx512f', 'avx512cd', 'avx512bw', 'avx512dq', 'avx512vl']
				foreach feature : exts
					if features.get('gcc', false) and features.get(ext, true) and not c.has_argument('-m@0@'.format(feature))
						rtcd_options += ['--disable-@0@'.format(ext)]
					else
						if features.get(ext, true) # soft_enabled
							if not features.has(ext)
								message('\tenabling @0@'.format(ext))
							endif
							features.set(ext, true)
						endif
					endif
				endforeach
				if features.get('gcc', true) and not c.compiles('''
					#include <immintrin.h>
					void f(void) {
						__m512i x = _mm512_set1_epi16(0);
						(void)x;
					}
					''',
					name: 'supports AVX512',
					args: '-mavx512f'
				)
					warning('disabling avx512: not supported by compiler')
					features.set('avx512', false)
					rtcd_options += ['--disable-avx512']
				endif
			else
				# use the shortened version for the flag: sse4_1 -> sse4
				exts = []
				if ext.contains('_')
					exts += [ext.split('_')[0]]
				else
					exts += [ext]
				endif
				opt = ext
				foreach feature : exts
					if features.get('gcc', false) and features.get(opt, true) and not c.has_argument('-m@0@'.format(feature))
						rtcd_options += ['--disable-@0@'.format(feature)]
					else
						if features.get(opt, true) # soft_enabled
							if not features.has(opt)
								message('\tenabling @0@'.format(opt))
							endif
							features.set(opt, true)
						endif
					endif
				endforeach
			endif
		endif
	endforeach

	nasm_exe = find_program('nasm', required: false)
	if meson.version().version_compare('> 1.1.0')
		yasm_exe = find_program('yasm', required: false)
	else
		# Removing Yasm support because Meson adds optimization flags
		# which it doesn't support.
		# https://github.com/mesonbuild/meson/issues/11726
		yasm_exe = disabler()
	endif
	# Adding Meson overrides manually.
	if not nasm_exe.found() and not yasm_exe.found()
		if host_machine.system() == 'windows'
			nasm_exe = find_program('nasm_windows_exe')
		elif host_machine.system() == 'darwin'
			nasm_exe = find_program('nasm_macos_exe')
		endif
	endif
	if nasm_exe.found()
		# Apple ships version 0.98 of nasm through at least Xcode 6. Revisit
		# this check if they start shipping a compatible version.
		out = run_command(nasm_exe, '-v', capture: true, check: true).stdout().strip()
		as = 'nasm'
		if out.contains('Apple')
			warning('Unsupported version of nasm: @0@'.format(out))
			as = 'auto'
		elif ['linux', 'solaris'].contains(tgt_os)
			out = out.split()
			if out[1].to_lower() == 'version'
				if out[2].version_compare('<2.09')
					error('nasm @0@ does not support section alignment'.format(out[2]))
				endif
			else
				error('unexpected nasm version string: @0@'.format(out))
			endif
		endif
	elif yasm_exe.found()
		as = 'yasm'
	endif

	if as == 'auto'
		error('Neither yasm nor nasm have been found. See the prerequisites section in the README for more info.')
	else
		add_languages('nasm', required: true)
	endif

	as_sfx = '.asm'

	# Nasm flags are Meson handled.
	if tgt_os == 'iphonesimulator'
		sdk_version = run_command(xcrun_exe, '--sdk', tgt_os, '--show-sdk-version', check: true, capture: true)
		if sdk_version.version_compare('> 8.0')
			# yasm v1.3.0 doesn't know what -fembed-bitcode means, so turning it
			# on is pointless (unless building a C-only lib). Warn the user, but
			# do nothing here.
			warning('Bitcode embed disabled for simulator targets.')
		endif
	endif
elif tgt_isa.startswith('loongarch')
	inline_asm = 'void foo(void) { __asm__ volatile(@0@); }'
	if features.get('lsx', false)
		features.set('lsx', c.compiles(inline_asm.format('"vadd.b $vr0, $vr1, $vr1"', name: 'inline asm for Loongson lsx')))
	endif
	if features.get('lsx', false)
		feature = 'runtime_cpu_detect'
		if features.get(feature, true) # soft_enabled
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endif
	if features.get('lasx', false)
		features.set('lasx', c.compiles(inline_asm.format('"xvadd.b $xr0, $xr1, $xr1"', name: 'inline asm for Loongson lasx')))
	endif
	if features.get('lasx', false)
		feature = 'runtime_cpu_detect'
		if features.get(feature, true) # soft_enabled
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endif
elif ['gnu', 'gcc'].contains(tgt_cc)
	features.set('gcc', true)
endif

# Try to enable CPU specific tuning
if tune_cpu != ''
	if tune_cflags != ''
		add_project_arguments(
			c.get_supported_arguments(tune_cflags.format(tune_cpu), checked: 'require'),
			language: 'c'
		)
	else
		warning('CPU tuning not supported by this toolchain')
	endif
endif

# gcov is Meson handled

if features.get('gprof', false)
	gcc_flags = ['-pg']

	add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
	add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')
endif

# optimizations are Meson handled

# pic is Meson handled

# dropping the longjmp interception check because it's been shipped for
# well over a decade now.

# gnu_strip is meson handled via Dstrip

# Try to determine target endianness
features.set('big_endian', target_machine.endian() == 'big')
if c.compiles('static inline int function(void) {}', name: 'supports inline keyword')
	features.set('INLINE', 'inline')
endif

# Almost every platform uses pthreads.
if features.get('multithread', false)
	threads_dep = c.find_library('threads', required: false)
	if c.compiles('''
		#include <pthread.h>
		#include <stddef.h>
		int main(void) { return pthread_create(NULL, NULL, NULL, NULL); }''',
		name: 'supports pthreads',
		dependencies: threads_dep
	)
		extra_libs += threads_dep
	else
		features.set('pthread_h', false)
	endif
endif

# only for MIPS platforms
if tgt_isa.startswith('mips')
	if features.get('big_endian', false)
		if features.get('dspr2', false)
			warning('dspr2 optimizations are available only for little endian platforms')
			features.set('dspr2', false)
		endif
		if features.get('msa', false)
			warning('msa optimizations are available only for little endian platforms')
			features.get('msa', false)
		endif
		if features.get('mmi', false)
			warning('mmi optimizations are available only for little endian platforms')
			features.get('mmi', false)
		endif
	endif
endif

# only for LOONGARCH platforms
if tgt_isa.startswith('loongarch')
	if features.get('big_endian', false)
		if features.get('lsx', false)
			warning('lsx optimizations are available only for little endian platforms')
			features.set('lsx', false)
		endif
		if features.get('lasx', false)
			warning('lasx optimizations are available only for little endian platforms')
			features.get('lasx', false)
		endif
	endif
endif

# glibc needs these
if features.get('linux', false)
	add_project_arguments(
		'-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64',
		language: ['c', 'cpp']
	)
elif tgt_os == 'android'
	api_level = c.get_define('__ANDROID_API__')
	if api_level.version_compare('< 24') and tgt_isa == 'armv7'
		warning('Disabling transparent large-file-support for Android API < 24 on armv7-a')
		add_project_arguments(
			'-U_FILE_OFFSET_BITS',
			language: ['c', 'cpp']
		)
	endif
endif

if features.get('gcc', false)
	gcc_flags = [
		'-Wdeclaration-after-statement',
		'-Wdisabled-optimization',
		'-Wextra-semi',
		'-Wextra-semi-stmt',
		'-Wfloat-conversion',
		'-Wformat=2',
		'-Wparentheses-equality',
		'-Wpointer-arith',
		'-Wtype-limits',
		'-Wcast-qual',
		'-Wvla',
		'-Wimplicit-function-declaration',
		'-Wmissing-declarations',
		'-Wmissing-prototypes',
		'-Wuninitialized',
		'-Wunreachable-code-loop-increment',
		'-Wunused',
	]

	add_project_arguments(c.get_supported_arguments(gcc_flags), language: 'c')
	add_project_arguments(cpp.get_supported_arguments(gcc_flags), language: 'cpp')

	# gtest does not do well with
	# these flags so add them explicitly to CFLAGS only.
	add_project_arguments(c.get_supported_arguments('-Wundef'), language: 'c')
	add_project_arguments(c.get_supported_arguments('-Wframe-larger-than=52000'), language: 'c')

	if (features.get('mips', false) or features.get('INLINE', '') == '') and features.get('extra_warnings', false)
		add_project_arguments(c.get_supported_arguments('-Wno-unused-function'), language: 'c')
		add_project_arguments(cpp.get_supported_arguments('-Wno-unused-function'), language: 'cpp')
	endif

	# Avoid this warning for third_party C++ sources. Some reorganization
	# would be needed to apply this only to test/*.cc.
	add_project_arguments(c.get_supported_arguments('-Wshorten-64-to-32'), language: 'c')

	# Quiet gcc 6 vs 7 abi warnings:
	# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77728
	if features.get('arm', false)
		add_project_arguments(cpp.get_supported_arguments('-Wno-psabi'), language: 'cpp')
	endif

	# Enforce C++11 compatibility.
	add_project_arguments(
		cpp.get_supported_arguments(
			'-Wc++14-extensions',
			'-Wc++17-extensions',
			'-Wc++20-extensions',
		),
		language: 'cpp'
	)
	# disable some warnings specific to libyuv.
	libyuv_cpp_args += cpp.get_supported_arguments(
		'-Wno-missing-declarations',
		'-Wno-missing-prototypes',
		'-Wno-pass-failed',
		'-Wno-unused-parameter',
	)
endif

if features.get('icc', false)
	# Warning levels are governed globally by Meson.
	icc_flags = [
		'-Wpointer-arith',
		# ICC has a number of floating point optimizations that we disable
		# in favor of deterministic output WRT to other compilers
		'-fp-model=precise',
	]

	add_project_arguments(c.get_supported_arguments(icc_flags), language: 'c')
	add_project_arguments(cpp.get_supported_arguments(icc_flags), language: 'cpp')
endif

# Enable extra, harmless warnings. These might provide additional insight
# to what the compiler is doing and why, but in general, but they shouldn't
# be treated as fatal, even if we're treating warnings as errors.
extra_warnings = [
	'-Wdisabled-optimization',
	'-Winline',
	# RVCT is not yet supported by Meson.
	# '--remarks',
]

if features.get('extra_warnings', false)
	add_project_arguments(c.get_supported_arguments(extra_warnings), language: 'c')
	if features.get('gcc', false) and features.get('werror', false)
		foreach w: extra_warnings
			add_project_arguments(c.get_supported_arguments('-Wno-error=@0@'.format(w)), language: 'c')
		endforeach
	endif
endif

if features.get('mips', false)
	features.set('dequant_tokens', true)
	features.set('dc_recon', true)
endif

if features.get('internal_stats', false)
	features.set('vp9_postproc', true)
endif

# "Enable" the postbuild target if building for visual studio.
# The only relevant bits for Meson is the __inline definition.
if tgt_cc == 'msvs'
	if get_option('backend').startswith('vs')
		features.set('solution', true)
	endif
	features.set('INLINE', '__inline')
	add_project_arguments(
		'-D_CRT_SECURE_NO_WARNINGS', '-D_CRT_SECURE_NO_DEPRECATE',
		language: ['c', 'cpp']
	)
endif

# Other toolchain specific defaults
if target_machine.cpu_family().startswith('x86')
	feature = 'postproc'
	if features.get(feature, true)
		if not features.has(feature)
			message('\tenabling @0@'.format(feature))
		endif
		features.set(feature, true)
	endif
endif

if features.get('postproc_visualizer', false) and not features.get('postproc', false)
	error('postproc_visualizer requires postproc to be enabled')
endif

# Enable unit tests by default if we have a working C++ compiler.
if tgt_cc == 'msvs'
	enable_features = ['unit_tests', 'webm_io', 'libyuv']
	foreach feature: enable_features
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
elif tgt_os == 'android'
	enable_features = ['libyuv']
	if cpp.has_argument('-std=gnu++11')
		add_project_arguments('-std=gnu++11', language: 'cpp')
		enable_features += ['webm_io']
	endif
	foreach feature: enable_features
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
	# GTestLog must be modified to use Android logging utilities.
elif tgt_os == 'darwin'
	# Meson already handles the cpp_std flag.
	# iOS/ARM builds do not work with gtest. This does not match
	# x86 targets.
elif target_machine.system() == 'iphonesimulator'
	enable_features = ['libyuv']
	if cpp.has_argument('-std=gnu++11')
		add_project_arguments('-std=gnu++11', language: 'cpp')
		enable_features += ['webm_io']
	endif
	foreach feature: enable_features
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
elif target_machine.system() == 'windows'
	# Some mingw toolchains don't have pthread available by default.
	# Treat these more like visual studio where threading in gtest
	# would be disabled for the same reason.
	enable_features = []
	if cpp.has_argument('-std=gnu++11')
		add_project_arguments('-std=gnu++11', language: 'cpp')
		enable_features += ['unit_tests', 'webm_io']
	endif
	if cpp.compiles('int z;')
		enable_features += ['libyuv']
	endif
	foreach feature: enable_features
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
else
	enable_features = []
	if cpp.has_argument('-std=gnu++11')
		add_project_arguments('-std=gnu++11', language: 'cpp')
		if features.get('pthread_h', false)
			enable_features += ['unit_tests']
		endif
		enable_features += ['webm_io']
	endif
	if cpp.compiles('int z;')
		enable_features += ['libyuv']
	endif
	foreach feature: enable_features
		if features.get(feature, true)
			if not features.has(feature)
				message('\tenabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endforeach
endif

### process_detect ###

# Shared builds are supported everywhere thanks to
# the Meson generation of the module definition files.
# if features.get('shared', false) and not ['linux', 'solaris', 'darwin', 'iphonesimulator'].contains(tgt_os) and not features.get('gnu', false)
# 	# Again, no OS/2 because Meson itself doens't support it
# 	error('Shared library build is only supported on ELF and Darwin for now')
# endif

features.set('unistd_h', c.has_header('unistd.h'))
if c.has_header('vpx/vpx_integer.h', include_directories: include_directories('.'))
	features.set('vpx_vpx_integer_h', true)
	features.set('vpx_ports', true)
endif

if features.get('neon', false)
	c.has_header('arm_neon.h', required: true)
endif

### process_targets ###

cfgdata = configuration_data()

cfgdata.set('INLINE', features.get('INLINE', ''))

foreach arch : ARCH_LIST
	cfgdata.set10('VPX_ARCH_@0@'.format(arch.to_upper()), features.get(arch, false))
endforeach

foreach have : HAVE_LIST
	cfgdata.set10('HAVE_@0@'.format(have.to_upper()), features.get(have, false))
endforeach

foreach feature : CONFIG_LIST
	cfgdata.set10('CONFIG_@0@'.format(feature.to_upper()), features.get(feature, false))
endforeach

foreach var : VAR_LIST
	cfgdata.set10(var.to_upper(), features.get(var, false))
endforeach

version_str = 'v@0@'.format(meson.project_version())
bare_version = meson.project_version().split('.')

git = find_program('git', required: false)
if git.found()
	git_tag = run_command('git', 'describe', '--match=v[0-9]*',
		capture: true,
		check: false,
		env: {
			'GIT_DIR': meson.current_source_dir() / '.git'
		}
	)
	if git_tag.returncode() == 0
		version_str = git_tag.stdout().strip()
		bare_version = version_str.substring(1).split('.')
	endif
endif

python_exe = find_program('python3', version: '>= 3.8', required: true)

major_version = bare_version.get(0, 0)
minor_version = bare_version.get(1, 0)
patch_version = bare_version.get(2, '').split('-').get(0, 0)
extra_version = run_command(
	python_exe,
	'-c',
	'print(\'-\'.join(\'@0@\'.split(\'-\')[1:]))'.format(version_str),
	capture: true,
	check: true
).stdout().strip()

vpx_config_h = configure_file(
	output: 'vpx_config.h',
	configuration: cfgdata,
)

if features.get('win_arm64_neon_h_workaround', false)
	vpx_neon_h = configure_file(
		input: 'meson/arm_neon.h',
		output: 'arm_neon.h',
		copy: true
	)
endif

version_cfgdata = configuration_data()

#since they'll be used as integers below make sure they are or force to 0
version_cfgdata.set('VERSION_MAJOR', major_version)
version_cfgdata.set('VERSION_MINOR', minor_version)
version_cfgdata.set('VERSION_PATCH', patch_version)
version_cfgdata.set_quoted('VERSION_EXTRA', extra_version)
version_cfgdata.set('VERSION_PACKED', '((VERSION_MAJOR<<16)|(VERSION_MINOR<<8)|(VERSION_PATCH))')
version_cfgdata.set_quoted('VERSION_STRING_NOSP', version_str)
version_cfgdata.set_quoted('VERSION_STRING', ' @0@'.format(version_str))

vpx_version_h = configure_file(
	output: 'vpx_version.h',
	configuration: version_cfgdata
)

config_mk_generator = find_program('meson/transform_config.py', required: true)

config_mk = configure_file(
	command: [config_mk_generator, '@OUTPUT@', '@INPUT@'],
	input: [vpx_config_h, vpx_version_h],
	output: 'config.mk',
)

##
## END APPLICATION SPECIFIC CONFIGURATION
##

if meson.version().version_compare('>= 1.1.0')
	configure_args = meson.build_options().strip()
else
	extractor = find_program('meson/capture_build_options.py', required: true)
	configure_args = run_command(extractor, check: true).stdout().strip()
endif

vpx_config_data = configuration_data()
vpx_config_data.set_quoted('CONFIGURE_ARGS', configure_args)

vpx_config_c = configure_file(
	input: 'meson/vpx_config.c',
	output: 'vpx_config.c',
	configuration: vpx_config_data,
)

# libs.mk

rtcd_exe = find_program('build/make/rtcd.pl', required: true)

extra_libs += c.find_library('m', required: false)

codec_srcs = [
	vpx_config_c,
]
codec_doc_srcs = []
codec_doc_sections = []
codec_headers = []
codec_exports = []
codec_rtcds = {}

# What no one told me, and is veery tucked into the Makefiles,
# is that Google's relying on regexp'd per-file architecture flags.
# Best we can do here is simulate them and make libraries that'll be
# link_whole'd into the final binary.
if tgt_cc == 'msvs'
	arch_flags = {
		'mmx': [],
		'sse2': [],
		'sse3': [],
		'ssse3': [],
		'sse4_1': [],
		'avx': c.get_supported_arguments('-march:avx'),
		'avx2': c.get_supported_arguments('-march:avx2'),
		'avx512': c.get_supported_arguments('-march:avx512'),
	}
else
	arch_flags = {
		# x86[_64]
		'mmx': ['-mmmx'],
		'sse2': ['-msse2'],
		'sse3': ['-msse3'],
		'ssse3': ['-mssse3'],
		'sse4_1': ['-msse4.1'],
		'avx': ['-mavx'],
		'avx2': ['-mavx2'],
		'avx512': ['-mavx512f', '-mavx512cd', '-mavx512bw', '-mavx512dq', '-mavx512vl'],

		# POWER
		'vsx' : ['-maltivec', '-mvsx'],

		# MIPS
		'msa': ['-mmsa'],

		# LOONGARCH
		'lsx': ['-mlsx'],
		'lasx': ['-mlasx'],
	}
endif

codec_arch_prereqs = []
codec_arch_srcs = {}
codec_arch_headers = {}
codec_arch_libs = []

#
# Rule to make assembler configuration file from C configuration file
#
config_asm_generator = find_program('meson/transform_config_asm.py', required: true)

if asm_conversion_exe.found()
	# Android expects conversion to output ".asm" to ".asm.S"
	# See e.g. idct_neon.asm
	stdinout_wrapper_exe = find_program('meson/stdinout_wrapper.py', required: true)
	asm_transformer = generator(
		stdinout_wrapper_exe,
		arguments: ['--input', '@INPUT@', '--output', '@OUTPUT@', asm_conversion_exe.full_path()] + asm_conversion_cmd,
		output: '@0@@1@'.format('@BASENAME@', as_sfx)
	)
endif

if features.get('x86', false) or features.get('x86_64', false)
	config_asm = configure_file(
		command: [config_asm_generator, '@INPUT@', '@OUTPUT@', '--format=yasm'],
		input: vpx_config_h,
		output: 'vpx_config.asm',
	)
elif asm_conversion_exe.found()
	ads_config_asm = configure_file(
		command: [config_asm_generator, '@INPUT@', '@OUTPUT@'],
		input: vpx_config_h,
		output: 'vpx_config.adstmp',
	)
	config_asm = configure_file(
		command: [stdinout_wrapper_exe, '--input', '@INPUT@', '--output', '@OUTPUT@', asm_conversion_exe.full_path()] + asm_conversion_cmd,
		input: ads_config_asm,
		output: 'vpx_config.asm',
	)
else
	config_asm = configure_file(
		command: [config_asm_generator, '@INPUT@', '@OUTPUT@'],
		input: vpx_config_h,
		output: 'vpx_config.asm',
	)
endif

rtcd_h_template = [rtcd_exe, '--arch=@0@'.format(tgt_isa), '--config=@INPUT0@'] + rtcd_options

doxy_template = find_program('meson/generate_doxy.py', required: true)

generate_component_dox = find_program('meson/generate_component_dox.py', required: true)

#
# Add assembler dependencies for configuration.
#

codec_srcs += vpx_version_h

subdir('third_party')
subdir('vpx')
subdir('vpx_mem')
subdir('vpx_scale')
subdir('vpx_ports')
subdir('vpx_dsp')
subdir('vpx_util')
subdir('vp8')
subdir('vp9')

foreach symbol, input_file : codec_rtcds
	rtcd_filename = '@0@.h'.format(symbol)
	rtcd_h = configure_file(
		command: rtcd_h_template + ['--sym=@0@'.format(symbol), '@INPUT1@'],
		input: [config_mk, input_file],
		output: rtcd_filename,
		capture: true,
	)

	codec_srcs += rtcd_h
	codec_arch_prereqs += rtcd_h
endforeach

gen_def_exe = find_program('meson/gen_def.py', required: true)

gen_def_cmd = [
	gen_def_exe,
	'--name=vpx',
	'--out=@OUTPUT@'
]

if tgt_os != 'windows' and c.symbols_have_underscore_prefix()
	gen_def_cmd += ['--underscore']
endif

if ['darwin', 'iphonesimulator'].contains(tgt_os)
	vpx_def_name = 'libvpx.syms'
	vpx_def = configure_file(
		command: gen_def_cmd + ['--format=mac', '@INPUT@'],
		input: codec_exports,
		output: vpx_def_name,
	)
	link_args += ['-Wl,-exported_symbols_list,@0@'.format(meson.current_build_dir() / vpx_def_name)]
elif tgt_os == 'windows'
	vpx_def = configure_file(
		command: gen_def_cmd + ['--format=win', '@INPUT@'],
		input: codec_exports,
		output: 'libvpx.def',
	)
else
	vpx_def_name = 'libvpx.ver'
	vpx_def = configure_file(
		command: gen_def_cmd + ['--format=linux', '@INPUT@'],
		input: codec_exports,
		output: vpx_def_name,
	)
	link_args += ['-Wl,--version-script,@0@'.format(meson.current_build_dir() / vpx_def_name)]
endif

soversion = '8.0.0'

foreach arch, srcs : codec_arch_srcs
	codec_arch_libs += static_library(
		'vpx-@0@'.format(arch),
		codec_arch_prereqs + srcs,
		extra_files: codec_arch_headers.get(comp_name, []),
		c_args: arch_flags.get(arch, []),
		dependencies: extra_libs,
	)
endforeach

if features.get('static', false) and features.get('shared', false)
	libvpx = both_libraries(
		'vpx',
		codec_srcs,
		link_args: link_args,
		extra_files: codec_headers,
		dependencies: extra_libs,
		link_whole: codec_arch_libs,
		version: soversion,
		vs_module_defs: vpx_def,
		install: features.get('install_libs'),
	)
else
	libvpx = library(
		'vpx',
		codec_srcs,
		link_args: link_args,
		extra_files: codec_headers,
		dependencies: extra_libs,
		link_whole: codec_arch_libs,
		version: soversion,
		vs_module_defs: vpx_def,
		install: features.get('install_libs'),
	)
endif

libvpx_dep = declare_dependency(
	link_with: libvpx,
	dependencies: extra_libs,
	include_directories: include_directories('.'),
)

meson.override_dependency('vpx', libvpx_dep)

pkg = import('pkgconfig')

pkg.generate(
	libvpx,
	description: 'WebM Project VPx codec implementation',
	version: meson.project_version(),
)

if features.get('examples', false)
	subdir('examples')
endif

if features.get('tools', false)
	subdir('tools')
endif

if features.get('unit_tests', false)
	if features.get('encoders', false)
		rc_rtc_headers = files(
			'vpx/vp8.h',
			'vpx/vp8cx.h',
			'vpx/vpx_ext_ratectrl.h',
			'vpx/internal/vpx_ratectrl_rtc.h',
		)

		rc_rtc_srcs = []

		if features.get('vp9_encoder', false)
			rc_rtc_headers += files(
				'vp9/ratectrl_rtc.h',
			)
			rc_rtc_srcs += files(
				'vp9/ratectrl_rtc.cc',
			)
		endif
		if features.get('vp8_encoder', false)
			rc_rtc_headers += files(
				'vp8/vp8_ratectrl_rtc.h',
			)
			rc_rtc_srcs += files(
				'vp8/vp8_ratectrl_rtc.cc',
			)
		endif
		vpxrc_lib = static_library(
			'vpxrc',
			rc_rtc_srcs,
			extra_files: codec_headers + rc_rtc_headers,
			dependencies: extra_libs + libvpx_dep,
		)
	endif

	if features.get('vp9_encoder', false) and features.get('rate_ctrl', false)
		simple_encode_lib = static_library(
			'simple_encode',
			codec_srcs + files(
				'vp9/simple_encode.cc',
				'ivfenc.c'
			),
			extra_files: codec_headers + files(
				'vp9/simple_encode.h',
				'ivfenc.h',
			),
			dependencies: extra_libs + libvpx_dep,
		)
	endif

	curl_exe = find_program('curl', required: false, disabler: true)
	check_test_data = find_program('meson/check_test_data.py', required: true)
	vpxdec_sh = find_program('test/vpxdec.sh', required: false, disabler: true)
	vpxenc_sh = find_program('test/vpxenc.sh', required: false, disabler: true)
	examples_sh = find_program('test/examples.sh', required: false, disabler: true)

	subdir('test')
endif

if features.get('install_docs', false)
	libs_doxy = configure_file(
		command: [doxy_template, '--sections', codec_doc_sections, '--include', meson.current_source_dir(), '--output', '@OUTPUT@', '@INPUT@'],
		input: codec_doc_srcs,
		output: 'libs.doxy',
	)

	codec_dox = files(
		'mainpage.dox',
		'keywords.dox',
		'usage.dox',
		'usage_cx.dox',
		'usage_dx.dox',
	)

	example_path = [
		meson.current_source_dir(), #for CHANGELOG, README, etc
		meson.current_build_dir() / 'examples',
	]

	generate_doxyfile = find_program('meson/generate_doxyfile.py', required: true)

	doxyfile_prelude = files(
		'libs.doxy_template'
	)

	if features.get('examples', false)
		doxyfile_prelude += examples_doxy
	endif

	if features.get('tools', false)
		doxyfile_prelude += tools_doxy
	endif

	doxyfile_prelude += libs_doxy

	doxyfile = configure_file(
		command: [
			generate_doxyfile,
			'--prelude', doxyfile_prelude,
			'--strip', meson.current_source_dir(), meson.current_build_dir(),
			'--example-path', example_path,
			'--output', '@OUTPUT@',
			'@INPUT@'],
		output: 'Doxyfile',
		input: codec_dox
	)

	docs = custom_target(
		'docs',
		input: doxyfile,
		output: 'html',
		command: [doxygen, doxyfile],
		console: true,
		install: true,
		install_dir: get_option('datadir') / meson.project_name(),
	)
endif
