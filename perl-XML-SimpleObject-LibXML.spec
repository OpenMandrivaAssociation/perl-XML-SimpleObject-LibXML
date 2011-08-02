%define pkg_name        XML-SimpleObject-LibXML
%define pkg_version     0.60
%define rpm_pkg_version 0.60

Summary:       Simple object representation of an XML::LibXML DOM object
Name:          perl-%{pkg_name}
Version:       %{rpm_pkg_version}
Release:       %mkrel 1
Group:         Development/Perl
License:       Artistic
URL:           http://search.cpan.org/dist/%{pkg_name}/
Source0:       http://www.cpan.org/authors/id/D/DB/DBRIAN/%{pkg_name}-%{pkg_version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl-devel

%description
This is a short and simple class allowing simple object access to a parsed
XML::LibXML tree, with methods for fetching children and attributes in as
clean a manner as possible.

%prep
%setup -q -n %{pkg_name}-%{pkg_version}

%build
perl Makefile.PL
%make OPTMIZE="%{optflags}"

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_sitelib}/XML/SimpleObject/*.pm
%{perl_sitelib}/XML/SimpleObject/*.pl
/usr/local/share/man/man3/*.3pm

%changelog
* Tue May 22 2007 Marius Feraru <altblue@n0i.net> - 0.60-2.n0i.2
- spec file (re)created using N0i::CPAN::RPMizer v1.14.7

* Tue Apr 18 2006 Marius Feraru <altblue@n0i.net> 0.60-1.n0i.1
- spec file (re)created using N0i::CPAN::RPMizer v1.12.1
- rebuild on perl 5.8.8
