%define libxrender %mklibname xrender 1
Name: libxrender
Summary:  X Render Library
Version: 0.9.4
Release: %mkrel 4
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

%package -n %{libxrender}
Summary:  X Render Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxrender}
X Render Library

#-----------------------------------------------------------

%package -n %{libxrender}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxrender} = %{version}
Requires: x11-proto-devel >= 1.0.0
Requires: libx11-devel >= 1.0.0
Provides: libxrender-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxrender}-devel
Development files for %{name}

%pre -n %{libxrender}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxrender}-devel
%defattr(-,root,root)
%{_libdir}/libXrender.so
%{_libdir}/libXrender.la
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h

#-----------------------------------------------------------

%package -n %{libxrender}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxrender}-devel = %{version}
Provides: libxrender-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxrender}-static-devel
Static development files for %{name}

%files -n %{libxrender}-static-devel
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
%post -n %{libxrender} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libxrender} -p /sbin/ldconfig
%endif

%files -n %{libxrender}
%defattr(-,root,root)
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0


