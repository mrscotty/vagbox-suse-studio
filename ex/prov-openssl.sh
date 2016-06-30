#!/bin/bash

set -e

export CFLAGS="-fPIC"
cd ~

if [ ! -f /vagrant/cache/openssl-1.0.1m.tar.gz ]; then
    mkdir -p /vagrant/cache
    cd /vagrant/cache && wget http://openssl.org/source/openssl-1.0.1m.tar.gz
fi

tar -xzf /vagrant/cache/openssl-1.0.1m.tar.gz
(cd ~/openssl-1.0.1m && ./config --prefix=/opt/myperl/ssl --openssldir=/opt/myperl/ssl shared)
(cd ~/openssl-1.0.1m && make depend all)
(cd ~/openssl-1.0.1m && sudo make install)

if [ -d /usr/local/lib ]; then
    sudo rmdir /usr/local/lib
fi
cd /usr/local && sudo ln -s lib64 lib


