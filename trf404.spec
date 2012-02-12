%define _pkg_base trf

Summary: Tandem Repeats Finder
Name: %{_pkg_base}-%{version}
Version: 4.04
Release: 2%{?dist}
License: Custom
Group: Application/Bioinformatics
BuildArch:	x86_64

Provides: trf

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://tandem.bu.edu/trf/downloads/trf404.linux64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tandem Repeats Finder is a program to locate and display tandem repeats in DNA sequences.

%prep
%eupa_validate_workflow_pkg_name
rm -rf %{_builddir}/%{name}
mkdir %{_builddir}/%{name}
cp %{_sourcedir}/trf404.linux64 %{_builddir}/%{name}/trf
# TIP: RepeatMasker depends on the exe (or a symlink) being named 'trf'

%build
# precompiled binary

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

cd %{_builddir}/%{name}
install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 trf %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/trf

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post

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
%{_install_dir}/trf

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/trf
%{_install_dir}/__bin__/ReadMe


%changelog
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu> 4.04-2
- add Provides: trf
* Fri Jan 27 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
