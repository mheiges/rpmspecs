%define pkg_base MUMmer

Summary: MUMmer is a system for rapidly aligning entire genomes.
Name: %{pkg_base}-%{version}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

# install everything but  src/
install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}

install -m 0755 annotate %{install_dir}
install -m 0755 combineMUMs %{install_dir}
install -m 0755 delta-filter %{install_dir}
install -m 0755 dnadiff %{install_dir}
install -m 0755 exact-tandems %{install_dir}
install -m 0755 gaps %{install_dir}
install -m 0755 mapview %{install_dir}
install -m 0755 mgaps %{install_dir}
install -m 0755 mummer %{install_dir}
install -m 0755 mummerplot %{install_dir}
install -m 0755 nucmer %{install_dir}
install -m 0755 nucmer2xfig %{install_dir}
install -m 0755 promer %{install_dir}
install -m 0755 repeat-match %{install_dir}
install -m 0755 run-mummer1 %{install_dir}
install -m 0755 run-mummer3 %{install_dir}
install -m 0755 show-aligns %{install_dir}
install -m 0755 show-coords %{install_dir}
install -m 0755 show-diff %{install_dir}
install -m 0755 show-snps %{install_dir}
install -m 0755 show-tiling %{install_dir}

install -m 0644 ACKNOWLEDGEMENTS %{install_dir}
install -m 0644 ChangeLog %{install_dir}
install -m 0644 COPYRIGHT %{install_dir}
install -m 0644 INSTALL %{install_dir}
install -m 0644 LICENSE %{install_dir}
install -m 0644 README %{install_dir}

cp -a aux_bin %{install_dir}
cp -a scripts %{install_dir}
cp -a docs %{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
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
%define install_dir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}
%define bundle_bin_dir %{install_dir}/__bin__
cd %{install_dir}

# remake scripts to fix paths
cd %{install_dir}/scripts
make clean BIN_DIR=%{install_dir} > /dev/null
make BIN_DIR=%{install_dir} AUX_BIN_DIR=%{install_dir}/aux_bin SCRIPT_DIR=%{install_dir}/scripts > /dev/null


%postun
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
%dir %{install_dir}/aux_bin
%dir %{install_dir}/scripts
%dir %{install_dir}/docs
%dir %{install_dir}/docs/web
%dir %{install_dir}/docs/web/manual
%dir %{install_dir}/docs/web/examples
%dir %{install_dir}/docs/web/examples/data

%{install_dir}/mummer
%{install_dir}/ACKNOWLEDGEMENTS
%{install_dir}/COPYRIGHT
%{install_dir}/ChangeLog
%{install_dir}/INSTALL
%{install_dir}/LICENSE
%{install_dir}/README
%{install_dir}/annotate
%{install_dir}/aux_bin/postnuc
%{install_dir}/aux_bin/postpro
%{install_dir}/aux_bin/prenuc
%{install_dir}/aux_bin/prepro
%{install_dir}/combineMUMs
%{install_dir}/delta-filter
%{install_dir}/dnadiff
%{install_dir}/docs/Makefile
%{install_dir}/docs/README
%{install_dir}/docs/differences.README
%{install_dir}/docs/dnadiff.README
%{install_dir}/docs/mapview.README
%{install_dir}/docs/maxmat3man.tex
%{install_dir}/docs/maxmat3src.pdf
%{install_dir}/docs/nucmer.README
%{install_dir}/docs/optionman.sty
%{install_dir}/docs/promer.README
%{install_dir}/docs/run-mummer1.README
%{install_dir}/docs/run-mummer3.README
%{install_dir}/docs/skaff.sty
%{install_dir}/docs/web/MUMmer.pdf
%{install_dir}/docs/web/MUMmer2.pdf
%{install_dir}/docs/web/MUMmer3.pdf
%{install_dir}/docs/web/XFiles.pdf
%{install_dir}/docs/web/applications.html
%{install_dir}/docs/web/compare.html
%{install_dir}/docs/web/examples/data/B_anthracis_Mslice.fasta
%{install_dir}/docs/web/examples/data/B_anthracis_contigs.fasta
%{install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.cds
%{install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.fasta
%{install_dir}/docs/web/examples/data/D_melanogaster_2Rslice.utr
%{install_dir}/docs/web/examples/data/D_pseudoobscura_contigs.fasta
%{install_dir}/docs/web/examples/data/H_pylori26695_Bslice.fasta
%{install_dir}/docs/web/examples/data/H_pylori26695_Eslice.fasta
%{install_dir}/docs/web/examples/data/H_pyloriJ99_Bslice.fasta
%{install_dir}/docs/web/examples/data/H_pyloriJ99_Eslice.fasta
%{install_dir}/docs/web/examples/data/README
%{install_dir}/docs/web/examples/data/mapview_0.fig
%{install_dir}/docs/web/examples/data/mapview_0.pdf
%{install_dir}/docs/web/examples/data/mummer.fplot
%{install_dir}/docs/web/examples/data/mummer.gp
%{install_dir}/docs/web/examples/data/mummer.mums
%{install_dir}/docs/web/examples/data/mummer.ps
%{install_dir}/docs/web/examples/data/mummer.rplot
%{install_dir}/docs/web/examples/data/mummer1.align
%{install_dir}/docs/web/examples/data/mummer1.errorsgaps
%{install_dir}/docs/web/examples/data/mummer1.gaps
%{install_dir}/docs/web/examples/data/mummer1.out
%{install_dir}/docs/web/examples/data/mummer3.align
%{install_dir}/docs/web/examples/data/mummer3.errorsgaps
%{install_dir}/docs/web/examples/data/mummer3.gaps
%{install_dir}/docs/web/examples/data/mummer3.out
%{install_dir}/docs/web/examples/data/nucmer.cluster
%{install_dir}/docs/web/examples/data/nucmer.coords
%{install_dir}/docs/web/examples/data/nucmer.delta
%{install_dir}/docs/web/examples/data/nucmer.snps
%{install_dir}/docs/web/examples/data/nucmer.tiling
%{install_dir}/docs/web/examples/data/promer.aligns
%{install_dir}/docs/web/examples/data/promer.cluster
%{install_dir}/docs/web/examples/data/promer.coords
%{install_dir}/docs/web/examples/data/promer.delta
%{install_dir}/docs/web/examples/dotplot.gif
%{install_dir}/docs/web/examples/examples_logo.gif
%{install_dir}/docs/web/examples/index.html
%{install_dir}/docs/web/examples/mapplot.gif
%{install_dir}/docs/web/examples/mapview_fig.jpg
%{install_dir}/docs/web/examples/mummer_ps.jpg
%{install_dir}/docs/web/index.html
%{install_dir}/docs/web/logo.gif
%{install_dir}/docs/web/manual/AlignmentTypes.odg
%{install_dir}/docs/web/manual/AlignmentTypes.pdf
%{install_dir}/docs/web/manual/covplot.gif
%{install_dir}/docs/web/manual/dotplot.gif
%{install_dir}/docs/web/manual/gaps.gif
%{install_dir}/docs/web/manual/index.html
%{install_dir}/docs/web/manual/manual_logo.gif
%{install_dir}/docs/web/manual/mapplot.gif
%{install_dir}/docs/web/manual/mgaps.gif
%{install_dir}/docs/web/manual/multiplota.gif
%{install_dir}/docs/web/manual/multiplotb.gif
%{install_dir}/docs/web/manual/nuc_proex.gif
%{install_dir}/docs/web/manual/nucex.gif
%{install_dir}/docs/web/manual/osi.gif
%{install_dir}/docs/web/manual/pro_proex.gif
%{install_dir}/docs/web/mummer-help.gif
%{install_dir}/docs/web/mummer-users.gif
%{install_dir}/exact-tandems
%{install_dir}/gaps
%{install_dir}/mapview
%{install_dir}/mgaps
%{install_dir}/mummerplot
%{install_dir}/nucmer
%{install_dir}/nucmer2xfig
%{install_dir}/promer
%{install_dir}/repeat-match
%{install_dir}/run-mummer1
%{install_dir}/run-mummer3
%{install_dir}/scripts/Foundation.pm
%{install_dir}/scripts/Makefile
%{install_dir}/scripts/dnadiff.pl
%{install_dir}/scripts/exact-tandems.csh
%{install_dir}/scripts/mapview.pl
%{install_dir}/scripts/mummerplot.pl
%{install_dir}/scripts/nucmer.pl
%{install_dir}/scripts/nucmer.pl.~1.5.~
%{install_dir}/scripts/nucmer2xfig.pl
%{install_dir}/scripts/promer.pl
%{install_dir}/scripts/run-mummer1.csh
%{install_dir}/scripts/run-mummer3.csh
%{install_dir}/scripts/tandem-repeat.awk
%{install_dir}/show-aligns
%{install_dir}/show-coords
%{install_dir}/show-diff
%{install_dir}/show-snps
%{install_dir}/show-tiling

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/annotate
%{install_dir}/__bin__/combineMUMs
%{install_dir}/__bin__/delta-filter
%{install_dir}/__bin__/dnadiff
%{install_dir}/__bin__/exact-tandems
%{install_dir}/__bin__/gaps
%{install_dir}/__bin__/mapview
%{install_dir}/__bin__/mgaps
%{install_dir}/__bin__/mummer
%{install_dir}/__bin__/mummerplot
%{install_dir}/__bin__/nucmer
%{install_dir}/__bin__/nucmer2xfig
%{install_dir}/__bin__/promer
%{install_dir}/__bin__/repeat-match
%{install_dir}/__bin__/run-mummer1
%{install_dir}/__bin__/run-mummer3
%{install_dir}/__bin__/show-aligns
%{install_dir}/__bin__/show-coords
%{install_dir}/__bin__/show-diff
%{install_dir}/__bin__/show-snps
%{install_dir}/__bin__/show-tiling


%changelog
* Mon Jan 23 2012 Mark Heiges <mheiges@uga.edu> 3.23-1
- Initial release.
