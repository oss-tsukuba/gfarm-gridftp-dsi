Summary: Gfarm GridFTP DSI
Name: gfarm-gridftp-dsi
Version: 1.0.5
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://oss-tsukuba.org/en/software/gfarm/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gfarm-devel
Requires: gfarm-libs

%description
Gfarm GridFTP DSI is a plugin of GridFTP server for Gfarm file system.

%prep
%setup -q

%build
%configure ${GFARM_GRIDFTP_DSI_CONFIGURE_OPTION}
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
%doc RELNOTES
%doc LICENSE
%{_libdir}/libglobus_gridftp_server_gfarm.a
%{_libdir}/libglobus_gridftp_server_gfarm.la
%{_libdir}/libglobus_gridftp_server_gfarm.so
%{_libdir}/libglobus_gridftp_server_gfarm.so.0
%{_libdir}/libglobus_gridftp_server_gfarm.so.0.0.0

%changelog
* Tue Jun 01 2021 Osamu Tatebe <tatebe@cs.tsukuba.ac.jp> 1.0.5-1
- Initial packaging.
