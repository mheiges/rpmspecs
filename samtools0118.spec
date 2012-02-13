%define _pkg_base samtools

Summary: Utilities for manipulating SAM formated DNA sequence alignments.
Name: %{_pkg_base}-%{version}
Version: 0.1.18
Release: 2%{?dist}
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
install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{_pre_install_dir}/bcftools
install -m 0755 -d %{_pre_install_dir}/examples
install -m 0755 -d %{_pre_install_dir}/man
install -m 0755 -d %{_pre_install_dir}/man/man1
install -m 0755 -d %{_pre_install_dir}/misc


install -m 0755 bcftools/bcftools %{_pre_install_dir}/bcftools
install -m 0755 bcftools/vcfutils.pl %{_pre_install_dir}/bcftools
install -m 0755 misc/blast2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/bowtie2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/export2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/interpolate_sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/maq2sam-long %{_pre_install_dir}/misc
install -m 0755 misc/maq2sam-short %{_pre_install_dir}/misc
install -m 0755 misc/md5fa %{_pre_install_dir}/misc
install -m 0755 misc/md5sum-lite %{_pre_install_dir}/misc
install -m 0755 misc/novo2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/psl2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/sam2vcf.pl %{_pre_install_dir}/misc
install -m 0755 misc/samtools.pl %{_pre_install_dir}/misc
install -m 0755 misc/seqtk %{_pre_install_dir}/misc
install -m 0755 misc/soap2sam.pl %{_pre_install_dir}/misc
install -m 0755 misc/varfilter.py %{_pre_install_dir}/misc
install -m 0755 misc/wgsim %{_pre_install_dir}/misc
install -m 0755 misc/wgsim_eval.pl %{_pre_install_dir}/misc
install -m 0755 misc/zoom2sam.pl %{_pre_install_dir}/misc
install -m 0755 razip %{_pre_install_dir}
install -m 0755 samtools %{_pre_install_dir}

install -m 0644 AUTHORS %{_pre_install_dir}
install -m 0644 bcftools/bcf.tex %{_pre_install_dir}/bcftools
install -m 0644 bcftools/README %{_pre_install_dir}/bcftools
install -m 0644 ChangeLog %{_pre_install_dir}
install -m 0644 COPYING %{_pre_install_dir}
install -m 0644 examples/00README.txt %{_pre_install_dir}/examples
install -m 0644 examples/ex1.fa %{_pre_install_dir}/examples
install -m 0644 examples/ex1.sam.gz %{_pre_install_dir}/examples
install -m 0644 examples/toy.fa %{_pre_install_dir}/examples
install -m 0644 examples/toy.sam %{_pre_install_dir}/examples
install -m 0644 INSTALL %{_pre_install_dir}
install -m 0644 misc/HmmGlocal.java %{_pre_install_dir}/misc
install -m 0644 NEWS %{_pre_install_dir}
install -m 0644 samtools.1 %{_pre_install_dir}/man/man1

%mfest_bin  bcftools/bcftools          bcftools
%mfest_bin  bcftools/vcfutils.pl       vcfutils.pl
%mfest_bin  misc/blast2sam.pl          blast2sam.pl
%mfest_bin  misc/bowtie2sam.pl         bowtie2sam.pl
%mfest_bin  misc/export2sam.pl         export2sam.pl
%mfest_bin  misc/interpolate_sam.pl    interpolate_sam.pl
%mfest_bin  misc/maq2sam-long          maq2sam-long
%mfest_bin  misc/maq2sam-short         maq2sam-short
%mfest_bin  misc/md5fa                 md5fa
%mfest_bin  misc/md5sum-lite           md5sum-lite
%mfest_bin  misc/novo2sam.pl           novo2sam.pl
%mfest_bin  misc/psl2sam.pl            psl2sam.pl
%mfest_bin  misc/sam2vcf.pl            sam2vcf.pl
%mfest_bin  misc/samtools.pl           samtools.pl
%mfest_bin  misc/seqtk                 seqtk
%mfest_bin  misc/soap2sam.pl           soap2sam.pl
%mfest_bin  misc/varfilter.py          varfilter.py
%mfest_bin  misc/wgsim                 wgsim
%mfest_bin  misc/wgsim_eval.pl         wgsim_eval.pl
%mfest_bin  misc/zoom2sam.pl           zoom2sam.pl
%mfest_bin  razip                      
%mfest_bin  samtools                   


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/misc
%dir %{_install_dir}/bcftools
%dir %{_install_dir}/examples
%dir %{_install_dir}/man
%dir %{_install_dir}/man/man1

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

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 0.1.18-2
- add MANIFEST.EUPATH
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
