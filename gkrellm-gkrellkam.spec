Summary:	Image watcher plugin
Summary(pl):	Wtyczka do ¶ledzenia obrazków
Name:		gkrellm-gkrellkam
Version:	0.3.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://telia.dl.sourceforge.net/sourceforge/gkrellkam/gkrellkam_%{version}.tar.gz
URL:		http://gkrellkam.sourceforge.net/
BuildRequires:	gkrellm-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
You can have a periodically updated image of whatever you want, albeit
squeezed into a little gkrellm panel. Each panel can watch a single
image, or cycle through a list of images, or run a script and use the
output of the script as the filename of an image. GKrellKam even knows
how to get images out on the Internet - this is what allows you to
watch webcams.

%description -l pl
GKrellKam pozwala okresowo uaktualniaæ dowolny obrazek umieszczony w
ma³ym panelu gkrellma. Ka¿dy panel mo¿e ¶ledziæ pojedynczy obrazek lub
cyklicznie prze³±czaæ listê obrazków, albo urucomiæ skrypt i u¿ywaæ
jego wyj¶cia jako nazwy obrazka. GKrellKam potrafi nawet ¶ci±gaæ
obrazki z Internetu, pozwalaj±c na ¶ledzenie kamer internetowych.

%prep
%setup -q -n gkrellkam-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC `gtk-config --cflags` `imlib-config --cflags-gdk` -I/usr/X11R6/include/gkrellm" \
	LDFLAGS="%{rpmldflags} -shared -Wl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/gkrellm,%{_mandir}/man5}

install gkrellkam.so $RPM_BUILD_ROOT%{_libdir}/gkrellm
install gkrellkam-list.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README Todo example.list
%attr(755,root,root) %{_libdir}/gkrellm/gkrellkam.so
%{_mandir}/man5/*
