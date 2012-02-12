%define _pkg_base phred

Summary: Single, simple example file
Name: %{_pkg_base}-%{version}
Version: 0.020425.c
Release: 3%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: phred-dist-020425.c-acd.tar.Z

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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__
%define bundle_profile_dir  %{_install_dir}/__profile__
%define bundle_lib_dir  %{_install_dir}/__lib__

install -m 0755 -d %{_install_dir}
install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{bundle_profile_dir}
install -m 0755 -d %{bundle_lib_dir}

install -m 0711 phred %{_install_dir}
install -m 0711 daev %{_install_dir}

install -m 0644 phredpar.dat %{_install_dir}
install -m 0644 phredpar.dat %{bundle_lib_dir}
install -m 0644 INSTALL %{_install_dir}
install -m 0644 NEWS %{_install_dir}
install -m 0644 PHRED.DOC %{_install_dir}
install -m 0644 DAEV.DOC %{_install_dir}

cat <<EOF >  %{bundle_profile_dir}/phred.sh
export PHRED_PARAMETER_FILE=%{_install_dir}/phredpar.dat
EOF

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
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
%define _install_dir $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}/%{version}
cat <<EOF >  %{_install_dir}/__profile__/phred.sh
export PHRED_PARAMETER_FILE=%{_install_dir}/phredpar.dat
EOF

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
%{_install_dir}/daev
%{_install_dir}/phred
%{_install_dir}/phredpar.dat 
%{_install_dir}/INSTALL
%{_install_dir}/NEWS
%{_install_dir}/PHRED.DOC
%{_install_dir}/DAEV.DOC

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/phred
%{_install_dir}/__bin__/daev
%{_install_dir}/__bin__/ReadMe

%dir %{_install_dir}/__profile__
%{_install_dir}/__profile__/phred.sh

%dir %{_install_dir}/__lib__
%{_install_dir}/__lib__/phredpar.dat

%changelog
* Thu Feb 9 2012 Mark Heiges <mheiges@uga.edu> 0.071220.c-3
- fix $PHRED_PARAMETER_FILE
* Tue Feb 7 2012 Mark Heiges <mheiges@uga.edu> 0.020425.c-2
- clean up profile directory management
* Sat Feb 4 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
