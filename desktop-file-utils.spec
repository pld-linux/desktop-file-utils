Summary:	A couple of command line utilities for working with desktop entries
Summary(pl.UTF-8):	Kilka narzędzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.15
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2fe8ebe222fc33cd4a959415495b7eed
URL:		http://www.freedesktop.org/wiki/Software/desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
desktop-file-utils contains a couple of command line utilities for
working with desktop entries.

%description -l pl.UTF-8
desktop-file-utils zawiera kilka narzędzi uruchamianych z linii
poleceń, służących do pracy z elementami biurkowymi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_desktopdir}/mimeinfo.cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/desktop-file-install
%attr(755,root,root) %{_bindir}/desktop-file-validate
%attr(755,root,root) %{_bindir}/update-desktop-database
%ghost %{_desktopdir}/mimeinfo.cache
