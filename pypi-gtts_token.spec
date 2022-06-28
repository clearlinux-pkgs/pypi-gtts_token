#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-gtts_token
Version  : 1.1.4
Release  : 31
URL      : https://files.pythonhosted.org/packages/78/b4/e2306352c5b5d777c9d39cbf17f21b10be40cbe7271329473d424700aa41/gTTS-token-1.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/b4/e2306352c5b5d777c9d39cbf17f21b10be40cbe7271329473d424700aa41/gTTS-token-1.1.4.tar.gz
Summary  : Calculates a token to run the Google Translate text to speech
Group    : Development/Tools
License  : MIT
Requires: pypi-gtts_token-license = %{version}-%{release}
Requires: pypi-gtts_token-python = %{version}-%{release}
Requires: pypi-gtts_token-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)

%description
====

%package license
Summary: license components for the pypi-gtts_token package.
Group: Default

%description license
license components for the pypi-gtts_token package.


%package python
Summary: python components for the pypi-gtts_token package.
Group: Default
Requires: pypi-gtts_token-python3 = %{version}-%{release}

%description python
python components for the pypi-gtts_token package.


%package python3
Summary: python3 components for the pypi-gtts_token package.
Group: Default
Requires: python3-core
Provides: pypi(gtts_token)
Requires: pypi(requests)

%description python3
python3 components for the pypi-gtts_token package.


%prep
%setup -q -n gTTS-token-1.1.4
cd %{_builddir}/gTTS-token-1.1.4
pushd ..
cp -a gTTS-token-1.1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656402198
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gtts_token
cp %{_builddir}/gTTS-token-1.1.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gtts_token/748ee85e743c7323d44803cdba103206fdb58874
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gtts_token/748ee85e743c7323d44803cdba103206fdb58874

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
