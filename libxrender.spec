# libxrender is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xrender %{major}
%define devname %mklibname xrender -d

%if %{with compat32}
%define lib32name libxrender%{major}
%define dev32name libxrender-devel
%endif

%global optflags %{optflags} -O3

Summary:	X Render Library
Name:		libxrender
Version:	0.9.11
Release:	2
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
X Render Library.

%package -n %{libname}
Summary:	X Render Library
Group:		Development/X11

%description -n %{libname}
X Render Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Render Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X Render Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXrender-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure \
%if %{cross_compiling}
	--disable-malloc0returnsnull
%endif

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXrender.so.%{major}*

%files -n %{devname}
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%doc %{_docdir}/libXrender/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXrender.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXrender.so
%{_prefix}/lib/pkgconfig/xrender.pc
%endif
