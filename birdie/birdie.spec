Name:           birdie
Version: 	1.1
Release:        0%{?dist}
Summary:        A twitter client for Linux
License:        GPLv3
URL:            http://birdieapp.github.io
Source0:        %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
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

%description
A beautiful Twitter client for GNU/Linux

%prep
%setup -q

%build
%{cmake} .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.birdieapp.birdie.gschema.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/locale/*/*/birdie.mo
%{_datadir}/indicators/messages/applications/birdie

%changelog
* Fri Feb 21 2014 Ryan Lerch <ryanlerch@fedoraproject.org> 1.1-0
- Initial Release
