%define _pkg_base mavid

Summary: multiple DNA sequence alignment program
Name: %{_pkg_base}-%{version}
Version: 2.0.4
Release: 1%{?dist}
License: open source
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://bio.math.berkeley.edu/mavid/download/mavid-package-2.0.4.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
MAVID is a multiple DNA sequence alignment program.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n mavid-package-%{version}

%build
make

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 -d %{_install_dir}/examples
install -m 0755 -d %{_install_dir}/mavid
install -m 0755 -d %{_install_dir}/utils
install -m 0755 -d %{_install_dir}/utils/checkfasta
install -m 0755 -d %{_install_dir}/utils/cut_alignment
install -m 0755 -d %{_install_dir}/utils/extract_seq
install -m 0755 -d %{_install_dir}/utils/extract_tree
install -m 0755 -d %{_install_dir}/utils/fasta2phylip
install -m 0755 -d %{_install_dir}/utils/phylip2fasta
install -m 0755 -d %{_install_dir}/utils/project_alignment
install -m 0755 -d %{_install_dir}/utils/randtree
install -m 0755 -d %{_install_dir}/utils/root_tree
install -m 0755 -d %{_install_dir}/utils/translate_coords
install -m 0755 -d %{_install_dir}/utils/tree_dists

install -m 0755 mavid/mavid %{_install_dir}/mavid
install -m 0755 mavid/mavid.pl %{_install_dir}/mavid
install -m 0755 utils/checkfasta/checkfasta %{_install_dir}/utils/checkfasta
install -m 0755 utils/cut_alignment/cut_alignment %{_install_dir}/utils/cut_alignment
install -m 0755 utils/extract_seq/extract_seq %{_install_dir}/utils/extract_seq
install -m 0755 utils/extract_tree/extract_tree %{_install_dir}/utils/extract_tree
install -m 0755 utils/fasta2phylip/fasta2phylip %{_install_dir}/utils/fasta2phylip
install -m 0755 utils/phylip2fasta/phylip2fasta %{_install_dir}/utils/phylip2fasta
install -m 0755 utils/project_alignment/project_alignment %{_install_dir}/utils/project_alignment
install -m 0755 utils/randtree/randtree %{_install_dir}/utils/randtree
install -m 0755 utils/root_tree/root_tree %{_install_dir}/utils/root_tree
install -m 0755 utils/tree_dists/tree_dists %{_install_dir}/utils/tree_dists

install -m 0644 INSTALL %{_install_dir}
install -m 0644 mavid/README %{_install_dir}/mavid
install -m 0644 Copyright %{_install_dir}
install -m 0644 examples/unrooted_tree %{_install_dir}/examples
install -m 0644 examples/seqs %{_install_dir}/examples
install -m 0644 examples/seqs.masked %{_install_dir}/examples
install -m 0644 examples/tree %{_install_dir}/examples
install -m 0644 examples/README %{_install_dir}/examples


# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/mavid/mavid
ln -s %{ln_path}/mavid/mavid.pl
ln -s %{ln_path}/utils/project_alignment/project_alignment
ln -s %{ln_path}/utils/randtree/randtree
ln -s %{ln_path}/utils/root_tree/root_tree
ln -s %{ln_path}/utils/fasta2phylip/fasta2phylip
ln -s %{ln_path}/utils/extract_seq/extract_seq
ln -s %{ln_path}/utils/tree_dists/tree_dists
ln -s %{ln_path}/utils/checkfasta/checkfasta
ln -s %{ln_path}/utils/cut_alignment/cut_alignment
ln -s %{ln_path}/utils/extract_tree/extract_tree
ln -s %{ln_path}/utils/phylip2fasta/phylip2fasta

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
%dir %{_install_dir}/examples
%dir %{_install_dir}/mavid
%dir %{_install_dir}/utils
%dir %{_install_dir}/utils/checkfasta
%dir %{_install_dir}/utils/cut_alignment
%dir %{_install_dir}/utils/extract_seq
%dir %{_install_dir}/utils/extract_tree
%dir %{_install_dir}/utils/fasta2phylip
%dir %{_install_dir}/utils/phylip2fasta
%dir %{_install_dir}/utils/project_alignment
%dir %{_install_dir}/utils/randtree
%dir %{_install_dir}/utils/root_tree
%dir %{_install_dir}/utils/translate_coords
%dir %{_install_dir}/utils/tree_dists

%{_install_dir}/Copyright
%{_install_dir}/examples/README
%{_install_dir}/examples/seqs
%{_install_dir}/examples/seqs.masked
%{_install_dir}/examples/tree
%{_install_dir}/examples/unrooted_tree
%{_install_dir}/INSTALL
%{_install_dir}/mavid/mavid
%{_install_dir}/mavid/mavid.pl
%{_install_dir}/mavid/README
%{_install_dir}/utils/checkfasta/checkfasta
%{_install_dir}/utils/cut_alignment/cut_alignment
%{_install_dir}/utils/extract_seq/extract_seq
%{_install_dir}/utils/extract_tree/extract_tree
%{_install_dir}/utils/fasta2phylip/fasta2phylip
%{_install_dir}/utils/phylip2fasta/phylip2fasta
%{_install_dir}/utils/project_alignment/project_alignment
%{_install_dir}/utils/randtree/randtree
%{_install_dir}/utils/root_tree/root_tree
%{_install_dir}/utils/tree_dists/tree_dists

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/mavid
%{_install_dir}/__bin__/mavid.pl
%{_install_dir}/__bin__/project_alignment
%{_install_dir}/__bin__/randtree
%{_install_dir}/__bin__/root_tree
%{_install_dir}/__bin__/fasta2phylip
%{_install_dir}/__bin__/extract_seq
%{_install_dir}/__bin__/tree_dists
%{_install_dir}/__bin__/checkfasta
%{_install_dir}/__bin__/cut_alignment
%{_install_dir}/__bin__/extract_tree
%{_install_dir}/__bin__/phylip2fasta

%{_install_dir}/__bin__/ReadMe


%changelog
* Thu Feb 2 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
