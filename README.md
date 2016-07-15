# Building Vagrant Boxes From Suse Studio

This document and set of helper scripts is used to create Vagrant
boxes from base appliances created on Suse Studio [https://susestudio.com].

## Background

The licensing for using SLES 11 restricts access to RPM repositories unless
you have a paid subscription. Since I build RPMs for an open source project,
I'd rather not have the additional expenses, but I'd still like to use a
real SLES 11 for creating the RPMs (rather than building on OpenSUSE).

In my workflow, the appliance is customized locally and boxed in vagrant.
With Suse Studio, I can specify all the packages when I create the OVF 
image and then use the resulting image in my Vagrant workflow. If I ever
need new RPMs from SuSE, I just re-create the original base appliance.

## Next Steps

This documents the creation of a vagrant box for building
OpenXPKI packages on SuSE SLES 11 SP3.

With this image, you should be able to build the following packages:

    myperl, myperl-buildtools
    myperl-dbi, myperl-fcgi
    myperl-dbi-oracle
    myperl-openxpki-*

The entire process can be broken down into the following tasks:

* Creating the initial appliance (OVF image) on Suse Studio
* Importing in VirtualBox and adding Guest Additions
* Creating a vagrant box from the VirtualBox image with the needed prereqs

The contents of this repository are:

* ex/       scripts used to do the dirty work
* cache/    location of cached files (i.e. openssl tarball, oracle rpm)

# Creating the Initial Appliance (OVF Image)

NOTE: To skip configuring the appliance manually, just visit the
following page to download the preconfigured appliance:

    https://susestudio.com/u/shardin
    https://susestudio.com/a/Asu0Ke/oxi-build-sles-11-sp3

At https://susestudio.com, login and navigate to your main account page. Then,
do the following steps:

* Create appliance on SuSE Studio from SLES 11 SP3
* Increase disk size to 30 GB
* Add vagrant customize block to build script
* Add home:mrscotty Open Build Service to list of repositories
* Add additional RPMs
    * bc
    * gcc
    * gettext-tools
    * git, git-core
    * kernel-default-devel
    * libexpat1, libexpat-devel
    * libmysqlclient-devel
    * make
    * sudo
    * unzip
    * zlib-devel
* Add vagrant user (password = 'vagrant')
* Change root password to 'vagrant'
* Select default format "OVF Virtual Machine / ESXi (.ovf)"
* Add vagrant.pub as file to be pulled from
    https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub
* Add the following to the build script:

    ##################################################
    # Customizations for vagrant
    ##################################################

    # SSH authorized keys
    mkdir -p ~vagrant/.ssh
    cp /vagrant.pub ~vagrant/.ssh/authorized_keys
    chown -R vagrant ~vagrant/.ssh
    chmod 0700 ~vagrant/.ssh
    chmod 0600 ~vagrant/.ssh/authorized_keys

    # Configure SSH Daemon:
    echo "UseDNS no" >> /etc/ssh/sshd_config

    # Configure Sudo:
    echo "vagrant ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

    # NOTE: This disables the EULA display and prompt for the user.
    # Disabling this allows us to import the box into the vagrant
    # environment automatically.
    #rm /etc/init.d/suse_studio_firstboot

* Build
* Create "VMware Workstation / VirtualBox (.vmdk)" image
* Download new image

    # Note: replace version number with latest version
    tar xzf ~/Downloads/oxibuild_myperl_SLES_11_SP3.x86_64-0.0.4.vmx.tar.gz

# Import into VirtualBox and add Guest Additions

* Import the OVF File as a new VM named "vm" (the default name)
    * Add CDROM virtual drive (leave empty)
    * Add an auto-mounted share folder for the current directory that
      mounts at "suse-studio"
* Power on the virtual machine
* Accept EULA
* Login as vagrant/vagrant
* From the VirtualBox menu "Devices", click "Insert VirtualBox Tools CD"
* Run the following:

    sudo mount /dev/cdrom /mnt
    sudo /mnt/VBoxLinuxAdditions.run
    sudo umount /mnt

To prepare the image with prerequisites for myperl / openxpki builds:

    /media/sf_suse-studio/ex/prepare-oxibuild.sh

# Create Vagrant Box From VirtualBox Image

* Create the vagrant box (replace 'vm' with the name in VirtualBox):

    rm -f package.box
    vagrant package --base vm
    vagrant box add --force mrscotty/sles11sp3-oxibuild package.box
    mv package.box mrscotty-sles11sp3-oxibuild-v3.box
    shasum mrscotty-sles11sp3-oxibuild-v3.box \
        > mrscotty-sles11sp3-oxibuild-v3.box.sha1

