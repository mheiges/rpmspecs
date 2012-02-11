%define pkg_base phred

Summary: Single, simple example file
Name: %{pkg_base}-%{version}
Version: 0.071220.c
Release: 3%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: phred-dist-071220.c-acd.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
An example RPM of no substance.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c %{name}

%build
make CFLAGS="-O3 -DANSI_C -DX86_GCC_LINUX"
make daev CFLAGS="-O3 -DANSI_C -DX86_GCC_LINUX"

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__
%define bundle_profile_dir  %{install_dir}/__profile__
%define bundle_lib_dir  %{install_dir}/__lib__

install -m 0755 -d %{install_dir}
install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{bundle_profile_dir}
install -m 0755 -d %{bundle_lib_dir}

install -m 0711 phred %{install_dir}
install -m 0711 daev %{install_dir}

install -m 0644 phredpar.dat %{install_dir}
install -m 0644 phredpar.dat %{bundle_lib_dir}
install -m 0644 INSTALL %{install_dir}
install -m 0644 NEWS %{install_dir}
install -m 0644 PHRED.DOC %{install_dir}
install -m 0644 DAEV.DOC %{install_dir}

cat <<EOF >  %{bundle_profile_dir}/phred.sh
export PHRED_PARAMETER_FILE=%{install_dir}/phredpar.dat
EOF

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/daev
ln -s %{ln_path}/phred

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post
%define install_dir $RPM_INSTALL_PREFIX0/software/%{pkg_base}/%{version}
cat <<EOF >  %{install_dir}/__profile__/phred.sh
export PHRED_PARAMETER_FILE=%{install_dir}/phredpar.dat
EOF

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
%{install_dir}/daev
%{install_dir}/phred
%{install_dir}/phredpar.dat 
%{install_dir}/INSTALL
%{install_dir}/NEWS
%{install_dir}/PHRED.DOC
%{install_dir}/DAEV.DOC

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/phred
%{install_dir}/__bin__/daev
%{install_dir}/__bin__/ReadMe

%dir %{install_dir}/__profile__
%{install_dir}/__profile__/phred.sh

%dir %{install_dir}/__lib__
%{install_dir}/__lib__/phredpar.dat

%changelog
* Thu Feb 9 2012 Mark Heiges <mheiges@uga.edu> 0.071220.c-3
- fix $PHRED_PARAMETER_FILE
* Tue Feb 7 2012 Mark Heiges <mheiges@uga.edu> 0.071220.c-2
- clean up profile directory management
* Sat Feb 4 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
