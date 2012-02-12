%define _pkg_base psipred

Summary: PSIPRED protein secondary structure prediction
Name: %{_pkg_base}-%{version}
Version: 3.21
Release: 1%{?dist}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
cp -a  bin                %{_install_dir}
cp -a  BLAST+             %{_install_dir}
cp -a  data               %{_install_dir}
cp     example.fasta      %{_install_dir}
cp     example.horiz      %{_install_dir}
cp     example.ss         %{_install_dir}
cp     example.ss2        %{_install_dir}
cp     LICENSE            %{_install_dir}
cp     README             %{_install_dir}
cp     runpsipred         %{_install_dir}
cp     runpsipred_single  %{_install_dir}
 

# set up symlinks. These are broken as installed and should be copied to 
# a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/runpsipred_single
ln -s %{ln_path}/runpsipred
ln -s %{ln_path}/bin/chkparse
ln -s %{ln_path}/bin/pfilt
ln -s %{ln_path}/bin/psipass2
ln -s %{ln_path}/bin/psipred
ln -s %{ln_path}/bin/seq2mtx

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF


%post
%define _install_dir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir %{_install_dir}/__bin__

cd %{_final_install_dir}

# patch paths
sed -i  "s|^set datadir.*|set datadir = %{_install_dir}/data|" runpsipred_single
sed -i  "s|^set execdir.*|set execdir = %{_install_dir}/bin|" runpsipred_single

sed -i  "s|^set dbname.*|set execdir = \$2|" runpsipred
sed -i  "s|^set ncbidir.*|set ncbidir = $RPM_INSTALL_PREFIX0/%{_software_topdir}/ncbi-blast2/ncbi-blast2-2.2.8|" runpsipred
sed -i  "s|^set execdir.*|set execdir = %{_install_dir}/bin|" runpsipred
sed -i  "s|^set datadir.*|set datadir = %{_install_dir}/data|" runpsipred


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
%dir %{_install_dir}/BLAST+
%dir %{_install_dir}/data
%dir %{_install_dir}/bin
%dir %{_install_dir}/__bin__

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
%{_install_dir}/__bin__/runpsipred_single
%{_install_dir}/__bin__/chkparse
%{_install_dir}/__bin__/pfilt
%{_install_dir}/__bin__/psipass2
%{_install_dir}/__bin__/psipred
%{_install_dir}/__bin__/runpsipred
%{_install_dir}/__bin__/seq2mtx
%{_install_dir}/__bin__/ReadMe



%changelog
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
