#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-yaml
Version  : 2.2.3
Release  : 71
URL      : https://pecl.php.net/get/yaml-2.2.3.tgz
Source0  : https://pecl.php.net/get/yaml-2.2.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-yaml-lib = %{version}-%{release}
Requires: php-yaml-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
BuildRequires : re2c
BuildRequires : yaml-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Yaml PHP Extension provides a wrapper to the LibYAML library.
It gives the user the ability to parse YAML document streams into PHP
constructs and emit PHP constructs as valid YAML 1.1 documents.

%package lib
Summary: lib components for the php-yaml package.
Group: Libraries
Requires: php-yaml-license = %{version}-%{release}

%description lib
lib components for the php-yaml package.


%package license
Summary: license components for the php-yaml package.
Group: Default

%description license
license components for the php-yaml package.


%prep
%setup -q -n yaml-2.2.3
cd %{_builddir}/yaml-2.2.3
pushd ..
cp -a yaml-2.2.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-yaml
cp %{_builddir}/yaml-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-yaml/5a96fce3231b38c51702c104bf339b6f035a30df || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/yaml.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-yaml/5a96fce3231b38c51702c104bf339b6f035a30df
