%define _pkg_base psipred

Summary: PSIPRED protein secondary structure prediction
Name: %{_pkg_base}-%{version}
Version: 3.21
Release: 2%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://bioinfadmin.cs.ucl.ac.uk/downloads/psipred/psipred321.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PSIPRED is a  simple and accurate secondary structure prediction method, incorporating two feed-forward neural networks which perform an analysis on output obtained from PSI-BLAST

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c %{name}-%{version}


%build
cd src
make
make install

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
cp -a  bin                %{_pre_install_dir}
cp -a  BLAST+             %{_pre_install_dir}
cp -a  data               %{_pre_install_dir}
cp     example.fasta      %{_pre_install_dir}
cp     example.horiz      %{_pre_install_dir}
cp     example.ss         %{_pre_install_dir}
cp     example.ss2        %{_pre_install_dir}
cp     LICENSE            %{_pre_install_dir}
cp     README             %{_pre_install_dir}
cp     runpsipred         %{_pre_install_dir}
cp     runpsipred_single  %{_pre_install_dir}
 
%mfest_bin  runpsipred_single     
%mfest_bin  runpsipred            
%mfest_bin  bin/chkparse          chkparse
%mfest_bin  bin/pfilt             pfilt
%mfest_bin  bin/psipass2          psipass2
%mfest_bin  bin/psipred           psipred
%mfest_bin  bin/seq2mtx           seq2mtx


%post
cd %{_post_install_dir}

# patch paths
sed -i  "s|^set datadir.*|set datadir = %{_post_install_dir}/data|" runpsipred_single
sed -i  "s|^set execdir.*|set execdir = %{_post_install_dir}/bin|" runpsipred_single

sed -i  "s|^set dbname.*|set execdir = \$2|" runpsipred
sed -i  "s|^set ncbidir.*|set ncbidir = $RPM_INSTALL_PREFIX0/%{_software_topdir}/ncbi-blast2/ncbi-blast2-2.2.8|" runpsipred
sed -i  "s|^set execdir.*|set execdir = %{_install_dir}/bin|" runpsipred
sed -i  "s|^set datadir.*|set datadir = %{_install_dir}/data|" runpsipred


%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root)

%dir %{_install_dir}
%dir %{_install_dir}/BLAST+
%dir %{_install_dir}/data
%dir %{_install_dir}/bin

%{_install_dir}/example.fasta
%{_install_dir}/BLAST+/README
%{_install_dir}/BLAST+/runpsipredplus
%{_install_dir}/data/weights.dat3
%{_install_dir}/data/weights.dat
%{_install_dir}/data/weights.dat2
%{_install_dir}/data/weights_p2.dat
%{_install_dir}/example.ss2
%{_install_dir}/bin/psipass2
%{_install_dir}/bin/pfilt
%{_install_dir}/bin/chkparse
%{_install_dir}/bin/seq2mtx
%{_install_dir}/bin/psipred
%{_install_dir}/runpsipred
%{_install_dir}/README
%{_install_dir}/runpsipred_single
%{_install_dir}/LICENSE
%{_install_dir}/example.horiz
%{_install_dir}/example.ss

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 3.21-2
- add MANIFEST.EUPATH
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
