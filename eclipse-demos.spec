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

