# Generated by rust2rpm 13
%bcond_without check

%global crate cargo-edit

Name:           rust-%{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        This extends Cargo to allow you to add and remove dependencies by modifying your `Cargo.toml` file from the command line

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/cargo-edit
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
This extends Cargo to allow you to add and remove dependencies by modifying
your `Cargo.toml` file from the command line. It contains `cargo add`, `cargo
rm`, and `cargo upgrade`.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/cargo-add
%{_bindir}/cargo-rm
%{_bindir}/cargo-upgrade
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+add-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+add-devel %{_description}

This package contains library source intended for building other packages
which use "add" feature of "%{crate}" crate.

%files       -n %{name}+add-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+atty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atty-devel %{_description}

This package contains library source intended for building other packages
which use "atty" feature of "%{crate}" crate.

%files       -n %{name}+atty-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-devel %{_description}

This package contains library source intended for building other packages
which use "cli" feature of "%{crate}" crate.

%files       -n %{name}+cli-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rm-devel %{_description}

This package contains library source intended for building other packages
which use "rm" feature of "%{crate}" crate.

%files       -n %{name}+rm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+structopt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+structopt-devel %{_description}

This package contains library source intended for building other packages
which use "structopt" feature of "%{crate}" crate.

%files       -n %{name}+structopt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-external-apis-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-external-apis-devel %{_description}

This package contains library source intended for building other packages
which use "test-external-apis" feature of "%{crate}" crate.

%files       -n %{name}+test-external-apis-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+upgrade-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+upgrade-devel %{_description}

This package contains library source intended for building other packages
which use "upgrade" feature of "%{crate}" crate.

%files       -n %{name}+upgrade-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Sep 22 18:48:02 CEST 2020 pluth <pluth@0t.re> - 0.6.0-1
- Initial package
