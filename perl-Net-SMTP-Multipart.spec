#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP-Multipart
Summary:	Net::SMTP::Multpiart perl module
Summary(cs.UTF-8):	Modul Net::SMTP::Multipart pro Perl
Summary(da.UTF-8):	Perlmodul Net::SMTP::Multipart
Summary(de.UTF-8):	Net::SMTP::Multipart Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::SMTP::Multipart
Summary(fr.UTF-8):	Module Perl Net::SMTP::Multipart
Summary(it.UTF-8):	Modulo di Perl Net::SMTP::Multipart
Summary(ja.UTF-8):	Net::SMTP::Multipart Perl モジュール
Summary(ko.UTF-8):	Net::SMTP::Multipart 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::SMTP::Multipart
Summary(pl.UTF-8):	Moduł perla Net::SMTP::Multipart
Summary(pt_BR.UTF-8):	Módulo Perl Net::SMTP::Multipart
Summary(pt.UTF-8):	Módulo de Perl Net::SMTP::Multipart
Summary(ru.UTF-8):	Модуль для Perl Net::SMTP::Multipart
Summary(sv.UTF-8):	Net::SMTP::Multipart Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::SMTP::Multipart
Summary(zh_CN.UTF-8):	Net::SMTP::Multipart Perl 模块
Name:		perl-Net-SMTP-Multipart
Version:	1.5
Release:	3
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

%description -l pl.UTF-8
Ten moduł używa Net::SMTP i Mime::Base64 do komponowania i wysyłania
wieloczęściowych wiadomości e-mail. Używa metod Net::SMTP, ale
upraszcza komponowanie wieloczęściowych wiadomości przez udostępnianie
swoich wewnętrznych metod: Header, Text, FileAttach i End.

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
