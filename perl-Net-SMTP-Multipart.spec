#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP-Multipart
Summary:	Net::SMTP::Multpiart perl module
Summary(cs):	Modul Net::SMTP::Multipart pro Perl
Summary(da):	Perlmodul Net::SMTP::Multipart
Summary(de):	Net::SMTP::Multipart Perl Modul
Summary(es):	Módulo de Perl Net::SMTP::Multipart
Summary(fr):	Module Perl Net::SMTP::Multipart
Summary(it):	Modulo di Perl Net::SMTP::Multipart
Summary(ja):	Net::SMTP::Multipart Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::SMTP::Multipart ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Net::SMTP::Multipart
Summary(pl):	Modu³ perla Net::SMTP::Multipart
Summary(pt_BR):	Módulo Perl Net::SMTP::Multipart
Summary(pt):	Módulo de Perl Net::SMTP::Multipart
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::SMTP::Multipart
Summary(sv):	Net::SMTP::Multipart Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::SMTP::Multipart
Summary(zh_CN):	Net::SMTP::Multipart Perl Ä£¿é
Name:		perl-Net-SMTP-Multipart
Version:	1.5
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ba9a4a9c2d96a0fff6de587b6d72bce
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses the Net::SMTP and Mime::Base64 modules to compose and
send multipart mail messages. It uses the Net::SMTP methods, but
simplifies formatting of multipart messages using its internal methods
Header, Text, FileAttach and End.

%description -l pl
Ten modu³ u¿ywa Net::SMTP i Mime::Base64 do komponowania i wysy³ania
wieloczê¶ciowych wiadomo¶ci e-mail. U¿ywa metod Net::SMTP, ale
upraszcza komponowanie wieloczê¶ciowych wiadomo¶ci przez udostêpnianie
swoich wewnêtrznych metod: Header, Text, FileAttach i End.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Net/SMTP/Multipart.pm
%{_mandir}/man3/*
