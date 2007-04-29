# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Mbox-MessageParser

Summary: Fast and simple mbox folder reader
Name: perl-Mail-Mbox-MessageParser
Version: 1.5000
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Mbox-MessageParser/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Mbox-MessageParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(FileHandle::Unget)
Requires: perl

%description
Mail::Mbox::MessageParser is a fast and simple mbox folder reader.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
echo | %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
echo | %makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST README
%{_mandir}/man3/*
%{perl_vendorlib}/Mail/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.5000-1
- Updated to release 1.5000.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.4005-1
Updated to release 1.4005.

* Tue May 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.4003-1
- Updated to release 1.4003.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4002-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.4002-1
- Updated to release 1.4002.

* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.4001-1
- Updated to release 1.4001.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 1.2130-1
- Initial package. (using DAR)
