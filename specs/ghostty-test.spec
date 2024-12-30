###
# Inspiration taken from https://gitlab.com/pgill/ghostty-rpm
###
%global debug_package %{nil}
%global tmp_dir /tmp/offline-cache

Name:    ghostty
Version: 1.0.0
Release: 1%{?dist}
Summary: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

License: MIT
URL: https://github.com/ghostty-org/ghostty
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch: x86_64

# https://ghostty.org/docs/install/build#dependencies
BuildRequires: zig >= 0.13
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel

BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib2-devel
BuildRequires: harfbuzz-devel
BuildRequires: libpng-devel
BuildRequires: oniguruma-devel
BuildRequires: pandoc-cli
BuildRequires: pixman-devel
BuildRequires: pkg-config
BuildRequires: zlib-ng-devel

Requires: fontconfig
Requires: freetype
Requires: glib2
Requires: gtk4
Requires: harfbuzz
Requires: libadwaita
Requires: libpng
Requires: oniguruma
Requires: pixman
Requires: zlib-ng



%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p %{tmp_dir}
mkdir -p %{ghostty_tmp_dir}
ZIG_GLOBAL_CACHE_DIR=%{tmp_dir} ./nix/build-support/fetch-zig-cache.sh
zig build \
    --summary all \
    --prefix "%{buildroot}%{_prefix}" \
    --system "%{tmp_dir}/p" \
    -Doptimize=ReleaseFast \
    -Dcpu=baseline \
    -Dpie=true \
    -Demit-docs


%files
%license LICENSE
%{_bindir}/ghostty
%{_prefix}/share/applications/com.mitchellh.ghostty.desktop
%{_prefix}/share/bash-completion/completions/ghostty.bash
%{_prefix}/share/bat/syntaxes/ghostty.sublime-syntax
%{_prefix}/share/fish/vendor_completions.d/ghostty.fish
%{_prefix}/share/ghostty
%{_prefix}/share/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_prefix}/share/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_prefix}/share/man/man1/ghostty.1
%{_prefix}/share/man/man5/ghostty.5
%{_prefix}/share/nvim/site/ftdetect/ghostty.vim
%{_prefix}/share/nvim/site/ftplugin/ghostty.vim
%{_prefix}/share/nvim/site/syntax/ghostty.vim
%{_prefix}/share/terminfo/g/ghostty
%{_prefix}/share/terminfo/ghostty.termcap
%{_prefix}/share/terminfo/ghostty.terminfo
%{_prefix}/share/terminfo/x/xterm-ghostty
%{_prefix}/share/vim/vimfiles/ftdetect/ghostty.vim
%{_prefix}/share/vim/vimfiles/ftplugin/ghostty.vim
%{_prefix}/share/vim/vimfiles/syntax/ghostty.vim
%{_prefix}/share/zsh/site-functions/_ghostty

%changelog
%autochangelog
