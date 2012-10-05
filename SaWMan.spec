Summary:	Shared application and Window Manager
Summary(pl.UTF-8):	Zarządca współdzielonych aplikacji i okien
Name:		SaWMan
Version:	1.6.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}.tar.gz
# Source0-md5:	aeb87cd87a4241f9d4d55a6a363c4b4a
URL:		http://www.directfb.org/index.php?path=Platform/SaWMan
BuildRequires:	DirectFB-devel >= 1:1.6.0
BuildRequires:	pkgconfig >= 1:0.9
Requires:	DirectFB >= 1:1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfblibdir	%{_libdir}/directfb-1.6-0

%description
SaWMan is a new window manager module for use with DirectFB. Its main
difference to the default module is that it allows one process to be
an application and window manager, implementing all kinds of
diversity, while SaWMan is only the working horse.

%description -l pl.UTF-8
SaWMan to nowy moduł zarządcy okien dla DirectFB. Główną różnicą w
stosunku do domyślnego modułu jest to, że pozwala jednemu procesowi
być aplikacją i zarządcą okien, implementując wszystkie urozmaicenia,
podczas gdy SaWMan jest tylko silnikiem.

%package devel
Summary:	Header files for sawman library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sawman
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:1.6.0

%description devel
Header files for sawman library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sawman.

%package static
Summary:	Static sawman library
Summary(pl.UTF-8):	Statyczna biblioteka sawman
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sawman library.

%description static -l pl.UTF-8
Statyczna biblioteka sawman.

%prep
%setup -q

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/swmdump
%attr(755,root,root) %{_libdir}/libsawman-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsawman-1.6.so.0
%attr(755,root,root) %{dfblibdir}/wm/libdirectfbwm_sawman.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsawman.so
%{_libdir}/libsawman.la
%{_includedir}/sawman
%{_pkgconfigdir}/sawman.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsawman.a
%{dfblibdir}/wm/libdirectfbwm_sawman.[aol]*
