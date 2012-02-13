%define _pkg_base trf

Summary: Tandem Repeats Finder
Name: %{_pkg_base}-%{version}
Version: 4.04
Release: 3%{?dist}
License: Custom
Group: Application/Bioinformatics
BuildArch:	x86_64

Provides: trf

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://tandem.bu.edu/trf/downloads/trf404.linux64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tandem Repeats Finder is a program to locate and display tandem repeats in DNA sequences.

%prep
%eupa_validate_workflow_pkg_name
rm -rf %{_builddir}/%{name}
mkdir %{_builddir}/%{name}
cp %{S:0} %{_builddir}/%{name}/trf
# TIP: RepeatMasker depends on the exe (or a symlink) being named 'trf'

%build
# precompiled binary

%install
%{__rm} -rf %{buildroot}

cd %{_builddir}/%{name}
install -m 0755 -d %{_pre_install_dir}
install -m 0755 trf %{_pre_install_dir}

%mfest_bin  trf                              

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%{_install_dir}/trf

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 4.04-3
- add MANIFEST.EUPATH
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu> 4.04-2
- add Provides: trf
* Fri Jan 27 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
