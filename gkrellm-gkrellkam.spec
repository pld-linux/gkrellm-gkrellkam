Summary:	Image watcher plugin
Summary(pl):	Wtyczka do �ledzenia obrazk�w
Name:		gkrellm-gkrellkam
Version:	2.0.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/gkrellkam_%{version}.tar.gz
# Source0-md5:	657c99de172bc7598098a6a4196ff07b
URL:		http://gkrellkam.sourceforge.net/
BuildRequires:	gkrellm-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can have a periodically updated image of whatever you want, albeit
squeezed into a little gkrellm panel. Each panel can watch a single
image, or cycle through a list of images, or run a script and use the
output of the script as the filename of an image. GKrellKam even knows
how to get images out on the Internet - this is what allows you to
watch webcams.

%description -l pl
GKrellKam pozwala okresowo uaktualnia� dowolny obrazek umieszczony w
ma�ym panelu gkrellma. Ka�dy panel mo�e �ledzi� pojedynczy obrazek lub
cyklicznie prze��cza� list� obrazk�w, albo uruchomi� skrypt i u�ywa�
jego wyj�cia jako nazwy obrazka. GKrellKam potrafi nawet �ci�ga�
obrazki z Internetu, pozwalaj�c na �ledzenie kamer internetowych.

%prep
%setup -q -n gkrellkam-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/gkrellm2/plugins,%{_mandir}/man5}

install gkrellkam2.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins
install gkrellkam-list.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README Todo example.list
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellkam2.so
%{_mandir}/man5/*
