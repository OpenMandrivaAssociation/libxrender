%define libname %mklibname xrender 1
%define develname %mklibname xrender -d
%define staticname %mklibname xrender -s -d

Name: libxrender
Summary:  X Render Library
Version: 0.9.6
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2
# (fc) disable Xrender on DMX (Mdk bug #19925)
Patch0: libXrender-0.9.1-dmx.patch
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Render Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Render Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Render Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 1.0.0
Requires: libx11-devel >= 1.0.0
Provides: libxrender-devel = %{version}-%{release}
Provides: libxrender1-devel = %{version}-%{release}
Obsoletes: %{mklibname xrender 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXrender.so
%{_libdir}/libXrender.la
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%{_docdir}/libXrender/*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxrender-static-devel = %{version}-%{release}
Provides: libxrender1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xrender 1 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXrender.a

#-----------------------------------------------------------

%prep
%setup -q -n libXrender-%{version}
%patch0 -p1 -b .dmx

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0


