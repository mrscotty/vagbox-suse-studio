#!/bin/bash
#
# This script automates the process of taking a virgin SuSE Studio
# OVF image and preparing it for Vagrant boxing.
#
# The VirtuaBox Guest Aditions CD must be "inserted" before execution.

set -e

mount /dev/cdrom /mnt
/mnt/VBoxLinuxAdditions.run
umount /mnt

dirname=$(dirname $0)
$dirname/prov-ora.sh
$dirname/prov-openssl.sh
$dirname/prov-perlbrew.sh
$dirname/cleanbox-sles.sh

echo "You may now run '/sbin/poweroff' to continue"
