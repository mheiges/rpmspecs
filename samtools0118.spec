%define _pkg_base samtools

Summary: Utilities for manipulating SAM formated DNA sequence alignments.
Name: %{_pkg_base}-%{version}
Version: 0.1.18
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/samtools/files/samtools/%{version}/samtools-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
SAM Tools provide various utilities for manipulating alignments in the SAM format, including sorting, merging, indexing and generating alignments in a per-position format.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n samtools-%{version}

%build
make
make razip

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 -d %{_install_dir}/bcftools
install -m 0755 -d %{_install_dir}/examples
install -m 0755 -d %{_install_dir}/man
install -m 0755 -d %{_install_dir}/man/man1
install -m 0755 -d %{_install_dir}/misc


install -m 0755 bcftools/bcftools %{_install_dir}/bcftools
install -m 0755 bcftools/vcfutils.pl %{_install_dir}/bcftools
install -m 0755 misc/blast2sam.pl %{_install_dir}/misc
install -m 0755 misc/bowtie2sam.pl %{_install_dir}/misc
install -m 0755 misc/export2sam.pl %{_install_dir}/misc
install -m 0755 misc/interpolate_sam.pl %{_install_dir}/misc
install -m 0755 misc/maq2sam-long %{_install_dir}/misc
install -m 0755 misc/maq2sam-short %{_install_dir}/misc
install -m 0755 misc/md5fa %{_install_dir}/misc
install -m 0755 misc/md5sum-lite %{_install_dir}/misc
install -m 0755 misc/novo2sam.pl %{_install_dir}/misc
install -m 0755 misc/psl2sam.pl %{_install_dir}/misc
install -m 0755 misc/sam2vcf.pl %{_install_dir}/misc
install -m 0755 misc/samtools.pl %{_install_dir}/misc
install -m 0755 misc/seqtk %{_install_dir}/misc
install -m 0755 misc/soap2sam.pl %{_install_dir}/misc
install -m 0755 misc/varfilter.py %{_install_dir}/misc
install -m 0755 misc/wgsim %{_install_dir}/misc
install -m 0755 misc/wgsim_eval.pl %{_install_dir}/misc
install -m 0755 misc/zoom2sam.pl %{_install_dir}/misc
install -m 0755 razip %{_install_dir}
install -m 0755 samtools %{_install_dir}

install -m 0644 AUTHORS %{_install_dir}
install -m 0644 bcftools/bcf.tex %{_install_dir}/bcftools
install -m 0644 bcftools/README %{_install_dir}/bcftools
install -m 0644 ChangeLog %{_install_dir}
install -m 0644 COPYING %{_install_dir}
install -m 0644 examples/00README.txt %{_install_dir}/examples
install -m 0644 examples/ex1.fa %{_install_dir}/examples
install -m 0644 examples/ex1.sam.gz %{_install_dir}/examples
install -m 0644 examples/toy.fa %{_install_dir}/examples
install -m 0644 examples/toy.sam %{_install_dir}/examples
install -m 0644 INSTALL %{_install_dir}
install -m 0644 misc/HmmGlocal.java %{_install_dir}/misc
install -m 0644 NEWS %{_install_dir}
install -m 0644 samtools.1 %{_install_dir}/man/man1


# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/bcftools/bcftools
ln -s %{ln_path}/bcftools/vcfutils.pl
ln -s %{ln_path}/misc/blast2sam.pl
ln -s %{ln_path}/misc/bowtie2sam.pl
ln -s %{ln_path}/misc/export2sam.pl
ln -s %{ln_path}/misc/interpolate_sam.pl
ln -s %{ln_path}/misc/maq2sam-long
ln -s %{ln_path}/misc/maq2sam-short
ln -s %{ln_path}/misc/md5fa
ln -s %{ln_path}/misc/md5sum-lite
ln -s %{ln_path}/misc/novo2sam.pl
ln -s %{ln_path}/misc/psl2sam.pl
ln -s %{ln_path}/misc/sam2vcf.pl
ln -s %{ln_path}/misc/samtools.pl
ln -s %{ln_path}/misc/seqtk
ln -s %{ln_path}/misc/soap2sam.pl
ln -s %{ln_path}/misc/varfilter.py
ln -s %{ln_path}/misc/wgsim
ln -s %{ln_path}/misc/wgsim_eval.pl
ln -s %{ln_path}/misc/zoom2sam.pl
ln -s %{ln_path}/razip
ln -s %{ln_path}/samtools



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
%dir %{_install_dir}/misc
%dir %{_install_dir}/bcftools
%dir %{_install_dir}/examples

%{_install_dir}/AUTHORS
%{_install_dir}/bcftools/bcf.tex
%{_install_dir}/bcftools/bcftools
%{_install_dir}/bcftools/README
%{_install_dir}/bcftools/vcfutils.pl
%{_install_dir}/ChangeLog
%{_install_dir}/COPYING
%{_install_dir}/examples/00README.txt
%{_install_dir}/examples/ex1.fa
%{_install_dir}/examples/ex1.sam.gz
%{_install_dir}/examples/toy.fa
%{_install_dir}/examples/toy.sam
%{_install_dir}/INSTALL
%{_install_dir}/misc/blast2sam.pl
%{_install_dir}/misc/bowtie2sam.pl
%{_install_dir}/misc/export2sam.pl
%{_install_dir}/misc/HmmGlocal.java
%{_install_dir}/misc/interpolate_sam.pl
%{_install_dir}/misc/maq2sam-long
%{_install_dir}/misc/maq2sam-short
%{_install_dir}/misc/md5fa
%{_install_dir}/misc/md5sum-lite
%{_install_dir}/misc/novo2sam.pl
%{_install_dir}/misc/psl2sam.pl
%{_install_dir}/misc/sam2vcf.pl
%{_install_dir}/misc/samtools.pl
%{_install_dir}/misc/seqtk
%{_install_dir}/misc/soap2sam.pl
%{_install_dir}/misc/varfilter.py
%{_install_dir}/misc/varfilter.pyc
%{_install_dir}/misc/varfilter.pyo
%{_install_dir}/misc/wgsim
%{_install_dir}/misc/wgsim_eval.pl
%{_install_dir}/misc/zoom2sam.pl
%{_install_dir}/NEWS
%{_install_dir}/razip
%{_install_dir}/samtools
%{_install_dir}/man/man1/samtools.1

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/bcftools
%{_install_dir}/__bin__/blast2sam.pl
%{_install_dir}/__bin__/bowtie2sam.pl
%{_install_dir}/__bin__/export2sam.pl
%{_install_dir}/__bin__/interpolate_sam.pl
%{_install_dir}/__bin__/maq2sam-long
%{_install_dir}/__bin__/maq2sam-short
%{_install_dir}/__bin__/md5fa
%{_install_dir}/__bin__/md5sum-lite
%{_install_dir}/__bin__/novo2sam.pl
%{_install_dir}/__bin__/psl2sam.pl
%{_install_dir}/__bin__/razip
%{_install_dir}/__bin__/sam2vcf.pl
%{_install_dir}/__bin__/samtools
%{_install_dir}/__bin__/samtools.pl
%{_install_dir}/__bin__/seqtk
%{_install_dir}/__bin__/soap2sam.pl
%{_install_dir}/__bin__/varfilter.py
%{_install_dir}/__bin__/vcfutils.pl
%{_install_dir}/__bin__/wgsim
%{_install_dir}/__bin__/wgsim_eval.pl
%{_install_dir}/__bin__/zoom2sam.pl

%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
