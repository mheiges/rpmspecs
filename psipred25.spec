%define pkg_base psipred

Summary: PSIPRED protein secondary structure prediction
Name: psipred25
Version: 2.5
Release: 1%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://bioinfadmin.cs.ucl.ac.uk/downloads/psipred/psipred25.tar.gz

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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{name}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
cp -a  bin                %{install_dir}
cp -a  data               %{install_dir}
cp     LICENSE            %{install_dir}
cp     README             %{install_dir}
cp     runpsipred         %{install_dir}
cp     runpsipred_single  %{install_dir}
 

# set up symlinks. These are broken as installed and should be copied to 
# a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
cd %{bundle_bin_dir}
ln -s ../software/%{pkg_base}/%{name}/runpsipred_single
ln -s ../software/%{pkg_base}/%{name}/runpsipred
ln -s ../software/%{pkg_base}/%{name}/bin/chkparse
ln -s ../software/%{pkg_base}/%{name}/bin/pfilt
ln -s ../software/%{pkg_base}/%{name}/bin/psipass2
ln -s ../software/%{pkg_base}/%{name}/bin/psipred
ln -s ../software/%{pkg_base}/%{name}/bin/seq2mtx

%post
%define install_dir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{name}
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
%define install_dir  %{prefix}/software/%{pkg_base}/%{name}

%dir %{install_dir}
%dir %{install_dir}/data
%dir %{install_dir}/bin
%dir %{install_dir}/__bin__

%{install_dir}/data/weights.dat3
%{install_dir}/data/weights.dat
%{install_dir}/data/weights.dat2
%{install_dir}/data/weights_p2.dat
%{install_dir}/data/weights.dat4
%{install_dir}/data/weights_s.dat
%{install_dir}/data/weights_s.dat2
%{install_dir}/data/weights_s.dat3
%{install_dir}/bin/psipass2
%{install_dir}/bin/pfilt
%{install_dir}/bin/seq2mtx
%{install_dir}/bin/psipred
%{install_dir}/runpsipred
%{install_dir}/README
%{install_dir}/runpsipred_single
%{install_dir}/LICENSE
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