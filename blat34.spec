%define _pkg_base blat

Summary: BLAST-Like Alignment Tool
Name: %{_pkg_base}-%{version}
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
%eupa_validate_workflow_pkg_name
%setup -q -n blatSrc

%build
export MACHTYPE=%{_arch}
export BINDIR=$PWD/_BUILD
mkdir $BINDIR
make


%install
%{__rm} -rf %{buildroot}
install -m 0755 -d %{buildroot}

cd _BUILD
install -m 0755 blat %{buildroot}
install -m 0755 faToNib %{buildroot}
install -m 0755 faToTwoBit %{buildroot}
install -m 0755 gfClient %{buildroot}
install -m 0755 gfServer %{buildroot}
install -m 0755 nibFrag %{buildroot}
install -m 0755 pslPretty %{buildroot}
install -m 0755 pslReps %{buildroot}
install -m 0755 pslSort %{buildroot}
install -m 0755 twoBitInfo %{buildroot}
install -m 0755 twoBitToFa %{buildroot}

%mfest_bin blat
%mfest_bin faToNib
%mfest_bin faToTwoBit
%mfest_bin gfClient
%mfest_bin gfServer
%mfest_bin nibFrag
%mfest_bin pslPretty
%mfest_bin pslReps
%mfest_bin pslSort
%mfest_bin twoBitInfo
%mfest_bin twoBitToFa

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
%{_install_dir}/gfServer
%{_install_dir}/blat
%{_install_dir}/faToNib
%{_install_dir}/pslPretty
%{_install_dir}/nibFrag
%{_install_dir}/pslReps
%{_install_dir}/twoBitInfo
%{_install_dir}/gfClient
%{_install_dir}/twoBitToFa
%{_install_dir}/faToTwoBit
%{_install_dir}/pslSort
%{_manifest_file}


%changelog
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.