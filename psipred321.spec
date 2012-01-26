%define pkg_base psipred

Summary: PSIPRED protein secondary structure prediction
Name: psipred321
Version: 3.21
Release: 3%{?dist}
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
%setup -q -c %{name}-%{version}


%build
cd src
make
make install

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
cp -a  bin                %{install_dir}
cp -a  BLAST+             %{install_dir}
cp -a  data               %{install_dir}
cp     example.fasta      %{install_dir}
cp     example.horiz      %{install_dir}
cp     example.ss         %{install_dir}
cp     example.ss2        %{install_dir}
cp     LICENSE            %{install_dir}
cp     README             %{install_dir}
cp     runpsipred         %{install_dir}
cp     runpsipred_single  %{install_dir}
 

# set up symlinks. These are broken as installed and should be copied to 
# a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
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
%define install_dir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}
%define bundle_bin_dir %{install_dir}/__bin__

cd %{install_dir}

# patch paths
sed -i  "s|^set datadir.*|set datadir = %{install_dir}/data|" runpsipred_single
sed -i  "s|^set execdir.*|set execdir = %{install_dir}/bin|" runpsipred_single

sed -i  "s|^set dbname.*|set execdir = \$2|" runpsipred
sed -i  "s|^set ncbidir.*|set ncbidir = $RPM_INSTALL_PREFIX0/software/ncbi-blast2/ncbi-blast2-2.2.8|" runpsipred
sed -i  "s|^set execdir.*|set execdir = %{install_dir}/bin|" runpsipred
sed -i  "s|^set datadir.*|set datadir = %{install_dir}/data|" runpsipred


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
%dir %{install_dir}/BLAST+
%dir %{install_dir}/data
%dir %{install_dir}/bin
%dir %{install_dir}/__bin__

%{install_dir}/example.fasta
%{install_dir}/BLAST+/README
%{install_dir}/BLAST+/runpsipredplus
%{install_dir}/data/weights.dat3
%{install_dir}/data/weights.dat
%{install_dir}/data/weights.dat2
%{install_dir}/data/weights_p2.dat
%{install_dir}/example.ss2
%{install_dir}/bin/psipass2
%{install_dir}/bin/pfilt
%{install_dir}/bin/chkparse
%{install_dir}/bin/seq2mtx
%{install_dir}/bin/psipred
%{install_dir}/runpsipred
%{install_dir}/README
%{install_dir}/runpsipred_single
%{install_dir}/LICENSE
%{install_dir}/example.horiz
%{install_dir}/example.ss
%{install_dir}/__bin__/runpsipred_single
%{install_dir}/__bin__/chkparse
%{install_dir}/__bin__/pfilt
%{install_dir}/__bin__/psipass2
%{install_dir}/__bin__/psipred
%{install_dir}/__bin__/runpsipred
%{install_dir}/__bin__/seq2mtx
%{install_dir}/__bin__/ReadMe



%changelog
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu> 2.5-3
- declare __bin__/ReadMe as file instead of dir
* Sun Jan 22 2012 Mark Heiges <mheiges@uga.edu> 3.21-2
- change install path to %{prefix}/software/%{pgk_name}/%{version}
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
