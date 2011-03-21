#
Summary:	Modules for c-icap ICAP server
Name:		c-icap-modules
Version:	0.1.3
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/c-icap/c_icap_modules-%{version}.tar.gz
# Source0-md5:	e1ced11a487495d621c2db3a11a5262f
Patch0:		%{name}-build.patch
URL:		http://c-icap.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules for c-icap ICAP server

%package -n c-icap-srv_clamav
Summary:	ClamAV service for c-icap
Group:		Development/Libraries
Requires:	c-icap

%description -n c-icap-srv_clamav
ClamAV service for c-icap.

%description -n c-icap-srv_clamav -l pl.UTF-8
ClamAV service for c-icap.

%package -n c-icap-srv_url_check
Summary:	URL check service for c-icap
Group:		Development/Libraries
Requires:	c-icap

%description -n c-icap-srv_url_check
URL check service for c-icap.

%description -n c-icap-srv_url_check -l pl.UTF-8
URL check service for c-icap.

%prep
%setup -q -n c_icap_modules-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-c-icap=
%{__automake}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/c-icap
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -n c-icap-srv_clamav
%defattr(644,root,root,755)
%{_sysconfdir}/c-icap/srv_clamav.conf
%attr(755,root,root) %{_libdir}/c_icap/srv_clamav.so

%files -n c-icap-srv_url_check
%defattr(644,root,root,755)
%{_sysconfdir}/c-icap/srv_url_check.conf
%attr(755,root,root) %{_libdir}/c_icap/srv_url_check.so
