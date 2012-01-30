%define pkg_base clustalw

Summary:  CLUSTAL W Multiple Sequence Alignment Program
Name: %{pkg_base}-%{version}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{install_dir}
install -m 0755 -d %{install_dir}/doc

install -m 0755 clustalw %{install_dir}

install -m 0644 clustalv.doc %{install_dir}/doc
install -m 0644 clustalw_help %{install_dir}/doc
install -m 0644 clustalw.doc %{install_dir}/doc
install -m 0644 clustalw.ms %{install_dir}/doc
install -m 0644 coldna.par %{install_dir}
install -m 0644 colprint.par %{install_dir}
install -m 0644 colprot.par %{install_dir}
install -m 0644 globin.pep %{install_dir}
install -m 0644 gon90.bla %{install_dir}
install -m 0644 matrixseries.gon %{install_dir}
install -m 0644 phcolor.par %{install_dir}
install -m 0644 README %{install_dir}/doc

## precompiled COFF format alpha executable, not supported on our systems
#install -m 0644 njplot/test.ph %{install_dir}/njplot
#install -m 0644 njplot/bigtest.phb %{install_dir}/njplot
#install -m 0644 njplot/njplot.alpha %{install_dir}/njplot
#install -m 0644 njplot/njplot.help %{install_dir}/njplot
#install -m 0644 njplot/unrooted.alpha %{install_dir}/njplot
#install -m 0644 njplot/README %{install_dir}/njplot

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
install -m 0755 -d %{bundle_bin_dir}
cd %{bundle_bin_dir}
ln -s %{ln_path}/clustalw

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to .cp -p ../../../bin (say, by Puppet %{install_dir}
or other non-RPM methods).
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
%dir %{install_dir}
%dir %{install_dir}/doc
%{install_dir}/clustalw
%{install_dir}/coldna.par
%{install_dir}/colprint.par
%{install_dir}/colprot.par
%{install_dir}/doc/README
%{install_dir}/doc/clustalv.doc
%{install_dir}/doc/clustalw.doc
%{install_dir}/doc/clustalw.ms
%{install_dir}/doc/clustalw_help
%{install_dir}/globin.pep
%{install_dir}/gon90.bla
%{install_dir}/matrixseries.gon
%{install_dir}/phcolor.par

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/clustalw
%{install_dir}/__bin__/ReadMe


%changelog
* Fri Jan 27 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
