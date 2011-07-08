Summary: X.Org X11 libXcursor runtime library
Name: libXcursor
Version: 1.1.10
Release: 2%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Source1: index.theme

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel >= 0.8.2

Obsoletes: XFree86-libs, xorg-x11-libs

%description
X.Org X11 libXcursor runtime library

%package devel
Summary: X.Org X11 libXcursor development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
X.Org X11 libXcursor development package

%prep
%setup -q

# Disable static library creation by default.
%define with_static 0

%build
#export CFLAGS="$RPM_OPT_FLAGS -DICONDIR=\"/usr/share/icons\""
%configure \
%if ! %{with_static}
	--disable-static
%endif
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/share/icons/default
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/icons/default/index.theme

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2
%dir %{_datadir}/icons/default
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/icons/default/index.theme

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%if %{with_static}
%{_libdir}/libXcursor.a
%endif
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
#%dir %{_mandir}/man3x
%{_mandir}/man3/Xcursor*.3*

%changelog
* Mon May 10 2010 Ray Strode <rstrode@redhat.com> 1.1.10-2
- Update default cursor theme to dmz-aa
  Resolves: #559765

* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.1.10-1
- libXcursor 1.1.10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.1.9-5
- Un-require xorg-x11-filesystem
- Remove useless %%dir

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.1.9-3
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.9-2
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.1.9-1
- libXcursor 1.1.9

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.8-3
- Rebuild for PPC toolchain bug

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> 1.1.8-3
- Don't own /usr/share/icons
- Require pkgconfig in -devel

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.1.8-2
- Don't install INSTALL

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.1.8-1
- Update to 1.1.8

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.1.7-1.1
- rebuild

* Wed Jun 07 2006 Mike A. Harris <mharris@redhat.com> 1.1.7-1
- Update to 1.1.7 from X11R7.1

* Wed Jun 07 2006 Mike A. Harris <mharris@redhat.com> 1.1.6-2
- Added "BuildRequires: xorg-x11-proto-devel"
- Added "Requires: xorg-x11-proto-devel" to devel package, needed by xcursor.pc
- Replace "makeinstall" with "make install DESTDIR=..."
- Remove package ownership of mandir/libdir/etc.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.1.6-1
- Update to 1.1.6

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.1.5.2-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.1.5.2-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.1.5.2-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.1.5.2-1
- Updated libXcursor to version 1.1.5.2 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 1.1.5.1-1
- Updated libXcursor to version 1.1.5.1 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.
- Added default index.theme file to set BlueCurve as the default cursor theme
  to fix bug (#175532).

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 1.1.5-1
- Updated libXcursor to version 1.1.5 from X11R7 RC2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 1.1.4-1
- Updated libXcursor to version 1.1.4 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 1.1.3-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 1.1.3-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 1.1.3-1
- Initial build.
