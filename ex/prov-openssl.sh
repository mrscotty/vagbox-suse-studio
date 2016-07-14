#!/bin/bash

set -e

if [ "$UID" == "0" ]; then
    SUDO=
else
    SUDO=sudo
fi

export CFLAGS="-fPIC"
cd ~

if [ -d /vagrant ]; then
    CACHEDIR=/vagrant/cache
else
    CACHEDIR=~/cache
fi

if [ ! -f $CACHEDIR/openssl-1.0.1m.tar.gz ]; then
    mkdir -p $CACHEDIR
    cd $CACHEDIR && wget http://openssl.org/source/openssl-1.0.1m.tar.gz
fi

tar -xzf $CACHEDIR/openssl-1.0.1m.tar.gz
(cd ~/openssl-1.0.1m && ./config --prefix=/opt/myperl/ssl --openssldir=/opt/myperl/ssl shared)
(cd ~/openssl-1.0.1m && make depend all)
(cd ~/openssl-1.0.1m && $SUDO make install)

if [ -d /usr/local/lib ]; then
    $SUDO rmdir /usr/local/lib
fi
cd /usr/local && $SUDO ln -s lib64 lib


