Name:		task-razorqt
Version:	1
Release:	3
Summary:	Metapackage for razor-qt
Group:		Graphical desktop/Other
License:	GPL
URL:		http://razor-qt.org
Requires:	desktop-common-data
Requires:	razorqt-desktop
Requires:	razorqt-appswitcher
Requires:	razorqt-session
Requires:	razorqt-panel
Requires:	razorqt-autosuspend
Requires:	razorqt-runner
Requires:	razorqt-policykit-agent
Requires:	task-x11
Requires:	drakconf
Requires:	dbus-x11

Suggests:	razorqt-confupdate
Suggests:	qterminal
Suggests:	qastools
Suggests:	andromeda
Suggests:	qbittorrent
Suggests:	juffed
Suggests:	qlipper
# this package requires gtk2 libs
# Suggests:	xarchiver
Suggests:	lightdm-razorqt-greeter
Suggests:	screengrab
Suggests:	silicon-image-burner
Suggests:	silicon-data-disc
Suggests:	silicon-audio-disc
Suggests:	silicon-converter
Suggests:	silicon-copy-disc
Suggests:	silicon-plugin-system-tray
Suggests:	silicon-plugin-single-inner-dialog
Suggests:	xscreensaver
Suggests:	nomacs
Suggests:	qupzilla
Suggests:	trojita

BuildArch:	noarch

# Obsoletes:	old razor

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Razor-Qt Desktop Environment.

%files
