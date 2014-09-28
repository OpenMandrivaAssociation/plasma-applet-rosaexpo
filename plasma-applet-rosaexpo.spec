# for rosa apps I don't need debug.Sflo
%define debug_package	%{nil}

Name:				plasma-applet-rosaexpo
Version:			0.1
Release:			1
Summary:			Expo applet
License:			GPLv2+
Group:				Graphical desktop/KDE
Url:				https://abf.io/uxteam/rosapanel-devel/tree/devel/expo-applet
# git source in rosapanel/expo-applet
# thanks to Dimitry Ashkadov
Source:				expo-applet.tar.gz
BuildRequires:		cmake >= 2.8
BuildRequires:		qt4-devel >= 4.8
BuildRequires:		kdebase4-workspace-devel
BuildRequires:		kdelibs4-devel

Requires:		kdebase4-workspace >= 4.11.4
# no point installing it twice
# this is already included in rosapanel. Sflo
Conflicts:		rosapanel

%description
Expo applet for KDE.

%prep
%setup -qn expo-applet


%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

%files 
%{_kde_libdir}/kde4/plasma_applet_rosaexpo.so
%{_kde_appsdir}/plasma/packages/com.rosalab.expo/
%{_kde_services}/plasma-applet-rosaexpo.desktop



