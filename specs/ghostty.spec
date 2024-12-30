Name:    ghostty
Version: 1.0.0
Release: %autorelease
Summary: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

License: MIT
URL: https://github.com/ghostty-org/ghostty
# https://github.com/ghostty-org/ghostty/blob/main/PACKAGING.md
Source0: https://release.files.ghostty.org/%{version}/ghostty-source.tar.gz
Source1: https://release.files.ghostty.org/%{version}/ghostty-source.tar.gz.minisig

# Dependencies
BuildRequires: zig >= 0.13
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: minisign
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_desktop_files
BuildRequires: desktop-file-utils

%description
Ghostty is a terminal emulator that differentiates itself by being fast, feature-rich, and native.
While there are many excellent terminal emulators available, they all force you to choose between speed,
features, or native UIs. Ghostty provides all three.

%prep
# Verify signature before extracting
cat > ghostty.pub << EOF
untrusted comment: Ghostty minisign public key
RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
EOF

minisign -Vm %{SOURCE0} -p ghostty.pub -x %{SOURCE1}

%autosetup -n ghostty-source

# Fetch Zig dependencies during prep
export ZIG_GLOBAL_CACHE_DIR=%{_builddir}/zig-cache
./nix/build-support/fetch-zig-cache.sh

%build
DESTDIR=/tmp/ghostty \
zig build \
  --prefix /usr \
  --system %{_builddir}/zig-cache/p \
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

