## Written 2006 by Martin Bartosch for the OpenXPKI project
## Adapted for myperl-dbd-mysql by Scott Hardin
## Copyright (C) 2005-2014 by The OpenXPKI Project

%define pkgname myperl-fcgi
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 0
%define __perl /opt/myperl/bin/perl

name:      %{pkgname}
summary:   Apache fcgi packaged for myperl
version:   5.26.0

release: 1

vendor:    OpenXPKI Project
packager:  Scott Hardin <scott@hnsc.de>
license:   Apache
group:     Applications/CPAN
url:       http://www.openxpki.org
buildroot: %{_tmppath}/%{name}-%{version}
prefix:    %{_prefix}
BuildRequires: myperl myperl-buildtools
Requires: myperl
# The auto-prereq code picks up libexpat.so.0, but this is not explicitly
# supplied by the libexpat1 SLES package.
AutoReqProv: no
#source:    %{pkgname}-%{version}.tar.gz

Source1:    https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-0.78.tar.gz


%description
Apache fcgi packaged for myperl

Packaging information:
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
export PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR=%{buildroot}"
export DESTDIR="%{buildroot}"


$PERL $CPANM $CPANM_OPTS %{SOURCE1}


cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}


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

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

#%attr(0755,root,openxpki) /srv/www/openxpki/mason-data

%changelog
* Fri Feb 19 2016 scott@hnsc.de
- copy from oxi repo
* Mon Aug 15 2011 m.bartosch@cynops.de
- Fixed file permissions in package
* Thu Feb 03 2011 m.bartosch@cynops.de
- Renovated build process, using generic template mechanism
* Mon Nov 27 2006 m.bartosch@cynops.de
- Initial build.
