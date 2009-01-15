Summary: DBD-Oracle module for perl
Name: perl-DBD-Oracle
Version: 1.22
Release: 5.git.7fc0379cc4c831588d075d19586b14b8777f36a2%{?dist}
License:  GPL+ or Artistic
Group: Development/Libraries
Source0: %{name}-%{version}.tar.gz
Url: http://www.cpan.org
BuildRoot: %{_tmppath}/perl-DBD-Oracle-buildroot/
BuildRequires: perl >= 0:5.6.1, perl(DBI)
BuildRequires: oracle-instantclient-devel
Requires: perl >= 0:5.6.1

%description
DBD-Oracle module for perl

%package explain
Summary: Oora_explain script from DBD-Oracle module for perl
Group: Development/Libraries

%description explain
ora_explain script

%prep
%define modname %(echo %{name}| sed 's/perl-//')
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%setup -q -n %{modname}-%{version} 

%build

MKFILE=$(rpm -ql oracle-instantclient-devel | grep demo.mk)
ORACLE_HOME=$(rpm -ql oracle-instantclient-basic | \
    awk '/libclntsh.so/ { gsub("/lib/libclntsh.so.*", ""); print ;}')
export ORACLE_HOME
perl Makefile.PL -m $MKFILE INSTALLDIRS="vendor" PREFIX=%{_prefix}
make  %{?_smp_mflags} OPTIMIZE="%{optflags}"

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} pure_install

rm -f `find $RPM_BUILD_ROOT -type f -name perllocal.pod -o -name .packlist`

%files
%defattr(-,root,root)
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/Oraperl.pm
%{perl_vendorarch}/oraperl.ph
%{_mandir}/man3/*

%files explain
%defattr(-,root,root)
%{_bindir}/ora_explain
%{_mandir}/man1/ora_explain.1.gz

%changelog
* Wed Dec 10 2008 Michael Mraka <michael.mraka@redhat.com> 1.22-5
- simplified %%build and %%instal stage
- resolved #470999

* Tue Nov 25 2008 Miroslav Suchy <msuchy@redhat.com> 1.22-2
- added buildrequires for oracle-lib-compat
- rebased to DBD::Oracle 1.22
- removed DBD-Oracle-1.14-blobsyn.patch

* Thu Oct 16 2008 Milan Zazrivec 1.21-4
- bumped release for minor release tagging
- added %%{?dist} to release

* Tue Aug 26 2008 Mike McCune 1.21-3
- Cleanup spec file to work in fedora and our new Makefile structure

* Wed Jul  2 2008 Michael Mraka <michael.mraka@redhat.com> 1.21-2
- rebased to DBD::Oracle 1.21, Oracle Instantclient 10.2.0.4
- ora_explain moved into subpackage

* Wed May 21 2008 Jan Pazdziora - 1.19-8
- rebuild on RHEL 4 as well.

* Fri Dec 05 2007 Michael Mraka <michael.mraka@redhat.com>
- update to DBD::Oracle 1.19 to support oracle-instantclient

* Fri Jun 20 2003 Mihai Ibanescu <misa@redhat.com>
- Linking against Oracle 9i Release 2 client libraries. 

* Sun Nov 11 2001 Chip Turner <cturner@redhat.com>
- update to DBD::Oracle 1.12 to fix LOB bug

* Mon Jul 23 2001 Cristian Gafton <gafton@redhat.com>
- compile against oracle libraries using -rpath setting
- disable as many checks as we can from the default Makefile.PL

* Mon Apr 30 2001 Chip Turner <cturner@redhat.com>
- Spec file was autogenerated. 
