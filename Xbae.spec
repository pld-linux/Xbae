Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Summary(pl):	XbaeMatrix jest motifowym widgetem wy¶wietlaj±cym tabelki
Name:		Xbae
Version:	4.50.95
Release:	1
License:	BSD-like (Bell Communications Research)
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/xbae/%{name}-%{version}.tar.gz
# Source0-md5:	1b4a0666dc9b574b3be5675110906699
Patch0:		%{name}-link.patch
URL:		http://xbae.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	motif-devel >= 2.0
BuildRequires:	%{_aclocaldir}/ac_find_motif.m4
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}
Requires:	motif-devel >= 2.0

%description devel
XbaeMatrix header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do XbaeMatrix.

%package static
Summary:	XbaeMatrix static library
Summary(pl):	Biblioteki statyczne XbaeMatrix
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XbaeMatrix static library.

%description static -l pl
Biblioteki statyczne XbaeMatrix.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

rm -f doc/Makefile* doc/images/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libXbae.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libXbae.so
%{_libdir}/libXbae.la
%{_includedir}/Xbae
%{_aclocaldir}/ac_find_xbae.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXbae.a
