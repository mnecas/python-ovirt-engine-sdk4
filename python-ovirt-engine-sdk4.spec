Name: python-ovirt-engine-sdk4
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.4.18
Release: 0.1.master.20210722105223%{?release_suffix}%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://ovirt.org
Source: ovirt-engine-sdk-python-4.4.18_master.tar.gz

BuildRequires: gcc
BuildRequires: libxml2-devel
Requires: libxml2

%description
This package contains the Python SDK for version 4 of the oVirt Engine
API.

%package -n python3-ovirt-engine-sdk4
Summary: oVirt Engine Software Development Kit (Python)
BuildRequires: python3-devel
Requires: libxml2
Requires: python3
Requires: python3-pycurl >= 7.43.0-6
Requires: python3-six

%description -n python3-ovirt-engine-sdk4
This package contains the Python 3 SDK for version 4 of the oVirt Engine
API.

%setup -q -n ovirt-engine-sdk-python-4.4.18_master


%build
%py3_build


%install
%py3_install


%files -n python3-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%{python3_sitearch}/*

%changelog
* Thu Jul 2 2020 Martin Perina <mperina@redhat.com> - 4.4.4-1
- Update to model 4.4.17
- Improve examples code around image transfer features

* Thu Jun 06 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.1-1
- 4.3.1
- Adhere to Fedora packaging guidelines naming schema

* Wed Jun 14 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0
