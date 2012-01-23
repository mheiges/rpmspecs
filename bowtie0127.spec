%define pkg_base bowtie

Summary: bowtie is a short read aligner for short DNA sequences
Name: bowtie0127
Version: 0.12.7
Release: 1%{?dist}
License: GPL
Group: Testing
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
%setup -q -n bowtie-%{version}

%build
make

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}

cp -a doc %{install_dir}
cp -a genomes %{install_dir}
cp -a indexes %{install_dir}
cp -a reads %{install_dir}
cp -a scripts %{install_dir}
install -m 0755 bowtie-inspect %{install_dir}
install -m 0755 bowtie-build %{install_dir}
install -m 0755 bowtie %{install_dir}
install -m 0644 TUTORIAL %{install_dir}
install -m 0644 VERSION %{install_dir}
install -m 0644 NEWS %{install_dir}
install -m 0644 MANUAL.markdown %{install_dir}
install -m 0644 MANUAL %{install_dir}
install -m 0644 COPYING %{install_dir}
install -m 0644 AUTHORS %{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
# for i in $(find bowtie bowtie-build bowtie-inspect scripts/ -type f -print); do echo "ln -s %{ln_path}/$i"; done; 
%define ln_path ../software/%{pkg_base}/%{version}
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

%post

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define install_dir  %{prefix}/software/%{pkg_base}/%{version}
%dir %{install_dir}
%dir %{install_dir}/__bin__
%dir %{install_dir}/doc
%dir %{install_dir}/genomes
%dir %{install_dir}/indexes
%dir %{install_dir}/reads
%dir %{install_dir}/scripts

%{install_dir}/bowtie-inspect
%{install_dir}/bowtie-build
%{install_dir}/bowtie
%{install_dir}/AUTHORS
%{install_dir}/COPYING
%{install_dir}/MANUAL
%{install_dir}/MANUAL.markdown
%{install_dir}/NEWS
%{install_dir}/TUTORIAL
%{install_dir}/VERSION
# for i in $(find doc genomes indexes reads scripts -type f -print); do echo "%{install_dir}/$i"; done;
%{install_dir}/doc/style.css
%{install_dir}/doc/strip_markdown.pl
%{install_dir}/doc/manual.html
%{install_dir}/doc/README
%{install_dir}/genomes/NC_008253.fna
%{install_dir}/indexes/e_coli.rev.1.ebwt
%{install_dir}/indexes/e_coli.3.ebwt
%{install_dir}/indexes/e_coli.1.ebwt
%{install_dir}/indexes/e_coli.2.ebwt
%{install_dir}/indexes/e_coli.README
%{install_dir}/indexes/e_coli.rev.2.ebwt
%{install_dir}/indexes/e_coli.4.ebwt
%{install_dir}/reads/e_coli_1000.fa
%{install_dir}/reads/e_coli_1000_2.fa
%{install_dir}/reads/e_coli_10000snp.fq
%{install_dir}/reads/e_coli_1000_1.fq
%{install_dir}/reads/e_coli_1000_2.fq
%{install_dir}/reads/e_coli_1000.fq
%{install_dir}/reads/e_coli_10000snp.fa
%{install_dir}/reads/e_coli_1000.raw
%{install_dir}/reads/e_coli_1000_1.fa
%{install_dir}/scripts/gen_occ_lookup.pl
%{install_dir}/scripts/reconcile_alignments_pe.pl
%{install_dir}/scripts/convert_quals.pl
%{install_dir}/scripts/make_s_cerevisiae.sh
%{install_dir}/scripts/make_h_sapiens_ncbi36.sh
%{install_dir}/scripts/pe_verify.pl
%{install_dir}/scripts/make_hg19.sh
%{install_dir}/scripts/gen_2b_occ_lookup.pl
%{install_dir}/scripts/reconcile_alignments.pl
%{install_dir}/scripts/make_galGal3.sh
%{install_dir}/scripts/make_e_coli.sh
%{install_dir}/scripts/random_bowtie_tests.sh
%{install_dir}/scripts/colorize_fasta.pl
%{install_dir}/scripts/make_mm8.sh
%{install_dir}/scripts/make_h_sapiens_ncbi37.sh
%{install_dir}/scripts/random_bowtie_tests.pl
%{install_dir}/scripts/make_rn4.sh
%{install_dir}/scripts/make_b_taurus_UMD3.sh
%{install_dir}/scripts/make_mm9.sh
%{install_dir}/scripts/make_canFam2.sh
%{install_dir}/scripts/build_test.sh
%{install_dir}/scripts/make_c_elegans_ws200.sh
%{install_dir}/scripts/mapability.pl
%{install_dir}/scripts/make_m_musculus_ncbi37.sh
%{install_dir}/scripts/random_bowtie_tests_p.sh
%{install_dir}/scripts/gen_solqual_lookup.pl
%{install_dir}/scripts/gen_dnamasks2colormask.pl
%{install_dir}/scripts/best_verify.pl
%{install_dir}/scripts/colorize_fastq.pl
%{install_dir}/scripts/make_hg18.sh
%{install_dir}/scripts/fastq_to_tabbed.pl
%{install_dir}/scripts/bs_mapability.pl
%{install_dir}/scripts/make_a_thaliana_tair.sh
%{install_dir}/scripts/make_d_melanogaster_fb5_22.sh

%{install_dir}/__bin__/bowtie
%{install_dir}/__bin__/bowtie-build
%{install_dir}/__bin__/bowtie-inspect
%{install_dir}/__bin__/gen_occ_lookup.pl
%{install_dir}/__bin__/reconcile_alignments_pe.pl
%{install_dir}/__bin__/convert_quals.pl
%{install_dir}/__bin__/make_s_cerevisiae.sh
%{install_dir}/__bin__/make_h_sapiens_ncbi36.sh
%{install_dir}/__bin__/pe_verify.pl
%{install_dir}/__bin__/make_hg19.sh
%{install_dir}/__bin__/gen_2b_occ_lookup.pl
%{install_dir}/__bin__/reconcile_alignments.pl
%{install_dir}/__bin__/make_galGal3.sh
%{install_dir}/__bin__/make_e_coli.sh
%{install_dir}/__bin__/random_bowtie_tests.sh
%{install_dir}/__bin__/colorize_fasta.pl
%{install_dir}/__bin__/make_mm8.sh
%{install_dir}/__bin__/make_h_sapiens_ncbi37.sh
%{install_dir}/__bin__/random_bowtie_tests.pl
%{install_dir}/__bin__/make_rn4.sh
%{install_dir}/__bin__/make_b_taurus_UMD3.sh
%{install_dir}/__bin__/make_mm9.sh
%{install_dir}/__bin__/make_canFam2.sh
%{install_dir}/__bin__/build_test.sh
%{install_dir}/__bin__/make_c_elegans_ws200.sh
%{install_dir}/__bin__/mapability.pl
%{install_dir}/__bin__/make_m_musculus_ncbi37.sh
%{install_dir}/__bin__/random_bowtie_tests_p.sh
%{install_dir}/__bin__/gen_solqual_lookup.pl
%{install_dir}/__bin__/gen_dnamasks2colormask.pl
%{install_dir}/__bin__/best_verify.pl
%{install_dir}/__bin__/colorize_fastq.pl
%{install_dir}/__bin__/make_hg18.sh
%{install_dir}/__bin__/fastq_to_tabbed.pl
%{install_dir}/__bin__/bs_mapability.pl
%{install_dir}/__bin__/make_a_thaliana_tair.sh
%{install_dir}/__bin__/make_d_melanogaster_fb5_22.sh

%changelog
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.