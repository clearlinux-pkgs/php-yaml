#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-yaml
Version  : 2.2.0
Release  : 10
URL      : https://pecl.php.net/get/yaml-2.2.0.tgz
Source0  : https://pecl.php.net/get/yaml-2.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-yaml-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : re2c
BuildRequires : yaml-dev

%description
The Yaml PHP Extension provides a wrapper to the LibYAML library.
It gives the user the ability to parse YAML document streams into PHP
constructs and emit PHP constructs as valid YAML 1.1 documents.

%package lib
Summary: lib components for the php-yaml package.
Group: Libraries

%description lib
lib components for the php-yaml package.


%prep
%setup -q -n yaml-2.2.0
cd %{_builddir}/yaml-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/yaml.so
