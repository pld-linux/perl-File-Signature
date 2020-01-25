#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	Signature
Summary:	File::Signature - Detect changes to a file's content or attributes
Summary(pl.UTF-8):	File::Signature - wykrywa zmiany zawartości plików albo ich atrybutów
Name:		perl-File-Signature
Version:	1.009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JE/JEREMY/File-Signature-%{version}.tar.gz
# Source0-md5:	ef5baa7b8fcf50b8c3136810ca6aa964
URL:		http://search.cpan.org/dist/File-Signature/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way to monitor files for changes. It implements
an object oriented interface to file "signatures." In the case of this
module, a signature includes an MD5 digest (other digests may be added
later), the file's size, its inode number, its mode, its owner's uid,
its group's gid, and its mtime. This information is associated with a
file by the file's "pathname." The pathname is considered to be the
file's unique identifier. In reality, a file may have more than one
pathname, but this module doesn't recognize that. It will simply treat
two differing pathnames as two different files, even if they refer to
the same file.

As this module checks whether a file changes over time, a minimal use
of it would include the time when the signature was created and a
different time when the signature is regenerated and compared with the
previous one. The amount of time between these checks is arbitrary.
This module makes it easy to save a signature object and then load it
and check for consistency at a later time, whether seconds or years
have passed.

%description -l pl.UTF-8
Moduł ten wykrywa zmiany zawartości plików albo ich atrybutów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
