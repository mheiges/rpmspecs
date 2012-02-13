%define _pkg_base hmmer

Summary: biosequence analysis using hidden markov models
Name: %{_pkg_base}-%{version}
Version: 2.3.2
Release: 2%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://selab.janelia.org/%{_software_topdir}/hmmer/2.3.2/hmmer-2.3.2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
HMMER is used for searching sequence databases for homologs of protein 
sequences, and for making protein sequence alignments. It implements 
methods using probabilistic models called profile hidden Markov models 
(profile HMMs).

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n hmmer-%{version}

%build
./configure
make
make check

%install
%{__rm} -rf %{buildroot}

make install prefix=%{_pre_install_dir}

%mfest_bin  bin/hmmalign             hmmalign
%mfest_bin  bin/hmmbuild             hmmbuild
%mfest_bin  bin/hmmcalibrate         hmmcalibrate
%mfest_bin  bin/hmmconvert           hmmconvert
%mfest_bin  bin/hmmemit              hmmemit
%mfest_bin  bin/hmmfetch             hmmfetch
%mfest_bin  bin/hmmindex             hmmindex
%mfest_bin  bin/hmmpfam              hmmpfam
%mfest_bin  bin/hmmsearch            hmmsearch


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/bin
%dir %{_install_dir}/man
%dir %{_install_dir}/man/man1

%{_install_dir}/bin/hmmalign
%{_install_dir}/bin/hmmbuild
%{_install_dir}/bin/hmmcalibrate
%{_install_dir}/bin/hmmconvert
%{_install_dir}/bin/hmmemit
%{_install_dir}/bin/hmmfetch
%{_install_dir}/bin/hmmindex
%{_install_dir}/bin/hmmpfam
%{_install_dir}/bin/hmmsearch

%{_install_dir}/man/man1/hmmalign.1
%{_install_dir}/man/man1/hmmbuild.1
%{_install_dir}/man/man1/hmmcalibrate.1
%{_install_dir}/man/man1/hmmconvert.1
%{_install_dir}/man/man1/hmmemit.1
%{_install_dir}/man/man1/hmmer.1
%{_install_dir}/man/man1/hmmfetch.1
%{_install_dir}/man/man1/hmmindex.1
%{_install_dir}/man/man1/hmmpfam.1
%{_install_dir}/man/man1/hmmsearch.1

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2.3.2-2
- use MANIFEST.EUPATH
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
