Summary:	A couple of command line utilities for working with desktop entries
Summary(pl):	Kilka narzêdzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.7
Release:	4
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/Software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	32b948c2676170dc01ac4849c00bc5d6
Source1:	%{name}-default-modules.conf
Patch0:		%{name}-menu.patch
Patch1:		%{name}-hide_empty_submenus.patch
Patch2:		%{name}-directory_change_notify.patch
Patch3:		%{name}-directory_mtime.patch
Patch4:		%{name}-onlyshowin.patch
Patch5:		%{name}-nodisplay.patch
Patch6:		%{name}-noshowin.patch
Patch7:		%{name}-home_dir.patch
Patch8:		%{name}-directory_nodisplay.patch
Patch9:		%{name}-directory_onlyshowin.patch
Patch10:	%{name}-directory_noshowin.patch
# don't append / at end of URL
URL:		http://www.freedesktop.org/software/desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	popt-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
desktop-file-utils contains a couple of command line utilities for
working with desktop entries.

%description -l pl
desktop-file-utils zawiera kilka narzêdzi uruchamianych z linii
poleceñ, s³u¿±cych do pracy z elementami biurkowymi.

%package -n gnome-vfs2-module-menu
Summary:	Freedesktop.org style menu support module for gnome-vfs
Summary(pl):	Obs³uga menu wed³ug specyfikacji z freedesktop.org
Group:		Applications
Provides:	gnome-vfs-menu-module
Obsoletes:	gnome-vfs2-vfolder-menu
Requires:	gnome-vfs2 >= 2.6.1.1-3.1
Requires:	applnk >= 1.9.3-2

%description -n gnome-vfs2-module-menu
This package contains module for gnome-vfs supporting menu with
specification declared by freedesktop.org .

%description -n gnome-vfs2-module-menu -l pl
Ten pakiet zawiera modu³ obs³ugi menu dla gnome-vfs wed³ug
specyfikacji freedesktop.org .

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove unused *.la for gnome-vfs modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la

# not needed - it's only for testing purposes
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gnome-vfs-2.0/modules/menu-modules.conf

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gnome-vfs-2.0/modules/default-modules.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*

%files -n gnome-vfs2-module-menu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
%{_sysconfdir}/gnome-vfs-2.0/modules/default-modules.conf
