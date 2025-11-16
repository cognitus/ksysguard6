%global date        20251116
%global commit      7c16d8f83db00ba7508ba1b8805b36e74f40c76c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global min_qt_version 6.6.0
%global min_kf_version 6.0.0

Name:    ksysguard6
Version: 6.0.1^%{date}git%{shortcommit}
Release: 6%{?dist}
Summary: KDE Process Management application, port for KDE6

License: GPLv2
URL:     https://github.com/cognitus/ksysguard6
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib 

BuildRequires: cmake(Qt6Core) >= %{min_qt_version}
BuildRequires: qt6-qtbase-private-devel

%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Xml)

BuildRequires: cmake(KF6Config) >= %{min_kf_version}
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuffCore)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(KSysGuard)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libcap)
BuildRequires: lm_sensors-devel

Recommends:    ksysguardd6 = %{version}-%{release}

%description
KSysGuard is a program to monitor various elements of your system, or any
other remote system with the KSysGuard daemon (ksysgardd) installed. 
Currently the daemon has been ported to Linux, FreeBSD, Irix, NetBSD,
OpenBSD, Solaris and Tru64 with varying degrees of completion.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n ksysguardd6
Summary: Performance monitor daemon
%description -n ksysguardd6
%{summary}. 


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --with-html --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.ksysguard.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.ksysguard.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.systemmonitor.desktop


%files devel
%{_libdir}/libprocesscore_ksg6.so
%dir %{_includedir}/ksysguard6
%{_includedir}/ksysguard6/processcore/*.h


%files -f %{name}.lang
%doc README
%license COPYING COPYING.DOC
%{_bindir}/ksysguard
%{_bindir}/systemmonitor
%{_libdir}/libprocesscore_ksg6.so.*
%{_kf6_plugindir}/kded/ksysguard6.so
%{_kf6_qtplugindir}/ksysguard6/process/ksysguard_plugin_network.so
%{_kf6_qtplugindir}/ksysguard6/process/ksysguard_plugin_nvidia.so
%{_kf6_libexecdir}/kauth/ksysguardprocesslist_helper_ksg6
%caps(cap_net_raw=pe) %{_libexecdir}/ksysguard6/ksgrd_network_helper
%{_datadir}/applications/org.kde.ksysguard.desktop
%{_datadir}/applications/org.kde.systemmonitor.desktop
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper_ksg6.service
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper_ksg6.conf
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper_ksg6.policy
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/knotifications6/ksysguard.notifyrc
%{_datadir}/knsrcfiles/ksysguard.knsrc
%{_datadir}/ksysguard/ProcessTable.sgrd
%{_datadir}/ksysguard/SystemLoad2.sgrd
%{_datadir}/kxmlgui5/ksysguard/ksysguardui.rc
%{_metainfodir}/org.kde.ksysguard.appdata.xml

%files -n ksysguardd6
%license COPYING COPYING.DOC
%config %{_sysconfdir}/ksysguarddrc
%{_bindir}/ksysguardd


%changelog
* Mon Apr 21 2025 Yaroslav Sidlovsky <zawertun@gmail.com> - 6.0.1^20250305gitf98ae6e-5
- added cap_net_raw=ep for ksgrd_network_helper

* Mon Apr 21 2025 Yaroslav Sidlovsky <zawertun@gmail.com> - 6.0.1^20250305gitf98ae6e-4
- git revision f98ae6e7b1046f018abd4737fd63b6cbc357f5a2 (Mar 5, 2025)

* Mon Nov 11 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 6.0.1^20240620gitcb178ae-3
- rebuild

* Thu Aug 01 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 6.0.1^20240620gitcb178ae-2
- BR: cmake(Qt6WebEngineWidgets) only for %%qt6_qtwebengine_arches

* Thu Aug 01 2024 Yaroslav Sidlovsky <zawertun@gmail.com>
- Spec for version 6.0.1, git revision cb178ae288358389ec442e8bec89b2e6fa0f290e


