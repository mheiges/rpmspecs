%define _pkg_base MUMmer

Summary: MUMmer is a system for rapidly aligning entire genomes.
Name: %{_pkg_base}-%{version}
Version: 3.23
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/mummer/files/mummer/3.23/MUMmer3.23.tar.gz
Patch0: mummer323-tail.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
MUMmer is a system for rapidly aligning entire genomes.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n MUMmer%{version}
%patch0 -p1

%build
make check
make install

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

# install everything but  src/
install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}

install -m 0755 annotate %{_install_dir}
install -m 0755 combineMUMs %{_install_dir}
install -m 0755 delta-filter %{_install_dir}
install -m 0755 dnadiff %{_install_dir}
install -m 0755 exact-tandems %{_install_dir}
install -m 0755 gaps %{_install_dir}
install -m 0755 mapview %{_install_dir}
install -m 0755 mgaps %{_install_dir}
install -m 0755 mummer %{_install_dir}
install -m 0755 mummerplot %{_install_dir}
install -m 0755 nucmer %{_install_dir}
install -m 0755 nucmer2xfig %{_install_dir}
install -m 0755 promer %{_install_dir}
install -m 0755 repeat-match %{_install_dir}
install -m 0755 run-mummer1 %{_install_dir}
install -m 0755 run-mummer3 %{_install_dir}
install -m 0755 show-aligns %{_install_dir}
install -m 0755 show-coords %{_install_dir}
install -m 0755 show-diff %{_install_dir}
install -m 0755 show-snps %{_install_dir}
install -m 0755 show-tiling %{_install_dir}

install -m 0644 ACKNOWLEDGEMENTS %{_install_dir}
install -m 0644 ChangeLog %{_install_dir}
install -m 0644 COPYRIGHT %{_install_dir}
install -m 0644 INSTALL %{_install_dir}
install -m 0644 LICENSE %{_install_dir}
install -m 0644 README %{_install_dir}

cp -a aux_bin %{_install_dir}
cp -a scripts %{_install_dir}
cp -a docs %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/annotate
ln -s %{ln_path}/combineMUMs
ln -s %{ln_path}/delta-filter
ln -s %{ln_path}/dnadiff
ln -s %{ln_path}/exact-tandems
ln -s %{ln_path}/gaps
ln -s %{ln_path}/mapview
ln -s %{ln_path}/mgaps
ln -s %{ln_path}/mummer
ln -s %{ln_path}/mummerplot
ln -s %{ln_path}/nucmer
ln -s %{ln_path}/nucmer2xfig
ln -s %{ln_path}/promer
ln -s %{ln_path}/repeat-match
ln -s %{ln_path}/run-mummer1
ln -s %{ln_path}/run-mummer3
ln -s %{ln_path}/show-aligns
ln -s %{ln_path}/show-coords
ln -s %{ln_path}/show-diff
ln -s %{ln_path}/show-snps
ln -s %{ln_path}/show-tiling

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post
%define _install_dir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir %{_install_dir}/__bin__
cd %{_final_install_dir}

# remake scripts to fix paths
cd %{_final_install_dir}/scripts
make clean BIN_DIR=%{_install_dir} > /dev/null
make BIN_DIR=%{_install_dir} AUX_BIN_DIR=%{_install_dir}/aux_bin SCRIPT_DIR=%{_install_dir}/scripts > /dev/null


%postun
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
%dir %{_install_dir}/aux_bin
%dir %{_install_dir}/scripts
%dir %{_install_dir}/docs
%dir %{_install_dir}/docs/web
%dir %{_install_dir}/docs/web/manual
%dir %{_install_dir}/docs/web/examples
%dir %{_install_dir}/docs/web/examples/data

%{_install_dir}/mummer
%{_install_dir}/ACKNOWLEDGEMENTS
%{_install_dir}/COPYRIGHT
%{_install_dir}/ChangeLog
%{_install_dir}/INSTALL
%{_install_dir}/LICENSE
%{_install_dir}/README
%{_install_dir}/annotate
%{_install_dir}/aux_bin/postnuc
%{_install_dir}/aux_bin/postpro
%{_install_dir}/aux_bin/prenuc
%{_install_dir}/aux_bin/prepro
%{_install_dir}/combineMUMs
%{_install_dir}/delta-filter
%{_install_dir}/dnadiff
%{_install_dir}/docs/Makefile
%{_install_dir}/docs/README
%{_install_dir}/docs/differences.README
%{_install_dir}/docs/dnadiff.README
%{_install_dir}/docs/mapview.README
%{_install_dir}/docs/maxmat3man.tex
%{_install_dir}/docs/maxmat3src.pdf
%{_install_dir}/docs/nucmer.README
%{_install_dir}/docs/optionman.sty
%{_install_dir}/docs/promer.README
%{_install_dir}/docs/run-mummer1.README
%{_install_dir}/docs/run-mummer3.README
%{_install_dir}/docs/skaff.sty
%{_install_dir}/docs/web/MUMmer.pdf
%{_install_dir}/docs/web/MUMmer2.pdf
%{_install_dir}/docs/web/MUMmer3.pdf
%{_install_dir}/docs/web/XFiles.pdf
%{_install_dir}/docs/web/applications.html
%{_install_dir}/docs/web/compare.html
%{_install_dir}/docs/web/examples/data/B_anthracis_Mslice.fasta
%{_install_dir}/docs/web/examples/data/B_anthracis_contigs.fasta
%{_install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.cds
%{_install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.fasta
%{_install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.utr
%{_install_dir}/docs/web/examples/data/D_pseudoobscura_contigs.fasta
%{_install_dir}/docs/web/examples/data/H_pylori26695_Bslice.fasta
%{_install_dir}/docs/web/examples/data/H_pylori26695_Eslice.fasta
%{_install_dir}/docs/web/examples/data/H_pyloriJ99_Bslice.fasta
%{_install_dir}/docs/web/examples/data/H_pyloriJ99_Eslice.fasta
%{_install_dir}/docs/web/examples/data/README
%{_install_dir}/docs/web/examples/data/mapview_0.fig
%{_install_dir}/docs/web/examples/data/mapview_0.pdf
%{_install_dir}/docs/web/examples/data/mummer.fplot
%{_install_dir}/docs/web/examples/data/mummer.gp
%{_install_dir}/docs/web/examples/data/mummer.mums
%{_install_dir}/docs/web/examples/data/mummer.ps
%{_install_dir}/docs/web/examples/data/mummer.rplot
%{_install_dir}/docs/web/examples/data/mummer1.align
%{_install_dir}/docs/web/examples/data/mummer1.errorsgaps
%{_install_dir}/docs/web/examples/data/mummer1.gaps
%{_install_dir}/docs/web/examples/data/mummer1.out
%{_install_dir}/docs/web/examples/data/mummer3.align
%{_install_dir}/docs/web/examples/data/mummer3.errorsgaps
%{_install_dir}/docs/web/examples/data/mummer3.gaps
%{_install_dir}/docs/web/examples/data/mummer3.out
%{_install_dir}/docs/web/examples/data/nucmer.cluster
%{_install_dir}/docs/web/examples/data/nucmer.coords
%{_install_dir}/docs/web/examples/data/nucmer.delta
%{_install_dir}/docs/web/examples/data/nucmer.snps
%{_install_dir}/docs/web/examples/data/nucmer.tiling
%{_install_dir}/docs/web/examples/data/promer.aligns
%{_install_dir}/docs/web/examples/data/promer.cluster
%{_install_dir}/docs/web/examples/data/promer.coords
%{_install_dir}/docs/web/examples/data/promer.delta
%{_install_dir}/docs/web/examples/dotplot.gif
%{_install_dir}/docs/web/examples/examples_logo.gif
%{_install_dir}/docs/web/examples/index.html
%{_install_dir}/docs/web/examples/mapplot.gif
%{_install_dir}/docs/web/examples/mapview_fig.jpg
%{_install_dir}/docs/web/examples/mummer_ps.jpg
%{_install_dir}/docs/web/index.html
%{_install_dir}/docs/web/logo.gif
%{_install_dir}/docs/web/manual/AlignmentTypes.odg
%{_install_dir}/docs/web/manual/AlignmentTypes.pdf
%{_install_dir}/docs/web/manual/covplot.gif
%{_install_dir}/docs/web/manual/dotplot.gif
%{_install_dir}/docs/web/manual/gaps.gif
%{_install_dir}/docs/web/manual/index.html
%{_install_dir}/docs/web/manual/manual_logo.gif
%{_install_dir}/docs/web/manual/mapplot.gif
%{_install_dir}/docs/web/manual/mgaps.gif
%{_install_dir}/docs/web/manual/multiplota.gif
%{_install_dir}/docs/web/manual/multiplotb.gif
%{_install_dir}/docs/web/manual/nuc_proex.gif
%{_install_dir}/docs/web/manual/nucex.gif
%{_install_dir}/docs/web/manual/osi.gif
%{_install_dir}/docs/web/manual/pro_proex.gif
%{_install_dir}/docs/web/mummer-help.gif
%{_install_dir}/docs/web/mummer-users.gif
%{_install_dir}/exact-tandems
%{_install_dir}/gaps
%{_install_dir}/mapview
%{_install_dir}/mgaps
%{_install_dir}/mummerplot
%{_install_dir}/nucmer
%{_install_dir}/nucmer2xfig
%{_install_dir}/promer
%{_install_dir}/repeat-match
%{_install_dir}/run-mummer1
%{_install_dir}/run-mummer3
%{_install_dir}/scripts/Foundation.pm
%{_install_dir}/scripts/Makefile
%{_install_dir}/scripts/dnadiff.pl
%{_install_dir}/scripts/exact-tandems.csh
%{_install_dir}/scripts/mapview.pl
%{_install_dir}/scripts/mummerplot.pl
%{_install_dir}/scripts/nucmer.pl
%{_install_dir}/scripts/nucmer.pl.~1.5.~
%{_install_dir}/scripts/nucmer2xfig.pl
%{_install_dir}/scripts/promer.pl
%{_install_dir}/scripts/run-mummer1.csh
%{_install_dir}/scripts/run-mummer3.csh
%{_install_dir}/scripts/tandem-repeat.awk
%{_install_dir}/show-aligns
%{_install_dir}/show-coords
%{_install_dir}/show-diff
%{_install_dir}/show-snps
%{_install_dir}/show-tiling

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/annotate
%{_install_dir}/__bin__/combineMUMs
%{_install_dir}/__bin__/delta-filter
%{_install_dir}/__bin__/dnadiff
%{_install_dir}/__bin__/exact-tandems
%{_install_dir}/__bin__/gaps
%{_install_dir}/__bin__/mapview
%{_install_dir}/__bin__/mgaps
%{_install_dir}/__bin__/mummer
%{_install_dir}/__bin__/mummerplot
%{_install_dir}/__bin__/nucmer
%{_install_dir}/__bin__/nucmer2xfig
%{_install_dir}/__bin__/promer
%{_install_dir}/__bin__/repeat-match
%{_install_dir}/__bin__/run-mummer1
%{_install_dir}/__bin__/run-mummer3
%{_install_dir}/__bin__/show-aligns
%{_install_dir}/__bin__/show-coords
%{_install_dir}/__bin__/show-diff
%{_install_dir}/__bin__/show-snps
%{_install_dir}/__bin__/show-tiling


%changelog
* Mon Jan 23 2012 Mark Heiges <mheiges@uga.edu> 3.23-1
- Initial release.
