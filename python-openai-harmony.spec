Name:           python-openai-harmony
Version:        0.0.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenAI_s response format for its open-weight model series gpt-oss

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            ...
Source:         %{pypi_source openai_harmony}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'openai-harmony' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-openai-harmony
Summary:        %{summary}

%description -n python3-openai-harmony %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-openai-harmony demo


%prep
%autosetup -p1 -n openai_harmony-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x demo


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l openai_harmony


%check
%pyproject_check_import


%files -n python3-openai-harmony -f %{pyproject_files}


%changelog
%autochangelog
