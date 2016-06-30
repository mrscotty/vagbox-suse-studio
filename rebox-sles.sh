#!/bin/bash

set -e

basebox=mrscotty/sles11sp3
destbox=mrscotty/sles11sp3-oxibuild
destpkg=mrscotty-sles11sp3-oxibuild.box

if [ ! -f Vagrantfile ]; then
    vagrant init $basebox
fi

if [ -f .vagrant/machines/default/virtualbox/id ]; then
    vagrant destroy -f
fi

vagrant up
vagrant ssh --command "/vagrant/ex/prov-ora.sh"
vagrant ssh --command "/vagrant/ex/prov-openssl.sh"
vagrant ssh --command "/vagrant/ex/prov-perlbrew.sh"
vagrant ssh --command "/vagrant/ex/cleanbox-sles.sh"

if [ -e $destpkg ]; then
    rm $destpkg
fi
vagrant package --output $destpkg
if  vagrant box list | grep -q $destbox; then
    vagrant box remove $destbox
fi
vagrant --force box add $destbox $destpkg
