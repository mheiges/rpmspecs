%define _pkg_base phred

Summary: Single, simple example file
Name: %{_pkg_base}-%{version}
Version: 0.020425.c
Release: 5%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: phred-dist-020425.c-acd.tar.Z

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
An example RPM of no substance.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c %{name}

%build
make CFLAGS="-O3 -DANSI_C -DX86_GCC_LINUX"
make daev CFLAGS="-O3 -DANSI_C -DX86_GCC_LINUX"

%install
%{__rm} -rf %{buildroot}

%define bundle_profile_dir  %{_pre_install_dir}/__profile__

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{bundle_profile_dir}
install -m 0755 -d %{bundle_lib_dir}

install -m 0711 phred %{_pre_install_dir}
install -m 0711 daev %{_pre_install_dir}

install -m 0644 phredpar.dat %{_pre_install_dir}
install -m 0644 INSTALL %{_pre_install_dir}
install -m 0644 NEWS %{_pre_install_dir}
install -m 0644 PHRED.DOC %{_pre_install_dir}
install -m 0644 DAEV.DOC %{_pre_install_dir}

install -m 0644 phredpar.dat %{bundle_lib_dir}

cat <<EOF >  %{bundle_profile_dir}/phred.sh
export PHRED_PARAMETER_FILE=%{_pre_install_dir}/phredpar.dat
EOF

%mfest_bin       daev                              
%mfest_bin       phred                              
%mfest_profile   __profile__/phred.sh phred.sh
%mfest_lib       phredpar.dat

%post
cat <<EOF >  %{_post_install_dir}/__profile__/phred.sh
export PHRED_PARAMETER_FILE=%{_post_install_dir}/phredpar.dat
EOF

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%{_install_dir}/daev
%{_install_dir}/phred
%{_install_dir}/phredpar.dat 
%{_install_dir}/INSTALL
%{_install_dir}/NEWS
%{_install_dir}/PHRED.DOC
%{_install_dir}/DAEV.DOC

%dir %{_install_dir}/__profile__
%{_install_dir}/__profile__/phred.sh

%{_install_dir}/%{_manifest_file}

%changelog
* Fri Feb 24 2012 Mark Heiges <mheiges@uga.edu> 0.020425.c-5
- fix profile in MANIFEST
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 0.020425.c-4
- add MANIFEST.EUPATH
* Thu Feb 9 2012 Mark Heiges <mheiges@uga.edu> 0.020425.c-3
- fix $PHRED_PARAMETER_FILE
* Tue Feb 7 2012 Mark Heiges <mheiges@uga.edu> 0.020425.c-2
- clean up profile directory management
* Sat Feb 4 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
