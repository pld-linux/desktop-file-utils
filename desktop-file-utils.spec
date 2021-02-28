Summary:	A couple of command line utilities for working with desktop entries
Summary(pl.UTF-8):	Narzędzia linii poleceń do pracy z plikami desktop
Name:		desktop-file-utils
Version:	0.26
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
# Source0-md5:	29739e005f5887cf41639b8450f3c23f
URL:		https://www.freedesktop.org/wiki/Software/desktop-file-utils
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
desktop-file-utils contains a couple of command line utilities for
working with desktop entries.

%description -l pl.UTF-8
Pakiet desktop-file-utils zawiera kilka narzędzi uruchamianych z linii
poleceń, służących do pracy z plikami desktop.

%package -n emacs-desktop-entry-mode
Summary:	Desktop entry mode for Emacs
Summary(pl.UTF-8):	Tryb plików desktop dla Emacsa
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}
Requires:	emacs
BuildArch:	noarch

%description -n emacs-desktop-entry-mode
Desktop entry mode for Emacs.

%description -n emacs-desktop-entry-mode -l pl.UTF-8
Tryb plików desktop dla Emacsa.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%ninja_install -C build

touch $RPM_BUILD_ROOT%{_desktopdir}/mimeinfo.cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/desktop-file-edit
%attr(755,root,root) %{_bindir}/desktop-file-install
%attr(755,root,root) %{_bindir}/desktop-file-validate
%attr(755,root,root) %{_bindir}/update-desktop-database
%{_mandir}/man1/desktop-file-edit.1*
%{_mandir}/man1/desktop-file-install.1*
%{_mandir}/man1/desktop-file-validate.1*
%{_mandir}/man1/update-desktop-database.1*
%ghost %{_desktopdir}/mimeinfo.cache

%files -n emacs-desktop-entry-mode
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/desktop-entry-mode.el
