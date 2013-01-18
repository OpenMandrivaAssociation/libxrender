%define major 1
%define libname %mklibname xrender %{major}
%define develname %mklibname xrender -d

Name:		libxrender
Summary:	X Render Library
Version:	0.9.7
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.bz2
# (fc) disable Xrender on DMX (Mdk bug #19925)
Patch0:		libXrender-0.9.7-dmx.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X Render Library.

%package -n %{libname}
Summary:	X Render Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{EVRD}

%description -n %{libname}
X Render Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	libxrender-devel = %{EVRD}
Obsoletes:	%{_lib}xrender1-devel < 0.9.7
Obsoletes:	%{_lib}xrender-static-devel < 0.9.7
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXrender.so.%{major}*

%files -n %{develname}
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%{_includedir}/X11/extensions/Xrender.h
%dir %{_docdir}/libXrender
%{_docdir}/libXrender/*



%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.7-1
+ Revision: 783973
- version update 0.9.7

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.6-5
+ Revision: 783374
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.6-4
+ Revision: 745662
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-3
+ Revision: 662427
- mass rebuild

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.6-2
+ Revision: 638564
- added missing switch for static pkg
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.9.6-1mdv2011.0
+ Revision: 556455
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.9.5-2mdv2010.1
+ Revision: 464042
- Ship the docs too

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 0.9.5-1mdv2010.1
+ Revision: 463644
- fix build
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.4-5mdv2010.0
+ Revision: 425935
- rebuild

* Fri Nov 07 2008 Olivier Blin <blino@mandriva.org> 0.9.4-4mdv2009.1
+ Revision: 300390
- rebuild for new xcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.4-3mdv2009.0
+ Revision: 223084
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.9.4-2mdv2008.1
+ Revision: 151687
- Update BuildRequires and rebuild.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Thierry Vignaud <tv@mandriva.org> 0.9.4-1mdv2008.1
+ Revision: 96067
- new release

* Mon Aug 20 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.9.3-1mdv2008.0
+ Revision: 68019
- new upstream release: 0.9.3

