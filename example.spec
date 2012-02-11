%define _pkg_base example

Summary: Single, simple example file
Name: %{_pkg_base}-%{version}
Version: 2012.01.19
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: example-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
An example RPM of no substance.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n example-%{version}

%build
echo "echo install date" `date` >> script.sh

%install
%{__rm} -rf %{buildroot}
install -m 0755 -d %{_install_dir}
install -m 0755 script.sh %{_install_dir}
install -m 0644 data.dat %{_install_dir}
install -m 0644 example.sh %{_install_dir}

%mfest_lib data.dat screenLibs/vector.seq
%mfest_bin script.sh
%mfest_profile example.sh

%post
cd %{_final_install_dir}
sed -i  "s|@MACRO@|%{_final_install_dir}|" script.sh

%postun
# remove _pkg_base dir if empty
%define _parent $RPM_INSTALL_PREFIX0/%{_software_topdir}/%{_pkg_base}
if [ ! "$(ls -A %{_parent})" ]; then
    rmdir %{_parent}
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define _install_dir  %{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%dir %{_install_dir}
%{_install_dir}/script.sh
%{_install_dir}/example.sh
%{_install_dir}/data.dat

%{_manifest_file}

%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
