Summary: phred parameter file
Name: phredpar_dat
Version: 020425
Release: 1%{?dist}
License: Unknown
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: phredpar.dat

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
phred parameter file, containing chromatogram chemistry and instrumentation data.
This file is a repackaged copy from phred %{version} and its installation needs to 
match the version of phred used.

%prep
%eupa_validate_workflow_pkg_name
rm -rf %{_builddir}/%{name}
mkdir %{_builddir}/%{name}
cp %{_sourcedir}/phredpar.dat %{_builddir}/%{name}

%build

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/lib

cd %{_builddir}/%{name}
install -m 0755 -d %{_install_dir}
install -m 0644 phredpar.dat %{_install_dir}

%post

%postun

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define _install_dir  %{prefix}/lib
%{_install_dir}/phredpar.dat


%changelog
* Wed Feb 8 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
