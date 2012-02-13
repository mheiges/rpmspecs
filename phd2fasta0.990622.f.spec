%define _pkg_base phd2fasta

Summary: Phd2fasta reads phd files from phred and consed
Name: %{_pkg_base}-%{version}
Version: 0.990622.f
Release: 2%{?dist}
License: Custom
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

# source provided by email from Brent Ewing <bge@u.washington.edu>
# 	Subject: 	phred distribution
#	Date: 	February 4, 2012 4:23:36 PM EST
#	To: 	Mark Heiges <mheiges@uga.edu>
Source0: phd2fasta-acd-dist.tar.Z

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The phred software reads DNA sequencing trace files, calls bases, and 
assigns a quality value to each called base. Phred works well with 
trace files from the following manufacturers' sequencing machines: 
Amersham Biosciences, Applied Biosystems, Beckman Instruments, and 
LI-COR Life Sciences.
http://www.phrap.org/phredphrapconsed.html

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c phd2fasta-acd-dist-%{version}

%build
make

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
install -m 0711 phd2fasta %{_pre_install_dir}
install -m 0644 PHD2FASTA.DOC %{_pre_install_dir}
install -m 0644 INSTALL %{_pre_install_dir}

%mfest_bin  phd2fasta                              


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%{_install_dir}/phd2fasta
%{_install_dir}/PHD2FASTA.DOC
%{_install_dir}/INSTALL

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 0.990622.f-2
- add MANIFEST.EUPATH
* Sat Feb 4 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
