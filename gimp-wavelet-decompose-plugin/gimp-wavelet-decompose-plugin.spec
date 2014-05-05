Name:           gimp-wavelet-decompose-plugin
Version:        0.1.2
Release:        0%{?dist}
Summary:        Gimp wavelet decompose plugin

License:        GPLv2+
URL:            http://registry.gimp.org/node/11742
Source0:        http://registry.gimp.org/files/wavelet-decompose-%{version}.tar.gz

BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig
BuildRequires:  gettext

Requires:       gimp >= 2.4

%description
This plugin (available in the GIMP interface at Filters > Generic > Wavelet Decompose) losslessly decomposes a layer of an image into layers of wavelet scales. This means that you can edit the image on different detail scales (frequencies). The trivial recomposition of the image can be done by GIMP's layer modes so you can see the results of your modifications instantly. Among the applications are retouching, noise reduction, and enhancing global contrast.


%prep
%setup -q -n wavelet-decompose-%{version}
sed -i -e 's/CFLAGS.*/& $(shell echo $$CFLAGS)/' src/Makefile
sed -i 's|gimptool-2.0 --libs)|gimptool-2.0 --libs) -lm|' src/Makefile
echo '#!/bin/bash' > configure
chmod +x configure


%build
%configure
make %{?_smp_mflags}


%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
sed -i "s|/usr/share/locale|%{buildroot}%{_datadir}/locale|" po/Makefile
mkdir -p %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
install -m 0755 -p src/wavelet-decompose %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/it/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES
make install po
%find_lang gimp20-wavelet-decompose-plug-in


%files -f gimp20-wavelet-decompose-plug-in.lang
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/gimp/2.0/plug-ins/wavelet-decompose



%changelog
* Mon May 05 2014 Ryan Lerch <ryanlerch@fedoraproject.org> - 0.1.2-0
Initial Release
