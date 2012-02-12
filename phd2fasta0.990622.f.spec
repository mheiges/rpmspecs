%define _pkg_base phd2fasta

Summary: Phd2fasta reads phd files from phred and consed
Name: %{_pkg_base}-%{version}
Version: 0.990622.f
Release: 1%{?dist}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0111 phd2fasta %{_install_dir}
install -m 0644 PHD2FASTA.DOC %{_install_dir}
install -m 0644 INSTALL %{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/phd2fasta

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
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
%dir %{_install_dir}
%{_install_dir}/phd2fasta
%{_install_dir}/PHD2FASTA.DOC
%{_install_dir}/INSTALL

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/phd2fasta
%{_install_dir}/__bin__/ReadMe


%changelog
* Sat Feb 4 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
