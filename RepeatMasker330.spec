%define pkg_base RepeatMasker

Summary: RepeatMaser software for masking low complexity DNA sequences
Name: %{pkg_base}-%{version}
Version: 3.3.0
Release: 1%{?dist}
License: Open Software License v. 2.1
Group: Application/Bioinformatics
BuildArch:	x86_64

Requires: wu_blast-2.0MP_20060504
Requires: blastn
Requires: trf
Requires: cross_match

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://www.repeatmasker.org/RepeatMasker-open-3-3-0.tar.gz
Source1: http://www.girinst.org/server/RepBase/protected/repeatmaskerlibraries/repeatmaskerlibraries-20110920.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
RepeatMasker is a program that screens DNA sequences for interspersed repeats and low complexity DNA sequences.
Includes libraries from Genetic Information Research Institute.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n RepeatMasker -a 1

%build
sed -i  "s|^#\!.*|#\!/usr/bin/env perl|" DateRepeats
sed -i  "s|^#\!.*|#\!/usr/bin/env perl|" ProcessRepeats
sed -i  "s|^#\!.*|#\!/usr/bin/env perl|" RepeatMasker
sed -i  "s|^#\!.*|#\!/usr/bin/env perl|" util/queryRepeatDatabase.pl
sed -i  "s|^#\!.*|#\!/usr/bin/env perl|" util/queryTaxonomyDatabase.pl

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

cp RepeatMaskerConfig.tmpl RepeatMaskerConfig.pm

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
install -m 0755 -d %{install_dir}/Libraries
install -m 0755 -d %{install_dir}/Matrices
install -m 0755 -d %{install_dir}/Matrices/crossmatch
install -m 0755 -d %{install_dir}/Matrices/ncbi
install -m 0755 -d %{install_dir}/Matrices/ncbi/nt
install -m 0755 -d %{install_dir}/Matrices/wublast
install -m 0755 -d %{install_dir}/Matrices/wublast/aa
install -m 0755 -d %{install_dir}/Matrices/wublast/nt
install -m 0755 -d %{install_dir}/util

install -m 0755 util/queryRepeatDatabase.pl %{install_dir}/util
install -m 0755 util/dupliconToSVG.pl %{install_dir}/util
install -m 0755 util/buildRMLibFromEMBL.pl %{install_dir}/util
install -m 0755 util/queryTaxonomyDatabase.pl %{install_dir}/util
install -m 0755 util/calcDivergenceFromAlign.pl %{install_dir}/util
install -m 0755 util/rmOutToGFF3.pl %{install_dir}/util
install -m 0755 DupMasker %{install_dir}
install -m 0755 DateRepeats %{install_dir}
install -m 0755 ProcessRepeats %{install_dir}
install -m 0755 RepeatProteinMask %{install_dir}
install -m 0755 RepeatMasker %{install_dir}

install -m 0644 ArrayList.pm %{install_dir}
install -m 0644 ArrayListIterator.pm %{install_dir}
install -m 0644 bluegrad.jpg %{install_dir}
install -m 0644 CrossmatchSearchEngine.pm %{install_dir}
install -m 0644 daterepeats.help %{install_dir}
install -m 0644 DeCypherSearchEngine.pm %{install_dir}
install -m 0644 FastaDB.pm %{install_dir}
install -m 0644 HTMLAnnotHeader.html %{install_dir}
install -m 0644 INSTALL %{install_dir}
install -m 0644 Libraries/RepeatMaskerLib.embl %{install_dir}/Libraries
install -m 0644 Libraries/RepeatPeps.lib %{install_dir}/Libraries
install -m 0644 Libraries/RepeatPeps.readme %{install_dir}/Libraries
install -m 0644 license.txt %{install_dir}
install -m 0644 LineHash.pm %{install_dir}
install -m 0644 Matrices/crossmatch/14p35g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p37g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p39g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p41g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p43g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p45g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p47g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p49g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p51g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p53g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p35g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p37g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p39g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p41g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p43g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p45g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p47g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p49g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p51g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p53g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p35g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p37g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p39g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p41g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p43g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p45g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p47g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p49g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p51g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p53g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p35g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p37g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p39g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p41g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p43g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p45g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p47g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p49g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p51g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p53g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/30p53g.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/at.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/identity.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/simple.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/simple1.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/transp.matrix %{install_dir}/Matrices/crossmatch
install -m 0644 Matrices/ncbi/nt/14p35g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p37g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p39g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p41g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p43g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p45g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p47g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p49g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p51g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p53g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p35g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p37g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p39g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p41g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p43g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p45g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p47g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p49g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p51g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p53g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p35g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p37g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p39g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p41g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p43g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p45g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p47g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p49g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p51g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p53g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p35g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p37g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p39g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p41g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p43g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p45g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p47g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p49g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p51g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p53g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/30p53g.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/at.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/atx.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/identity.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/ncbiblastdefault.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simple.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simple1.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simplex.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/wublastdefault.matrix %{install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/wublast/aa/14p35g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p37g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p39g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p41g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p43g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p45g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p47g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p49g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p51g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p53g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p35g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p37g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p39g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p41g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p43g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p45g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p47g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p49g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p51g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p53g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p35g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p37g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p39g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p41g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p43g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p45g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p47g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p49g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p51g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p53g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p35g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p37g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p39g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p41g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p43g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p45g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p47g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p49g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p51g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p53g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/30p53g.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/at.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/identity.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/simple.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/simple1.matrix %{install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/nt/14p35g.matrix %{install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/14p35g.matrix.4.2 %{install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/14p35g.matrix.4.4 %{install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix %{install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix.4.2 %{install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix.4.4 %{install_dir}/Matrices/wublast/nt
install -m 0644 NCBIBlastSearchEngine.pm %{install_dir}
install -m 0644 PubRef.pm %{install_dir}
install -m 0644 README %{install_dir}
install -m 0644 RepbaseEMBL.pm %{install_dir}
install -m 0644 RepbaseRecord.pm %{install_dir}
install -m 0644 RepeatAnnotationData.pm %{install_dir}
install -m 0644 repeatmasker.help %{install_dir}
install -m 0644 RepeatMaskerConfig.pm %{install_dir}
install -m 0644 RepeatMaskerConfig.pm %{install_dir}
install -m 0644 RepeatMaskerConfig.tmpl %{install_dir}
install -m 0644 SearchEngineI.pm %{install_dir}
install -m 0644 SearchResult.pm %{install_dir}
install -m 0644 SearchResultCollection.pm %{install_dir}
install -m 0644 SeqDBI.pm %{install_dir}
install -m 0644 SimpleBatcher.pm %{install_dir}
install -m 0644 taxonomy.dat %{install_dir}
install -m 0644 Taxonomy.pm %{install_dir}
install -m 0644 TRF.pm %{install_dir}
install -m 0644 TRFResult.pm %{install_dir}
install -m 0644 WUBlastSearchEngine.pm %{install_dir}
install -m 0644 WUBlastXSearchEngine.pm %{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/DateRepeats
ln -s %{ln_path}/DupMasker
ln -s %{ln_path}/ProcessRepeats
ln -s %{ln_path}/RepeatMasker
ln -s %{ln_path}/RepeatProteinMask

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%pre

%post
%define install_dir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}
%define bundle_bin_dir %{install_dir}/__bin__

mkdir -p $RPM_INSTALL_PREFIX0/tmp/RepeatMasker
chmod 1777 $RPM_INSTALL_PREFIX0/tmp/RepeatMasker

cd %{install_dir}
sed -i  "s|\$CROSSMATCH_DIR *=.*|\$CROSSMATCH_DIR = \"$RPM_INSTALL_PREFIX0/bin\";|" RepeatMaskerConfig.pm
sed -i  "s|\$WUBLAST_DIR *=.*|\$WUBLAST_DIR = \"$RPM_INSTALL_PREFIX0/bin\";|" RepeatMaskerConfig.pm
sed -i  "s|\$TRF_PRGM *=.*|\$TRF_PRGM = \"$RPM_INSTALL_PREFIX0/bin/trf\";|" RepeatMaskerConfig.pm
sed -i  "s|@LIBPATH *= *( \$REPEATMASKER_LIB_DIR,|@LIBPATH = ( \$REPEATMASKER_LIB_DIR, \"$RPM_INSTALL_PREFIX0/tmp/RepeatMasker\",|" RepeatMaskerConfig.pm

$RPM_INSTALL_PREFIX0/software/wu_blast/2.0MP_20060504/xdformat -p -I $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib > /dev/null 2>&1


%postun
# remove files that were added in %post
[[ -e $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpd ]] && \
    rm $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpd
[[ -e $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpi ]] && \
    rm $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpi
[[ -e $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xps ]] && \
    rm $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xps
[[ -e $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpt ]] && \
    rm $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpt

rmdir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}/Libraries
rmdir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}

# remove pkg_base dir if empty
%define parent $RPM_INSTALL_PREFIX0/software/%{pkg_base}
if [ ! "$(ls -A %{parent})" ]; then
    rmdir %{parent}
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define install_dir  %{prefix}/software/%{pkg_base}/%{version}
%dir %{install_dir}
%dir %{install_dir}/util
%dir %{install_dir}/Matrices
%dir %{install_dir}/Matrices/ncbi
%dir %{install_dir}/Matrices/ncbi/nt
%dir %{install_dir}/Matrices/wublast
%dir %{install_dir}/Matrices/wublast/nt
%dir %{install_dir}/Matrices/wublast/aa
%dir %{install_dir}/Matrices/crossmatch
%dir %{install_dir}/Libraries

%{install_dir}/ArrayList.pm
%{install_dir}/ArrayListIterator.pm
%{install_dir}/bluegrad.jpg
%{install_dir}/CrossmatchSearchEngine.pm
%{install_dir}/DateRepeats
%{install_dir}/daterepeats.help
%{install_dir}/DeCypherSearchEngine.pm
%{install_dir}/DupMasker
%{install_dir}/FastaDB.pm
%{install_dir}/HTMLAnnotHeader.html
%{install_dir}/INSTALL
%{install_dir}/Libraries/RepeatMaskerLib.embl
%{install_dir}/Libraries/RepeatPeps.lib
%{install_dir}/Libraries/RepeatPeps.readme
%{install_dir}/license.txt
%{install_dir}/LineHash.pm
%{install_dir}/Matrices/crossmatch/14p35g.matrix
%{install_dir}/Matrices/crossmatch/14p37g.matrix
%{install_dir}/Matrices/crossmatch/14p39g.matrix
%{install_dir}/Matrices/crossmatch/14p41g.matrix
%{install_dir}/Matrices/crossmatch/14p43g.matrix
%{install_dir}/Matrices/crossmatch/14p45g.matrix
%{install_dir}/Matrices/crossmatch/14p47g.matrix
%{install_dir}/Matrices/crossmatch/14p49g.matrix
%{install_dir}/Matrices/crossmatch/14p51g.matrix
%{install_dir}/Matrices/crossmatch/14p53g.matrix
%{install_dir}/Matrices/crossmatch/18p35g.matrix
%{install_dir}/Matrices/crossmatch/18p37g.matrix
%{install_dir}/Matrices/crossmatch/18p39g.matrix
%{install_dir}/Matrices/crossmatch/18p41g.matrix
%{install_dir}/Matrices/crossmatch/18p43g.matrix
%{install_dir}/Matrices/crossmatch/18p45g.matrix
%{install_dir}/Matrices/crossmatch/18p47g.matrix
%{install_dir}/Matrices/crossmatch/18p49g.matrix
%{install_dir}/Matrices/crossmatch/18p51g.matrix
%{install_dir}/Matrices/crossmatch/18p53g.matrix
%{install_dir}/Matrices/crossmatch/20p35g.matrix
%{install_dir}/Matrices/crossmatch/20p37g.matrix
%{install_dir}/Matrices/crossmatch/20p39g.matrix
%{install_dir}/Matrices/crossmatch/20p41g.matrix
%{install_dir}/Matrices/crossmatch/20p43g.matrix
%{install_dir}/Matrices/crossmatch/20p45g.matrix
%{install_dir}/Matrices/crossmatch/20p47g.matrix
%{install_dir}/Matrices/crossmatch/20p49g.matrix
%{install_dir}/Matrices/crossmatch/20p51g.matrix
%{install_dir}/Matrices/crossmatch/20p53g.matrix
%{install_dir}/Matrices/crossmatch/25p35g.matrix
%{install_dir}/Matrices/crossmatch/25p37g.matrix
%{install_dir}/Matrices/crossmatch/25p39g.matrix
%{install_dir}/Matrices/crossmatch/25p41g.matrix
%{install_dir}/Matrices/crossmatch/25p43g.matrix
%{install_dir}/Matrices/crossmatch/25p45g.matrix
%{install_dir}/Matrices/crossmatch/25p47g.matrix
%{install_dir}/Matrices/crossmatch/25p49g.matrix
%{install_dir}/Matrices/crossmatch/25p51g.matrix
%{install_dir}/Matrices/crossmatch/25p53g.matrix
%{install_dir}/Matrices/crossmatch/30p53g.matrix
%{install_dir}/Matrices/crossmatch/at.matrix
%{install_dir}/Matrices/crossmatch/identity.matrix
%{install_dir}/Matrices/crossmatch/simple.matrix
%{install_dir}/Matrices/crossmatch/simple1.matrix
%{install_dir}/Matrices/crossmatch/transp.matrix
%{install_dir}/Matrices/ncbi/nt/14p35g.matrix
%{install_dir}/Matrices/ncbi/nt/14p37g.matrix
%{install_dir}/Matrices/ncbi/nt/14p39g.matrix
%{install_dir}/Matrices/ncbi/nt/14p41g.matrix
%{install_dir}/Matrices/ncbi/nt/14p43g.matrix
%{install_dir}/Matrices/ncbi/nt/14p45g.matrix
%{install_dir}/Matrices/ncbi/nt/14p47g.matrix
%{install_dir}/Matrices/ncbi/nt/14p49g.matrix
%{install_dir}/Matrices/ncbi/nt/14p51g.matrix
%{install_dir}/Matrices/ncbi/nt/14p53g.matrix
%{install_dir}/Matrices/ncbi/nt/18p35g.matrix
%{install_dir}/Matrices/ncbi/nt/18p37g.matrix
%{install_dir}/Matrices/ncbi/nt/18p39g.matrix
%{install_dir}/Matrices/ncbi/nt/18p41g.matrix
%{install_dir}/Matrices/ncbi/nt/18p43g.matrix
%{install_dir}/Matrices/ncbi/nt/18p45g.matrix
%{install_dir}/Matrices/ncbi/nt/18p47g.matrix
%{install_dir}/Matrices/ncbi/nt/18p49g.matrix
%{install_dir}/Matrices/ncbi/nt/18p51g.matrix
%{install_dir}/Matrices/ncbi/nt/18p53g.matrix
%{install_dir}/Matrices/ncbi/nt/20p35g.matrix
%{install_dir}/Matrices/ncbi/nt/20p37g.matrix
%{install_dir}/Matrices/ncbi/nt/20p39g.matrix
%{install_dir}/Matrices/ncbi/nt/20p41g.matrix
%{install_dir}/Matrices/ncbi/nt/20p43g.matrix
%{install_dir}/Matrices/ncbi/nt/20p45g.matrix
%{install_dir}/Matrices/ncbi/nt/20p47g.matrix
%{install_dir}/Matrices/ncbi/nt/20p49g.matrix
%{install_dir}/Matrices/ncbi/nt/20p51g.matrix
%{install_dir}/Matrices/ncbi/nt/20p53g.matrix
%{install_dir}/Matrices/ncbi/nt/25p35g.matrix
%{install_dir}/Matrices/ncbi/nt/25p37g.matrix
%{install_dir}/Matrices/ncbi/nt/25p39g.matrix
%{install_dir}/Matrices/ncbi/nt/25p41g.matrix
%{install_dir}/Matrices/ncbi/nt/25p43g.matrix
%{install_dir}/Matrices/ncbi/nt/25p45g.matrix
%{install_dir}/Matrices/ncbi/nt/25p47g.matrix
%{install_dir}/Matrices/ncbi/nt/25p49g.matrix
%{install_dir}/Matrices/ncbi/nt/25p51g.matrix
%{install_dir}/Matrices/ncbi/nt/25p53g.matrix
%{install_dir}/Matrices/ncbi/nt/30p53g.matrix
%{install_dir}/Matrices/ncbi/nt/at.matrix
%{install_dir}/Matrices/ncbi/nt/atx.matrix
%{install_dir}/Matrices/ncbi/nt/identity.matrix
%{install_dir}/Matrices/ncbi/nt/ncbiblastdefault.matrix
%{install_dir}/Matrices/ncbi/nt/simple.matrix
%{install_dir}/Matrices/ncbi/nt/simple1.matrix
%{install_dir}/Matrices/ncbi/nt/simplex.matrix
%{install_dir}/Matrices/ncbi/nt/wublastdefault.matrix
%{install_dir}/Matrices/wublast/aa/14p35g.matrix
%{install_dir}/Matrices/wublast/aa/14p37g.matrix
%{install_dir}/Matrices/wublast/aa/14p39g.matrix
%{install_dir}/Matrices/wublast/aa/14p41g.matrix
%{install_dir}/Matrices/wublast/aa/14p43g.matrix
%{install_dir}/Matrices/wublast/aa/14p45g.matrix
%{install_dir}/Matrices/wublast/aa/14p47g.matrix
%{install_dir}/Matrices/wublast/aa/14p49g.matrix
%{install_dir}/Matrices/wublast/aa/14p51g.matrix
%{install_dir}/Matrices/wublast/aa/14p53g.matrix
%{install_dir}/Matrices/wublast/aa/18p35g.matrix
%{install_dir}/Matrices/wublast/aa/18p37g.matrix
%{install_dir}/Matrices/wublast/aa/18p39g.matrix
%{install_dir}/Matrices/wublast/aa/18p41g.matrix
%{install_dir}/Matrices/wublast/aa/18p43g.matrix
%{install_dir}/Matrices/wublast/aa/18p45g.matrix
%{install_dir}/Matrices/wublast/aa/18p47g.matrix
%{install_dir}/Matrices/wublast/aa/18p49g.matrix
%{install_dir}/Matrices/wublast/aa/18p51g.matrix
%{install_dir}/Matrices/wublast/aa/18p53g.matrix
%{install_dir}/Matrices/wublast/aa/20p35g.matrix
%{install_dir}/Matrices/wublast/aa/20p37g.matrix
%{install_dir}/Matrices/wublast/aa/20p39g.matrix
%{install_dir}/Matrices/wublast/aa/20p41g.matrix
%{install_dir}/Matrices/wublast/aa/20p43g.matrix
%{install_dir}/Matrices/wublast/aa/20p45g.matrix
%{install_dir}/Matrices/wublast/aa/20p47g.matrix
%{install_dir}/Matrices/wublast/aa/20p49g.matrix
%{install_dir}/Matrices/wublast/aa/20p51g.matrix
%{install_dir}/Matrices/wublast/aa/20p53g.matrix
%{install_dir}/Matrices/wublast/aa/25p35g.matrix
%{install_dir}/Matrices/wublast/aa/25p37g.matrix
%{install_dir}/Matrices/wublast/aa/25p39g.matrix
%{install_dir}/Matrices/wublast/aa/25p41g.matrix
%{install_dir}/Matrices/wublast/aa/25p43g.matrix
%{install_dir}/Matrices/wublast/aa/25p45g.matrix
%{install_dir}/Matrices/wublast/aa/25p47g.matrix
%{install_dir}/Matrices/wublast/aa/25p49g.matrix
%{install_dir}/Matrices/wublast/aa/25p51g.matrix
%{install_dir}/Matrices/wublast/aa/25p53g.matrix
%{install_dir}/Matrices/wublast/aa/30p53g.matrix
%{install_dir}/Matrices/wublast/aa/at.matrix
%{install_dir}/Matrices/wublast/aa/identity.matrix
%{install_dir}/Matrices/wublast/aa/simple.matrix
%{install_dir}/Matrices/wublast/aa/simple1.matrix
%{install_dir}/Matrices/wublast/nt/14p35g.matrix
%{install_dir}/Matrices/wublast/nt/14p35g.matrix.4.2
%{install_dir}/Matrices/wublast/nt/14p35g.matrix.4.4
%{install_dir}/Matrices/wublast/nt/20p41g.matrix
%{install_dir}/Matrices/wublast/nt/20p41g.matrix.4.2
%{install_dir}/Matrices/wublast/nt/20p41g.matrix.4.4
%{install_dir}/NCBIBlastSearchEngine.pm
%{install_dir}/ProcessRepeats
%{install_dir}/PubRef.pm
%{install_dir}/README
%{install_dir}/RepbaseEMBL.pm
%{install_dir}/RepbaseRecord.pm
%{install_dir}/RepeatAnnotationData.pm
%{install_dir}/RepeatMasker
%{install_dir}/repeatmasker.help
%{install_dir}/RepeatMaskerConfig.pm
%{install_dir}/RepeatMaskerConfig.tmpl
%{install_dir}/RepeatProteinMask
%{install_dir}/SearchEngineI.pm
%{install_dir}/SearchResult.pm
%{install_dir}/SearchResultCollection.pm
%{install_dir}/SeqDBI.pm
%{install_dir}/SimpleBatcher.pm
%{install_dir}/taxonomy.dat
%{install_dir}/Taxonomy.pm
%{install_dir}/TRF.pm
%{install_dir}/TRFResult.pm
%{install_dir}/util/buildRMLibFromEMBL.pl
%{install_dir}/util/calcDivergenceFromAlign.pl
%{install_dir}/util/dupliconToSVG.pl
%{install_dir}/util/queryRepeatDatabase.pl
%{install_dir}/util/queryTaxonomyDatabase.pl
%{install_dir}/util/rmOutToGFF3.pl
%{install_dir}/WUBlastSearchEngine.pm
%{install_dir}/WUBlastXSearchEngine.pm

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/DateRepeats
%{install_dir}/__bin__/DupMasker
%{install_dir}/__bin__/ProcessRepeats
%{install_dir}/__bin__/RepeatMasker
%{install_dir}/__bin__/RepeatProteinMask


%changelog
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
