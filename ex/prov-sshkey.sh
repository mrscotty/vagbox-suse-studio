#!/bin/bash
# Installing Vagrant SSH Key
#

set -x
# exit on error
set -e

basedir=$(dirname $0)
. $basedir/settings.rc

if [ ! -d ~vagrant/.ssh ]; then
    mkdir ~vagrant/.ssh
fi

if [ ! -f ~vagrant/.ssh/authorized_keys ]; then
    wget -O ~vagrant/.ssh/authorized_keys \
        https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub
    $SUDO chmod 0700 ~vagrant/.ssh
    $SUDO chmod 0600 ~vagrant/.ssh/authorized_keys
fi


