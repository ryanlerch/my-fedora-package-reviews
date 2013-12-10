Name:               key-mon
Version:            1.16
Release:            1%{?dist}
Summary:            A screen cast utility that displays your keyboard and mouse status
Group:              Development/Libraries
License:            ASL 2.0
URL:                http://code.google.com/p/key-mon/
Source0:            https://pypi.python.org/packages/source/k/key-mon/key-mon-%{version}.zip
BuildArch:          noarch
BuildRequires:      python2-devel
BuildRequires:      desktop-file-utils
Requires:           pygtk2
Requires:           python-xlib
Requires:           librsvg2

%description
Key-mon is useful for teaching since it shows the current status of your
keyboard and mouse and you use them in another application.  No longer do
you need to say 'Now I'm pressing the Ctrl-D key', your students can just
see the keystroke for themselves.

%prep
%setup -q
rm src/keymon/themes/clear/config~

#remove hashbang python line from library python files
for lib in src/keymon/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications icons/%{name}.desktop
#manually install the manpage
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_mandir}/man1/%{name}.1*
%doc README.rst COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{python2_sitelib}/keymon/
%{python2_sitelib}/key_mon-%{version}*

%changelog
* Fri Dec 06 2013  Ryan Lerch <ryanlerch@fedoraproject.org> 1.16-1
- initial package for Fedora
