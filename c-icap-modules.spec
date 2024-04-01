#
# Conditional build:
%bcond_without	clamav		# clamav / virusfilter module
#
%ifarch x32
%undefine	with_clamav
%endif
Summary:	Modules for c-icap ICAP server
Summary(pl.UTF-8):	Moduły dla serwera ICAP c-icap
Name:		c-icap-modules
Version:	0.5.7
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	https://downloads.sourceforge.net/c-icap/c_icap_modules-%{version}.tar.gz
# Source0-md5:	08c4721a26840bb0ff95fcaa64b686c3
Patch0:		%{name}-build.patch
Patch1:		clamav0.101.patch
URL:		https://c-icap.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	c-icap-devel >= 0.5
%{?with_clamav:BuildRequires:	clamav-devel >= 0.90}
BuildRequires:	db-devel >= 4.2
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules for c-icap ICAP server.

%description -l pl.UTF-8
Moduły dla serwera ICAP c-icap.

%package -n c-icap-srv_clamav
Summary:	ClamAV service for c-icap
Summary(pl.UTF-8):	Usługa ClamAV dla c-icap
Group:		Networking/Daemons
Requires:	c-icap >= 0.5

%description -n c-icap-srv_clamav
ClamAV service for c-icap.

%description -n c-icap-srv_clamav -l pl.UTF-8
Usługa ClamAV dla c-icap.

%package -n c-icap-srv_url_check
Summary:	URL check service for c-icap
Summary(pl.UTF-8):	Usługa sprawdzania URL-i dla c-icap
Group:		Networking/Daemons
Requires:	c-icap >= 0.5

%description -n c-icap-srv_url_check
URL check service for c-icap.

%description -n c-icap-srv_url_check -l pl.UTF-8
Usługa sprawdzania URL-i dla c-icap.

%package -n c-icap-srv_content_filtering
Summary:	Content filtering service for c-icap
Summary(pl.UTF-8):	Usługa filtrowania treści dla c-icap
Group:		Networking/Daemons
Requires:	c-icap >= 0.5

%description -n c-icap-srv_content_filtering
Content filtering service for c-icap.

%description -n c-icap-srv_content_filtering -l pl.UTF-8
Usługa filtrowania treści dla c-icap.

%prep
%setup -q -n c_icap_modules-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
export CFLAGS="%{rpmcflags} -I/usr/include/clamav"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/c-icap
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Not installed by upstream
cp -a services/content_filtering/srv_content_filtering.conf.default \
	$RPM_BUILD_ROOT%{_sysconfdir}/c-icap/srv_content_filtering.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/c_icap/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with clamav}
%files -n c-icap-srv_clamav
%defattr(644,root,root,755)
%doc README SPONSORS
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/clamav_mod.conf
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/clamd_mod.conf
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/virus_scan.conf
%{_sysconfdir}/c-icap/clamav_mod.conf.default
%{_sysconfdir}/c-icap/clamd_mod.conf.default
%{_sysconfdir}/c-icap/virus_scan.conf.default
%attr(755,root,root) %{_libdir}/c_icap/clamav_mod.so
%attr(755,root,root) %{_libdir}/c_icap/clamd_mod.so
%attr(755,root,root) %{_libdir}/c_icap/virus_scan.so
%{_datadir}/c_icap/templates/virus_scan
%endif

%files -n c-icap-srv_url_check
%defattr(644,root,root,755)
%doc README SPONSORS
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/srv_url_check.conf
%{_sysconfdir}/c-icap/srv_url_check.conf.default
%attr(755,root,root) %{_libdir}/c_icap/srv_url_check.so
%{_datadir}/c_icap/templates/srv_url_check
%{_bindir}/c-icap-mods-sguardDB
%{_mandir}/man8/c-icap-mods-sguardDB.8*

%files -n c-icap-srv_content_filtering
%defattr(644,root,root,755)
%doc README SPONSORS
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/srv_content_filtering.conf
%{_sysconfdir}/c-icap/srv_content_filtering.conf.default
%attr(755,root,root) %{_libdir}/c_icap/srv_content_filtering.so
%{_datadir}/c_icap/templates/srv_content_filtering
