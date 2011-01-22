Summary:	Python blip.pl API
Name:		python-blipapi
Version:	0.02.04
Release:	2
License:	GPL v2 or LGPL
Group:		Libraries/Python
Source0:	http://blipapi.googlecode.com/files/BlipApiPY-%{version}.tar.bz2
# Source0-md5:	38892df4239376e51300e5455a319664
URL:		http://code.google.com/p/blipapi/
%pyrequires_eq	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python blip.pl API.

%prep
%setup -q -n blipapi

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/blipapi*
%{py_sitescriptdir}/*.egg-info
