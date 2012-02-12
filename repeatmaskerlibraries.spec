%define _pkg_base example

Summary: RepeatMasker libraries
Name: %{_pkg_base}-%{version}
Version: 20110920
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://www.girinst.org/server/RepBase/protected/repeatmaskerlibraries/repeatmaskerlibraries-20110920.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Repeat libraries for the program RepeatMasker

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n Libraries

%build
echo "echo install date" `date` >> script.sh

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 script.sh %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/script.sh

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
sed -i  "s|@MACRO@|%{_install_dir}|" script.sh

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
%{_install_dir}/script.sh

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/script.sh
%{_install_dir}/__bin__/ReadMe


%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
