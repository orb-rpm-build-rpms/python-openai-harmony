Name:           python-openai-harmony
Version:        0.0.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenAI_s response format for its open-weight model series gpt-oss

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/openai/harmony
Source:         %{pypi_source openai_harmony}

# Update the pyo3 binding to 0.29 (the version Fedora ships); upstream 0.0.8
# pins 0.25.x. Submitted upstream at https://github.com/openai/harmony.
Patch0:         pyo3-0.29.patch
# Fedora-only: drop the optional wasm-binding feature, whose wasm-bindgen crate
# stack Fedora does not package. cargo metadata resolves optional deps even when
# the feature is disabled, so the crates must be absent from the manifest.
Patch1:         drop-wasm-binding.patch

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo-rpm-macros


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
# The upstream lock pins pyo3 0.25.x and the now-removed wasm crates; drop it so
# cargo re-resolves the patched manifest against Fedora's packaged registry.
rm -f Cargo.lock
# Rust bindings: resolve crates against Fedora's packaged registry (offline).
%cargo_prep


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x demo
# pyo3 is an *optional* crate, pulled in only by the "python-binding" feature
# (see Cargo.toml [features]); [tool.maturin] builds with that feature enabled.
# Pass -f so the pyo3 crate is emitted as a BuildRequires. -t so the dev-deps
# (pretty_assertions) that cargo metadata needs to re-resolve the lockless
# manifest are emitted too.
%cargo_generate_buildrequires -t -f python-binding


%build
export RUSTFLAGS='%{build_rustflags}'
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
