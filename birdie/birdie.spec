Name:           birdie
Version:        1.1
Release:        1%{?dist}
Summary:        A twitter client for Linux
License:        GPLv3
URL:            http://birdieapp.github.io
Source0:        https://github.com/birdieapp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gtk3-devel >= 3.10
BuildRequires: vala-devel >= 0.22.1
BuildRequires: intltool
BuildRequires: glib2-devel
BuildRequires: libpurple-devel
BuildRequires: sqlite-devel
BuildRequires: libXtst-devel
BuildRequires: libgee06-devel
BuildRequires: rest-devel
BuildRequires: json-glib-devel
BuildRequires: libnotify-devel
BuildRequires: libcanberra-devel
BuildRequires: webkitgtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: desktop-file-utils

%description
A beautiful GNOME Twitter client for Linux

%prep
%setup -q

%build
%{cmake} .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/update-desktop-database &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.birdieapp.birdie.gschema.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/indicators/messages/applications/birdie

%changelog
* Fri Feb 21 2014 Ryan Lerch <ryanlerch@fedoraproject.org> 1.1-1
- Initial Release
