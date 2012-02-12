%define _pkg_base RepeatMasker

Summary: RepeatMaser software for masking low complexity DNA sequences
Name: %{_pkg_base}-%{version}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

cp RepeatMaskerConfig.tmpl RepeatMaskerConfig.pm

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 -d %{_install_dir}/Libraries
install -m 0755 -d %{_install_dir}/Matrices
install -m 0755 -d %{_install_dir}/Matrices/crossmatch
install -m 0755 -d %{_install_dir}/Matrices/ncbi
install -m 0755 -d %{_install_dir}/Matrices/ncbi/nt
install -m 0755 -d %{_install_dir}/Matrices/wublast
install -m 0755 -d %{_install_dir}/Matrices/wublast/aa
install -m 0755 -d %{_install_dir}/Matrices/wublast/nt
install -m 0755 -d %{_install_dir}/util

install -m 0755 util/queryRepeatDatabase.pl %{_install_dir}/util
install -m 0755 util/dupliconToSVG.pl %{_install_dir}/util
install -m 0755 util/buildRMLibFromEMBL.pl %{_install_dir}/util
install -m 0755 util/queryTaxonomyDatabase.pl %{_install_dir}/util
install -m 0755 util/calcDivergenceFromAlign.pl %{_install_dir}/util
install -m 0755 util/rmOutToGFF3.pl %{_install_dir}/util
install -m 0755 DupMasker %{_install_dir}
install -m 0755 DateRepeats %{_install_dir}
install -m 0755 ProcessRepeats %{_install_dir}
install -m 0755 RepeatProteinMask %{_install_dir}
install -m 0755 RepeatMasker %{_install_dir}

install -m 0644 ArrayList.pm %{_install_dir}
install -m 0644 ArrayListIterator.pm %{_install_dir}
install -m 0644 bluegrad.jpg %{_install_dir}
install -m 0644 CrossmatchSearchEngine.pm %{_install_dir}
install -m 0644 daterepeats.help %{_install_dir}
install -m 0644 DeCypherSearchEngine.pm %{_install_dir}
install -m 0644 FastaDB.pm %{_install_dir}
install -m 0644 HTMLAnnotHeader.html %{_install_dir}
install -m 0644 INSTALL %{_install_dir}
install -m 0644 Libraries/RepeatMaskerLib.embl %{_install_dir}/Libraries
install -m 0644 Libraries/RepeatPeps.lib %{_install_dir}/Libraries
install -m 0644 Libraries/RepeatPeps.readme %{_install_dir}/Libraries
install -m 0644 license.txt %{_install_dir}
install -m 0644 LineHash.pm %{_install_dir}
install -m 0644 Matrices/crossmatch/14p35g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p37g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p39g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p41g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p43g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p45g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p47g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p49g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p51g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/14p53g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p35g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p37g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p39g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p41g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p43g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p45g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p47g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p49g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p51g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/18p53g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p35g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p37g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p39g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p41g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p43g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p45g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p47g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p49g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p51g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/20p53g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p35g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p37g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p39g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p41g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p43g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p45g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p47g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p49g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p51g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/25p53g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/30p53g.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/at.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/identity.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/simple.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/simple1.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/crossmatch/transp.matrix %{_install_dir}/Matrices/crossmatch
install -m 0644 Matrices/ncbi/nt/14p35g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p37g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p39g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p41g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p43g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p45g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p47g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p49g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p51g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/14p53g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p35g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p37g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p39g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p41g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p43g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p45g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p47g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p49g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p51g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/18p53g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p35g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p37g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p39g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p41g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p43g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p45g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p47g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p49g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p51g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/20p53g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p35g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p37g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p39g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p41g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p43g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p45g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p47g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p49g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p51g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/25p53g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/30p53g.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/at.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/atx.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/identity.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/ncbiblastdefault.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simple.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simple1.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/simplex.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/ncbi/nt/wublastdefault.matrix %{_install_dir}/Matrices/ncbi/nt
install -m 0644 Matrices/wublast/aa/14p35g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p37g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p39g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p41g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p43g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p45g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p47g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p49g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p51g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/14p53g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p35g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p37g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p39g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p41g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p43g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p45g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p47g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p49g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p51g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/18p53g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p35g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p37g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p39g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p41g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p43g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p45g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p47g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p49g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p51g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/20p53g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p35g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p37g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p39g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p41g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p43g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p45g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p47g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p49g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p51g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/25p53g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/30p53g.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/at.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/identity.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/simple.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/aa/simple1.matrix %{_install_dir}/Matrices/wublast/aa
install -m 0644 Matrices/wublast/nt/14p35g.matrix %{_install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/14p35g.matrix.4.2 %{_install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/14p35g.matrix.4.4 %{_install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix %{_install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix.4.2 %{_install_dir}/Matrices/wublast/nt
install -m 0644 Matrices/wublast/nt/20p41g.matrix.4.4 %{_install_dir}/Matrices/wublast/nt
install -m 0644 NCBIBlastSearchEngine.pm %{_install_dir}
install -m 0644 PubRef.pm %{_install_dir}
install -m 0644 README %{_install_dir}
install -m 0644 RepbaseEMBL.pm %{_install_dir}
install -m 0644 RepbaseRecord.pm %{_install_dir}
install -m 0644 RepeatAnnotationData.pm %{_install_dir}
install -m 0644 repeatmasker.help %{_install_dir}
install -m 0644 RepeatMaskerConfig.pm %{_install_dir}
install -m 0644 RepeatMaskerConfig.pm %{_install_dir}
install -m 0644 RepeatMaskerConfig.tmpl %{_install_dir}
install -m 0644 SearchEngineI.pm %{_install_dir}
install -m 0644 SearchResult.pm %{_install_dir}
install -m 0644 SearchResultCollection.pm %{_install_dir}
install -m 0644 SeqDBI.pm %{_install_dir}
install -m 0644 SimpleBatcher.pm %{_install_dir}
install -m 0644 taxonomy.dat %{_install_dir}
install -m 0644 Taxonomy.pm %{_install_dir}
install -m 0644 TRF.pm %{_install_dir}
install -m 0644 TRFResult.pm %{_install_dir}
install -m 0644 WUBlastSearchEngine.pm %{_install_dir}
install -m 0644 WUBlastXSearchEngine.pm %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
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
%define _install_dir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir %{_install_dir}/__bin__

mkdir -p $RPM_INSTALL_PREFIX0/tmp/RepeatMasker
chmod 1777 $RPM_INSTALL_PREFIX0/tmp/RepeatMasker

cd %{_final_install_dir}
sed -i  "s|\$CROSSMATCH_DIR *=.*|\$CROSSMATCH_DIR = \"$RPM_INSTALL_PREFIX0/bin\";|" RepeatMaskerConfig.pm
sed -i  "s|\$WUBLAST_DIR *=.*|\$WUBLAST_DIR = \"$RPM_INSTALL_PREFIX0/bin\";|" RepeatMaskerConfig.pm
sed -i  "s|\$TRF_PRGM *=.*|\$TRF_PRGM = \"$RPM_INSTALL_PREFIX0/bin/trf\";|" RepeatMaskerConfig.pm
sed -i  "s|@LIBPATH *= *( \$REPEATMASKER_LIB_DIR,|@LIBPATH = ( \$REPEATMASKER_LIB_DIR, \"$RPM_INSTALL_PREFIX0/tmp/RepeatMasker\",|" RepeatMaskerConfig.pm

$RPM_INSTALL_PREFIX0/%{_software_topdir}/wu_blast/2.0MP_20060504/xdformat -p -I $RPM_INSTALL_PREFIX0/software/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib > /dev/null 2>&1


%postun
# remove files that were added in %post
[[ -e $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpd ]] && \
    rm $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpd
[[ -e $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpi ]] && \
    rm $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpi
[[ -e $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xps ]] && \
    rm $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xps
[[ -e $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpt ]] && \
    rm $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries/RepeatPeps.lib.xpt

rmdir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}/Libraries
rmdir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}

# remove _pkg_base dir if empty
%define parent $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}
if [ ! "$(ls -A %{_parent})" ]; then
    rmdir %{_parent}
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define _install_dir  %{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%dir %{_install_dir}
%dir %{_install_dir}/util
%dir %{_install_dir}/Matrices
%dir %{_install_dir}/Matrices/ncbi
%dir %{_install_dir}/Matrices/ncbi/nt
%dir %{_install_dir}/Matrices/wublast
%dir %{_install_dir}/Matrices/wublast/nt
%dir %{_install_dir}/Matrices/wublast/aa
%dir %{_install_dir}/Matrices/crossmatch
%dir %{_install_dir}/Libraries

%{_install_dir}/ArrayList.pm
%{_install_dir}/ArrayListIterator.pm
%{_install_dir}/bluegrad.jpg
%{_install_dir}/CrossmatchSearchEngine.pm
%{_install_dir}/DateRepeats
%{_install_dir}/daterepeats.help
%{_install_dir}/DeCypherSearchEngine.pm
%{_install_dir}/DupMasker
%{_install_dir}/FastaDB.pm
%{_install_dir}/HTMLAnnotHeader.html
%{_install_dir}/INSTALL
%{_install_dir}/Libraries/RepeatMaskerLib.embl
%{_install_dir}/Libraries/RepeatPeps.lib
%{_install_dir}/Libraries/RepeatPeps.readme
%{_install_dir}/license.txt
%{_install_dir}/LineHash.pm
%{_install_dir}/Matrices/crossmatch/14p35g.matrix
%{_install_dir}/Matrices/crossmatch/14p37g.matrix
%{_install_dir}/Matrices/crossmatch/14p39g.matrix
%{_install_dir}/Matrices/crossmatch/14p41g.matrix
%{_install_dir}/Matrices/crossmatch/14p43g.matrix
%{_install_dir}/Matrices/crossmatch/14p45g.matrix
%{_install_dir}/Matrices/crossmatch/14p47g.matrix
%{_install_dir}/Matrices/crossmatch/14p49g.matrix
%{_install_dir}/Matrices/crossmatch/14p51g.matrix
%{_install_dir}/Matrices/crossmatch/14p53g.matrix
%{_install_dir}/Matrices/crossmatch/18p35g.matrix
%{_install_dir}/Matrices/crossmatch/18p37g.matrix
%{_install_dir}/Matrices/crossmatch/18p39g.matrix
%{_install_dir}/Matrices/crossmatch/18p41g.matrix
%{_install_dir}/Matrices/crossmatch/18p43g.matrix
%{_install_dir}/Matrices/crossmatch/18p45g.matrix
%{_install_dir}/Matrices/crossmatch/18p47g.matrix
%{_install_dir}/Matrices/crossmatch/18p49g.matrix
%{_install_dir}/Matrices/crossmatch/18p51g.matrix
%{_install_dir}/Matrices/crossmatch/18p53g.matrix
%{_install_dir}/Matrices/crossmatch/20p35g.matrix
%{_install_dir}/Matrices/crossmatch/20p37g.matrix
%{_install_dir}/Matrices/crossmatch/20p39g.matrix
%{_install_dir}/Matrices/crossmatch/20p41g.matrix
%{_install_dir}/Matrices/crossmatch/20p43g.matrix
%{_install_dir}/Matrices/crossmatch/20p45g.matrix
%{_install_dir}/Matrices/crossmatch/20p47g.matrix
%{_install_dir}/Matrices/crossmatch/20p49g.matrix
%{_install_dir}/Matrices/crossmatch/20p51g.matrix
%{_install_dir}/Matrices/crossmatch/20p53g.matrix
%{_install_dir}/Matrices/crossmatch/25p35g.matrix
%{_install_dir}/Matrices/crossmatch/25p37g.matrix
%{_install_dir}/Matrices/crossmatch/25p39g.matrix
%{_install_dir}/Matrices/crossmatch/25p41g.matrix
%{_install_dir}/Matrices/crossmatch/25p43g.matrix
%{_install_dir}/Matrices/crossmatch/25p45g.matrix
%{_install_dir}/Matrices/crossmatch/25p47g.matrix
%{_install_dir}/Matrices/crossmatch/25p49g.matrix
%{_install_dir}/Matrices/crossmatch/25p51g.matrix
%{_install_dir}/Matrices/crossmatch/25p53g.matrix
%{_install_dir}/Matrices/crossmatch/30p53g.matrix
%{_install_dir}/Matrices/crossmatch/at.matrix
%{_install_dir}/Matrices/crossmatch/identity.matrix
%{_install_dir}/Matrices/crossmatch/simple.matrix
%{_install_dir}/Matrices/crossmatch/simple1.matrix
%{_install_dir}/Matrices/crossmatch/transp.matrix
%{_install_dir}/Matrices/ncbi/nt/14p35g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p37g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p39g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p41g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p43g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p45g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p47g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p49g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p51g.matrix
%{_install_dir}/Matrices/ncbi/nt/14p53g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p35g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p37g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p39g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p41g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p43g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p45g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p47g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p49g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p51g.matrix
%{_install_dir}/Matrices/ncbi/nt/18p53g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p35g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p37g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p39g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p41g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p43g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p45g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p47g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p49g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p51g.matrix
%{_install_dir}/Matrices/ncbi/nt/20p53g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p35g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p37g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p39g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p41g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p43g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p45g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p47g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p49g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p51g.matrix
%{_install_dir}/Matrices/ncbi/nt/25p53g.matrix
%{_install_dir}/Matrices/ncbi/nt/30p53g.matrix
%{_install_dir}/Matrices/ncbi/nt/at.matrix
%{_install_dir}/Matrices/ncbi/nt/atx.matrix
%{_install_dir}/Matrices/ncbi/nt/identity.matrix
%{_install_dir}/Matrices/ncbi/nt/ncbiblastdefault.matrix
%{_install_dir}/Matrices/ncbi/nt/simple.matrix
%{_install_dir}/Matrices/ncbi/nt/simple1.matrix
%{_install_dir}/Matrices/ncbi/nt/simplex.matrix
%{_install_dir}/Matrices/ncbi/nt/wublastdefault.matrix
%{_install_dir}/Matrices/wublast/aa/14p35g.matrix
%{_install_dir}/Matrices/wublast/aa/14p37g.matrix
%{_install_dir}/Matrices/wublast/aa/14p39g.matrix
%{_install_dir}/Matrices/wublast/aa/14p41g.matrix
%{_install_dir}/Matrices/wublast/aa/14p43g.matrix
%{_install_dir}/Matrices/wublast/aa/14p45g.matrix
%{_install_dir}/Matrices/wublast/aa/14p47g.matrix
%{_install_dir}/Matrices/wublast/aa/14p49g.matrix
%{_install_dir}/Matrices/wublast/aa/14p51g.matrix
%{_install_dir}/Matrices/wublast/aa/14p53g.matrix
%{_install_dir}/Matrices/wublast/aa/18p35g.matrix
%{_install_dir}/Matrices/wublast/aa/18p37g.matrix
%{_install_dir}/Matrices/wublast/aa/18p39g.matrix
%{_install_dir}/Matrices/wublast/aa/18p41g.matrix
%{_install_dir}/Matrices/wublast/aa/18p43g.matrix
%{_install_dir}/Matrices/wublast/aa/18p45g.matrix
%{_install_dir}/Matrices/wublast/aa/18p47g.matrix
%{_install_dir}/Matrices/wublast/aa/18p49g.matrix
%{_install_dir}/Matrices/wublast/aa/18p51g.matrix
%{_install_dir}/Matrices/wublast/aa/18p53g.matrix
%{_install_dir}/Matrices/wublast/aa/20p35g.matrix
%{_install_dir}/Matrices/wublast/aa/20p37g.matrix
%{_install_dir}/Matrices/wublast/aa/20p39g.matrix
%{_install_dir}/Matrices/wublast/aa/20p41g.matrix
%{_install_dir}/Matrices/wublast/aa/20p43g.matrix
%{_install_dir}/Matrices/wublast/aa/20p45g.matrix
%{_install_dir}/Matrices/wublast/aa/20p47g.matrix
%{_install_dir}/Matrices/wublast/aa/20p49g.matrix
%{_install_dir}/Matrices/wublast/aa/20p51g.matrix
%{_install_dir}/Matrices/wublast/aa/20p53g.matrix
%{_install_dir}/Matrices/wublast/aa/25p35g.matrix
%{_install_dir}/Matrices/wublast/aa/25p37g.matrix
%{_install_dir}/Matrices/wublast/aa/25p39g.matrix
%{_install_dir}/Matrices/wublast/aa/25p41g.matrix
%{_install_dir}/Matrices/wublast/aa/25p43g.matrix
%{_install_dir}/Matrices/wublast/aa/25p45g.matrix
%{_install_dir}/Matrices/wublast/aa/25p47g.matrix
%{_install_dir}/Matrices/wublast/aa/25p49g.matrix
%{_install_dir}/Matrices/wublast/aa/25p51g.matrix
%{_install_dir}/Matrices/wublast/aa/25p53g.matrix
%{_install_dir}/Matrices/wublast/aa/30p53g.matrix
%{_install_dir}/Matrices/wublast/aa/at.matrix
%{_install_dir}/Matrices/wublast/aa/identity.matrix
%{_install_dir}/Matrices/wublast/aa/simple.matrix
%{_install_dir}/Matrices/wublast/aa/simple1.matrix
%{_install_dir}/Matrices/wublast/nt/14p35g.matrix
%{_install_dir}/Matrices/wublast/nt/14p35g.matrix.4.2
%{_install_dir}/Matrices/wublast/nt/14p35g.matrix.4.4
%{_install_dir}/Matrices/wublast/nt/20p41g.matrix
%{_install_dir}/Matrices/wublast/nt/20p41g.matrix.4.2
%{_install_dir}/Matrices/wublast/nt/20p41g.matrix.4.4
%{_install_dir}/NCBIBlastSearchEngine.pm
%{_install_dir}/ProcessRepeats
%{_install_dir}/PubRef.pm
%{_install_dir}/README
%{_install_dir}/RepbaseEMBL.pm
%{_install_dir}/RepbaseRecord.pm
%{_install_dir}/RepeatAnnotationData.pm
%{_install_dir}/RepeatMasker
%{_install_dir}/repeatmasker.help
%{_install_dir}/RepeatMaskerConfig.pm
%{_install_dir}/RepeatMaskerConfig.tmpl
%{_install_dir}/RepeatProteinMask
%{_install_dir}/SearchEngineI.pm
%{_install_dir}/SearchResult.pm
%{_install_dir}/SearchResultCollection.pm
%{_install_dir}/SeqDBI.pm
%{_install_dir}/SimpleBatcher.pm
%{_install_dir}/taxonomy.dat
%{_install_dir}/Taxonomy.pm
%{_install_dir}/TRF.pm
%{_install_dir}/TRFResult.pm
%{_install_dir}/util/buildRMLibFromEMBL.pl
%{_install_dir}/util/calcDivergenceFromAlign.pl
%{_install_dir}/util/dupliconToSVG.pl
%{_install_dir}/util/queryRepeatDatabase.pl
%{_install_dir}/util/queryTaxonomyDatabase.pl
%{_install_dir}/util/rmOutToGFF3.pl
%{_install_dir}/WUBlastSearchEngine.pm
%{_install_dir}/WUBlastXSearchEngine.pm

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/DateRepeats
%{_install_dir}/__bin__/DupMasker
%{_install_dir}/__bin__/ProcessRepeats
%{_install_dir}/__bin__/RepeatMasker
%{_install_dir}/__bin__/RepeatProteinMask


%changelog
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
