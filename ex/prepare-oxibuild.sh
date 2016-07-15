#!/bin/bash
#
# This script automates the process of taking a virgin SuSE Studio
# OVF image and preparing it for Vagrant boxing.
#
# The VirtuaBox Guest Aditions CD must be "inserted" before execution.

set -e

basedir=$(dirname $0)
. $basedir/settings.rc

basedir=$(dirname $0)
$basedir/prov-ora.sh
$basedir/prov-openssl.sh
$basedir/prov-perlbrew.sh
$basedir/cleanbox-sles.sh

echo "You may now run $SUDO '/sbin/poweroff' to continue"
