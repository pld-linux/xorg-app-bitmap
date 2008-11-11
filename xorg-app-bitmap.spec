Summary:	bitmap applications - bitmap editor and converter utilities
Summary(pl.UTF-8):	Aplikacje bitmap - narzędzia do modyfikowania i konwersji bitmap
Name:		xorg-app-bitmap
Version:	1.0.3
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bitmap-%{version}.tar.bz2
# Source0-md5:	98200c358e5401d648b980564d9ae39d
Patch0:		%{name}-xaw.patch
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
The bitmap program is a rudimentary tool for creating or editing
rectangular images made up of 1's and 0's. Bitmaps are used in X for
defining clipping regions, cursor shapes, icon shapes, and tile and
stipple patterns.

The bmtoa and atobm filters convert bitmap files to and from ASCII
strings. They are most commonly used to quickly print out bitmaps and
to generate versions for including in text.

%description -l pl.UTF-8
Program bitmap to podstawowe narzędzie do tworzenia i modyfikowania
prostokątnych obrazów złożonych z jedynek i zer. Bitmapy są używane
przez X do definiowania obszarów przycinania, kształtów kursorów,
kształtów ikon oraz wzorów kafli i punktowania.

Filtry bmtoa i atobm przekształcają pliki bitmap do i z łańcuchów
ASCII. Są najczęściej używane do szybkiego wypisywania bitmap i
generowania wersji do włączenia w tekst.

%prep
%setup -q -n bitmap-%{version}
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%{_datadir}/X11/app-defaults/Bitmap*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/atobm.1x*
%{_mandir}/man1/bitmap.1x*
%{_mandir}/man1/bmtoa.1x*
