# $Id$
# Authority: matthias

Summary: Real Time software audio/video Encoder library
Name: rte
Version: 0.5.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sourceforge.net/
Source: http://dl.sf.net/zapping/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: doxygen

%description
The RTE library is a frontend or wrapper of other libraries or programs
for real time video and audio compression on Linux. Currently it works
on x86 CPUs only, sorry. The library is designed to interface between
codecs and the Zapping TV viewer: http://zapping.sourceforge.net,
precisely its recording plugin.


%package devel
Summary: Real Time software audio/video Encoder library development files
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The RTE library is a frontend or wrapper of other libraries or programs
for real time video and audio compression on Linux. Currently it works
on x86 CPUs only, sorry. The library is designed to interface between
codecs and the Zapping TV viewer: http://zapping.sourceforge.net,
precisely its recording plugin.

This package contains the include file, static library and documentation
needed to develop programs that will use RTE.


%prep
%setup


%build
# In 0.5.2, configure has an exit status of 1...
%configure || :
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/*
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 0.5.2-1
- Update to 0.5.2.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.5.1-4
- Rebuild for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.5.1-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Feb 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1.
- Split the -devel package.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Fri Oct  4 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Updated.

* Tue Jun 18 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Requires gettext 0.11.2, amended doc list

* Tue Aug 8 2001 I�aki Garc�a Etxebarria <garetxe@users.sourceforge.net>
- Created

