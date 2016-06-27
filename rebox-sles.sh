#!/bin/bash

set -x
set -e

basebox=sles11sp3
destbox=sles11sp3-oxibuild

if [ ! -f Vagrantfile ]; then
    vagrant init $basebox
fi

exit

if [ -f .vagrant/machines/default/virtualbox/id ]; then
    vagrant destroy -f
fi

vagrant up
#vagrant ssh --command "sudo /sbin/lvm lvresize /dev/mapper/rootvg-home_lv -L 1G"
#vagrant ssh --command "sudo /sbin/resize2fs /dev/mapper/rootvg-home_lv"
#vagrant ssh --command "sudo rpm -ivh /vagrant/rpms/*.rpm"
#vagrant ssh --command "/vagrant/prov-perlbrew.sh"
#vagrant ssh --command "/vagrant/cleanbox-sles.sh"
vagrant ssh --command "/vagrant/vag-scripts/ex/prov-ora.sh"
vagrant ssh --command "/vagrant/vag-scripts/ex/prov-openssl.sh"
vagrant ssh --command "perl - --sudo App::cpanminus < /vagrant/vag-scripts/ex/prov-cpanm.sh"
vagrant ssh --command "/vagrant/vag-scripts/ex/prov-perl.sh"

if [ -e $boxname.box ]; then
    rm $boxname.box
fi
vagrant package --output $boxname.box
if  vagrant box list | grep -q $boxname; then
    vagrant box remove $boxname
fi
vagrant --force box add $boxname $boxname.box
