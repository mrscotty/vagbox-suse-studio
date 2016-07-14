#!/bin/bash
# Installing Oracle on SLES 11
#
# IMPORTANT: Due to the number of inodes needed, use a 20 GB storage image
# instead of just 10 GB on AWS.
#

set -x
# exit on error
set -e

if [ "$UID" == "0" ]; then
    SUDO=
else
    SUDO=sudo
fi

# Set up swapfile
if [ ! -f /var/swapfile ]; then
    $SUDO dd if=/dev/zero of=/var/swapfile bs=1024 count=1024000
    $SUDO /sbin/mkswap /var/swapfile
    $SUDO /sbin/swapon /var/swapfile
    echo "/var/swapfile none swap sw 0 0" | $SUDO tee -a /etc/fstab
    $SUDO /sbin/swapon -s
fi
#$SUDO /sbin/swapoff -v /dev/mapper/rootvg-swap_lv
#$SUDO /sbin/lvm lvresize /dev/mapper/rootvg-swap_lv -L 1405M
#$SUDO /sbin/mkswap /dev/mapper/rootvg-swap_lv
#$SUDO /sbin/swapon -va
#cat /proc/swaps


if [ ! -d /u01/app/oracle ]; then
#    $SUDO /sbin/lvcreate -L 2GB -n ora_lv rootvg
#    $SUDO /sbin/mkfs -t ext3 /dev/rootvg/ora_lv
    $SUDO mkdir -p /u01/app/oracle
#    echo "/dev/mapper/rootvg-ora_lv /u01/app/oracle ext3 defaults 0 0" | \
#        $SUDO tee -a /etc/fstab
#    $SUDO mount /u01/app/oracle
fi

if ! grep -q oracle /etc/group; then
    $SUDO /usr/sbin/groupadd dba
fi

if ! grep -q oracle /etc/passwd; then
    $SUDO /usr/sbin/useradd -d /u01/app/oracle -g dba oracle
fi

$SUDO chown oracle:dba /u01/app/oracle

if [ ! -f /vagrant/cache/oracle-xe-11.2.0-1.0.x86_64.rpm ]; then
    mkdir -p /vagrant/cache
    cd /vagrant/cache && \
        wget \
     https://s3.amazonaws.com/downloads.hnsc.de/misc/oracle-xe-11.2.0-1.0.x86_64.rpm.zip
    cd /vagrant/cache \
        && unzip oracle-xe-11.2.0-1.0.x86_64.rpm.zip \
        && mv Disk1/*.rpm . \
        && rm -rf Disk1
fi

$SUDO rpm -ivh /vagrant/cache/oracle-xe-11.2.0-1.0.x86_64.rpm

# Environment settings
ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
export ORACLE_HOME
LD_LIBRARY_PATH=$ORACLE_HOME/lib
export LD_LIBRARY_PATH

