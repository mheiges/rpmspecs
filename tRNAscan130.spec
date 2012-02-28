%define _pkg_base tRNAscan

Summary: tRNAscan-SE: An improved tool for transfer RNA detection
Name: %{_pkg_base}-%{version}
Version: 1.3
Release: 3%{?dist}
License: GPLv2
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://lowelab.ucsc.edu/software/tRNAscan-SE-%{version}.tar.gz

# patch tRNAscan-SE to use FindBin instead of fixed paths
Patch0: tRNAscan-SE-1.3.patch
Patch1: trnascan-1.4.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
tRNAscan-SE: An improved tool for transfer RNA detection

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n tRNAscan-SE-%{version}
%patch0 -p0
%patch1 -p0

%build
make
make utils

%install
%{__rm} -rf %{buildroot}

%define bundle_profile_dir  %{_pre_install_dir}/__profile__

make install BINDIR=%{_pre_install_dir}/bin LIBDIR=%{_pre_install_dir}/lib MANDIR=%{_pre_install_dir}/man
make install-utils BINDIR=%{_pre_install_dir}/bin LIBDIR=%{_pre_install_dir}/lib MANDIR=%{_pre_install_dir}/man

install -m 0755 -d %{bundle_profile_dir}
install -m 0755 -d %{_pre_install_dir}/doc
install -m 0644 README MANUAL INSTALL COPYING GNULICENSE FILES Release.history %{_pre_install_dir}/doc

install -m 0755 -d %{_pre_install_dir}/Demo
install -m 0644 Demo/* %{_pre_install_dir}/Demo

cat <<EOF >  %{bundle_profile_dir}/%{_pkg_base}.sh
export TSCAN_LIB_DIR=%{_pre_install_dir}/lib
EOF

cat <<EOF >  %{_pre_install_dir}/README.EUPATH
trnascan-1.4 is patched to use the TSCAN_LIB_DIR environment variable
to find tRNAscan's lib directory, instead of hardcoding it at compile
time.
EOF


%mfest_bin  bin/covels-SE       covels-SE                  
%mfest_bin  bin/coves-SE        coves-SE                  
%mfest_bin  bin/eufindtRNA      eufindtRNA                  
%mfest_bin  bin/reformat        reformat                  
%mfest_bin  bin/revcomp         revcomp                  
%mfest_bin  bin/seqstat         seqstat                  
%mfest_bin  bin/shuffle         shuffle                  
%mfest_bin  bin/trnascan-1.4    trnascan-1.4                  
%mfest_bin  bin/tRNAscan-SE     tRNAscan-SE                  
%mfest_profile   __profile__/%{_pkg_base}.sh %{_pkg_base}.sh


%post
cat <<EOF >  %{_post_install_dir}/__profile__/%{_pkg_base}.sh
export TSCAN_LIB_DIR=%{_post_install_dir}/lib
EOF

cat <<EOF >> %{_post_install_dir}/README.EUPATH
e.g.
    source %{_post_install_dir}/__profile__/%{_pkg_base}.sh
EOF

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/man
%dir %{_install_dir}/man/man1
%dir %{_install_dir}/bin
%dir %{_install_dir}/bin/tRNAscanSE
%dir %{_install_dir}/lib
%dir %{_install_dir}/Demo
%dir %{_install_dir}/doc
%dir %{_install_dir}/__profile__

%{_install_dir}/bin/covels-SE
%{_install_dir}/bin/coves-SE
%{_install_dir}/bin/eufindtRNA
%{_install_dir}/bin/reformat
%{_install_dir}/bin/revcomp
%{_install_dir}/bin/seqstat
%{_install_dir}/bin/shuffle
%{_install_dir}/bin/trnascan-1.4
%{_install_dir}/bin/tRNAscan-SE
%{_install_dir}/bin/tRNAscanSE/CM.pm
%{_install_dir}/bin/tRNAscanSE/Constants.pm
%{_install_dir}/bin/tRNAscanSE/Eufind.pm
%{_install_dir}/bin/tRNAscanSE/GeneticCode.pm
%{_install_dir}/bin/tRNAscanSE/LogFile.pm
%{_install_dir}/bin/tRNAscanSE/Options.pm
%{_install_dir}/bin/tRNAscanSE/ScanResult.pm
%{_install_dir}/bin/tRNAscanSE/Sequence.pm
%{_install_dir}/bin/tRNAscanSE/SS.pm
%{_install_dir}/bin/tRNAscanSE/Stats.pm
%{_install_dir}/bin/tRNAscanSE/Tscan.pm
%{_install_dir}/bin/tRNAscanSE/Utils.pm
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
%{_install_dir}/lib/Archaea-BHB-noncan.cm
%{_install_dir}/lib/Dsignal
%{_install_dir}/lib/ESELC.cm
%{_install_dir}/lib/ESELCinf-c.cm
%{_install_dir}/lib/gcode.cilnuc
%{_install_dir}/lib/gcode.echdmito
%{_install_dir}/lib/gcode.invmito
%{_install_dir}/lib/gcode.othmito
%{_install_dir}/lib/gcode.vertmito
%{_install_dir}/lib/gcode.ystmito
%{_install_dir}/lib/PSELC.cm
%{_install_dir}/lib/PSELCinf-c.cm
%{_install_dir}/lib/TPCsignal
%{_install_dir}/lib/TRNA2-arch.cm
%{_install_dir}/lib/TRNA2-archns.cm
%{_install_dir}/lib/TRNA2-bact.cm
%{_install_dir}/lib/TRNA2-bactns.cm
%{_install_dir}/lib/TRNA2-euk.cm
%{_install_dir}/lib/TRNA2-eukns.cm
%{_install_dir}/lib/TRNA2.cm
%{_install_dir}/lib/TRNA2ns.cm
%{_install_dir}/lib/TRNAinf-arch-3h-nc.cm
%{_install_dir}/lib/TRNAinf-arch-5h-nc.cm
%{_install_dir}/lib/TRNAinf-arch-c.cm
%{_install_dir}/lib/TRNAinf-arch-ns-c.cm
%{_install_dir}/lib/TRNAinf-bact-c.cm
%{_install_dir}/lib/TRNAinf-bact-ns-c.cm
%{_install_dir}/lib/TRNAinf-c.cm
%{_install_dir}/lib/TRNAinf-euk-c.cm
%{_install_dir}/lib/TRNAinf-euk-ns-c.cm
%{_install_dir}/lib/TRNAinf-ns-c.cm
%{_install_dir}/man/man1/tRNAscan-SE.1
%{_install_dir}/__profile__/%{_pkg_base}.sh
%{_install_dir}/README.EUPATH

%{_install_dir}/%{_manifest_file}


%changelog
* Fri Feb 24 2012 Mark Heiges <mheiges@uga.edu> 1.3-3
- fix profile in MANIFEST
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 1.3-2
- add MANIFEST.EUPATH
* Fri Feb 3 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
