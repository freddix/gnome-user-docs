Summary:	GNOME user focumentation
Name:		gnome-user-docs
Version:	3.6.2
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-user-docs/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	6301088417ce005772922e0e7ce0db4c
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	libxml2-progs
BuildRequires:	pkg-config
BuildRequires:	yelp-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General GNOME User Guide.

%description -l pl.UTF-8
Ogólna dokumentacja użytkownika GNOME.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-help --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gnome-help.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
