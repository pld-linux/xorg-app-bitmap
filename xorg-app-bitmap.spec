Summary:	bitmap applications - bitmap (XBM) editor and converter utilities
Summary(pl.UTF-8):	Aplikacje bitmap - narzędzia do modyfikowania i konwersji bitmap (XBM)
Name:		xorg-app-bitmap
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/bitmap-%{version}.tar.xz
# Source0-md5:	bc35592aa62bb3bc5fc78dd717be503f
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
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

# support __appmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__appmansuffix__/,.so man1/,' man/*.man

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%{_datadir}/X11/app-defaults/Bitmap*
%{_includedir}/X11/bitmaps/Dashes
%{_includedir}/X11/bitmaps/Down
%{_includedir}/X11/bitmaps/Excl
%{_includedir}/X11/bitmaps/FlipHoriz
%{_includedir}/X11/bitmaps/FlipVert
%{_includedir}/X11/bitmaps/Fold
%{_includedir}/X11/bitmaps/Left
%{_includedir}/X11/bitmaps/Right
%{_includedir}/X11/bitmaps/RotateLeft
%{_includedir}/X11/bitmaps/RotateRight
%{_includedir}/X11/bitmaps/Stipple
%{_includedir}/X11/bitmaps/Term
%{_includedir}/X11/bitmaps/Up
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
