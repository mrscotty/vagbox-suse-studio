#!/bin/bash
#
# This script automates the process of taking a virgin SuSE Studio
# OVF image and preparing it for Vagrant boxing.
#
# The VirtuaBox Guest Aditions CD must be "inserted" before execution.

set -e

if [ "$UID" == "0" ]; then
    SUDO=
else
    SUDO=sudo
fi

$SUDO mount /dev/cdrom /mnt
$SUDO /mnt/VBoxLinuxAdditions.run
$SUDO umount /mnt

dirname=$(dirname $0)
$dirname/prov-ora.sh
$dirname/prov-openssl.sh
$dirname/prov-perlbrew.sh
$dirname/cleanbox-sles.sh

echo "You may now run $SUDO '/sbin/poweroff' to continue"
