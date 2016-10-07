%define major 1
%define libname %mklibname xrender %{major}
%define devname %mklibname xrender -d

Summary:	X Render Library
Name:		libxrender
Version:	0.9.10
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2
# (fc) disable Xrender on DMX (Mdk bug #19925)
Patch0:		libXrender-0.9.7-dmx.patch

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
%setup -qn libXrender-%{version}
%apply_patches

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXrender.so.%{major}*

%files -n %{devname}
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%{_docdir}/libXrender/*

