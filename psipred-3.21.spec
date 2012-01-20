Summary: PSIPRED protein secondary structure prediction
Name: psipred
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
%setup -q -c %{name}-%{version}


%build
cd src
make
make install

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{name}/%{name}-%{version}
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
 

# set up symlinks. These are broken as installed and should be copied to a bin directory a few 
# parents up where they will be valid.
cd %{bundle_bin_dir}
ln -s ../software/%{name}/%{name}-%{version}/runpsipred_single
ln -s ../software/%{name}/%{name}-%{version}/runpsipred
ln -s ../software/%{name}/%{name}-%{version}/chkparse
ln -s ../software/%{name}/%{name}-%{version}/pfilt
ln -s ../software/%{name}/%{name}-%{version}/psipass2
ln -s ../software/%{name}/%{name}-%{version}/psipred
ln -s ../software/%{name}/%{name}-%{version}/seq2mtx

%post
%define install_dir $RPM_INSTALL_PREFIX0/software/%{name}/%{name}-%{version}
%define bundle_bin_dir %{install_dir}/__bin__

cd %{install_dir}

sed -i  "s|^set datadir.*|set datadir = %{install_dir}/data|" runpsipred_single
sed -i  "s|^set execdir.*|set execdir = %{install_dir}/bin|" runpsipred_single

sed -i  "s|^set dbname.*|set execdir = \$2|" runpsipred
sed -i  "s|^set ncbidir.*|set ncbidir = $RPM_INSTALL_PREFIX0/software/ncbi-blast2/ncbi-blast2-2.2.8|" runpsipred
sed -i  "s|^set execdir.*|set execdir = %{install_dir}/bin|" runpsipred
sed -i  "s|^set datadir.*|set datadir = %{install_dir}/data|" runpsipred


%preun
%define bin_dir $RPM_INSTALL_PREFIX0/bin

%postun
%define parent $RPM_INSTALL_PREFIX0/software/%{name}
if [ ! "$(ls -A %{parent})" ]; then
    rmdir %{parent}
fi

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root)
%define install_dir  %{prefix}/software/%{name}/%{name}-%{version}

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



%changelog
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.