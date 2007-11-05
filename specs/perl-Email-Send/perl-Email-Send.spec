# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Send

Summary: Send email
Name: perl-Email-Send
Version: 2.190
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Send/

Source: http://www.cpan.org/modules/by-module/Email/Email-Send-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl module for sending mail.

This package contains the following Perl module:

    Email::Send

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Email::Send.3pm*
%doc %{_mandir}/man3/Email::Send::NNTP.3pm*
%doc %{_mandir}/man3/Email::Send::Qmail.3pm*
%doc %{_mandir}/man3/Email::Send::SMTP.3pm*
%doc %{_mandir}/man3/Email::Send::Sendmail.3pm*
%doc %{_mandir}/man3/Email::Send::Test.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Send/
%{perl_vendorlib}/Email/Send.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 2.190-1
- Updated to release 2.190.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.185-1
- Updated to release 2.185.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.183-1
- Initial package.
