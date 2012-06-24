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
Summary(es):	M�dulo de Perl Net::SMTP::Multipart
Summary(fr):	Module Perl Net::SMTP::Multipart
Summary(it):	Modulo di Perl Net::SMTP::Multipart
Summary(ja):	Net::SMTP::Multipart Perl �⥸�塼��
Summary(ko):	Net::SMTP::Multipart �� ����
Summary(nb):	Perlmodul Net::SMTP::Multipart
Summary(pl):	Modu� perla Net::SMTP::Multipart
Summary(pt_BR):	M�dulo Perl Net::SMTP::Multipart
Summary(pt):	M�dulo de Perl Net::SMTP::Multipart
Summary(ru):	������ ��� Perl Net::SMTP::Multipart
Summary(sv):	Net::SMTP::Multipart Perlmodul
Summary(uk):	������ ��� Perl Net::SMTP::Multipart
Summary(zh_CN):	Net::SMTP::Multipart Perl ģ��
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
Ten modu� u�ywa Net::SMTP i Mime::Base64 do komponowania i wysy�ania
wielocz�ciowych wiadomo�ci e-mail. U�ywa metod Net::SMTP, ale
upraszcza komponowanie wielocz�ciowych wiadomo�ci przez udost�pnianie
swoich wewn�trznych metod: Header, Text, FileAttach i End.

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
