%define _pkg_base mdust

Summary: Standalone low complexity ("dust") filter
Name: %{_pkg_base}-%{version}
Version: 2010.07.22
Release: 2%{?dist}
License: Artistic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/gicl/files/other/mdust.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Standalone low complexity ("dust") filter

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n mdust

%build
make

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
install -m 0755 mdust %{_pre_install_dir}
install -m 0644 LICENSE %{_pre_install_dir}
install -m 0644 README %{_pre_install_dir}

%mfest_bin mdust

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}

%{_install_dir}/mdust
%{_install_dir}/LICENSE
%{_install_dir}/README

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2010.07.22-2
- use MANIFEST.EUPATH
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.