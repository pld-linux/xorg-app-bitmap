Summary:	bitmap application
Summary(pl):	Aplikacja bitmap
Name:		xorg-app-bitmap
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/app/bitmap-%{version}.tar.bz2
# Source0-md5:	8ac9c282836577abd085a6e8b75b3a30
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
# for dirs (only???)
Requires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bitmap application.

%description -l pl
Aplikacja bitmap.

%prep
%setup -q -n bitmap-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/*.1x*
