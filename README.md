# Building Vagrant Boxes From Suse Studio

    https://susestudio.com

Strategy: create an initial base box from the Suse Studio
and then customize locally with reboxing vagrant.

This documents the creation of a common vagrant box for building
OpenXPKI packages on SuSE SLES 11 SP3.

With this image, you should be able to build the following packages:

    myperl, myperl-buildtools
    myperl-dbi, myperl-fcgi
    myperl-dbi-oracle
    myperl-openxpki-*

The entire process can be broken down into the following tasks:

* Creating the initial appliance (OVF image) on Suse Studio
* Importing in VirtualBox and adding Guest Additions
* Creating a base vagrant box from the VirtualBox image
* Re-boxing the vagrant box with remaining prerequisites for myperl / openxpki

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

    tar xzf ~/Downloads/oxibuild_myperl_SLES_11_SP3.x86_64-0.0.4.vmx.tar.gz

# Import into VirtualBox and add Guest Additions

* Import the OVF File as a new VM named "vm" (the default name)
    * Add CDROM virtual drive (leave empty)
* Power on the virtual machine
* Accept EULA
* Login as root/linux
* Insert VirtualBox Tools CD and run the following:

    mount /dev/cdrom /mnt
    /mnt/VBoxLinuxAdditions.run
    /sbin/poweroff

# Create Base Vagrant Box From VirtualBox Image

* Create the vagrant box (replace 'vm' with the name in VirtualBox):

    rm package.box
    vagrant package --base vm
    vagrant box add --force mrscotty/sles11sp3 package.box

# Re-package Vagrant Box With Prerequisites for myperl / openxpki

This is based on the initial vagrant box created in the steps above.

Generate customized box from initial box...

    ./rebox-sles.sh
