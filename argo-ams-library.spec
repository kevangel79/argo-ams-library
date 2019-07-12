%global underscore() %(echo %1 | sed 's/-/_/g')

Name:           argo-ams-library
Summary:        A simple python library for interacting with the ARGO Messaging Service
Version:        0.4.2
Release:        1%{?dist}

Group:          Development/Libraries
License:        ASL 2.0  
URL:            https://github.com/ARGOeu/argo-ams-library
Source0:        %{name}-%{version}.tar.gz 

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch 

%if 0%{?el6}
BuildRequires:  python2-devel python34-devel
Requires:       python2-requests python34-requests
%endif

%if 0%{?el7}
BuildRequires:  python-devel python36-devel
Requires:       python-requests python36-requests
%endif

%description
A simple python library for interacting with the ARGO Messaging Service

%if 0%{?el6}
%package -n python2-%{name}
Summary:        A simple python library for interacting with the ARGO Messaging Service
%description -n python2-%{name}
A simple python library for interacting with the ARGO Messaging Service

%{?python_provide:%python_provide python2-%{name}}

%package -n python34-%{name}
Summary:        A simple python library for interacting with the ARGO Messaging Service
%description -n python34-%{name}
A simple python library for interacting with the ARGO Messaging Service

%{?python_provide:%python_provide python3-%{name}}
%endif

%if 0%{?el7}
%package -n python-%{name}
Summary:        A simple python library for interacting with the ARGO Messaging Service
%description -n python-%{name}
A simple python library for interacting with the ARGO Messaging Service

%{?python_provide:%python_provide python-%{name}}

%package -n python36-%{name}
Summary:        A simple python library for interacting with the ARGO Messaging Service
%description -n python36-%{name}
A simple python library for interacting with the ARGO Messaging Service

%{?python_provide:%python_provide python3-%{name}}
%endif

%prep
%setup -q

%build
%{py_build}
%{py3_build}

%install
rm -rf $RPM_BUILD_ROOT
%{py_install "--record=INSTALLED_FILES" } 
%{py3_install "--record=INSTALLED_FILES" } 

%if 0%{?el7}
%files -n python36-argo-ams-library -f INSTALLED_FILES
%doc examples/ README.md
%defattr(-,root,root,-)
%dir %{python3_sitelib}/%{underscore %{name}}
%{python3_sitelib}/%{underscore %{name}}/*.py[co]

%files -n python-argo-ams-library -f INSTALLED_FILES
%doc examples/ README.md
%defattr(-,root,root,-)
%dir %{python_sitelib}/%{underscore %{name}}
%{python_sitelib}/%{underscore %{name}}/*.py[co]
%endif

%if 0%{?el6}
%files -n python34-argo-ams-library -f INSTALLED_FILES
%doc examples/ README.md
%defattr(-,root,root,-)
%{python3_sitelib}/*

%files -n python2-argo-ams-library -f INSTALLED_FILES
%doc examples/ README.md
%defattr(-,root,root,-)
%{python_sitelib}/*
%endif

%changelog
* Tue Jun 19 2018 Daniel Vrcic <dvrcic@srce.hr>, Konstantinos Kagkelidis <kaggis@gmail.com>, agelostsal <agelos.tsal@gmail.com> - 0.4.1-1%{?dist}
- ARGO-1120 Extend AMS client to support X509 method via the authentication server
* Mon May 14 2018 Daniel Vrcic <dvrcic@srce.hr>, Konstantinos Kagkelidis <kaggis@gmail.com>, agelostsal <agelos.tsal@gmail.com> - 0.4.0-1%{?dist}
- ARGO-1103 Handle non-JSON AMS responses
- ARGO-1105 Extend ams library to support offset manipulation
- ARGO-1118 Fix returnImmediately parameter in sub pull request
- ARGO-1127 Wrap offsets low level methods into one
- ARGO-1153 Extract JSON error messages propagated through AMS
* Mon Jun 5 2017 Daniel Vrcic <dvrcic@srce.hr> - 0.2.0-1%{?dist}
- ARGO-782 Iterate over subscriptions and topics methods
- ARGO-789 Topic and subscription creation/deletion that mimic Google implementation
- ARGO-791 Methods for settings acls on topics and subscriptions
- ARGO-804 Has topic/sub methods should have ability to pass kwargs to python-requests library
- ARGO-812 Mimicked topic and subcription methods will always return corresponding objects
- ARGO-814 Publish method accepts directly list of AmsMessage objects
* Fri Mar 17 2017 Daniel Vrcic <dvrcic@srce.hr>, Themis Zamani <themiszamani@gmail.com>, Konstantinos Kagkelidis <kaggis@gmail.com> - 0.1.1-1%{?dist}
- ARGO-760 Has topic and subscription methods
- ARGO-770 AMS Library tests
* Thu Mar 2 2017 Daniel Vrcic <dvrcic@srce.hr> - 0.1.0-2%{?dist}
- ARGO-710 Provide examples of simple publishing and consuming
* Fri Feb 24 2017 Daniel Vrcic <dvrcic@srce.hr> - 0.1.0-1%{?dist}
- first version 
