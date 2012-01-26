%define pkg_base hmmer

Summary: biosequence analysis using hidden markov models
Name: hmmer232
Version: 2.3.2
Release: 1%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://selab.janelia.org/software/hmmer/2.3.2/hmmer-2.3.2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
HMMER is used for searching sequence databases for homologs of protein 
sequences, and for making protein sequence alignments. It implements 
methods using probabilistic models called profile hidden Markov models 
(profile HMMs).

%prep
%setup -q -n hmmer-%{version}

%build
./configure
make
make check

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

make install prefix=%{install_dir}
install -m 0755 -d %{bundle_bin_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/bin/hmmalign
ln -s %{ln_path}/bin/hmmbuild
ln -s %{ln_path}/bin/hmmcalibrate
ln -s %{ln_path}/bin/hmmconvert
ln -s %{ln_path}/bin/hmmemit
ln -s %{ln_path}/bin/hmmfetch
ln -s %{ln_path}/bin/hmmindex
ln -s %{ln_path}/bin/hmmpfam
ln -s %{ln_path}/bin/hmmsearch


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
%dir %{install_dir}/bin
%dir %{install_dir}/man
%dir %{install_dir}/man/man1

%{install_dir}/bin/hmmalign
%{install_dir}/bin/hmmbuild
%{install_dir}/bin/hmmcalibrate
%{install_dir}/bin/hmmconvert
%{install_dir}/bin/hmmemit
%{install_dir}/bin/hmmfetch
%{install_dir}/bin/hmmindex
%{install_dir}/bin/hmmpfam
%{install_dir}/bin/hmmsearch

%{install_dir}/man/man1/hmmalign.1
%{install_dir}/man/man1/hmmbuild.1
%{install_dir}/man/man1/hmmcalibrate.1
%{install_dir}/man/man1/hmmconvert.1
%{install_dir}/man/man1/hmmemit.1
%{install_dir}/man/man1/hmmer.1
%{install_dir}/man/man1/hmmfetch.1
%{install_dir}/man/man1/hmmindex.1
%{install_dir}/man/man1/hmmpfam.1
%{install_dir}/man/man1/hmmsearch.1

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/hmmalign
%{install_dir}/__bin__/hmmbuild
%{install_dir}/__bin__/hmmcalibrate
%{install_dir}/__bin__/hmmconvert
%{install_dir}/__bin__/hmmemit
%{install_dir}/__bin__/hmmfetch
%{install_dir}/__bin__/hmmindex
%{install_dir}/__bin__/hmmpfam
%{install_dir}/__bin__/hmmsearch


%changelog
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
