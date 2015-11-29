# TODO
# - fork of this exists as python-papyon.spec
Summary:	Python module for the MSN protocol
Summary(pl.UTF-8):	Moduł Pythona do protokołu MSN
Name:		python-pymsn
Version:	0.3.3
Release:	7
License:	GPL
Group:		Libraries/Python
Source0:	http://telepathy.freedesktop.org/releases/pymsn/pymsn-%{version}.tar.gz
# Source0-md5:	dbdb6f92569bae784084f0c3a146eb5b
URL:		http://telepathy.freedesktop.org/wiki/Pymsn
BuildRequires:	python >= 1:2.5
BuildRequires:	python-Crypto
BuildRequires:	python-devel
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-pygobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-Crypto
Requires:	python-pyOpenSSL
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
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%dir %{py_sitescriptdir}/pymsn
%{py_sitescriptdir}/pymsn/*.py[co]
%dir %{py_sitescriptdir}/pymsn/event
%{py_sitescriptdir}/pymsn/event/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gnet
%{py_sitescriptdir}/pymsn/gnet/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gnet/io
%{py_sitescriptdir}/pymsn/gnet/io/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gnet/message
%{py_sitescriptdir}/pymsn/gnet/message/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gnet/protocol
%{py_sitescriptdir}/pymsn/gnet/protocol/*.py[co]
%dir %{py_sitescriptdir}/pymsn/gnet/proxy
%{py_sitescriptdir}/pymsn/gnet/proxy/*.py[co]
%dir %{py_sitescriptdir}/pymsn/msnp
%{py_sitescriptdir}/pymsn/msnp/*.py[co]
%dir %{py_sitescriptdir}/pymsn/msnp2p
%{py_sitescriptdir}/pymsn/msnp2p/*.py[co]
%dir %{py_sitescriptdir}/pymsn/msnp2p/transport
%{py_sitescriptdir}/pymsn/msnp2p/transport/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service
%{py_sitescriptdir}/pymsn/service/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/AddressBook
%{py_sitescriptdir}/pymsn/service/AddressBook/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/AddressBook/scenario
%{py_sitescriptdir}/pymsn/service/AddressBook/scenario/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/AddressBook/scenario/contacts
%{py_sitescriptdir}/pymsn/service/AddressBook/scenario/contacts/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/AddressBook/scenario/groups
%{py_sitescriptdir}/pymsn/service/AddressBook/scenario/groups/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/AddressBook/scenario/sync
%{py_sitescriptdir}/pymsn/service/AddressBook/scenario/sync/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/ContentRoaming
%{py_sitescriptdir}/pymsn/service/ContentRoaming/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/ContentRoaming/scenario
%{py_sitescriptdir}/pymsn/service/ContentRoaming/scenario/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/OfflineIM
%{py_sitescriptdir}/pymsn/service/OfflineIM/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/OfflineIM/scenario
%{py_sitescriptdir}/pymsn/service/OfflineIM/scenario/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/Spaces
%{py_sitescriptdir}/pymsn/service/Spaces/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/Spaces/scenario
%{py_sitescriptdir}/pymsn/service/Spaces/scenario/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description
%{py_sitescriptdir}/pymsn/service/description/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/AB
%{py_sitescriptdir}/pymsn/service/description/AB/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/OIM
%{py_sitescriptdir}/pymsn/service/description/OIM/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/RSI
%{py_sitescriptdir}/pymsn/service/description/RSI/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/SchematizedStore
%{py_sitescriptdir}/pymsn/service/description/SchematizedStore/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/Sharing
%{py_sitescriptdir}/pymsn/service/description/Sharing/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/SingleSignOn
%{py_sitescriptdir}/pymsn/service/description/SingleSignOn/*.py[co]
%dir %{py_sitescriptdir}/pymsn/service/description/Spaces
%{py_sitescriptdir}/pymsn/service/description/Spaces/*.py[co]
%dir %{py_sitescriptdir}/pymsn/util
%{py_sitescriptdir}/pymsn/util/*.py[co]
%dir %{py_sitescriptdir}/pymsn/util/iso8601
%{py_sitescriptdir}/pymsn/util/iso8601/*.py[co]
%{py_sitescriptdir}/pymsn-*.egg-info
