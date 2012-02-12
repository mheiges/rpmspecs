%define _pkg_base bowtie

Summary: bowtie is a short read aligner for short DNA sequences
Name: %{_pkg_base}-%{version}
Version: 0.12.7
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/bowtie-bio/files/bowtie/%{version}/bowtie-%{version}-src.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Bowtie, an ultrafast, memory-efficient short read aligner for short DNA sequences (reads) 
from next-gen sequencers. Please cite: Langmead B, et al. Ultrafast and memory-efficient 
alignment of short DNA sequences to the human genome. Genome Biol 10:R25.


%prep
%eupa_validate_workflow_pkg_name
%setup -q -n bowtie-%{version}

%build
make

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}

cp -a doc %{_install_dir}
cp -a genomes %{_install_dir}
cp -a indexes %{_install_dir}
cp -a reads %{_install_dir}
cp -a scripts %{_install_dir}
install -m 0755 bowtie-inspect %{_install_dir}
install -m 0755 bowtie-build %{_install_dir}
install -m 0755 bowtie %{_install_dir}
install -m 0644 TUTORIAL %{_install_dir}
install -m 0644 VERSION %{_install_dir}
install -m 0644 NEWS %{_install_dir}
install -m 0644 MANUAL.markdown %{_install_dir}
install -m 0644 MANUAL %{_install_dir}
install -m 0644 COPYING %{_install_dir}
install -m 0644 AUTHORS %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
# for i in $(find bowtie bowtie-build bowtie-inspect scripts/ -type f -print); do echo "ln -s %{ln_path}/$i"; done; 
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/bowtie
ln -s %{ln_path}/bowtie-build
ln -s %{ln_path}/bowtie-inspect
ln -s %{ln_path}/scripts/gen_occ_lookup.pl
ln -s %{ln_path}/scripts/reconcile_alignments_pe.pl
ln -s %{ln_path}/scripts/convert_quals.pl
ln -s %{ln_path}/scripts/make_s_cerevisiae.sh
ln -s %{ln_path}/scripts/make_h_sapiens_ncbi36.sh
ln -s %{ln_path}/scripts/pe_verify.pl
ln -s %{ln_path}/scripts/make_hg19.sh
ln -s %{ln_path}/scripts/gen_2b_occ_lookup.pl
ln -s %{ln_path}/scripts/reconcile_alignments.pl
ln -s %{ln_path}/scripts/make_galGal3.sh
ln -s %{ln_path}/scripts/make_e_coli.sh
ln -s %{ln_path}/scripts/random_bowtie_tests.sh
ln -s %{ln_path}/scripts/colorize_fasta.pl
ln -s %{ln_path}/scripts/make_mm8.sh
ln -s %{ln_path}/scripts/make_h_sapiens_ncbi37.sh
ln -s %{ln_path}/scripts/random_bowtie_tests.pl
ln -s %{ln_path}/scripts/make_rn4.sh
ln -s %{ln_path}/scripts/make_b_taurus_UMD3.sh
ln -s %{ln_path}/scripts/make_mm9.sh
ln -s %{ln_path}/scripts/make_canFam2.sh
ln -s %{ln_path}/scripts/build_test.sh
ln -s %{ln_path}/scripts/make_c_elegans_ws200.sh
ln -s %{ln_path}/scripts/mapability.pl
ln -s %{ln_path}/scripts/make_m_musculus_ncbi37.sh
ln -s %{ln_path}/scripts/random_bowtie_tests_p.sh
ln -s %{ln_path}/scripts/gen_solqual_lookup.pl
ln -s %{ln_path}/scripts/gen_dnamasks2colormask.pl
ln -s %{ln_path}/scripts/best_verify.pl
ln -s %{ln_path}/scripts/colorize_fastq.pl
ln -s %{ln_path}/scripts/make_hg18.sh
ln -s %{ln_path}/scripts/fastq_to_tabbed.pl
ln -s %{ln_path}/scripts/bs_mapability.pl
ln -s %{ln_path}/scripts/make_a_thaliana_tair.sh
ln -s %{ln_path}/scripts/make_d_melanogaster_fb5_22.sh

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post

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
%dir %{_install_dir}/doc
%dir %{_install_dir}/genomes
%dir %{_install_dir}/indexes
%dir %{_install_dir}/reads
%dir %{_install_dir}/scripts

%{_install_dir}/bowtie-inspect
%{_install_dir}/bowtie-build
%{_install_dir}/bowtie
%{_install_dir}/AUTHORS
%{_install_dir}/COPYING
%{_install_dir}/MANUAL
%{_install_dir}/MANUAL.markdown
%{_install_dir}/NEWS
%{_install_dir}/TUTORIAL
%{_install_dir}/VERSION
# for i in $(find doc genomes indexes reads scripts -type f -print); do echo "%{_install_dir}/$i"; done;
%{_install_dir}/doc/style.css
%{_install_dir}/doc/strip_markdown.pl
%{_install_dir}/doc/manual.html
%{_install_dir}/doc/README
%{_install_dir}/genomes/NC_008253.fna
%{_install_dir}/indexes/e_coli.rev.1.ebwt
%{_install_dir}/indexes/e_coli.3.ebwt
%{_install_dir}/indexes/e_coli.1.ebwt
%{_install_dir}/indexes/e_coli.2.ebwt
%{_install_dir}/indexes/e_coli.README
%{_install_dir}/indexes/e_coli.rev.2.ebwt
%{_install_dir}/indexes/e_coli.4.ebwt
%{_install_dir}/reads/e_coli_1000.fa
%{_install_dir}/reads/e_coli_1000_2.fa
%{_install_dir}/reads/e_coli_10000snp.fq
%{_install_dir}/reads/e_coli_1000_1.fq
%{_install_dir}/reads/e_coli_1000_2.fq
%{_install_dir}/reads/e_coli_1000.fq
%{_install_dir}/reads/e_coli_10000snp.fa
%{_install_dir}/reads/e_coli_1000.raw
%{_install_dir}/reads/e_coli_1000_1.fa
%{_install_dir}/scripts/gen_occ_lookup.pl
%{_install_dir}/scripts/reconcile_alignments_pe.pl
%{_install_dir}/scripts/convert_quals.pl
%{_install_dir}/scripts/make_s_cerevisiae.sh
%{_install_dir}/scripts/make_h_sapiens_ncbi36.sh
%{_install_dir}/scripts/pe_verify.pl
%{_install_dir}/scripts/make_hg19.sh
%{_install_dir}/scripts/gen_2b_occ_lookup.pl
%{_install_dir}/scripts/reconcile_alignments.pl
%{_install_dir}/scripts/make_galGal3.sh
%{_install_dir}/scripts/make_e_coli.sh
%{_install_dir}/scripts/random_bowtie_tests.sh
%{_install_dir}/scripts/colorize_fasta.pl
%{_install_dir}/scripts/make_mm8.sh
%{_install_dir}/scripts/make_h_sapiens_ncbi37.sh
%{_install_dir}/scripts/random_bowtie_tests.pl
%{_install_dir}/scripts/make_rn4.sh
%{_install_dir}/scripts/make_b_taurus_UMD3.sh
%{_install_dir}/scripts/make_mm9.sh
%{_install_dir}/scripts/make_canFam2.sh
%{_install_dir}/scripts/build_test.sh
%{_install_dir}/scripts/make_c_elegans_ws200.sh
%{_install_dir}/scripts/mapability.pl
%{_install_dir}/scripts/make_m_musculus_ncbi37.sh
%{_install_dir}/scripts/random_bowtie_tests_p.sh
%{_install_dir}/scripts/gen_solqual_lookup.pl
%{_install_dir}/scripts/gen_dnamasks2colormask.pl
%{_install_dir}/scripts/best_verify.pl
%{_install_dir}/scripts/colorize_fastq.pl
%{_install_dir}/scripts/make_hg18.sh
%{_install_dir}/scripts/fastq_to_tabbed.pl
%{_install_dir}/scripts/bs_mapability.pl
%{_install_dir}/scripts/make_a_thaliana_tair.sh
%{_install_dir}/scripts/make_d_melanogaster_fb5_22.sh

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/bowtie
%{_install_dir}/__bin__/bowtie-build
%{_install_dir}/__bin__/bowtie-inspect
%{_install_dir}/__bin__/gen_occ_lookup.pl
%{_install_dir}/__bin__/reconcile_alignments_pe.pl
%{_install_dir}/__bin__/convert_quals.pl
%{_install_dir}/__bin__/make_s_cerevisiae.sh
%{_install_dir}/__bin__/make_h_sapiens_ncbi36.sh
%{_install_dir}/__bin__/pe_verify.pl
%{_install_dir}/__bin__/make_hg19.sh
%{_install_dir}/__bin__/gen_2b_occ_lookup.pl
%{_install_dir}/__bin__/reconcile_alignments.pl
%{_install_dir}/__bin__/make_galGal3.sh
%{_install_dir}/__bin__/make_e_coli.sh
%{_install_dir}/__bin__/random_bowtie_tests.sh
%{_install_dir}/__bin__/colorize_fasta.pl
%{_install_dir}/__bin__/make_mm8.sh
%{_install_dir}/__bin__/make_h_sapiens_ncbi37.sh
%{_install_dir}/__bin__/random_bowtie_tests.pl
%{_install_dir}/__bin__/make_rn4.sh
%{_install_dir}/__bin__/make_b_taurus_UMD3.sh
%{_install_dir}/__bin__/make_mm9.sh
%{_install_dir}/__bin__/make_canFam2.sh
%{_install_dir}/__bin__/build_test.sh
%{_install_dir}/__bin__/make_c_elegans_ws200.sh
%{_install_dir}/__bin__/mapability.pl
%{_install_dir}/__bin__/make_m_musculus_ncbi37.sh
%{_install_dir}/__bin__/random_bowtie_tests_p.sh
%{_install_dir}/__bin__/gen_solqual_lookup.pl
%{_install_dir}/__bin__/gen_dnamasks2colormask.pl
%{_install_dir}/__bin__/best_verify.pl
%{_install_dir}/__bin__/colorize_fastq.pl
%{_install_dir}/__bin__/make_hg18.sh
%{_install_dir}/__bin__/fastq_to_tabbed.pl
%{_install_dir}/__bin__/bs_mapability.pl
%{_install_dir}/__bin__/make_a_thaliana_tair.sh
%{_install_dir}/__bin__/make_d_melanogaster_fb5_22.sh

%changelog
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.