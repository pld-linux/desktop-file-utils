Summary:	A couple of command line utilities for working with desktop entries
Summary(pl):	Kilka narzêdzi do pracy z elementami biurkowymi
Name:		desktop-file-utils
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a1c8bcd648da58bfe0b142042292caa8
URL:		http://www.freedesktop.org/software/desktop-file-utils/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	popt-devel >= 1.5
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
%configure

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
