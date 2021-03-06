#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5BE41E162CD6358E (charles.kerr@canonical.com)
#
Name     : libappindicator
Version  : 12.10.0
Release  : 6
URL      : https://launchpad.net/libappindicator/12.10/12.10.0/+download/libappindicator-12.10.0.tar.gz
Source0  : https://launchpad.net/libappindicator/12.10/12.10.0/+download/libappindicator-12.10.0.tar.gz
Source1  : https://launchpad.net/libappindicator/12.10/12.10.0/+download/libappindicator-12.10.0.tar.gz.asc
Summary  : Application indicators
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: libappindicator-data = %{version}-%{release}
Requires: libappindicator-lib = %{version}-%{release}
Requires: libappindicator-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(indicator3-0.4)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : vala
Patch1: libappindicator-disable-python-bindings.patch

%description
A readme is the very beginning, a very nice place to start.  When you read
you begin with A-B-C when you code you begin with RE-AD-ME!

%package data
Summary: data components for the libappindicator package.
Group: Data

%description data
data components for the libappindicator package.


%package dev
Summary: dev components for the libappindicator package.
Group: Development
Requires: libappindicator-lib = %{version}-%{release}
Requires: libappindicator-data = %{version}-%{release}
Provides: libappindicator-devel = %{version}-%{release}
Requires: libappindicator = %{version}-%{release}

%description dev
dev components for the libappindicator package.


%package doc
Summary: doc components for the libappindicator package.
Group: Documentation

%description doc
doc components for the libappindicator package.


%package lib
Summary: lib components for the libappindicator package.
Group: Libraries
Requires: libappindicator-data = %{version}-%{release}
Requires: libappindicator-license = %{version}-%{release}

%description lib
lib components for the libappindicator package.


%package license
Summary: license components for the libappindicator package.
Group: Default

%description license
license components for the libappindicator package.


%prep
%setup -q -n libappindicator-12.10.0
cd %{_builddir}/libappindicator-12.10.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605557568
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static --with-gtk=3 \
--disable-gtk-doc-html \
--disable-mono-test \
--disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1605557568
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libappindicator
cp %{_builddir}/libappindicator-12.10.0/COPYING %{buildroot}/usr/share/package-licenses/libappindicator/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/libappindicator-12.10.0/COPYING.LGPL.2.1 %{buildroot}/usr/share/package-licenses/libappindicator/9a1929f4700d2407c70b507b3b2aaf6226a9543c
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/AppIndicator3-0.1.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/appindicator3-0.1.deps
/usr/share/vala/vapi/appindicator3-0.1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libappindicator3-0.1/libappindicator/app-indicator-enum-types.h
/usr/include/libappindicator3-0.1/libappindicator/app-indicator.h
/usr/lib64/libappindicator3.so
/usr/lib64/pkgconfig/appindicator3-0.1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libappindicator/annotation-glossary.html
/usr/share/gtk-doc/html/libappindicator/api-index-0-5.html
/usr/share/gtk-doc/html/libappindicator/api-index-deprecated.html
/usr/share/gtk-doc/html/libappindicator/api-index-full.html
/usr/share/gtk-doc/html/libappindicator/ch01.html
/usr/share/gtk-doc/html/libappindicator/home.png
/usr/share/gtk-doc/html/libappindicator/index.html
/usr/share/gtk-doc/html/libappindicator/index.sgml
/usr/share/gtk-doc/html/libappindicator/left.png
/usr/share/gtk-doc/html/libappindicator/libappindicator-app-indicator.html
/usr/share/gtk-doc/html/libappindicator/libappindicator.devhelp2
/usr/share/gtk-doc/html/libappindicator/object-tree.html
/usr/share/gtk-doc/html/libappindicator/right.png
/usr/share/gtk-doc/html/libappindicator/style.css
/usr/share/gtk-doc/html/libappindicator/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libappindicator3.so.1
/usr/lib64/libappindicator3.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libappindicator/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/libappindicator/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
