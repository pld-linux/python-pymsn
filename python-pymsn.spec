Summary:	Python module for the MSN protocol
Summary(pl.UTF-8):	Moduł Pythona do protokołu MSN
Name:		python-pymsn
Version:	0.2.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://telepathy.freedesktop.org/releases/pymsn/pymsn-%{version}.tar.gz
# Source0-md5:	db54e7181ed226e0f047e83677aa706d
URL:		http://telepathy.freedesktop.org/wiki/Pymsn
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-pygobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the MSN protocol.

%description -l pl.UTF-8
Moduł Pythona do protokołu MSN.

%prep
%setup -q -n pymsn-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%dir %{py_sitescriptdir}/pymsn
%{py_sitescriptdir}/pymsn/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gio
%{py_sitescriptdir}/pymsn/gio/*.py[co]
%{py_sitescriptdir}/pymsn-*.egg-info
