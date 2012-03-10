%define major 1
%define libname %mklibname xrender %{major}
%define develname %mklibname xrender -d

Name: libxrender
Summary:  X Render Library
Version: 0.9.7
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2
# (fc) disable Xrender on DMX (Mdk bug #19925)
Patch0: libXrender-0.9.7-dmx.patch

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Render Library

%package -n %{libname}
Summary:  X Render Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Render Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxrender-devel = %{version}-%{release}
Obsoletes: %{_lib}xrender1-devel
Obsoletes: %{_lib}xrender-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXrender-%{version}
%patch0 -p1 -b .dmx

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXrender.so.%{major}*

%files -n %{develname}
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%{_docdir}/libXrender/*

