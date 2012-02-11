%define pkg_base mavid

Summary: multiple DNA sequence alignment program
Name: %{pkg_base}-%{version}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
install -m 0755 -d %{install_dir}/examples
install -m 0755 -d %{install_dir}/mavid
install -m 0755 -d %{install_dir}/utils
install -m 0755 -d %{install_dir}/utils/checkfasta
install -m 0755 -d %{install_dir}/utils/cut_alignment
install -m 0755 -d %{install_dir}/utils/extract_seq
install -m 0755 -d %{install_dir}/utils/extract_tree
install -m 0755 -d %{install_dir}/utils/fasta2phylip
install -m 0755 -d %{install_dir}/utils/phylip2fasta
install -m 0755 -d %{install_dir}/utils/project_alignment
install -m 0755 -d %{install_dir}/utils/randtree
install -m 0755 -d %{install_dir}/utils/root_tree
install -m 0755 -d %{install_dir}/utils/translate_coords
install -m 0755 -d %{install_dir}/utils/tree_dists

install -m 0755 mavid/mavid %{install_dir}/mavid
install -m 0755 mavid/mavid.pl %{install_dir}/mavid
install -m 0755 utils/checkfasta/checkfasta %{install_dir}/utils/checkfasta
install -m 0755 utils/cut_alignment/cut_alignment %{install_dir}/utils/cut_alignment
install -m 0755 utils/extract_seq/extract_seq %{install_dir}/utils/extract_seq
install -m 0755 utils/extract_tree/extract_tree %{install_dir}/utils/extract_tree
install -m 0755 utils/fasta2phylip/fasta2phylip %{install_dir}/utils/fasta2phylip
install -m 0755 utils/phylip2fasta/phylip2fasta %{install_dir}/utils/phylip2fasta
install -m 0755 utils/project_alignment/project_alignment %{install_dir}/utils/project_alignment
install -m 0755 utils/randtree/randtree %{install_dir}/utils/randtree
install -m 0755 utils/root_tree/root_tree %{install_dir}/utils/root_tree
install -m 0755 utils/tree_dists/tree_dists %{install_dir}/utils/tree_dists

install -m 0644 INSTALL %{install_dir}
install -m 0644 mavid/README %{install_dir}/mavid
install -m 0644 Copyright %{install_dir}
install -m 0644 examples/unrooted_tree %{install_dir}/examples
install -m 0644 examples/seqs %{install_dir}/examples
install -m 0644 examples/seqs.masked %{install_dir}/examples
install -m 0644 examples/tree %{install_dir}/examples
install -m 0644 examples/README %{install_dir}/examples


# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
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
%dir %{install_dir}/examples
%dir %{install_dir}/mavid
%dir %{install_dir}/utils
%dir %{install_dir}/utils/checkfasta
%dir %{install_dir}/utils/cut_alignment
%dir %{install_dir}/utils/extract_seq
%dir %{install_dir}/utils/extract_tree
%dir %{install_dir}/utils/fasta2phylip
%dir %{install_dir}/utils/phylip2fasta
%dir %{install_dir}/utils/project_alignment
%dir %{install_dir}/utils/randtree
%dir %{install_dir}/utils/root_tree
%dir %{install_dir}/utils/translate_coords
%dir %{install_dir}/utils/tree_dists

%{install_dir}/Copyright
%{install_dir}/examples/README
%{install_dir}/examples/seqs
%{install_dir}/examples/seqs.masked
%{install_dir}/examples/tree
%{install_dir}/examples/unrooted_tree
%{install_dir}/INSTALL
%{install_dir}/mavid/mavid
%{install_dir}/mavid/mavid.pl
%{install_dir}/mavid/README
%{install_dir}/utils/checkfasta/checkfasta
%{install_dir}/utils/cut_alignment/cut_alignment
%{install_dir}/utils/extract_seq/extract_seq
%{install_dir}/utils/extract_tree/extract_tree
%{install_dir}/utils/fasta2phylip/fasta2phylip
%{install_dir}/utils/phylip2fasta/phylip2fasta
%{install_dir}/utils/project_alignment/project_alignment
%{install_dir}/utils/randtree/randtree
%{install_dir}/utils/root_tree/root_tree
%{install_dir}/utils/tree_dists/tree_dists

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/mavid
%{install_dir}/__bin__/mavid.pl
%{install_dir}/__bin__/project_alignment
%{install_dir}/__bin__/randtree
%{install_dir}/__bin__/root_tree
%{install_dir}/__bin__/fasta2phylip
%{install_dir}/__bin__/extract_seq
%{install_dir}/__bin__/tree_dists
%{install_dir}/__bin__/checkfasta
%{install_dir}/__bin__/cut_alignment
%{install_dir}/__bin__/extract_tree
%{install_dir}/__bin__/phylip2fasta

%{install_dir}/__bin__/ReadMe


%changelog
* Thu Feb 2 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
