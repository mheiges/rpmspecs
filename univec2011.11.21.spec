%define pkg_base univec

Summary: DNA vector sequences from NCBI's UniVec_Core
Name: %{pkg_base}-%{version}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}

cd %{_builddir}/%{name}
install -m 0755 -d %{install_dir}

install -m 0644 UniVec  %{install_dir}
install -m 0644 UniVec_Core %{install_dir}
install -m 0644 README.uv %{install_dir}

cat << EOF > %{install_dir}/MANIFEST.EUPATH
software/%{pkg_base}/%{version}/UniVec_Core,lib/screenLibs/vector.seq
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
%{install_dir}/UniVec
%{install_dir}/UniVec_Core
%{install_dir}/README.uv
%{install_dir}/MANIFEST.EUPATH


%changelog
* Wed Feb 8 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
