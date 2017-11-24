%define pkgname myperl-openxpki-core-deps
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 0
%define __perl /opt/myperl/bin/perl

name:      %{pkgname}
summary:   OpenXPKI Core Perl CPAN dependencies packaged for myperl
version:   1.19

release:   1

vendor:    OpenXPKI Project
packager:  Scott Hardin <scott@hnsc.de>
license:   Apache
group:     Applications/CPAN
url:       http://www.openxpki.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
prefix:    %(echo %{_prefix})
BuildRequires: myperl libexpat-devel
Requires: myperl libexpat1
# Some local installations are complicated and don't have the various prereqs declared
# correctly. So we need to disable the automatic prereq checking.
AutoReqProv: no

source:    develop.tar.gz

%description
OpenXPKI Core Perl CPAN dependencies packaged for myperl

Packaging information:
OpenXPKI version       1.19
Git commit hash:       
Git description:       
Git tags:              <no tag set>

%prep
%setup -q -n develop

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
set -e

PERL=%{__perl}

VENDORLIB=`%{__perl} "-V:vendorlib" | awk -F\' '{print $2}'`
VENDORARCH=`%{__perl} "-V:vendorarch" | awk -F\' '{print $2}'`
VENDORLIBEXP=%{buildroot}/`%{__perl} "-V:vendorlibexp" | awk -F\' '{print $2}'`
ARCHNAME=`%{__perl} "-V:archname" | awk -F\' '{print $2}'`
ARCHLIB=`%{__perl} "-V:archlib" | awk -F\' '{print $2}'`
VENDORMAN1EXP=`%{__perl} "-V:vendorman1direxp" | awk -F\' '{print $2}'`
VENDORMAN3EXP=`%{__perl} "-V:vendorman3direxp" | awk -F\' '{print $2}'`
VENDORSCRIPTEXP=`%{__perl} "-V:vendorscriptexp" | awk -F\' '{print $2}'`
PRIVLIB=`%{__perl} "-V:privlib" | awk -F\' '{print $2}'`
CPANM=/opt/myperl/bin/cpanm
CPANM_OPTS="--notest --skip-satisfied --skip-installed --verbose $CPANM_MIRROR"

# Environment vars neede for proper Perl module installation
export PERL5LIB=%{buildroot}/$VENDORARCH:%{buildroot}/$VENDORLIB
export PERL_MB_OPT="--destdir '%{buildroot}' --installdirs vendor"
export PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR=%{buildroot}"
# Keep Module::Install from trying to install stuff itself using cpanplus or cpan
export PERL_AUTOINSTALL="--skip"
export DESTDIR="%{buildroot}"

$CPANM $CPANM_OPTS Class::Std Config::Std
echo "DEBUG: current directory = `pwd`"
echo "DEBUG: contents of current directory:"
ls -la
echo "DEBUG: end of list"
echo "DEBUG: PATH=$PATH"
echo "DEBUG: using PERL=$PERL"
# KLUDGE: IO::Socket::SSL not installing corectly when
# picked up by cpanm as prereq of LDAP
$CPANM $CPANM_OPTS IO::Socket::SSL

echo "DEBUG: check whether IO::Socket::SSL loads"
%{__perl} -V
%{__perl} -e 'my $mod = "IO::Socket::SSL";my $file = "IO/Socket/SSL.pm"; local $@; warn eval { require $file } || ($@ ? "-- $@ --" : "0");'
%{__perl} -e 'my $mod = "IO::Socket::SSL";my $file = "IO/Socket/SSL.pm"; local $@; warn eval { require $file; $mod->VERSION } || ($@ ? "-- $@ --" : "0");'
(cd core/server && PERL_AUTOINSTALL=--skip PERL5LIB=$PERL5LIB $CPANM $CPANM_OPTS --installdeps .)

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

## SuSE Linux
#if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
#then
#    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
#    find %{buildroot} -name "perllocal.pod"  \
#        -exec '%{__sed} -e s+%{buildroot}++g {}' \;                 \
#        > %{buildroot}/var/adm/perl-modules/%{name}
#fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs rm -f

# myperl issue #2 - until I can get Pinto running, just remove the offending files
# DESTDIR = %{buildroot}

# This kludge automates the above explicit listing of files...
rpm -ql myperl myperl-buildtools \
    | perl -ne "chomp; print \"$DESTDIR/\$_ \" if -f \"$DESTDIR\$_\";" \
    | xargs rm -f

# TODO: SOAPsh.pl has /bin/env in shebang, which causes a dependency
# problem when rpm searches for automatic dependencies
perl -i -p -e 's{#!/bin/env}{#!/usr/bin/env}' $DESTDIR/$VENDORSCRIPTEXP/SOAPsh.pl

# no empty directories
#find %{buildroot}%{_prefix}             \
#    -type d -depth                      \
#    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    #print "%doc  README.md";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share /srv /var |;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

#%attr(0755,root,openxpki) /srv/www/openxpki/mason-data

%changelog
* Mon Sep 14 2015 scott@hnsc.de
- update for myperl-5.22.0


