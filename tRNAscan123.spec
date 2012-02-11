%define pkg_base tRNAscan

Summary: tRNAscan-SE: An improved tool for transfer RNA detection
Name: %{pkg_base}-%{version}
Version: 1.23
Release: 1%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://lowelab.ucsc.edu/software/tRNAscan-SE-%{version}.tar.gz

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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

make install BINDIR=%{install_dir}/bin LIBDIR=%{install_dir}/lib MANDIR=%{install_dir}/man
make install-utils BINDIR=%{install_dir}/bin LIBDIR=%{install_dir}/lib MANDIR=%{install_dir}/man

install -m 0755 -d %{install_dir}/doc
install -m 0644 README MANUAL INSTALL COPYING GNULICENSE FILES Release.history %{install_dir}/doc

install -m 0755 -d %{install_dir}/Demo
install -m 0644 Demo/* %{install_dir}/Demo

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
install -m 0755 -d %{bundle_bin_dir}
%define ln_path ../software/%{pkg_base}/%{version}/bin
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
%dir %{install_dir}/man
%dir %{install_dir}/man/man1
%dir %{install_dir}/bin
%dir %{install_dir}/lib

%{install_dir}/bin/covels-SE
%{install_dir}/bin/coves-SE
%{install_dir}/bin/eufindtRNA
%{install_dir}/bin/reformat
%{install_dir}/bin/revcomp
%{install_dir}/bin/seqstat
%{install_dir}/bin/shuffle
%{install_dir}/bin/trnascan-1.4
%{install_dir}/bin/tRNAscan-SE
%{install_dir}/Demo/C28G1.fa
%{install_dir}/Demo/DQ6060.fa
%{install_dir}/Demo/F22B7.fa
%{install_dir}/Demo/F59C12.fa
%{install_dir}/Demo/Sprz-sub.fa
%{install_dir}/doc/COPYING
%{install_dir}/doc/FILES
%{install_dir}/doc/GNULICENSE
%{install_dir}/doc/INSTALL
%{install_dir}/doc/MANUAL
%{install_dir}/doc/README
%{install_dir}/doc/Release.history
%{install_dir}/lib/Dsignal
%{install_dir}/lib/ESELC.cm
%{install_dir}/lib/gcode.cilnuc
%{install_dir}/lib/gcode.echdmito
%{install_dir}/lib/gcode.invmito
%{install_dir}/lib/gcode.othmito
%{install_dir}/lib/gcode.vertmito
%{install_dir}/lib/gcode.ystmito
%{install_dir}/lib/PSELC.cm
%{install_dir}/lib/TPCsignal
%{install_dir}/lib/TRNA2-arch.cm
%{install_dir}/lib/TRNA2-archns.cm
%{install_dir}/lib/TRNA2-bact.cm
%{install_dir}/lib/TRNA2-bactns.cm
%{install_dir}/lib/TRNA2-euk.cm
%{install_dir}/lib/TRNA2-eukns.cm
%{install_dir}/lib/TRNA2.cm
%{install_dir}/lib/TRNA2ns.cm
%{install_dir}/man/man1/tRNAscan-SE.1

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/covels-SE
%{install_dir}/__bin__/coves-SE
%{install_dir}/__bin__/eufindtRNA
%{install_dir}/__bin__/reformat
%{install_dir}/__bin__/revcomp
%{install_dir}/__bin__/seqstat
%{install_dir}/__bin__/shuffle
%{install_dir}/__bin__/trnascan-1.4
%{install_dir}/__bin__/tRNAscan-SE



%changelog
* Fri Feb 3 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
