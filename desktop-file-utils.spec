Summary:	A couple of command line utilities for working with desktop entries
Summary(pl):	Kilka narzêdzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/Software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	dcace3294470e9cdc9ebfe7de1881ece
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
Requires:	gnome-vfs2 >= 2.2.0

%description -n gnome-vfs2-module-menu
This package contains module for gnome-vfs supporting menu with
specification declared by freedesktop.org.

%description -n gnome-vfs2-module-menu -l pl
Ten pakiet zawiera modu³ obs³ugi menu dla gnome-vfs wed³ug
specyfikacji freedesktop.org.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*

%files -n gnome-vfs2-module-menu
%defattr(644,root,root,755)
%{_sysconfdir}/gnome-vfs-2.0/modules/menu-modules.conf
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
