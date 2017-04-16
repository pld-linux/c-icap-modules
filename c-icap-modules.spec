Summary:	Modules for c-icap ICAP server
Name:		c-icap-modules
Version:	0.4.5
Release:	1
License:	BSD
Group:		Libraries
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/c-icap/c_icap_modules-%{version}.tar.gz
# Source0-md5:	1a7eaa7a34ff35c2440cf303f7b45f22
Patch0:		%{name}-build.patch
URL:		http://c-icap.sourceforge.net/
BuildRequires:	bzip2-devel
BuildRequires:	c-icap-devel
BuildRequires:	clamav-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules for c-icap ICAP server

%package -n c-icap-srv_clamav
Summary:	ClamAV service for c-icap
Group:		Development/Libraries
Group:		Networking/Daemons
Requires:	c-icap

%description -n c-icap-srv_clamav
ClamAV service for c-icap.

%package -n c-icap-srv_url_check
Summary:	URL check service for c-icap
Group:		Development/Libraries
Group:		Networking/Daemons
Requires:	c-icap

%description -n c-icap-srv_url_check
URL check service for c-icap.

%package -n c-icap-srv_content_filtering
Summary:	Content filtering service for c-icap
Group:		Libraries
Group:		Networking/Daemons
Requires:	c-icap

%description -n c-icap-srv_content_filtering
Content filtering service for c-icap.

%prep
%setup -q -n c_icap_modules-%{version}
%patch0 -p1

%build
%{__autoconf}
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

%files -n c-icap-srv_clamav
%defattr(644,root,root,755)
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

%files -n c-icap-srv_url_check
%defattr(644,root,root,755)
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/srv_url_check.conf
%{_sysconfdir}/c-icap/srv_url_check.conf.default
%attr(755,root,root) %{_libdir}/c_icap/srv_url_check.so
%{_datadir}/c_icap/templates/srv_url_check
%{_bindir}/c-icap-mods-sguardDB
%{_mandir}/man8/c-icap-mods-sguardDB.8*

%files -n c-icap-srv_content_filtering
%defattr(644,root,root,755)
%attr(640,root,c-icap) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/srv_content_filtering.conf
%{_sysconfdir}/c-icap/srv_content_filtering.conf.default
%attr(755,root,root) %{_libdir}/c_icap/srv_content_filtering.so
%{_datadir}/c_icap/templates/srv_content_filtering
