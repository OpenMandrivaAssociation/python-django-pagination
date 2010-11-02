%define realname django-pagination

Name:           python-django-pagination
Version:        1.0.5
Release:        %mkrel 4
Summary:        Django pagination tools

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-pagination/
Source0:        http://django-pagination.googlecode.com/files/%{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
A set of utilities for creating robust pagination tools throughout a Django
application.

%prep
%setup -q -n %{realname}-%{version}
find -name '._*' -exec rm {} \;

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS.txt LICENSE.txt docs/
%{py_puresitedir}/*
