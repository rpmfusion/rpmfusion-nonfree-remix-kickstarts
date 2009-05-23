# Make sure you read /usr/share/doc/rpmfusion-nonfree-remix-kickstarts*/README 
# before distributing a linux distribution that is build with this kickstart file
#
%include ../rpmfusion-free-remix-kickstarts/rpmfusion-free-livecd-kde.ks
%include rpmfusion-nonfree-live-base.ks

# override repo definition from rpmfusion-nonfree-live-base.ks to make sure we
# get only rpmfusion-nonfree-release from the repo
repo --name=rpmfusion-nonfree-rawhide --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-rawhide&arch=$basearch --includepkgs=rpmfusion-nonfree-release
