%define _pkg_base tRNAscan

Summary: tRNAscan-SE: An improved tool for transfer RNA detection
Name: %{_pkg_base}-%{version}
Version: 1.23
Release: 1%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://lowelab.ucsc.edu/%{_software_topdir}/tRNAscan-SE-%{version}.tar.gz

# patch tRNAscan-SE to use FindBin instead of fixed paths
Patch0: tRNAscan-SE.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
tRNAscan-SE: An improved tool for transfer RNA detection

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n tRNAscan-SE-%{version}
%patch0 -p0

%build
make
make utils

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

make install BINDIR=%{_install_dir}/bin LIBDIR=%{_install_dir}/lib MANDIR=%{_install_dir}/man
make install-utils BINDIR=%{_install_dir}/bin LIBDIR=%{_install_dir}/lib MANDIR=%{_install_dir}/man

install -m 0755 -d %{_install_dir}/doc
install -m 0644 README MANUAL INSTALL COPYING GNULICENSE FILES Release.history %{_install_dir}/doc

install -m 0755 -d %{_install_dir}/Demo
install -m 0644 Demo/* %{_install_dir}/Demo

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
install -m 0755 -d %{bundle_bin_dir}
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}/bin
cd %{bundle_bin_dir}
ln -s %{ln_path}/covels-SE
ln -s %{ln_path}/coves-SE
ln -s %{ln_path}/eufindtRNA
ln -s %{ln_path}/reformat
ln -s %{ln_path}/revcomp
ln -s %{ln_path}/seqstat
ln -s %{ln_path}/shuffle
ln -s %{ln_path}/trnascan-1.4
ln -s %{ln_path}/tRNAscan-SE

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
%dir %{_install_dir}/man
%dir %{_install_dir}/man/man1
%dir %{_install_dir}/bin
%dir %{_install_dir}/lib

%{_install_dir}/bin/covels-SE
%{_install_dir}/bin/coves-SE
%{_install_dir}/bin/eufindtRNA
%{_install_dir}/bin/reformat
%{_install_dir}/bin/revcomp
%{_install_dir}/bin/seqstat
%{_install_dir}/bin/shuffle
%{_install_dir}/bin/trnascan-1.4
%{_install_dir}/bin/tRNAscan-SE
%{_install_dir}/Demo/C28G1.fa
%{_install_dir}/Demo/DQ6060.fa
%{_install_dir}/Demo/F22B7.fa
%{_install_dir}/Demo/F59C12.fa
%{_install_dir}/Demo/Sprz-sub.fa
%{_install_dir}/doc/COPYING
%{_install_dir}/doc/FILES
%{_install_dir}/doc/GNULICENSE
%{_install_dir}/doc/INSTALL
%{_install_dir}/doc/MANUAL
%{_install_dir}/doc/README
%{_install_dir}/doc/Release.history
%{_install_dir}/lib/Dsignal
%{_install_dir}/lib/ESELC.cm
%{_install_dir}/lib/gcode.cilnuc
%{_install_dir}/lib/gcode.echdmito
%{_install_dir}/lib/gcode.invmito
%{_install_dir}/lib/gcode.othmito
%{_install_dir}/lib/gcode.vertmito
%{_install_dir}/lib/gcode.ystmito
%{_install_dir}/lib/PSELC.cm
%{_install_dir}/lib/TPCsignal
%{_install_dir}/lib/TRNA2-arch.cm
%{_install_dir}/lib/TRNA2-archns.cm
%{_install_dir}/lib/TRNA2-bact.cm
%{_install_dir}/lib/TRNA2-bactns.cm
%{_install_dir}/lib/TRNA2-euk.cm
%{_install_dir}/lib/TRNA2-eukns.cm
%{_install_dir}/lib/TRNA2.cm
%{_install_dir}/lib/TRNA2ns.cm
%{_install_dir}/man/man1/tRNAscan-SE.1

%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/covels-SE
%{_install_dir}/__bin__/coves-SE
%{_install_dir}/__bin__/eufindtRNA
%{_install_dir}/__bin__/reformat
%{_install_dir}/__bin__/revcomp
%{_install_dir}/__bin__/seqstat
%{_install_dir}/__bin__/shuffle
%{_install_dir}/__bin__/trnascan-1.4
%{_install_dir}/__bin__/tRNAscan-SE



%changelog
* Fri Feb 3 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
