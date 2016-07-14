#!/bin/bash
#
# cleanbox-sles.sh - Cleans SuSE SLES installation for vagrant reboxing
#
# This is run by a non-root user (e.g. vagrant)

set -e

if [ "$UID" == "0" ]; then
    SUDO=
else
    SUDO=sudo
fi

if [ ! -d ~/.rpmbuild ]; then
    mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
fi

if [ ! -f ~/.rpmmacros ]; then
    echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
fi

export CFLAGS="-fPIC"

$SUDO perl -i.bak -pe 's{LogLevel VERBOSE}{LogLevel INFO}' /etc/ssh/sshd_config
$SUDO perl -i.bak -pe 's{^(.+/dev/ttyS0)}{#$1}' /etc/syslog-ng/syslog-ng.conf

# Clean up init scripts
for i in S04nfs S08Rcm.c; do
    if [ -e /etc/init.d/rc3.d/$i ]; then
        $SUDO mv /etc/init.d/rc3.d/$i /etc/init.d/rc3.d/disabled-$i
    fi
    if [ -e /etc/init.d/rc5.d/$i ]; then
        $SUDO mv /etc/init.d/rc5.d/$i /etc/init.d/rc3.d/disabled-$i
    fi
done

# Clean up logs
$SUDO rm -rf /var/log/*.gz
for i in lastlog warn messages; do
    $SUDO tee /var/log/$i < /dev/null
done

# Clean up homes
> ~/.bash_history && history -c && exit

