Summary:       MyApp Summary
Name:          myapp
Version:       %{_ver}
Release:       1
BuildArch:     noarch
Group:         SomeGroup
Vendor:        MyCorp
License:       MyLicenses
Source:        %{name}-%{version}.tar.gz
Source1:	   chkconfig.conf
AutoReqProv:   no

BuildRequires: java-1.6.0-openjdk-devel, boxuk-leiningen

%define _prefix /path/to/install

%description
A description of the application

%prep
%setup

%build
lein -v
lein bin

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{name}/bin
cp target/%{name} $RPM_BUILD_ROOT%{_prefix}/%{name}/bin/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
cp %{_sourcedir}/chkconfig.conf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}

chmod 755 $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}

%post
if [ "$1" = "1" ]; then
	chkconfig --add %{name}
fi
exit 0

%files
%defattr(-,root,root,-)
%attr(0755, root, root) /etc/init.d/%{name}
%attr(0744, root, root) %{_prefix}/%{name}/bin/%{name}

%pretrans
if [ -f %{_prefix}/%{name}/bin/%{name} ]; then
	service %{name} stop
	chkconfig %{name} off
fi

%posttrans
service %{name} start
chkconfig %{name} on
 
