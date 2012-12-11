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
* Tue Aug 02 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.60-1mdv2012.0
+ Revision: 692919
- bump new version spec file import from fedora
- Created package structure for perl-XML-SimpleObject-LibXML.

