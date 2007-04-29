# $Id$

# Authority: dries
# Upstream: Anthony Peacock <a,peacock$chime,ucl,ac,uk>

%define real_name HTML-Table
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Produces HTML tables
Name: perl-HTML-Table
Version: 2.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Table/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Table-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
HTML::Table is used to generate HTML tables for
CGI scripts.  By using the methods provided fairly
complex tables can be created, manipulated, then printed
from Perl scripts.  The module also greatly simplifies
creating tables within tables from Perl.  It is possible
to create an entire table using the methods provided and
never use an HTML tag.

HTML::Table also allows for creating dynamically sized
tables via its addRow and addCol methods.  These methods
automatically resize the table if passed more cell values
than will fit in the current table grid.

Methods are provided for nearly all valid table, row, and
cell tags specified for HTML 3.0.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/Table.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
