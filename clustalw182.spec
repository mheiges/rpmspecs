%define _pkg_base clustalw

Summary:  CLUSTAL W Multiple Sequence Alignment Program
Name: %{_pkg_base}-%{version}
Version: 1.82
Release: 1%{?dist}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{_install_dir}
install -m 0755 -d %{_install_dir}/doc

install -m 0755 clustalw %{_install_dir}

install -m 0644 clustalv.doc %{_install_dir}/doc
install -m 0644 clustalw_help %{_install_dir}/doc
install -m 0644 clustalw.doc %{_install_dir}/doc
install -m 0644 clustalw.ms %{_install_dir}/doc
install -m 0644 coldna.par %{_install_dir}
install -m 0644 colprint.par %{_install_dir}
install -m 0644 colprot.par %{_install_dir}
install -m 0644 globin.pep %{_install_dir}
install -m 0644 gon90.bla %{_install_dir}
install -m 0644 matrixseries.gon %{_install_dir}
install -m 0644 phcolor.par %{_install_dir}
install -m 0644 README %{_install_dir}/doc

## precompiled COFF format alpha executable, not supported on our systems
#install -m 0644 njplot/test.ph %{_install_dir}/njplot
#install -m 0644 njplot/bigtest.phb %{_install_dir}/njplot
#install -m 0644 njplot/njplot.alpha %{_install_dir}/njplot
#install -m 0644 njplot/njplot.help %{_install_dir}/njplot
#install -m 0644 njplot/unrooted.alpha %{_install_dir}/njplot
#install -m 0644 njplot/README %{_install_dir}/njplot

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
install -m 0755 -d %{bundle_bin_dir}
cd %{bundle_bin_dir}
ln -s %{ln_path}/clustalw

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to .cp -p ../../../bin (say, by Puppet %{_install_dir}
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

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/clustalw
%{_install_dir}/__bin__/ReadMe


%changelog
* Fri Jan 27 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
