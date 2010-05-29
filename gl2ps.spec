Summary:	GL2PS - an OpenGL to PostScript printing library
Summary(pl.UTF-8):	GL2PS - biblioteka drukowania z OpenGL-a do PostScriptu
Name:		gl2ps
Version:	1.3.5
Release:	2
License:	LGPL v2+ or GP2PS License v2+ (see COPYING.GL2PS)
Group:		Libraries
Source0:	http://www.geuz.org/gl2ps/src/%{name}-%{version}.tgz
# Source0-md5:	22e51ff57ecd35cb1cc22497a178a017
URL:		http://www.geuz.org/gl2ps/
BuildRequires:	OpenGL-devel
BuildRequires:	cmake
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GL2PS is a C library providing high quality vector output for any
OpenGL application. The main difference between GL2PS and other
similar libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more...

GL2PS can currently create PostScript (PS), Encapsulated PostScript
(EPS) and Portable Document Format (PDF) files, as well as LaTeX files
for the text fragments. Adding new vector output formats should be
relatively easy (and amongst the formats we would be interested in
adding, SVG is first in line). Meanwhile, you can use the excellent
pstoedit program to transform the PostScript files generated by GL2PS
into many other vector formats such as xfig, cgm, wmf, etc.

%description -l pl.UTF-8
GL2PS to biblioteka C zapewniająca wysokiej jakości wyjście wektorowe
dla dowolnej aplikacji OpenGL. Główna różnica między GL2PS a innymi
podobnymi bibliotekami polega na użyciu algorytmów sortujących
potrafiących obsłużyć przecinające się i rozciągnięte wielokąty, a
także obiekty nie będące rozmaitościami. GL2PS zapewnia zaawansowane
gładkie cieniowanie i renderowanie tekstu, usuwanie niewidocznych
prymitywów, mieszane wyjście wektorowo-bitmapowe i wiele więcej.

GL2PS aktualnie potrafi tworzyć pliki PostScript (PS), Encapsulated
PostScript (EPS) oraz Portable Document Format (PDF), a także pliki
LaTeXa dla fragmentów tekstowych. Dodanie nowych wyjściowych formatów
wektorowych powinno być względnie łatwe (a spośród formatów, których
dodanie zainteresowani byliby autorzy, pierwszym jest SVG). Tymczasem
można używać świetnego programu pstoedit do przekształcania plików
PostScript generowanych przez GL2PS na wiele innych formatów
wektorowych, takich jak xfig, cgm, wmf itp.

%package devel
Summary:	Header files for GL2PS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GL2PS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel

%description devel
Header files for GL2PS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GL2PS.

%package static
Summary:	Static GL2PS library
Summary(pl.UTF-8):	Statyczna biblioteka GL2PS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GL2PS library.

%description static -l pl.UTF-8
Statyczna biblioteka GL2PS.

%prep
%setup -q -n %{name}-%{version}-source

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
%{__cmake} . \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_prefix}/lib/libgl2ps.so,%{_libdir}/libgl2ps.so.0.0.0}
ln -s libgl2ps.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libgl2ps.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING.GL2PS README.txt TODO.txt
%attr(755,root,root) %{_libdir}/libgl2ps.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc gl2ps.pdf
%attr(755,root,root) %{_libdir}/libgl2ps.so
%{_includedir}/gl2ps.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgl2ps.a
