%bcond_without tests

%global pypi_name powerline-shell
%global pypi_version 0.7.0
%global forgeurl https://github.com/b-ryan/powerline-shell

# Upstream does not tag releases in Git or push code to PyPi
%global commit 7332357af633980ce5e65616518bcdbd509febcc

%forgemeta

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Powerline Shell Prompt
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch

# Make the tests pass
Patch:          %{forgeurl}/pull/547.patch
# Remove argparse dependency
Patch:          %{forgeurl}/pull/548.patch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  subversion
BuildRequires:  fossil
BuildRequires:  breezy
%endif


%global _description %{expand:
Powerline shell prompt for Bash, Zsh, Fish, and Tcsh.}


%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides    python3-%{pypi_name}


%description -n python3-%{pypi_name} %_description


%prep
%forgesetup
%autopatch -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements-dev.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files powerline_shell


%check
%if %{with tests}
%pytest
%endif
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/powerline-shell


%changelog
%autochangelog
