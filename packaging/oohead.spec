Name:           oohead
Version:        0.2.0
Release:        1%{?dist}
Summary:        Zero-copy prefix line and byte extractor with early pipe closure semantics.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oohead
Source0:        oohead-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oohead is a sovereign, capability-bounded PREFIX SLICER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oohead
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oohead-uninstall

%files
/usr/bin/oohead
/usr/bin/oohead-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
