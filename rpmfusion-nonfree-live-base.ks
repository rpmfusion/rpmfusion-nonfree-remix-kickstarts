# Make sure you read /usr/share/doc/rpmfusion-nonfree-remix-kickstarts*/README 
# before distributing a linux distribution that is build with this kickstart file
#
# Reminder: The RPM Fusion Nonfree repos depend on the Free repos; so you should
# include /usr/share/rpmfusion-free-remix-kickstarts/rpmfusion-free-live-base.ks
# directly or indirectly via some other "live" kickstart file from the package
# rpmfusion-free-remix-kickstarts in any kickstart files that include this file.
#
# Please note that the repos are configured to just track in 
# rpmfusion-nonfree-release and nothing else
#
## Reminder: enable and disable as well as modify following repos to make sure
## the repos match what is configured in fedora-live-base.ks

# To compose against the current release tree, use the following "repo"
repo --name=rpmfusion-nonfree --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-18&arch=$basearch --includepkgs=rpmfusion-nonfree-release
# To include updates, use the following "repo"
repo --name=rpmfusion-nonfree-updates --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-updates-released-18&arch=$basearch --includepkgs=rpmfusion-nonfree-release

# To compose against rawhide, use the following "repo"
#repo --name=rpmfusion-nonfree-rawhide --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-rawhide&arch=$basearch --includepkgs=rpmfusion-nonfree-release

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
rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 90ce094be31b30ca | awk ' { print $1 } ' | sort
echo "List of incuded RPM Fusion packages with their size:"
rpm -q --qf '%{SIZE} %{NAME}\n' $(rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 90ce094be31b30ca | awk ' { print $1 } ') | sort -n
echo
%end

