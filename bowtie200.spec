%define _pkg_base bowtie

Summary: bowtie is a short read aligner for short DNA sequences
Name: %{_pkg_base}-%{version}
Version: 2.0.0b5
%define pkg_version 2.0.0-beta5
Release: 2%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/bowtie-bio/files/bowtie2/%{pkg_version}/bowtie2-%{pkg_version}.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Bowtie, an ultrafast, memory-efficient short read aligner for short DNA sequences (reads) 
from next-gen sequencers. Please cite: Langmead B, et al. Ultrafast and memory-efficient 
alignment of short DNA sequences to the human genome. Genome Biol 10:R25.


%prep
%eupa_validate_workflow_pkg_name
%setup -q -n bowtie2-%{pkg_version}

%build
make

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}

cp -a doc %{_pre_install_dir}
cp -a example %{_pre_install_dir}
cp -a scripts %{_pre_install_dir}
install -m 0755 bowtie2 %{_pre_install_dir}
install -m 0755 bowtie2-inspect %{_pre_install_dir}
install -m 0755 bowtie2-build %{_pre_install_dir}
install -m 0755 bowtie2-align %{_pre_install_dir}
install -m 0644 TUTORIAL %{_pre_install_dir}
install -m 0644 VERSION %{_pre_install_dir}
install -m 0644 NEWS %{_pre_install_dir}
install -m 0644 MANUAL.markdown %{_pre_install_dir}
install -m 0644 MANUAL %{_pre_install_dir}
install -m 0644 COPYING %{_pre_install_dir}
install -m 0644 AUTHORS %{_pre_install_dir}

%mfest_bin  bowtie2
%mfest_bin  bowtie2-build
%mfest_bin  bowtie2-align
%mfest_bin  bowtie2-inspect          
%mfest_bin  scripts/gen_occ_lookup.pl                gen_occ_lookup.pl
%mfest_bin  scripts/convert_quals.pl                 convert_quals.pl
%mfest_bin  scripts/make_s_cerevisiae.sh             make_s_cerevisiae.sh
%mfest_bin  scripts/make_h_sapiens_ncbi36.sh         make_h_sapiens_ncbi36.sh
%mfest_bin  scripts/make_hg19.sh                     make_hg19.sh
%mfest_bin  scripts/gen_2b_occ_lookup.pl             gen_2b_occ_lookup.pl
%mfest_bin  scripts/make_e_coli.sh                   make_e_coli.sh
%mfest_bin  scripts/infer_fraglen.pl                 infer_fraglen.pl
%mfest_bin  scripts/make_h_sapiens_ncbi37.sh         make_h_sapiens_ncbi37.sh
%mfest_bin  scripts/make_rn4.sh                      make_rn4.sh
%mfest_bin  scripts/make_b_taurus_UMD3.sh            make_b_taurus_UMD3.sh
%mfest_bin  scripts/make_mm9.sh                      make_mm9.sh
%mfest_bin  scripts/make_canFam2.sh                  make_canFam2.sh
%mfest_bin  scripts/make_c_elegans_ws200.sh          make_c_elegans_ws200.sh
%mfest_bin  scripts/make_m_musculus_ncbi37.sh        make_m_musculus_ncbi37.sh
%mfest_bin  scripts/gen_solqual_lookup.pl            gen_solqual_lookup.pl
%mfest_bin  scripts/make_hg18.sh                     make_hg18.sh
%mfest_bin  scripts/make_a_thaliana_tair.sh          make_a_thaliana_tair.sh
%mfest_bin  scripts/make_d_melanogaster_fb5_22.sh    make_d_melanogaster_fb5_22.sh

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)

%dir %{_install_dir}
%dir %{_install_dir}/doc
%dir %{_install_dir}/example
%dir %{_install_dir}/scripts
%dir %{_install_dir}/example/reads
%dir %{_install_dir}/example/reference
%dir %{_install_dir}/example/index

%{_install_dir}/bowtie2
%{_install_dir}/bowtie2-inspect
%{_install_dir}/bowtie2-align
%{_install_dir}/bowtie2-build
%{_install_dir}/AUTHORS
%{_install_dir}/COPYING
%{_install_dir}/MANUAL
%{_install_dir}/MANUAL.markdown
%{_install_dir}/NEWS
%{_install_dir}/TUTORIAL
%{_install_dir}/VERSION
# for i in $(find doc example scripts -type f -print); do echo "%{_install_dir}/$i"; done;
%{_install_dir}/doc/style.css
%{_install_dir}/doc/strip_markdown.pl
%{_install_dir}/doc/manual.html
%{_install_dir}/doc/README
%{_install_dir}/example/reads/longreads.fq
%{_install_dir}/example/reads/reads_1.fq
%{_install_dir}/example/reads/reads_2.fq
%{_install_dir}/example/reads/simulate.pl
%{_install_dir}/example/index/lambda_virus.3.bt2
%{_install_dir}/example/index/lambda_virus.rev.1.bt2
%{_install_dir}/example/index/lambda_virus.4.bt2
%{_install_dir}/example/index/lambda_virus.2.bt2
%{_install_dir}/example/index/lambda_virus.1.bt2
%{_install_dir}/example/index/lambda_virus.rev.2.bt2
%{_install_dir}/example/reference/lambda_virus.fa
%{_install_dir}/scripts/gen_occ_lookup.pl
%{_install_dir}/scripts/convert_quals.pl
%{_install_dir}/scripts/make_s_cerevisiae.sh
%{_install_dir}/scripts/make_h_sapiens_ncbi36.sh
%{_install_dir}/scripts/make_hg19.sh
%{_install_dir}/scripts/gen_2b_occ_lookup.pl
%{_install_dir}/scripts/make_e_coli.sh
%{_install_dir}/scripts/infer_fraglen.pl
%{_install_dir}/scripts/make_h_sapiens_ncbi37.sh
%{_install_dir}/scripts/make_rn4.sh
%{_install_dir}/scripts/make_b_taurus_UMD3.sh
%{_install_dir}/scripts/make_mm9.sh
%{_install_dir}/scripts/make_canFam2.sh
%{_install_dir}/scripts/make_c_elegans_ws200.sh
%{_install_dir}/scripts/make_m_musculus_ncbi37.sh
%{_install_dir}/scripts/gen_solqual_lookup.pl
%{_install_dir}/scripts/make_hg18.sh
%{_install_dir}/scripts/make_a_thaliana_tair.sh
%{_install_dir}/scripts/make_d_melanogaster_fb5_22.sh
%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu>  2.0.0b5-2
- use MANIFEST.EUPATH
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.