%define _pkg_base clustalw

Summary:  CLUSTAL W Multiple Sequence Alignment Program
Name: %{_pkg_base}-%{version}
Version: 1.82
Release: 2%{?dist}
License: GNU Lesser General Public License
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://www.clustal.org/download/1.X/ftp-igbmc.u-strasbg.fr/pub/ClustalW/clustalw1.82.UNIX.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
CLUSTAL W is a general purpose multiple sequence alignment program for DNA or proteins

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n clustalw%{version}

%build
make

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{_pre_install_dir}/doc

install -m 0755 clustalw %{_pre_install_dir}

install -m 0644 clustalv.doc %{_pre_install_dir}/doc
install -m 0644 clustalw_help %{_pre_install_dir}/doc
install -m 0644 clustalw.doc %{_pre_install_dir}/doc
install -m 0644 clustalw.ms %{_pre_install_dir}/doc
install -m 0644 coldna.par %{_pre_install_dir}
install -m 0644 colprint.par %{_pre_install_dir}
install -m 0644 colprot.par %{_pre_install_dir}
install -m 0644 globin.pep %{_pre_install_dir}
install -m 0644 gon90.bla %{_pre_install_dir}
install -m 0644 matrixseries.gon %{_pre_install_dir}
install -m 0644 phcolor.par %{_pre_install_dir}
install -m 0644 README %{_pre_install_dir}/doc

%mfest_bin clustalw

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/doc
%{_install_dir}/clustalw
%{_install_dir}/coldna.par
%{_install_dir}/colprint.par
%{_install_dir}/colprot.par
%{_install_dir}/doc/README
%{_install_dir}/doc/clustalv.doc
%{_install_dir}/doc/clustalw.doc
%{_install_dir}/doc/clustalw.ms
%{_install_dir}/doc/clustalw_help
%{_install_dir}/globin.pep
%{_install_dir}/gon90.bla
%{_install_dir}/matrixseries.gon
%{_install_dir}/phcolor.par

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 1.82-2
- use MANIFEST.EUPATH
* Fri Jan 27 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
