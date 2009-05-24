# Make sure you read /usr/share/doc/rpmfusion-nonfree-remix-kickstarts*/README 
# before distributing a linux distribution that is build with this kickstart file
#
# Reminder: The RPM Fusion Nonfree repos depend on the Free repos; so you should
# include /usr/share/rpmfusion-free-remix-kickstarts/rpmfusion-free-live-base.ks
# directly or indirectly via some other "live" kickstart file from the package
# rpmfusion-free-remix-kickstarts in any kickstart files that include this file.

# enable and use RPM Fusion nonfree
repo --name=rpmfusion-nonfree-rawhide --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-rawhide&arch=$basearch

%packages
# unbrand; should be done by rpmfusion-free-live-base.ks, but we do it here as
# well just to be sure
-fedora-release
-fedora-logos
-fedora-release-notes
generic-release
generic-logos
generic-release-notes
%end

%post
echo "== RPM Fusion Nonfree: Base section =="
echo "Importing RPM Fusion keys"
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-*-primary
echo "List of packages from RPM Fusion Nonree:"
rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 206f8182b1981b68 -e 4d2a1bdc8dc43844 | awk ' { print $1 } ' | sort
echo "List of incuded RPM Fusion packages with their size:"
rpm -q --qf '%{SIZE} %{NAME}\n' $(rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 206f8182b1981b68 -e 4d2a1bdc8dc43844 | awk ' { print $1 } ') | sort -n
echo
%end

