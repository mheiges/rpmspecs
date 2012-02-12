%define _pkg_base RMAExpress

Summary: Single, simple example file
Name: %{_pkg_base}-%{version}
Version: 1.0.5
Release: 1%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://rmaexpress.bmbolstad.com/download/RMAExpress_%{version}_src.tar.gz


# REQUIRES wxGTK-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
An example RPM of no substance.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n RMAExpress_%{version} -c RMAExpress_%{version} 

%build
make


%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}

cp -a vc.proj %{_install_dir}

cp -p COPYING %{_install_dir}
cp -p RMABasic.ico %{_install_dir}
cp -p RMADataConv %{_install_dir}
cp -p RMADataConv_MasterLOGO.ico %{_install_dir}
cp -p RMADataConv_MasterLOGO.xpm %{_install_dir}
cp -p RMADataConv.coff %{_install_dir}
cp -p RMADataConv.ico %{_install_dir}
cp -p RMADataConv.rc %{_install_dir}
cp -p RMADataConv.xpm %{_install_dir}
cp -p RMAExpress %{_install_dir}
cp -p RMAExpress_MasterLOGO.ico %{_install_dir}
cp -p RMAExpress_MasterLOGO.xpm %{_install_dir}
cp -p RMAExpress.coff %{_install_dir}
cp -p RMAExpress.ico %{_install_dir}
cp -p RMAExpress.rc %{_install_dir}
cp -p RMAExpress.xpm %{_install_dir}
cp -p RMAExpressConsole %{_install_dir}




# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/RMADataConv
ln -s %{ln_path}/RMAExpress
ln -s %{ln_path}/RMAExpressConsole

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
%dir %{_install_dir}/vc.proj

%{_install_dir}/COPYING
%{_install_dir}/RMABasic.ico
%{_install_dir}/RMADataConv
%{_install_dir}/RMADataConv_MasterLOGO.ico
%{_install_dir}/RMADataConv_MasterLOGO.xpm
%{_install_dir}/RMADataConv.coff
%{_install_dir}/RMADataConv.ico
%{_install_dir}/RMADataConv.rc
%{_install_dir}/RMADataConv.xpm
%{_install_dir}/RMAExpress
%{_install_dir}/RMAExpress_MasterLOGO.ico
%{_install_dir}/RMAExpress_MasterLOGO.xpm
%{_install_dir}/RMAExpress.coff
%{_install_dir}/RMAExpress.ico
%{_install_dir}/RMAExpress.rc
%{_install_dir}/RMAExpress.xpm
%{_install_dir}/RMAExpressConsole 
%{_install_dir}/vc.proj/RMADataConv.vcproj
%{_install_dir}/vc.proj/RMAExpress.sln
%{_install_dir}/vc.proj/RMAExpress.vcproj
%{_install_dir}/vc.proj/RMAExpressConsole.vcproj

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/RMADataConv
%{_install_dir}/__bin__/RMAExpress
%{_install_dir}/__bin__/RMAExpressConsole
%{_install_dir}/__bin__/ReadMe


%changelog
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
