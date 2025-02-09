%define pkg_name        XML-SimpleObject-LibXML
%define pkg_version     0.60

Summary:       Simple object representation of an XML::LibXML DOM object
Name:          perl-%{pkg_name}
Version:       %perl_convert_version %{pkg_version}
Release:       5
Group:         Development/Perl
License:       Artistic
URL:           https://search.cpan.org/dist/%{pkg_name}/
Source0:       http://www.cpan.org/authors/id/D/DB/DBRIAN/%{pkg_name}-%{pkg_version}.tar.gz
BuildArch:     noarch
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
sed -i 's%/usr/local%/usr%g' Makefile
%make_build OPTMIZE="%{optflags}"

%install
%make_install

%clean

%files
%doc Changes README
%{_datadir}/perl*/XML/SimpleObject/LibXML.pm
%{_datadir}/perl*/XML/SimpleObject/ex.pl
%{_mandir}/man3/*.3pm*



%changelog
* Tue Aug 02 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.60-1mdv2012.0
+ Revision: 692919
- bump new version spec file import from fedora
- Created package structure for perl-XML-SimpleObject-LibXML.

