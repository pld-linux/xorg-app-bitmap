Summary:	bitmap application
Summary(pl):	Aplikacja bitmap
Name:		xorg-app-bitmap
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bitmap-%{version}.tar.bz2
# Source0-md5:	78e8ab5c1830e2cdfbff7a952162a5a7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
# for dirs (only???)
Requires:	xorg-data-xbitmaps
Requires:	xorg-lib-libXt >= 1.0.0
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/X11/app-defaults/*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/*.1x*
