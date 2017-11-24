#
# spec file for package perl
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# icecream 0


Name:           myperl
Summary:        Local installation of the Perl interpreter
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Languages/Perl
Version:        5.26.0
Release:        1
Vendor:         OpenXPKI Project
Packager:       Scott Hardin <scott@hnsc.de>
Autoreqprov:    off
%define pversion 5.26.0
Url:            http://www.perl.org/
Source:         http://www.cpan.org/src/5.0/perl-%{version}.tar.bz2
Source1:        cpanm
# rpmlintrc is needed to supress errors in the checking... 
Source2:        perl-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#PreReq:         perl-base = %version
#PreReq:         %fillup_prereq
#BuildRequires:  db-devel
#BuildRequires:  gdbm-devel
#BuildRequires:  libbz2-devel
#BuildRequires:  ncurses-devel
#BuildRequires:  zlib-devel
#Requires:       gzip	# needed in SuSEconfig.perl
Suggests:       perl-doc = %version
#
%if "%version" != "%pversion"
Provides:       myperl = %pversion-%release
%endif
Provides:       myperl-500
Provides:       myperl-macros
Provides:       myperl(:MODULE_COMPAT_%pversion)
Obsoletes:      myperl-macros
Provides:       myperl-Filter-Simple
Obsoletes:      myperl-Filter-Simple
Provides:       myperl-I18N-LangTags
Obsoletes:      myperl-I18N-LangTags
Provides:       myperl-MIME-Base64
Obsoletes:      myperl-MIME-Base64
Provides:       myperl-Storable
Obsoletes:      myperl-Storable
Provides:       myperl-Test-Simple = 0.98-%{release}
Obsoletes:      myperl-Test-Simple < 0.98
Provides:       myperl-Text-Balanced
Obsoletes:      myperl-Text-Balanced
Provides:       myperl-Time-HiRes
Obsoletes:      myperl-Time-HiRes
Provides:       myperl-libnet
Obsoletes:      myperl-libnet
Provides:       myperl-Compress-Raw-Zlib
Obsoletes:      myperl-Compress-Raw-Zlib
Provides:       myperl-Compress-Zlib
Obsoletes:      myperl-Compress-Zlib
Provides:       myperl-IO-Compress-Base
Obsoletes:      myperl-IO-Compress-Base
Provides:       myperl-IO-Compress-Zlib
Obsoletes:      myperl-IO-Compress-Zlib
Provides:       myperl-IO-Zlib
Obsoletes:      myperl-IO-Zlib
Provides:       myperl-Archive-Tar
Obsoletes:      myperl-Archive-Tar
Provides:       myperl-Module-Build = 0.3901
Provides:       myperl(Module::Build) = 0.3901
Obsoletes:      myperl-Module-Build < 0.3901
Provides:       myperl-Module-Pluggable = 4.0
Obsoletes:      myperl-Module-Pluggable < 4.0
Provides:       myperl-Locale-Maketext-Simple = 0.21
Obsoletes:      myperl-Locale-Maketext-Simple < 0.21
Provides:       myperl-Pod-Escapes = 1.04
Obsoletes:      myperl-Pod-Escapes < 1.04
Provides:       myperl-Pod-Simple = 3.2
Obsoletes:      myperl-Pod-Simple < 3.2
Provides:       myperl-ExtUtils-ParseXS
Obsoletes:      myperl-ExtUtils-ParseXS
Provides:       myperl-version
Obsoletes:      myperl-version
Provides:       myperl-Digest
Provides:       myperl-Digest-MD5
%define filelist %{pkgname}-%{version}-filelist

%description
myperl - Local Version of Practical Extraction and Report Language

Perl is optimized for scanning arbitrary text files, extracting
information from those text files, and printing reports based on that
information.  It is also good for many system management tasks. Perl is
intended to be practical (easy to use, efficient, and complete) rather
than beautiful (tiny, elegant, and minimal).

Some of the modules available on CPAN can be found in the "myperl"
series.

The "myperl" version is just a separate Perl installation parallel to
the system Perl that comes with the distribution.

%prep
%setup -q -n perl-%{pversion}
# setup cpanm
cp -a %{S:1} .

%build

# Note: setting vendorprefix=/opt/myperl actually causes it to use the
# directories /opt/myperl/lib/vendor_perl/<PERL_VERSION> and
# /opt/myperl/lib/vendor_perl/<PERL_VERSION>/x86_64-linux.

./Configure -des \
    $PERL_CONFIGURE_OPTS \
    -Dprefix=/opt/myperl \
    -Dman1dir=/opt/myperl/man/man1 \
    -Dman3dir=/opt/myperl/man/man3 \
    -Dvendorprefix=/opt/myperl \
    -Dvendorman1dir=/opt/myperl/man/man1 \
    -Dvendorman3dir=/opt/myperl/man/man3 \
    -Duseithreads \
    -Duseshrplib

# Change shebang in cpanm to myperl
perl -i -pe 's{#!/usr/bin/env perl}{#!/opt/myperl/bin/perl}' cpanm

%check
%ifnarch %arm
export SUSE_ASNEEDED=0
#make test
%endif

%install
MYPERL="./miniperl -Ilib"
make install DESTDIR=$RPM_BUILD_ROOT
set -x
ls -la
cp -a cpanm $RPM_BUILD_ROOT/opt/myperl/bin/
chmod 0755 $RPM_BUILD_ROOT/opt/myperl/bin/cpanm

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if (-f $f || -l $f);

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            #for qw|/etc %_prefix/man %_prefix/bin %_prefix/share /var |;
            for qw| /etc /opt /usr /srv /var |;

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


%files
%defattr(-,root,root)
/opt/myperl

%clean
[ "%{buildroot}" != "/" ] && rm -rf "%{buildroot}"


%changelog
* Thu Sep 10 2015 scott@hnsc.de
- Bump Perl version to 5.22.0
- minor cleanup
* Wed Jun 25 2014 scott@hnsc.de
- initial myperl package based on SuSE Perl and my own other packaging work
