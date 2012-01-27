%define pkg_base RMAExpress

Summary: Single, simple example file
Name: RMAExpress105
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
%setup -q -n RMAExpress_%{version} -c RMAExpress_%{version} 

%build
make


%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}

cp -a vc.proj %{install_dir}

cp -p COPYING %{install_dir}
cp -p RMABasic.ico %{install_dir}
cp -p RMADataConv %{install_dir}
cp -p RMADataConv_MasterLOGO.ico %{install_dir}
cp -p RMADataConv_MasterLOGO.xpm %{install_dir}
cp -p RMADataConv.coff %{install_dir}
cp -p RMADataConv.ico %{install_dir}
cp -p RMADataConv.rc %{install_dir}
cp -p RMADataConv.xpm %{install_dir}
cp -p RMAExpress %{install_dir}
cp -p RMAExpress_MasterLOGO.ico %{install_dir}
cp -p RMAExpress_MasterLOGO.xpm %{install_dir}
cp -p RMAExpress.coff %{install_dir}
cp -p RMAExpress.ico %{install_dir}
cp -p RMAExpress.rc %{install_dir}
cp -p RMAExpress.xpm %{install_dir}
cp -p RMAExpressConsole %{install_dir}




# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
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
%dir %{install_dir}/vc.proj

%{install_dir}/COPYING
%{install_dir}/RMABasic.ico
%{install_dir}/RMADataConv
%{install_dir}/RMADataConv_MasterLOGO.ico
%{install_dir}/RMADataConv_MasterLOGO.xpm
%{install_dir}/RMADataConv.coff
%{install_dir}/RMADataConv.ico
%{install_dir}/RMADataConv.rc
%{install_dir}/RMADataConv.xpm
%{install_dir}/RMAExpress
%{install_dir}/RMAExpress_MasterLOGO.ico
%{install_dir}/RMAExpress_MasterLOGO.xpm
%{install_dir}/RMAExpress.coff
%{install_dir}/RMAExpress.ico
%{install_dir}/RMAExpress.rc
%{install_dir}/RMAExpress.xpm
%{install_dir}/RMAExpressConsole 
%{install_dir}/vc.proj/RMADataConv.vcproj
%{install_dir}/vc.proj/RMAExpress.sln
%{install_dir}/vc.proj/RMAExpress.vcproj
%{install_dir}/vc.proj/RMAExpressConsole.vcproj

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/RMADataConv
%{install_dir}/__bin__/RMAExpress
%{install_dir}/__bin__/RMAExpressConsole
%{install_dir}/__bin__/ReadMe


%changelog
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
