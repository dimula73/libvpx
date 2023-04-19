# Building libvpx with Meson

This libvpx port requires Meson 0.64 or higher because it supports Nasm out of
the box.

Get Meson, either from your distro's package manager, or using pip:

```
python3 -m pip install meson --user
```

Get ninja, either from your distro's package manager, or using pip:

```
python3 -m pip install ninja-build --user
```

You will also need:

- Perl (for Windows users, Strawberry Perl suffices)
- Nasm >= 2.09 OR Yasm

**WARNING**: Mac OS X users with very old SDKs, please don't use the bundled Yasm.
It will be rejected out of the box.

Optional dependencies:

- cURL
- Doxygen 1.5.5.3 or higher

Then in the root folder (where this file resides):

```
meson setup build && meson compile -C build
```

I've tested that it builds and links with the following operating systems:

- macOS Big Sur 11.7.4 x86_64 (Xcode 13.2.1)
- Windows 10 21H2 x86_64
  - MSVC 17.6.0 Preview 2
  - Clang 16.0.1 (MSYS CLANG64)

# Running the tests:

The tests are **not** available by default because they require multi-gigabyte 
artifact that are downloaded at build time from Google's CDN. I believe they 
are intended to be run from inside Google's own CI infrastructure.

If cURL is not available, they will be silently skipped.

WARNING: some tests require `-Ddefault_library=static` to be available.

To run them, issue:

```
meson setup build -Ddefault_library=static -Dtests=true
meson test -C build
```

# Updating the libvpx base snapshot of the Meson port

The procedure is based on GStreamer's work on FFmpeg, which is available here:

https://gitlab.freedesktop.org/gstreamer/meson-ports/ffmpeg/-/blob/meson-4.4/README.meson

It should only be needed when updating from one feature version to another,
not for minor bug fix releases (assuming there aren't too many changes in
`configure` between minor bug fix releases).

The procedure is generally to (all scripts are in the `meson` folder):

- apply the `patch-configure.diff` patch to make all toggle options available
- in a Bash shell, run `./configure --help` and save the output to `tmp_meson_options.txt` **in the root folder**
- run the scripts `capture_build_options.py` and `parse_sources.py`
- make sure to bring back in the manual changes (that's the tedious part).

Both .py scripts work in place, you will need to check the diff and
revert some of the changes.

## The Python scripts

- `parse_sources.py` updates the meson.build files trying to keep the parsed
  source files within the `#### --- [END] GENERATED --- ####` specifiers

- `capture_build_options.py` updates the meson_options.txt file trying to keep
  the automatically parsed options within the
  `#### --- [END] GENERATED OPTIONS --- ####` specifiers

Then bump versions and check what changed in `configure` since the last time,
which is the other complicated bit, as it requires understanding of the
somewhat complex ffmpeg-based build system and of the way it was reimplemented
for the Meson port. I've made sure to keep it 1:1 as much as possible, while 
using some Meson-isms to accelerate things. You'll find most of the logic is 
based off `libs.mk`, `examples.mk`, `configure` and `build/make/configure.sh`.
The source files and functions for the different parts are added with comments.

Good luck!
