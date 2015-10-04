#%define strip /bin/true
#%define __requires_exclude  ^.*$
#%define __provides_exclude_from ^.*$
#%define __find_requires     %{nil}
#%global debug_package       %{nil}

Name:          libreoffice
Summary:       libreoffice kit for Sailfish OS
Version:       5.0.1.2
Release:       1
Group:         Applications
License:       MPLv2
URL:           https://github.com/foolab/lo-build
Source0:       %{name}-%{version}.tar.bz2
Patch0:        enable_lo_kit.diff
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpng)
BuildRequires: perl(Archive::Zip)
BuildRequires: zip
BuildRequires: gperf
BuildRequires: python
BuildRequires: bison
BuildRequires: flex
BuildRequires: fakelibs

%description
libreoffice kit for Sailfish OS

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1
mv ../tarballs external
# We don't want those
rm -rf dictionaries helpcontent2 translations

%build
./autogen.sh \
    --enable-release-build \
    --with-x=no \
    --disable-gconf \
    --without-junit \
    --disable-cups \
    --disable-gnome-vfs \
    --disable-gstreamer-0-10 \
    --disable-gstreamer-1-0 \
    --disable-liblangtag \
    --disable-lockdown \
    --disable-odk \
    --disable-postgresql-sdbc \
    --disable-python \
    --disable-randr \
    --disable-randr-link \
    --disable-systray \
    --without-helppack-integration \
    --without-java \
    --disable-firebird-sdbc \
    --enable-graphite=no \
    --disable-collada \
    --with-galleries=no \
    --disable-lpsolve \
    --disable-coinmp \
    --disable-pdfimport \
    --enable-hardlink-deliver \
    --disable-report-builder \
    --enable-dbgutil=no \
    --disable-dbus \
    --disable-sdremote \
    --disable-sdremote-bluetooth \
    --disable-gio \
    --with-webdav=none \
    --disable-cve-tests \
    --disable-extension-update \
    --disable-lotuswordpro \
    --disable-gltf \
    --without-help \
    --without-myspell-dicts \
    --without-doxygen \
    --with-theme="" \
    --with-alloc=system \
    --with-system-libxml=no \
    --enable-sal-log \
    --enable-fetch-external=no \
    --with-system-zlib \
    --with-system-expat \
    --with-system-openssl \
    --with-system-curl \
    --with-system-libpng
#    --enable-mergelibs

#make
make -j 1  -rs -f Makefile.gbuild build

%install
mkdir -p %{buildroot}/%{_libdir}/libreoffice/
find instdir/program -name "*.so*" | xargs chmod 644
#find instdir/program -name "*.so*" | xargs strip

mv instdir/program %{buildroot}/%{_libdir}/libreoffice/
#rm -rf `pwd`

%files
%defattr(-,root,root,-)
%{_libdir}/libreoffice/program/*
