%define _pkg_base univec

Summary: DNA vector sequences from NCBI's UniVec_Core
Name: %{_pkg_base}-%{version}
Version: 2011.11.21
Release: 1%{?dist}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}

cd %{_builddir}/%{name}
install -m 0755 -d %{_install_dir}

install -m 0644 UniVec  %{_install_dir}
install -m 0644 UniVec_Core %{_install_dir}
install -m 0644 README.uv %{_install_dir}

cat << EOF > %{_install_dir}/MANIFEST.EUPATH
software/%{_pkg_base}/%{version}/UniVec_Core,lib/screenLibs/vector.seq
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
%{_install_dir}/UniVec
%{_install_dir}/UniVec_Core
%{_install_dir}/README.uv
%{_install_dir}/MANIFEST.EUPATH


%changelog
* Wed Feb 8 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
