#!/bin/bash

set -x
set -e

curl -L https://install.perlbrew.pl | bash
source ~/perl5/perlbrew/etc/bashrc
echo "source ~/perl5/perlbrew/etc/bashrc" >> ~/.profile
latest=$(perlbrew available | head -n 1)
perlbrew --notest install perl-stable
perlbrew switch $(perlbrew list | head -n 1)
perlbrew install-cpanm

cpanm Class::Std Config::Std Test::LeakTrace Template

