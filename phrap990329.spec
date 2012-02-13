%define _pkg_base phrap

Summary: phrap, cross_mach, swat
Name: %{_pkg_base}-%{version}
Version: 0.990329
Release: 3%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

Provides: cluster,swat,cross_match,loco,phrap,phrapview


%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

# original source file Name: %{_pkg_base}-%{version}
# 1/23/2012 email from Phil Green <pg@solduc.biotech.washington.edu>
# to mheiges@uga.edu
# Subject: phrap/cross_match/swat ver 0.990329 (PROGRAM CODE) 

Source0: http://software.apidb.org/source/phrap-0.990329-distrib.tar.Z
Patch0: phrapview.patch

# Patch from
# Eric Haugen ehaugen at u.washington.edu
# on Phui -- Phred Phrap Consed Autofinish Users Group mail list
# Thu Mar 8 20:43:33 PST 2007
# phrap.manyreads Segmentation fault on Red Hat Linux
# phrap version 0.990329 "gets compiled incorrectly on 64-bit Linux".
# http://mailman2.u.washington.edu/pipermail/phui/2007-March/000035.html
Patch1: phrap-64bit.patch


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
phrap is a program for assembling shotgun DNA sequence data.

cross_match is a general purpose utility for comparing any two 
DNA sequence sets using a 'banded' version of swat.

swat is a program for searching one or more DNA or protein query 
sequences, or a query profile, against a sequence database, using 
an efficient implementation of the Smith-Waterman or Needleman-Wunsch 
algorithms with linear (affine) gap penalties. For each match an 
empirical measure of statistical significance derived from the 
observed score distribution is computed.


%prep
%eupa_validate_workflow_pkg_name
%setup -q -c phrap-%{version}
%patch0 -p0
%patch1 -p0

%build
make


%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}

install -m 0711 cluster %{_pre_install_dir}
install -m 0711 swat %{_pre_install_dir}
install -m 0711 cross_match %{_pre_install_dir}
install -m 0711 loco %{_pre_install_dir}
install -m 0711 phrap %{_pre_install_dir}
install -m 0711 phrapview %{_pre_install_dir}

install -m 0644 penalty2 %{_pre_install_dir}
install -m 0644 vector.seq %{_pre_install_dir}
install -m 0644 PAM250 %{_pre_install_dir}
install -m 0644 phrap.doc %{_pre_install_dir}
install -m 0644 swat.doc %{_pre_install_dir}
install -m 0644 general.doc %{_pre_install_dir}
install -m 0644 mat50 %{_pre_install_dir}
install -m 0644 mat70 %{_pre_install_dir}
install -m 0644 BLOSUM50 %{_pre_install_dir}
install -m 0644 BLOSUM62 %{_pre_install_dir}

%mfest_bin  cluster                              
%mfest_bin  swat                              
%mfest_bin  cross_match                              
%mfest_bin  loco                              
%mfest_bin  phrap                              
%mfest_bin  phrapview                              


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}

%{_install_dir}/BLOSUM50
%{_install_dir}/BLOSUM62
%{_install_dir}/PAM250
%{_install_dir}/cluster
%{_install_dir}/cross_match
%{_install_dir}/general.doc
%{_install_dir}/loco
%{_install_dir}/mat50
%{_install_dir}/mat70
%{_install_dir}/penalty2
%{_install_dir}/phrap
%{_install_dir}/phrap.doc
%{_install_dir}/phrapview
%{_install_dir}/swat
%{_install_dir}/swat.doc
%{_install_dir}/vector.seq

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 0.990329-3
- add MANIFEST.EUPATH
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu> 0.990329-2
- add Provides
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
