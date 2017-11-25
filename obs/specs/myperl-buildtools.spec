## Written 2006 by Martin Bartosch for the OpenXPKI project
## Adapted for myperl-dbd-mysql by Scott Hardin
## Copyright (C) 2005-2014 by The OpenXPKI Project

%define pkgname myperl-buildtools
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 0
%define __perl /opt/myperl/bin/perl

name:      %{pkgname}
summary:   myperl build tools
version:   5.26.0

release: 1

vendor:    OpenXPKI Project
packager:  Scott Hardin <scott@hnsc.de>
license:   Apache
group:     Applications/CPAN
url:       http://www.openxpki.org
buildroot: %{_tmppath}/%{name}-%{version}
prefix:    %{_prefix}
BuildRequires: myperl
Requires: myperl
# The auto-prereq code picks up libexpat.so.0, but this is not explicitly
# supplied by the libexpat1 SLES package.
AutoReqProv: no
#source:    %{pkgname}-%{version}.tar.gz

Source1:    https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4224.tar.gz
Source2:    https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Class-Std-0.013.tar.gz
Source3:    https://cpan.metacpan.org/authors/id/B/BR/BRICKER/Config-Std-0.903.tar.gz
Source4:    https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
Source5:    https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302113.tar.gz
Source6:    https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.127.tar.gz


%description
Various CPAN modules needed for building other myperl packages

Packaging information:
myperl version         5.26.0
Git commit hash:       
Git description:       
Git tags:              <no tag set>

%prep

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

PERL=%{__perl}

VENDORLIB=`%{__perl} "-V:vendorlib" | awk -F\' '{print $2}'`
VENDORARCH=`%{__perl} "-V:vendorarch" | awk -F\' '{print $2}'`
VENDORLIBEXP=%{buildroot}/`%{__perl} "-V:vendorlibexp" | awk -F\' '{print $2}'`
ARCHNAME=`%{__perl} "-V:archname" | awk -F\' '{print $2}'`
ARCHLIB=`%{__perl} "-V:archlib" | awk -F\' '{print $2}'`
PRIVLIB=`%{__perl} "-V:privlib" | awk -F\' '{print $2}'`
CPANM=/opt/myperl/bin/cpanm
CPANM_OPTS="--notest --skip-satisfied --skip-installed --verbose $CPANM_MIRROR"

# Environment vars neede for proper Perl module installation
export PERL5LIB=%{buildroot}/$VENDORARCH:%{buildroot}/$VENDORLIB
export PERL_MB_OPT="--destdir '%{buildroot}' --installdirs vendor"
export PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='%{buildroot}' NO_META=true NO_MYMETA=true"
#export DESTDIR="%{buildroot}"

SOURCEDIR=%{_sourcedir}
# ExtUtils::MakeMaker needs to be 'forced' since an older version
# is already installed
#$CPANM --notest --verbose ExtUtils::MakeMaker
#$CPANM $CPANM_OPTS Config::Std Test::NoWarnings Test::Tester Test::Deep

#$PERL $CPANM $CPANM_OPTS %{SOURCE1}
$PERL $CPANM $CPANM_OPTS %{SOURCE2}
$PERL $CPANM $CPANM_OPTS %{SOURCE3}
$PERL $CPANM $CPANM_OPTS %{SOURCE4}
#$PERL $CPANM $CPANM_OPTS %{SOURCE5}
$PERL $CPANM $CPANM_OPTS %{SOURCE6}


cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# remove files that conflict with myperl base package
echo "INFO: cleaning duplicate files from %{buildroot}%{_prefix}"
(cd %{buildroot} && rm -f \
    opt/myperl/bin/config_data \
    opt/myperl/bin/instmodsh \
    opt/myperl/man/man1/config_data.1 \
    opt/myperl/man/man1/instmodsh.1 \
    opt/myperl/man/man3/CPAN::*.3 \
    opt/myperl/man/man3/ExtUtils::*.3 \
    opt/myperl/man/man3/Module::Build*.3 \
    opt/myperl/man/man3/Test::Builder*.3 \
    opt/myperl/man/man3/Test::More.3 \
    opt/myperl/man/man3/Test::Simple.3 \
    opt/myperl/man/man3/Test::Tutorial.3 )


%{__perl} -MFile::Find -MConfig -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    #print "%doc  README.md";
    print "%dir /opt/myperl/lib/vendor_perl";
    print "%dir $Config{vendorarch}";
    print "%dir $Config{vendorarch}/auto";
    print "%dir $Config{vendorlib}";
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

echo "*** BEGIN DEBUG ***"
cat %{filelist}
echo "*** END DEBUG ***"

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Thu Jun 23 2016 scott@hnsc.de
- update for open build service from opensuse
* Fri Feb 19 2016 scott@hnsc.de
- copy from oxi repo
* Mon Aug 15 2011 m.bartosch@cynops.de
- Fixed file permissions in package
* Thu Feb 03 2011 m.bartosch@cynops.de
- Renovated build process, using generic template mechanism
* Mon Nov 27 2006 m.bartosch@cynops.de
- Initial build.
