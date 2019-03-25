%define major 1
%define libname %mklibname xrender %{major}
%define devname %mklibname xrender -d

%global optflags %{optflags} -O3

Summary:	X Render Library
Name:		libxrender
Version:	0.9.10
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Render Library.

%package -n %{libname}
Summary:	X Render Library
Group:		Development/X11
Provides:	%{name} = %{EVRD}

%description -n %{libname}
X Render Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxrender-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXrender-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libXrender.so.%{major}*

%files -n %{devname}
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%{_docdir}/libXrender/*

