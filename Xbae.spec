Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Summary(pl):	XbaeMatrix jest motifowym widgetem wy¶wietlaj±cym tabelki
Name:		Xbae
Version:	4.9.1
Release:	2
License:	BSD-like (Bell Communications Research)
Group:		X11/Libraries
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
Patch0:		%{name}-link.patch
BuildRequires:	lesstif-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
XbaeMatrix jest motifowym widgetem wy¶wietlaj±cym tabelki z³o¿one z
pól w sposób podobny do arkuszy kalkulacyjnych. Tabelê mo¿na przewijaæ
i poddawaæ edycji. Ka¿de pole zazwyczaj wy¶wietla tekst, ale mo¿e
tak¿e bitmapê (bez mo¿liwo¶ci edycji).

%package devel
Summary:	XbaeMatrix header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja XbaeMatrix
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
XbaeMatrix header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do XbaeMatrix.

%package static
Summary:	XbaeMatrix static library
Summary(pl):	Biblioteki statyczne XbaeMatrix
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
XbaeMatrix static library.

%description static -l pl
Biblioteki statyczne XbaeMatrix.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-static \
	--with-editres \
	--with-x-includes=/usr/X11R6/include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

rm -f doc/Makefile* doc/images/Makefile*

gzip -9nf AUTHORS ChangeLog README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,NEWS}.gz
%attr(755,root,root) %{_libdir}/libXbae.so.*.*

%files devel
%defattr(644,root,root,755)
%doc FAQ.html doc/*
%attr(755,root,root) %{_libdir}/libXbae.so
%attr(755,root,root) %{_libdir}/libXbae.la
%{_includedir}/Xbae
%{_aclocaldir}/ac_find_xbae.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXbae.a
