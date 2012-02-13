%define _pkg_base mavid

Summary: multiple DNA sequence alignment program
Name: %{_pkg_base}-%{version}
Version: 2.0.4
Release: 2%{?dist}
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

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{_pre_install_dir}/examples
install -m 0755 -d %{_pre_install_dir}/mavid
install -m 0755 -d %{_pre_install_dir}/utils
install -m 0755 -d %{_pre_install_dir}/utils/checkfasta
install -m 0755 -d %{_pre_install_dir}/utils/cut_alignment
install -m 0755 -d %{_pre_install_dir}/utils/extract_seq
install -m 0755 -d %{_pre_install_dir}/utils/extract_tree
install -m 0755 -d %{_pre_install_dir}/utils/fasta2phylip
install -m 0755 -d %{_pre_install_dir}/utils/phylip2fasta
install -m 0755 -d %{_pre_install_dir}/utils/project_alignment
install -m 0755 -d %{_pre_install_dir}/utils/randtree
install -m 0755 -d %{_pre_install_dir}/utils/root_tree
install -m 0755 -d %{_pre_install_dir}/utils/translate_coords
install -m 0755 -d %{_pre_install_dir}/utils/tree_dists

install -m 0755 mavid/mavid %{_pre_install_dir}/mavid
install -m 0755 mavid/mavid.pl %{_pre_install_dir}/mavid
install -m 0755 utils/checkfasta/checkfasta %{_pre_install_dir}/utils/checkfasta
install -m 0755 utils/cut_alignment/cut_alignment %{_pre_install_dir}/utils/cut_alignment
install -m 0755 utils/extract_seq/extract_seq %{_pre_install_dir}/utils/extract_seq
install -m 0755 utils/extract_tree/extract_tree %{_pre_install_dir}/utils/extract_tree
install -m 0755 utils/fasta2phylip/fasta2phylip %{_pre_install_dir}/utils/fasta2phylip
install -m 0755 utils/phylip2fasta/phylip2fasta %{_pre_install_dir}/utils/phylip2fasta
install -m 0755 utils/project_alignment/project_alignment %{_pre_install_dir}/utils/project_alignment
install -m 0755 utils/randtree/randtree %{_pre_install_dir}/utils/randtree
install -m 0755 utils/root_tree/root_tree %{_pre_install_dir}/utils/root_tree
install -m 0755 utils/tree_dists/tree_dists %{_pre_install_dir}/utils/tree_dists

install -m 0644 INSTALL %{_pre_install_dir}
install -m 0644 mavid/README %{_pre_install_dir}/mavid
install -m 0644 Copyright %{_pre_install_dir}
install -m 0644 examples/unrooted_tree %{_pre_install_dir}/examples
install -m 0644 examples/seqs %{_pre_install_dir}/examples
install -m 0644 examples/seqs.masked %{_pre_install_dir}/examples
install -m 0644 examples/tree %{_pre_install_dir}/examples
install -m 0644 examples/README %{_pre_install_dir}/examples

%mfest_bin  mavid/mavid                                mavid
%mfest_bin  mavid/mavid.pl                             mavid.pl
%mfest_bin  utils/project_alignment/project_alignment  project_alignment
%mfest_bin  utils/randtree/randtree                    randtree
%mfest_bin  utils/root_tree/root_tree                  root_tree
%mfest_bin  utils/fasta2phylip/fasta2phylip            fasta2phylip
%mfest_bin  utils/extract_seq/extract_seq              extract_seq
%mfest_bin  utils/tree_dists/tree_dists                tree_dists
%mfest_bin  utils/checkfasta/checkfasta                checkfasta
%mfest_bin  utils/cut_alignment/cut_alignment          cut_alignment
%mfest_bin  utils/extract_tree/extract_tree            extract_tree
%mfest_bin  utils/phylip2fasta/phylip2fasta            phylip2fasta

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)

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

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2.0.4-2
- use MANIFEST.EUPATH
* Thu Feb 2 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
