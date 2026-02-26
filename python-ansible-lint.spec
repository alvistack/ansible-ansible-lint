# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ansible-lint
Epoch: 100
Version: 26.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Best practices checker for Ansible
License: GPL-3.0-or-later
URL: https://github.com/ansible/ansible-lint/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Checks playbooks for practices and behavior that could potentially be
improved.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%package -n ansible-lint
Summary: Best practices checker for Ansible
Requires: ansible-core >= 2.16.14
Requires: black >= 24.3.0
Requires: python3
Requires: python3-ansible-compat >= 25.8.0
Requires: python3-cffi >= 1.15.1
Requires: python3-cryptography >= 38
Requires: python3-distro >= 1.9.0
Requires: python3-filelock >= 3.8.2
Requires: python3-jsonschema >= 4.10.0
Requires: python3-packaging >= 22.0
Requires: python3-pathspec >= 0.10.3
Requires: python3-pyyaml >= 6.0.1
Requires: python3-referencing >= 0.36.2
Requires: python3-ruamel-yaml >= 0.18.11
Requires: python3-ruamel-yaml-clib >= 0.2.12
Requires: python3-subprocess-tee >= 0.4.1
Requires: python3-wcmatch >= 8.1.2
Requires: python3-yamllint >= 1.34.0
Provides: python3-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-lint) = %{epoch}:%{version}-%{release}

%description -n ansible-lint
Checks playbooks for practices and behavior that could potentially be
improved.

%files -n ansible-lint
%license COPYING
%{_bindir}/*
%{python3_sitelib}/*

%changelog
