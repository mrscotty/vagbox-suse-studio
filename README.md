# Building Vagrant Boxes From Suse Studio

    https://susestudio.com

Strategy: create an initial base box from the Suse Studio
and then customize locally with reboxing vagrant.

This documents the creation of a common vagrant box for building
OpenXPKI packages on SuSE SLES 11 SP3. It uses the following
packages from build.opensuse.org:

    myperl, myperl-buildtools, myperl-fcgi

Note: other myperl RPMs are also available at the build server

    http://download.opensuse.org/repositories/home:/mrscotty/SLE_11_SP3/

Unfortunately, the myperl-dbi-oracle is NOT available there because the
prerequisites (i.e. Oracle) is not publicly available as an RPM.

With this image, you should be able to build the following packages:

    myperl-dbi-oracle
    myperl-openxpki-*

## Creating the Starting Vagrant Box

### Creating an Appliance

* Create appliance on SuSE Studio from SLES 11 SP3
* Increase disk size to 30 GB
* Increase swap partition to 1200 MB
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
    * myperl, myperl-buildtools, myperl-fcgi
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

* Build
* Create "VMware Workstation / VirtualBox (.vmdk)" image
* Download new image

    tar xzf ~/Downloads/oxibuild_myperl_SLES_11_SP3.x86_64-0.0.4.vmx.tar.gz

### Import into VirtualBox

* Import the OVF File
    * Rename to 'oxibuild-myperl-sles11sp3'
    * Add CDROM virtual drive
* Power on the virtual machine

### Modify Image for Vagrant

* Accept EULA
* Login as root/linux
* Insert VirtualBox Tools CD and run the following:

    sudo mount /dev/cdrom /mnt
    sudo /mnt/VBoxLinuxAdditions.run
    sudo /sbin/poweroff

### Create New Vagrant Box

* Create the vagrant box (replace 'vm' with the name in VirtualBox):

    vagrant package --base vm
    vagrant add --force sles11sp3 package.box

## Customizing Vagrant Box

This is based on the initial vagrant box directly imported from Suse Studio.

First, get the vag-scripts...

    git clone gitolite@83.141.25.44:users/scotty/vag-scripts

Generate customized box from initial box...

    ./rebox-sles.sh
