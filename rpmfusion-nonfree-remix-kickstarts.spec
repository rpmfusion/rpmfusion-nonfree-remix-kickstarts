Name:       rpmfusion-nonfree-remix-kickstarts
# we follow the spin-kickstarts version scheme as the files in this 
# package highly depend on them anyway
Version:    0.18.0
Release:    0.1%{?dist}
Summary:    Kickstart files for creating distributions with packages RPM Fusion nonfree

Group:      Applications/System
License:    GPLv3+
URL:        http://rpmfusion.org/remix-kickstarts
Source1:    rpmfusion-remix-kickstarts-README
Source2:    rpmfusion-remix-kickstarts-COPYING
Source10:   rpmfusion-nonfree-live-base.ks
Source11:   rpmfusion-nonfree-livecd-desktop.ks
Source12:   rpmfusion-nonfree-livecd-kde.ks
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:   spin-kickstarts >= %{version}
Requires:   rpmfusion-free-remix-kickstarts >= %{version}

%description
A number of kickstarts files you can use to create a Linux distribution or 
a Fedora Remix with packages from RPM Fusion. Please remember to read the 
README file if you want to distribute what you made with tools that used
these kickstart files!

%prep
echo "nothing to setup"

%build
echo "nothing to build"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -m644 %{SOURCE1} README
install -p -m644 %{SOURCE2} COPYING
install -t $RPM_BUILD_ROOT%{_datadir}/%{name}/ -p -m644 \
  %{SOURCE10}  \
  %{SOURCE11}  \
  %{SOURCE12}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_datadir}/%{name}/

%changelog
* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.18.0-0.1
- Update to 0.18.0

* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.16.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.16.0-0.1
- Update to pre 16.0

* Mon Jun 01 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-5
- add disabled repo definitions for f11 release
- make the base config "includepkgs=rpmfusion-nonfree-release"

* Sat May 23 2009 Thorsten Leemhuis <fedora at leemhuis dot info> - 0.11.1-4
- fix cut'n'paste typo in require

* Fri May 22 2009 Thorsten Leemhuis <fedora at leemhuis dot info> - 0.11.1-3
- initial version, based on rpmfusion-free-remix-kickstarts
