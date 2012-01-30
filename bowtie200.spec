%define pkg_base bowtie

Summary: bowtie is a short read aligner for short DNA sequences
Name: %{pkg_base}-%{version}
Version: 2.0.0b5
%define pkg_version 2.0.0-beta5
Release: 1%{?dist}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}

cp -a doc %{install_dir}
cp -a example %{install_dir}
cp -a scripts %{install_dir}
install -m 0755 bowtie2 %{install_dir}
install -m 0755 bowtie2-inspect %{install_dir}
install -m 0755 bowtie2-build %{install_dir}
install -m 0755 bowtie2-align %{install_dir}
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
# for i in $(find bowtie2 bowtie2-build bowtie2-align bowtie2-inspect scripts/ -type f -print); do echo "ln -s %{ln_path}/$i"; done; 
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/bowtie2
ln -s %{ln_path}/bowtie2-build
ln -s %{ln_path}/bowtie2-align
ln -s %{ln_path}/bowtie2-inspect
ln -s %{ln_path}/scripts/gen_occ_lookup.pl
ln -s %{ln_path}/scripts/convert_quals.pl
ln -s %{ln_path}/scripts/make_s_cerevisiae.sh
ln -s %{ln_path}/scripts/make_h_sapiens_ncbi36.sh
ln -s %{ln_path}/scripts/make_hg19.sh
ln -s %{ln_path}/scripts/gen_2b_occ_lookup.pl
ln -s %{ln_path}/scripts/make_e_coli.sh
ln -s %{ln_path}/scripts/infer_fraglen.pl
ln -s %{ln_path}/scripts/make_h_sapiens_ncbi37.sh
ln -s %{ln_path}/scripts/make_rn4.sh
ln -s %{ln_path}/scripts/make_b_taurus_UMD3.sh
ln -s %{ln_path}/scripts/make_mm9.sh
ln -s %{ln_path}/scripts/make_canFam2.sh
ln -s %{ln_path}/scripts/make_c_elegans_ws200.sh
ln -s %{ln_path}/scripts/make_m_musculus_ncbi37.sh
ln -s %{ln_path}/scripts/gen_solqual_lookup.pl
ln -s %{ln_path}/scripts/make_hg18.sh
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
%dir %{install_dir}/doc
%dir %{install_dir}/example
%dir %{install_dir}/scripts
%dir %{install_dir}/example/reads
%dir %{install_dir}/example/reference
%dir %{install_dir}/example/index

%{install_dir}/bowtie2
%{install_dir}/bowtie2-inspect
%{install_dir}/bowtie2-align
%{install_dir}/bowtie2-build
%{install_dir}/AUTHORS
%{install_dir}/COPYING
%{install_dir}/MANUAL
%{install_dir}/MANUAL.markdown
%{install_dir}/NEWS
%{install_dir}/TUTORIAL
%{install_dir}/VERSION
# for i in $(find doc example scripts -type f -print); do echo "%{install_dir}/$i"; done;
%{install_dir}/doc/style.css
%{install_dir}/doc/strip_markdown.pl
%{install_dir}/doc/manual.html
%{install_dir}/doc/README
%{install_dir}/example/reads/longreads.fq
%{install_dir}/example/reads/reads_1.fq
%{install_dir}/example/reads/reads_2.fq
%{install_dir}/example/reads/simulate.pl
%{install_dir}/example/index/lambda_virus.3.bt2
%{install_dir}/example/index/lambda_virus.rev.1.bt2
%{install_dir}/example/index/lambda_virus.4.bt2
%{install_dir}/example/index/lambda_virus.2.bt2
%{install_dir}/example/index/lambda_virus.1.bt2
%{install_dir}/example/index/lambda_virus.rev.2.bt2
%{install_dir}/example/reference/lambda_virus.fa
%{install_dir}/scripts/gen_occ_lookup.pl
%{install_dir}/scripts/convert_quals.pl
%{install_dir}/scripts/make_s_cerevisiae.sh
%{install_dir}/scripts/make_h_sapiens_ncbi36.sh
%{install_dir}/scripts/make_hg19.sh
%{install_dir}/scripts/gen_2b_occ_lookup.pl
%{install_dir}/scripts/make_e_coli.sh
%{install_dir}/scripts/infer_fraglen.pl
%{install_dir}/scripts/make_h_sapiens_ncbi37.sh
%{install_dir}/scripts/make_rn4.sh
%{install_dir}/scripts/make_b_taurus_UMD3.sh
%{install_dir}/scripts/make_mm9.sh
%{install_dir}/scripts/make_canFam2.sh
%{install_dir}/scripts/make_c_elegans_ws200.sh
%{install_dir}/scripts/make_m_musculus_ncbi37.sh
%{install_dir}/scripts/gen_solqual_lookup.pl
%{install_dir}/scripts/make_hg18.sh
%{install_dir}/scripts/make_a_thaliana_tair.sh
%{install_dir}/scripts/make_d_melanogaster_fb5_22.sh


%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/bowtie2
%{install_dir}/__bin__/bowtie2-build
%{install_dir}/__bin__/bowtie2-inspect
%{install_dir}/__bin__/bowtie2-align
%{install_dir}/__bin__/gen_occ_lookup.pl
%{install_dir}/__bin__/convert_quals.pl
%{install_dir}/__bin__/make_s_cerevisiae.sh
%{install_dir}/__bin__/make_h_sapiens_ncbi36.sh
%{install_dir}/__bin__/make_hg19.sh
%{install_dir}/__bin__/gen_2b_occ_lookup.pl
%{install_dir}/__bin__/make_e_coli.sh
%{install_dir}/__bin__/infer_fraglen.pl
%{install_dir}/__bin__/make_h_sapiens_ncbi37.sh
%{install_dir}/__bin__/make_rn4.sh
%{install_dir}/__bin__/make_b_taurus_UMD3.sh
%{install_dir}/__bin__/make_mm9.sh
%{install_dir}/__bin__/make_canFam2.sh
%{install_dir}/__bin__/make_c_elegans_ws200.sh
%{install_dir}/__bin__/make_m_musculus_ncbi37.sh
%{install_dir}/__bin__/gen_solqual_lookup.pl
%{install_dir}/__bin__/make_hg18.sh
%{install_dir}/__bin__/make_a_thaliana_tair.sh
%{install_dir}/__bin__/make_d_melanogaster_fb5_22.sh

%changelog
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.