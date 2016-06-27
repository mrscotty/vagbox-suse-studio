# Building Vagrant Boxes From Suse Studio

    https://susestudio.com

# Creating an Appliance

* Create appliance on SuSE Studio from SLES 11 SP3
* Increase disk size to 30 GB
* Increase swap partition to 1200 MB
* Add vagrant customize block to build script
* Add home:mrscotty Open Build Service to list of repositories
* Add additional RPMs
    * sudo
    * kernel-default-devel
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

# Import into VirtualBox

* Import the OVF File
    * Rename to 'oxibuild-myperl-sles11sp3'
    * Add CDROM virtual drive
* Power on the virtual machine

# Modify Image for Vagrant

* Accept EULA
* Login as root/linux
* Get MAC address of first network interface

    /sbin/ifconfig eth0 | grep HWaddr

    This will be put in Vagrantfile as "config.vm.base_mac"
    
* Insert VirtualBox Tools CD and run the following:

    sudo mount /dev/cdrom /mnt
    sudo /mnt/VBoxLinuxAdditions.run

