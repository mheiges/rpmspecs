%define pkg_base blat

Summary: BLAST-Like Alignment Tool
Name: blat34
Version: 34
Release: 1%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://users.soe.ucsc.edu/~kent/src/blatSrc34.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BLAST-Like Alignment Tool

%prep
%setup -q -n blatSrc

%build
export MACHTYPE=%{_arch}
export BINDIR=%{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
mkdir -p $BINDIR
make

%install
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}

# set up symlinks. These are broken as installed and should be copied to 
# a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/blat
ln -s %{ln_path}/faToNib
ln -s %{ln_path}/faToTwoBit
ln -s %{ln_path}/gfClient
ln -s %{ln_path}/gfServer
ln -s %{ln_path}/nibFrag
ln -s %{ln_path}/pslPretty
ln -s %{ln_path}/pslReps
ln -s %{ln_path}/pslSort
ln -s %{ln_path}/twoBitInfo
ln -s %{ln_path}/twoBitToFa

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

# for i in $(find . -type f -printf '%P\n'); do echo "%{install_dir}/$i"; done;
%{install_dir}/gfServer
%{install_dir}/blat
%{install_dir}/faToNib
%{install_dir}/pslPretty
%{install_dir}/nibFrag
%{install_dir}/pslReps
%{install_dir}/twoBitInfo
%{install_dir}/gfClient
%{install_dir}/twoBitToFa
%{install_dir}/faToTwoBit
%{install_dir}/pslSort

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
#  for i in $(find . -type f -printf '%P\n'); do echo "%{install_dir}/__bin__/$i"; done;
%{install_dir}/__bin__/gfServer
%{install_dir}/__bin__/blat
%{install_dir}/__bin__/faToNib
%{install_dir}/__bin__/pslPretty
%{install_dir}/__bin__/nibFrag
%{install_dir}/__bin__/pslReps
%{install_dir}/__bin__/twoBitInfo
%{install_dir}/__bin__/gfClient
%{install_dir}/__bin__/twoBitToFa
%{install_dir}/__bin__/faToTwoBit
%{install_dir}/__bin__/pslSort


%changelog
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.