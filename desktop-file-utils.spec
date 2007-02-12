Summary:	A couple of command line utilities for working with desktop entries
Summary(pl.UTF-8):	Kilka narzędzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.12
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	335b91ec70ea1c08f87dfde8c5926e7b
# don't append / at end of URL
URL:		http://www.freedesktop.org/wiki/Software_2fdesktop_2dfile_2dutils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.11.2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
