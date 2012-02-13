%define _pkg_base blat

Summary: BLAST-Like Alignment Tool
Name: %{_pkg_base}-%{version}
Version: 34
Release: 2%{?dist}
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

%install
%{__rm} -rf %{buildroot}

export MACHTYPE=%{_arch}
export BINDIR=%{_pre_install_dir}
mkdir -p $BINDIR
make

cd  %{_pre_install_dir}
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
%rm_pkg_base_dir


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root)
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
%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu>
- use MANIFEST.EUPATH
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.