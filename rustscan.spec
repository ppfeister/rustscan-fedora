# prevent library files from being installed
%global cargo_install_lib 0

Name: rustscan
Version: 2.2.3
Release: 1%{?dist}
Summary: The modern port scanner

License: GPL-3.0-only
URL: https://github.com/rustscan/rustscan
Source0: %{URL}/archive/%{version}.tar.gz

Patch0: 0001-rc1.patch
Patch1: 0002-Downgrade-anstream.patch

BuildRequires: cargo-rpm-macros >= 24
BuildRequires: help2man

%global _description %{expand:
RustScan is a modern take on the port scanner. Sleek & fast. All while
providing extensive extendability to you.

Not to mention RustScan uses Adaptive Learning to improve itself over time,
making it the best port scanner for you.
}

%description %{_description}


%prep
%autosetup -n RustScan-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build


%install
%cargo_install

install -d '%{buildroot}%{_mandir}/man1'
help2man \
    --no-info \
    --version-string='%{version}' \
    --name='%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/rustscan.1' \
    '%{buildroot}%{_bindir}/rustscan'


%files
%license LICENSE
%doc README.md
%{_bindir}/rustscan
%{_mandir}/man1/rustscan.1*


%changelog
* Tue Jul 02 2024 Paul Pfeister <code@pfeister.dev> - 2.2.3-1
- Initial packaging
