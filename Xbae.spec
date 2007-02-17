%define		_truename xbae
Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Summary(pl.UTF-8):	XbaeMatrix jest motifowym widgetem wyświetlającym tabelki
Name:		Xbae
Version:	4.60.4
Release:	1
License:	BSD-like (Bell Communications Research)
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/xbae/%{_truename}-%{version}.tar.gz
# Source0-md5:	9690059474bb05191dccd041ff5052bd
URL:		http://xbae.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	motif-devel >= 2.0
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

%description -l pl.UTF-8
XbaeMatrix jest motifowym widgetem wyświetlającym tabelki złożone z
pól w sposób podobny do arkuszy kalkulacyjnych. Tabelę można przewijać
i poddawać edycji. Każde pole zazwyczaj wyświetla tekst, ale może
także bitmapę (bez możliwości edycji).

%package devel
Summary:	XbaeMatrix header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja XbaeMatrix
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	motif-devel >= 2.0

%description devel
XbaeMatrix header files and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do XbaeMatrix.

%package static
Summary:	XbaeMatrix static library
Summary(pl.UTF-8):	Biblioteki statyczne XbaeMatrix
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XbaeMatrix static library.

%description static -l pl.UTF-8
Biblioteki statyczne XbaeMatrix.

%prep
%setup -q -n %{_truename}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	--with-editres

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

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libXbae.so.*.*
%{_datadir}/Xbae

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libXbae.so
%{_includedir}/Xbae
%{_aclocaldir}/ac_find_xbae.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXbae.a
