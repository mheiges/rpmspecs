%define pkg_base phrap

Summary: phrap, cross_mach, swat
Name: %{pkg_base}-%{version}
Version: 0.990329
Release: 1%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

# original source file Name: %{pkg_base}-%{version}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}

install -m 0755 cluster %{install_dir}
install -m 0755 swat %{install_dir}
install -m 0755 cross_match %{install_dir}
install -m 0755 loco %{install_dir}
install -m 0755 phrap %{install_dir}
install -m 0755 phrapview %{install_dir}

install -m 0644 penalty2 %{install_dir}
install -m 0644 vector.seq %{install_dir}
install -m 0644 PAM250 %{install_dir}
install -m 0644 phrap.doc %{install_dir}
install -m 0644 makefile %{install_dir}
install -m 0644 swat.h %{install_dir}
install -m 0644 swat.doc %{install_dir}
install -m 0644 call_subs.o %{install_dir}
install -m 0644 general.doc %{install_dir}
install -m 0644 cross_match %{install_dir}
install -m 0644 cluster.o %{install_dir}
install -m 0644 mat50 %{install_dir}
install -m 0644 loco.o %{install_dir}
install -m 0644 mat70 %{install_dir}
install -m 0644 BLOSUM50 %{install_dir}
install -m 0644 BLOSUM62 %{install_dir}


# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/cluster
ln -s %{ln_path}/swat
ln -s %{ln_path}/cross_match
ln -s %{ln_path}/loco
ln -s %{ln_path}/phrap
ln -s %{ln_path}/phrapview


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

%{install_dir}/BLOSUM50
%{install_dir}/BLOSUM62
%{install_dir}/PAM250
%{install_dir}/call_subs.o
%{install_dir}/cluster
%{install_dir}/cluster.o
%{install_dir}/cross_match
%{install_dir}/general.doc
%{install_dir}/loco
%{install_dir}/loco.o
%{install_dir}/makefile
%{install_dir}/mat50
%{install_dir}/mat70
%{install_dir}/penalty2
%{install_dir}/phrap
%{install_dir}/phrap.doc
%{install_dir}/phrapview
%{install_dir}/swat
%{install_dir}/swat.doc
%{install_dir}/swat.h
%{install_dir}/vector.seq

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/cluster
%{install_dir}/__bin__/cross_match
%{install_dir}/__bin__/loco
%{install_dir}/__bin__/phrap
%{install_dir}/__bin__/phrapview
%{install_dir}/__bin__/swat


%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
