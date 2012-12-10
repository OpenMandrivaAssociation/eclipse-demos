Name:           eclipse-demos
Version:        0.0.1
Release:        %mkrel 0.2.3
Summary:        Eclipse demonstration screencasts

Group:          Development/Java
License:        Open Publication
URL:            http://sources.redhat.com/eclipse
Source0:        http://overholt.fedorapeople.org/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
Screencasts demonstrating various features of Eclipse.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}
cp -p * $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}-%{version}
%doc %{_datadir}/%{name}-%{version}/openpub.html
%{_datadir}/%{name}-%{version}/*.ogg



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-0.2.3mdv2011.0
+ Revision: 617996
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-0.2.2mdv2010.0
+ Revision: 428503
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0.1-0.2.1mdv2009.0
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 18 2007 David Walluck <walluck@mandriva.org> 0.0.1-0.2.1mdv2008.1
+ Revision: 100030
- import eclipse-demos


* Tue Sep 25 2007 Andrew Overholt <overholt@redhat.com> 0.0.1-2
- Drop totem requirement (one can use any number of players).
- Fix license to be "Open Publication".

* Mon Sep 24 2007 Andrew Overholt <overholt@redhat.com> 0.0.1-1
- Initial release.
