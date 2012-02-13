%define _pkg_base RMAExpress

Summary: Single, simple example file
Name: %{_pkg_base}-%{version}
Version: 1.0.5
Release: 2%{?dist}
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

install -m 0755 -d %{_pre_install_dir}

cp -a vc.proj %{_pre_install_dir}

cp -p COPYING %{_pre_install_dir}
cp -p RMABasic.ico %{_pre_install_dir}
cp -p RMADataConv %{_pre_install_dir}
cp -p RMADataConv_MasterLOGO.ico %{_pre_install_dir}
cp -p RMADataConv_MasterLOGO.xpm %{_pre_install_dir}
cp -p RMADataConv.coff %{_pre_install_dir}
cp -p RMADataConv.ico %{_pre_install_dir}
cp -p RMADataConv.rc %{_pre_install_dir}
cp -p RMADataConv.xpm %{_pre_install_dir}
cp -p RMAExpress %{_pre_install_dir}
cp -p RMAExpress_MasterLOGO.ico %{_pre_install_dir}
cp -p RMAExpress_MasterLOGO.xpm %{_pre_install_dir}
cp -p RMAExpress.coff %{_pre_install_dir}
cp -p RMAExpress.ico %{_pre_install_dir}
cp -p RMAExpress.rc %{_pre_install_dir}
cp -p RMAExpress.xpm %{_pre_install_dir}
cp -p RMAExpressConsole %{_pre_install_dir}


%mfest_bin  RMADataConv                              
%mfest_bin  RMAExpress                              
%mfest_bin  RMAExpressConsole                              

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)

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

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 1.0.5-2
- add MANIFEST.EUPATH
* Thu Jan 26 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
