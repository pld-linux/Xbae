Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Summary(pl):	XbaeMatrix jest motifowym widgetem wy∂wietlaj±cym tabelki
Name:		Xbae
Version:	4.9.1
Release:	1
License:	BSD-like (Bell Communications Research)
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
Patch0:		%{name}-link.patch
BuildRequires:	lesstif-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	man2html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description

The XbaeMatrix is a Motif-based widget which displays a grid of cells
in the same manner as a spreadsheet. The cell array is scrollable,
editable, and otherwise reasonably configurable in appearance. Each
cell usually displays text, but pixmaps can also be displayed (not
editable). The XbaeMatrix looks to some extent like a grid of
XmTextField widgets, but is actually implemented with a single
XmTextField. This means a big performance improvement due to less
overhead.

%description -l pl
XbaeMatrix jest motifowym widgetem wy∂wietlaj±cym tabelki z≥oøone z
pÛl w sposÛb podobny do arkuszy kalkulacyjnych. TabelÍ moøna przewijaÊ
i poddawaÊ edycji. Kaøde pole zazwyczaj wy∂wietla tekst, ale moøe
takøe bitmapÍ (bez moøliwo∂ci edycji).

%package devel
Summary:	XbaeMatrix header files and development documentation
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja XbaeMatrix
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
XbaeMatrix header files and development documentation.

%description devel -l pl
Pliki nag≥Ûwkowe i dokumentacja programisty do XbaeMatrix.

%package static
Summary:	XbaeMatrix static library
Summary(pl):	Biblioteki statyczne XbaeMatrix
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
XbaeMatrix static library.

%description static -l pl
Biblioteki statyczne XbaeMatrix.

%prep
%setup -q
%patch0 -p1

%build
libtoolize -c -f
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-static \
	--with-editres

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog README FAQ.html NEWS doc/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXbae.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,FAQ.html,NEWS}.gz doc/*.html.gz doc/images/*.png
%attr(755,root,root) %{_libdir}/libXbae.so
%attr(755,root,root) %{_libdir}/libXbae.la
%{_includedir}/Xbae
%{_aclocaldir}/ac_find_xbae.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXbae.a
