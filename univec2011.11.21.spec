%define _pkg_base univec

Summary: DNA vector sequences from NCBI's UniVec_Core
Name: %{_pkg_base}-%{version}
Version: 2011.11.21
Release: 2%{?dist}
License: Unknown
Group: Application/Bioinformatics
BuildArch: x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: ftp://ftp.ncbi.nih.gov/pub/UniVec/UniVec_Core
Source1: ftp://ftp.ncbi.nih.gov/pub/UniVec/UniVec
Source2: ftp://ftp.ncbi.nih.gov/pub/UniVec/README.uv

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
DNA vector sequences from NCBI's UniVec_Core

%prep
%eupa_validate_workflow_pkg_name
rm -rf %{_builddir}/%{name}
mkdir %{_builddir}/%{name}
cp %{_sourcedir}/UniVec %{_builddir}/%{name}
cp %{_sourcedir}/UniVec_Core %{_builddir}/%{name}
cp %{_sourcedir}/README.uv %{_builddir}/%{name}

%build

%install
%{__rm} -rf %{buildroot}

cd %{_builddir}/%{name}
install -m 0755 -d %{_pre_install_dir}

install -m 0644 UniVec  %{_pre_install_dir}
install -m 0644 UniVec_Core %{_pre_install_dir}
install -m 0644 README.uv %{_pre_install_dir}

%mfest_lib UniVec_Core screenLibs/vector.seq

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}

%{_install_dir}/UniVec
%{_install_dir}/UniVec_Core
%{_install_dir}/README.uv

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2011.11.21-2
- updated to use eupath macros
* Wed Feb 8 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
