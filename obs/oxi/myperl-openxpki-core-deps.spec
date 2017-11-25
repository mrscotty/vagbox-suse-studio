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
buildroot: %{_tmppath}/%{name}-%{version}
prefix:    %{_prefix}
#BuildRequires: myperl libexpat-devel
BuildRequires: myperl
#Requires: myperl libexpat1 myperl-buildtools
Requires: myperl myperl-buildtools
# Some local installations are complicated and don't have the various prereqs declared
# correctly. So we need to disable the automatic prereq checking.
AutoReqProv: no

Source0: https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-0.60.tar.gz
Source1: https://cpan.metacpan.org/authors/id/J/JH/JHI/Time-HiRes-1.9746.tar.gz
Source2: https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-0.99.tar.gz
Source3: https://cpan.metacpan.org/authors/id/P/PH/PHRED/SOAP-Lite-1.22.tar.gz
Source4: https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Pod-1.51.tar.gz
Source5: https://cpan.metacpan.org/authors/id/M/MA/MANU/Net-IP-1.26.tar.gz
Source6: https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-1.999811.tar.gz
Source7: https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-Simple-2.24.tar.gz
Source8: https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-1.13.tar.gz
Source9: https://cpan.metacpan.org/authors/id/A/AB/ABW/Template-Toolkit-2.27.tar.gz
Source10: https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-4.37.tar.gz
Source11: https://cpan.metacpan.org/authors/id/N/NE/NEKOKAK/DBIx-TransactionManager-1.13.tar.gz
Source12: https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Net-HTTP-6.17.tar.gz
Source13: https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Class-Std-0.013.tar.gz
Source14: https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Switch-2.17.tar.gz
Source15: https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Class-Accessor-Chained-0.01.tar.gz
Source16: https://cpan.metacpan.org/authors/id/M/MR/MRSCOTTY/Connector-1.23.tar.gz
Source17: https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
Source18: https://cpan.metacpan.org/authors/id/T/TI/TIMB/Devel-NYTProf-6.04.tar.gz
Source19: https://cpan.metacpan.org/authors/id/T/TT/TTAR/Crypt-OpenSSL-AES-0.02.tar.gz
Source20: https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-2017060201.tar.gz
Source21: https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Path-Class-0.37.tar.gz
Source22: https://cpan.metacpan.org/authors/id/L/LD/LDS/Crypt-CBC-2.33.tar.gz
Source23: https://cpan.metacpan.org/authors/id/B/BE/BENNING/LWP-Protocol-connect-6.09.tar.gz
Source24: https://cpan.metacpan.org/authors/id/A/AN/ANDYA/IPC-ShareLite-0.17.tar.gz
Source25: https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/XML-Validator-Schema-1.10.tar.gz
Source26: https://cpan.metacpan.org/authors/id/D/DI/DICHI/DBD-Mock/DBD-Mock-1.45.tar.gz
Source27: https://cpan.metacpan.org/authors/id/P/PD/PDWARREN/Mail-RFC822-Address-0.3.tar.gz
Source28: https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Config-Merge-1.04.tar.gz
Source29: https://cpan.metacpan.org/authors/id/L/LB/LBAXTER/Sys-SigAction-0.23.tar.gz
Source30: https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-2.97000.tar.gz
Source31: https://cpan.metacpan.org/authors/id/R/RA/RAZINF/Data-Password-1.12.tar.gz
Source32: https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Log-Log4perl-1.49.tar.gz
Source33: https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-1.34.tgz
Source34: https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Session-4.48.tar.gz
Source35: https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-Fast-2.13.tar.gz
Source36: https://cpan.metacpan.org/authors/id/T/TL/TLHACKQUE/Crypt-PKCS10-1.800201.tar.gz
Source37: https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-2.2008.tar.gz
Source38: https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.07.tar.gz
Source39: https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/MIME-tools-5.509.tar.gz
Source40: https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-1.10.tar.gz
Source41: https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-Params-Validate-0.21.tar.gz
Source42: https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz
Source43: https://cpan.metacpan.org/authors/id/B/BR/BRICKER/Config-Std-0.903.tar.gz
Source44: https://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-6.29.tar.gz
Source45: https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/IO-Prompt-0.997004.tar.gz
Source46: https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz
Source47: https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Workflow-1.45.tar.gz
Source48: https://cpan.metacpan.org/authors/id/B/BI/BILBO/Proc-SafeExec-1.5.tar.gz
Source49: https://cpan.metacpan.org/authors/id/S/SH/SHAY/perl-5.26.1.tar.bz2
Source50: https://cpan.metacpan.org/authors/id/D/DA/DAMI/SQL-Abstract-More-1.30.tar.gz
Source51: https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-Filter-XInclude-1.0.tar.gz
Source52: https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-0.05.tar.gz
Source53: https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-SAX-Writer-0.57.tar.gz
Source54: https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-0.99.tar.gz
Source55: https://cpan.metacpan.org/authors/id/K/KA/KARUPA/DBIx-Handler-0.14.tar.gz
Source56: https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.53.tar.gz
Source57: https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302113.tar.gz
Source58: https://cpan.metacpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-2.052.tar.gz
Source59: https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/Net-Server-2.009.tar.gz
Source60: https://cpan.metacpan.org/authors/id/M/MA/MARSCHAP/perl-ldap-0.65.tar.gz
Source61: https://cpan.metacpan.org/authors/id/N/NA/NANIS/Crypt-SSLeay-0.72.tar.gz
Source62: https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-UUID-1.221.tar.gz
Source63: https://cpan.metacpan.org/authors/id/G/GU/GUIDO/libintl-perl-1.29.tar.gz


%description
OpenXPKI Core Perl CPAN dependencies packaged for myperl

Packaging information:
OpenXPKI version       1.19
Git commit hash:       
Git description:       
Git tags:              <no tag set>

%prep
#%setup -q -n develop
%setup

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

#$CPANM $CPANM_OPTS Class::Std Config::Std
echo "DEBUG: current directory = `pwd`"
echo "DEBUG: contents of current directory:"
ls -la
echo "DEBUG: end of list"
echo "DEBUG: PATH=$PATH"
echo "DEBUG: using PERL=$PERL"
# KLUDGE: IO::Socket::SSL not installing corectly when
# picked up by cpanm as prereq of LDAP
#$CPANM $CPANM_OPTS IO::Socket::SSL

$PERL $CPANM $CPANM_OPTS %{Source0}
$PERL $CPANM $CPANM_OPTS %{Source1}
$PERL $CPANM $CPANM_OPTS %{Source2}
$PERL $CPANM $CPANM_OPTS %{Source3}
$PERL $CPANM $CPANM_OPTS %{Source4}
$PERL $CPANM $CPANM_OPTS %{Source5}
$PERL $CPANM $CPANM_OPTS %{Source6}
$PERL $CPANM $CPANM_OPTS %{Source7}
$PERL $CPANM $CPANM_OPTS %{Source8}
$PERL $CPANM $CPANM_OPTS %{Source9}
$PERL $CPANM $CPANM_OPTS %{Source10}
$PERL $CPANM $CPANM_OPTS %{Source11}
$PERL $CPANM $CPANM_OPTS %{Source12}
$PERL $CPANM $CPANM_OPTS %{Source13}
$PERL $CPANM $CPANM_OPTS %{Source14}
$PERL $CPANM $CPANM_OPTS %{Source15}
$PERL $CPANM $CPANM_OPTS %{Source16}
$PERL $CPANM $CPANM_OPTS %{Source17}
$PERL $CPANM $CPANM_OPTS %{Source18}
$PERL $CPANM $CPANM_OPTS %{Source19}
$PERL $CPANM $CPANM_OPTS %{Source20}
$PERL $CPANM $CPANM_OPTS %{Source21}
$PERL $CPANM $CPANM_OPTS %{Source22}
$PERL $CPANM $CPANM_OPTS %{Source23}
$PERL $CPANM $CPANM_OPTS %{Source24}
$PERL $CPANM $CPANM_OPTS %{Source25}
$PERL $CPANM $CPANM_OPTS %{Source26}
$PERL $CPANM $CPANM_OPTS %{Source27}
$PERL $CPANM $CPANM_OPTS %{Source28}
$PERL $CPANM $CPANM_OPTS %{Source29}
$PERL $CPANM $CPANM_OPTS %{Source30}
$PERL $CPANM $CPANM_OPTS %{Source31}
$PERL $CPANM $CPANM_OPTS %{Source32}
$PERL $CPANM $CPANM_OPTS %{Source33}
$PERL $CPANM $CPANM_OPTS %{Source34}
$PERL $CPANM $CPANM_OPTS %{Source35}
$PERL $CPANM $CPANM_OPTS %{Source36}
$PERL $CPANM $CPANM_OPTS %{Source37}
$PERL $CPANM $CPANM_OPTS %{Source38}
$PERL $CPANM $CPANM_OPTS %{Source39}
$PERL $CPANM $CPANM_OPTS %{Source40}
$PERL $CPANM $CPANM_OPTS %{Source41}
$PERL $CPANM $CPANM_OPTS %{Source42}
$PERL $CPANM $CPANM_OPTS %{Source43}
$PERL $CPANM $CPANM_OPTS %{Source44}
$PERL $CPANM $CPANM_OPTS %{Source45}
$PERL $CPANM $CPANM_OPTS %{Source46}
$PERL $CPANM $CPANM_OPTS %{Source47}
$PERL $CPANM $CPANM_OPTS %{Source48}
$PERL $CPANM $CPANM_OPTS %{Source49}
$PERL $CPANM $CPANM_OPTS %{Source50}
$PERL $CPANM $CPANM_OPTS %{Source51}
$PERL $CPANM $CPANM_OPTS %{Source52}
$PERL $CPANM $CPANM_OPTS %{Source53}
$PERL $CPANM $CPANM_OPTS %{Source54}
$PERL $CPANM $CPANM_OPTS %{Source55}
$PERL $CPANM $CPANM_OPTS %{Source56}
$PERL $CPANM $CPANM_OPTS %{Source57}
$PERL $CPANM $CPANM_OPTS %{Source58}
$PERL $CPANM $CPANM_OPTS %{Source59}
$PERL $CPANM $CPANM_OPTS %{Source60}
$PERL $CPANM $CPANM_OPTS %{Source61}
$PERL $CPANM $CPANM_OPTS %{Source62}
$PERL $CPANM $CPANM_OPTS %{Source63}



echo "DEBUG: check whether IO::Socket::SSL loads"
%{__perl} -V
%{__perl} -e 'my $mod = "IO::Socket::SSL";my $file = "IO/Socket/SSL.pm"; local $@; warn eval { require $file } || ($@ ? "-- $@ --" : "0");'
%{__perl} -e 'my $mod = "IO::Socket::SSL";my $file = "IO/Socket/SSL.pm"; local $@; warn eval { require $file; $mod->VERSION } || ($@ ? "-- $@ --" : "0");'
#(cd core/server && PERL_AUTOINSTALL=--skip PERL5LIB=$PERL5LIB $CPANM $CPANM_OPTS --installdeps .)

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


