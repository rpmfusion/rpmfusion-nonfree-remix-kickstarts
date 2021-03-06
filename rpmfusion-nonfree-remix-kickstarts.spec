Name:       rpmfusion-nonfree-remix-kickstarts
Version:    0.28
Release:    2%{?dist}
Summary:    Kickstart files for creating distributions with packages RPM Fusion nonfree

Group:      Applications/System
License:    GPLv3+
URL:        http://rpmfusion.org/remix-kickstarts
Source1:    rpmfusion-remix-kickstarts-README
Source2:    rpmfusion-remix-kickstarts-COPYING
Source10:   rpmfusion-nonfree-live-base.ks
Source11:   rpmfusion-nonfree-livecd-desktop.ks
Source12:   rpmfusion-nonfree-livecd-kde.ks
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -m644 %{SOURCE1} README
install -p -m644 %{SOURCE2} COPYING
install -t $RPM_BUILD_ROOT%{_datadir}/%{name}/ -p -m644 \
  %{SOURCE10}  \
  %{SOURCE11}  \
  %{SOURCE12}



%files
%doc COPYING README
%{_datadir}/%{name}/

%changelog
* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 22 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.28-1
- Update to 0.28

* Fri Sep 01 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.27-1
- Bump to 27

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.20.0-1
- Update to 20 final

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.20.0-0.1
- Update to 0.20.0
- Spec file clean-up

* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.18.0-0.1
- Update to 0.18.0

* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Sat Oct 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.16.0-0.1
- Update to 0.16.0

* Mon Jun 01 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-5
- add disabled repo definitions for f11 release

* Sun May 17 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-3
- rename to rpmfusion-free-remix-kickstarts and only include free bits

* Wed May 13 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-2
- package is GPLv3, not v2+
- s/remixes/remix/
- add a note about the version scheme

* Fri May 01 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-1
- initial version, based on spin-kickstarts from Fedora
