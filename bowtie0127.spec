%define _pkg_base bowtie

Summary: bowtie is a short read aligner for short DNA sequences
Name: %{_pkg_base}-%{version}
Version: 0.12.7
Release: 2%{?dist}
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
install -m 0755 -d %{_pre_install_dir}

cp -a doc %{_pre_install_dir}
cp -a genomes %{_pre_install_dir}
cp -a indexes %{_pre_install_dir}
cp -a reads %{_pre_install_dir}
cp -a scripts %{_pre_install_dir}
install -m 0755 bowtie-inspect %{_pre_install_dir}
install -m 0755 bowtie-build %{_pre_install_dir}
install -m 0755 bowtie %{_pre_install_dir}
install -m 0644 TUTORIAL %{_pre_install_dir}
install -m 0644 VERSION %{_pre_install_dir}
install -m 0644 NEWS %{_pre_install_dir}
install -m 0644 MANUAL.markdown %{_pre_install_dir}
install -m 0644 MANUAL %{_pre_install_dir}
install -m 0644 COPYING %{_pre_install_dir}
install -m 0644 AUTHORS %{_pre_install_dir}

%mfest_bin   bowtie
%mfest_bin   bowtie-build
%mfest_bin   bowtie-inspect
%mfest_bin   scripts/gen_occ_lookup.pl               gen_occ_lookup.pl
%mfest_bin   scripts/reconcile_alignments_pe.pl      reconcile_alignments_pe.pl
%mfest_bin   scripts/convert_quals.pl                convert_quals.pl
%mfest_bin   scripts/make_s_cerevisiae.sh            make_s_cerevisiae.sh
%mfest_bin   scripts/make_h_sapiens_ncbi36.sh        make_h_sapiens_ncbi36.sh
%mfest_bin   scripts/pe_verify.pl                    pe_verify.pl
%mfest_bin   scripts/make_hg19.sh                    make_hg19.sh
%mfest_bin   scripts/gen_2b_occ_lookup.pl            gen_2b_occ_lookup.pl
%mfest_bin   scripts/reconcile_alignments.pl         reconcile_alignments.pl
%mfest_bin   scripts/make_galGal3.sh                 make_galGal3.sh
%mfest_bin   scripts/make_e_coli.sh                  make_e_coli.sh
%mfest_bin   scripts/random_bowtie_tests.sh          random_bowtie_tests.sh
%mfest_bin   scripts/colorize_fasta.pl               colorize_fasta.pl
%mfest_bin   scripts/make_mm8.sh                     make_mm8.sh
%mfest_bin   scripts/make_h_sapiens_ncbi37.sh        make_h_sapiens_ncbi37.sh
%mfest_bin   scripts/random_bowtie_tests.pl          random_bowtie_tests.pl
%mfest_bin   scripts/make_rn4.sh                     make_rn4.sh
%mfest_bin   scripts/make_b_taurus_UMD3.sh           make_b_taurus_UMD3.sh
%mfest_bin   scripts/make_mm9.sh                     make_mm9.sh
%mfest_bin   scripts/make_canFam2.sh                 make_canFam2.sh
%mfest_bin   scripts/build_test.sh                   build_test.sh
%mfest_bin   scripts/make_c_elegans_ws200.sh         make_c_elegans_ws200.sh
%mfest_bin   scripts/mapability.pl                   mapability.pl
%mfest_bin   scripts/make_m_musculus_ncbi37.sh       make_m_musculus_ncbi37.sh
%mfest_bin   scripts/random_bowtie_tests_p.sh        random_bowtie_tests_p.sh
%mfest_bin   scripts/gen_solqual_lookup.pl           gen_solqual_lookup.pl
%mfest_bin   scripts/gen_dnamasks2colormask.pl       gen_dnamasks2colormask.pl
%mfest_bin   scripts/best_verify.pl                  best_verify.pl
%mfest_bin   scripts/colorize_fastq.pl               colorize_fastq.pl
%mfest_bin   scripts/make_hg18.sh                    make_hg18.sh
%mfest_bin   scripts/fastq_to_tabbed.pl              fastq_to_tabbed.pl
%mfest_bin   scripts/bs_mapability.pl                bs_mapability.pl
%mfest_bin   scripts/make_a_thaliana_tair.sh         make_a_thaliana_tair.sh
%mfest_bin   scripts/make_d_melanogaster_fb5_22.sh   make_d_melanogaster_fb5_22.sh


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
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
%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 0.12.7-2
- use MANIFEST.EUPATH
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.