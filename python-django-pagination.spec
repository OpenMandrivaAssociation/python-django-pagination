%define realname django-pagination

Name:           python-django-pagination
Version:        1.0.7
Release:        %mkrel 1
Summary:        Django pagination tools

Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/django-pagination
Source0:        http://pypi.python.org/packages/source/d/django-pagination/%{realname}-%{version}.tar.gz
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


%changelog
* Fri Nov 12 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 596501
- Update to 1.0.7
- Change the url to http://pypi.python.org/pypi/django-pagination , it's more up-to-date

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.5-5mdv2011.0
+ Revision: 592469
- really rebuild to get correct auto requries

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.5-4mdv2011.0
+ Revision: 592336
- rebuild to get correct auto requries

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.5-3mdv2011.0
+ Revision: 592245
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2010.0
+ Revision: 442096
- rebuild

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 349664
- import python-django-pagination


