Summary:	A couple of command line utilities for working with desktop entries
Summary(pl):	Kilka narzêdzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.11
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	b27a1890979caaca8e72ffe22af6e389
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

%description -l pl
desktop-file-utils zawiera kilka narzêdzi uruchamianych z linii
poleceñ, s³u¿±cych do pracy z elementami biurkowymi.

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
