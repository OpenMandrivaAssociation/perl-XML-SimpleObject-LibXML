%define upstream_version 0.60
%define pkg_name        XML-SimpleObject-LibXML
%define pkg_version     0.60

Summary:       Simple object representation of an XML::LibXML DOM object
Name:          perl-%{pkg_name}
Version:	0.60
Release:	1
Group:         Development/Perl
License:       Artistic
URL:           https://metacpan.org/dist/XML-SimpleObject-LibXML
Source0:	https://cpan.metacpan.org/authors/id/D/DB/DBRIAN/XML-SimpleObject-LibXML-0.60.tar.gz
BuildArch:     noarch
BuildRequires:	make
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



