%define _pkg_base signalp

Summary: SignalP predicts the presence and location of signal peptide cleavage sites in amino acid sequences
Name: %{_pkg_base}-%{version}
Version: 3.0
Release: 1%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: signalp-3.0.Linux.tar.Z
Patch0: signalp.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
SignalP predicts the presence and location of signal peptide cleavage sites 
in amino acid sequences.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n %{_pkg_base}-%{version}
%patch0 -p0

%build

%install
%{__rm} -rf %{buildroot}
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{_install_dir}
install -m 0755 -d %{_install_dir}/syn-2.0
install -m 0755 -d %{_install_dir}/how
install -m 0755 -d %{_install_dir}/hmm
install -m 0755 -d %{_install_dir}/syn-1.0
install -m 0755 -d %{_install_dir}/syn-1.1
install -m 0755 -d %{_install_dir}/mod
install -m 0755 -d %{_install_dir}/tmp
install -m 0755 -d %{_install_dir}/bin
install -m 0755 -d %{_install_dir}/test
install -m 0755 -d %{_install_dir}/syn

install -m 0711 signalp %{_install_dir}
install -m 0711 how/how_Linux %{_install_dir}/how
install -m 0711 hmm/decodeanhmm_Linux %{_install_dir}/hmm
install -m 0711 bin/combine-hmm-plp.awk %{_install_dir}/bin
install -m 0711 bin/mergeoutput.awk %{_install_dir}/bin
install -m 0711 bin/testhow %{_install_dir}/bin
install -m 0711 bin/combine-nn.awk %{_install_dir}/bin
install -m 0711 bin/in2how+fasta %{_install_dir}/bin

install -m 0444 signalp-3.0.readme %{_install_dir}
install -m 0444 syn-2.0/CS.euk.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/euk.param %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/gram+.param %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.3.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/gram-.param %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.1.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.4.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.2.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.5.syn %{_install_dir}/syn-2.0
install -m 0444 syn-1.0/CS.euk.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/euk.param %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/gram+.param %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.3.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/gram-.param %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.1.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.4.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.2.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.5.syn %{_install_dir}/syn-1.0
install -m 0444 syn-1.1/CS.euk.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.5.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/euk.param %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/gram+.param %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.5.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.5.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.3.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/gram-.param %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.5.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.1.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.4.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.2.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.5.syn %{_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.5.syn %{_install_dir}/syn-1.1
install -m 0444 mod/V.gram+.1.bsmod %{_install_dir}/mod
install -m 0444 mod/V.euk.4.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram+.4.bsmod %{_install_dir}/mod
install -m 0444 mod/V.euk.1.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram-.4.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram-.1.bsmod %{_install_dir}/mod
install -m 0444 mod/V.euk.2.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram-.2.bsmod %{_install_dir}/mod
install -m 0444 mod/V.euk.3.bsmod %{_install_dir}/mod
install -m 0444 mod/V.euk.5.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram-.5.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram+.5.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram+.2.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram+.3.bsmod %{_install_dir}/mod
install -m 0444 mod/V.gram-.3.bsmod %{_install_dir}/mod
install -m 0444 test/test5.seq %{_install_dir}/test
install -m 0444 test/test.ps %{_install_dir}/test
install -m 0444 test/test.seq %{_install_dir}/test
install -m 0444 test/test.out %{_install_dir}/test
install -m 0444 test/test.dat %{_install_dir}/test
install -m 0444 syn/CS.euk.3.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram+.5.syn %{_install_dir}/syn
install -m 0444 syn/euk.param %{_install_dir}/syn
install -m 0444 syn/CS.gram-.3.syn %{_install_dir}/syn
install -m 0444 syn/gram+.param %{_install_dir}/syn
install -m 0444 syn/SP.gram-.4.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram+.2.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram-.3.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram+.1.syn %{_install_dir}/syn
install -m 0444 syn/SP.euk.2.syn %{_install_dir}/syn
install -m 0444 syn/CS.euk.1.syn %{_install_dir}/syn
install -m 0444 syn/CS.euk.5.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram-.1.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram+.1.syn %{_install_dir}/syn
install -m 0444 syn/SP.euk.3.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram+.3.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram+.4.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram-.5.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram+.4.syn %{_install_dir}/syn
install -m 0444 syn/CS.euk.2.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram+.3.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram-.2.syn %{_install_dir}/syn
install -m 0444 syn/gram-.param %{_install_dir}/syn
install -m 0444 syn/SP.euk.5.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram-.4.syn %{_install_dir}/syn
install -m 0444 syn/SP.euk.1.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram-.1.syn %{_install_dir}/syn
install -m 0444 syn/CS.euk.4.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram-.2.syn %{_install_dir}/syn
install -m 0444 syn/SP.euk.4.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram+.2.syn %{_install_dir}/syn
install -m 0444 syn/SP.gram+.5.syn %{_install_dir}/syn
install -m 0444 syn/CS.gram-.5.syn %{_install_dir}/syn

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/signalp
ln -s %{ln_path}/how/how_Linux
ln -s %{ln_path}/hmm/decodeanhmm_Linux
ln -s %{ln_path}/bin/combine-hmm-plp.awk
ln -s %{ln_path}/bin/mergeoutput.awk
ln -s %{ln_path}/bin/testhow
ln -s %{ln_path}/bin/combine-nn.awk
ln -s %{ln_path}/bin/in2how+fasta


cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post
mkdir -p $RPM_INSTALL_PREFIX0/tmp/%{_pkg_base}
chmod 1777 $RPM_INSTALL_PREFIX0/tmp/%{_pkg_base}

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

%dir %{_install_dir}/syn-2.0
%dir %{_install_dir}/how
%dir %{_install_dir}/hmm
%dir %{_install_dir}/syn-1.0
%dir %{_install_dir}/syn-1.1
%dir %{_install_dir}/mod
%dir %{_install_dir}/tmp
%dir %{_install_dir}/bin
%dir %{_install_dir}/test
%dir %{_install_dir}/syn

%{_install_dir}/bin/combine-hmm-plp.awk
%{_install_dir}/bin/combine-nn.awk
%{_install_dir}/bin/in2how+fasta
%{_install_dir}/bin/mergeoutput.awk
%{_install_dir}/bin/testhow
%{_install_dir}/hmm/decodeanhmm_Linux
%{_install_dir}/how/how_Linux
%{_install_dir}/mod/V.euk.1.bsmod
%{_install_dir}/mod/V.euk.2.bsmod
%{_install_dir}/mod/V.euk.3.bsmod
%{_install_dir}/mod/V.euk.4.bsmod
%{_install_dir}/mod/V.euk.5.bsmod
%{_install_dir}/mod/V.gram-.1.bsmod
%{_install_dir}/mod/V.gram-.2.bsmod
%{_install_dir}/mod/V.gram-.3.bsmod
%{_install_dir}/mod/V.gram-.4.bsmod
%{_install_dir}/mod/V.gram-.5.bsmod
%{_install_dir}/mod/V.gram+.1.bsmod
%{_install_dir}/mod/V.gram+.2.bsmod
%{_install_dir}/mod/V.gram+.3.bsmod
%{_install_dir}/mod/V.gram+.4.bsmod
%{_install_dir}/mod/V.gram+.5.bsmod
%{_install_dir}/signalp
%{_install_dir}/signalp-3.0.readme
%{_install_dir}/syn-1.0/CS.euk.1.syn
%{_install_dir}/syn-1.0/CS.euk.2.syn
%{_install_dir}/syn-1.0/CS.euk.3.syn
%{_install_dir}/syn-1.0/CS.euk.4.syn
%{_install_dir}/syn-1.0/CS.euk.5.syn
%{_install_dir}/syn-1.0/CS.gram-.1.syn
%{_install_dir}/syn-1.0/CS.gram-.2.syn
%{_install_dir}/syn-1.0/CS.gram-.3.syn
%{_install_dir}/syn-1.0/CS.gram-.4.syn
%{_install_dir}/syn-1.0/CS.gram-.5.syn
%{_install_dir}/syn-1.0/CS.gram+.1.syn
%{_install_dir}/syn-1.0/CS.gram+.2.syn
%{_install_dir}/syn-1.0/CS.gram+.3.syn
%{_install_dir}/syn-1.0/CS.gram+.4.syn
%{_install_dir}/syn-1.0/CS.gram+.5.syn
%{_install_dir}/syn-1.0/euk.param
%{_install_dir}/syn-1.0/gram-.param
%{_install_dir}/syn-1.0/gram+.param
%{_install_dir}/syn-1.0/SP.euk.1.syn
%{_install_dir}/syn-1.0/SP.euk.2.syn
%{_install_dir}/syn-1.0/SP.euk.3.syn
%{_install_dir}/syn-1.0/SP.euk.4.syn
%{_install_dir}/syn-1.0/SP.euk.5.syn
%{_install_dir}/syn-1.0/SP.gram-.1.syn
%{_install_dir}/syn-1.0/SP.gram-.2.syn
%{_install_dir}/syn-1.0/SP.gram-.3.syn
%{_install_dir}/syn-1.0/SP.gram-.4.syn
%{_install_dir}/syn-1.0/SP.gram-.5.syn
%{_install_dir}/syn-1.0/SP.gram+.1.syn
%{_install_dir}/syn-1.0/SP.gram+.2.syn
%{_install_dir}/syn-1.0/SP.gram+.3.syn
%{_install_dir}/syn-1.0/SP.gram+.4.syn
%{_install_dir}/syn-1.0/SP.gram+.5.syn
%{_install_dir}/syn-1.1/CS.euk.1.syn
%{_install_dir}/syn-1.1/CS.euk.2.syn
%{_install_dir}/syn-1.1/CS.euk.3.syn
%{_install_dir}/syn-1.1/CS.euk.4.syn
%{_install_dir}/syn-1.1/CS.euk.5.syn
%{_install_dir}/syn-1.1/CS.gram-.1.syn
%{_install_dir}/syn-1.1/CS.gram-.2.syn
%{_install_dir}/syn-1.1/CS.gram-.3.syn
%{_install_dir}/syn-1.1/CS.gram-.4.syn
%{_install_dir}/syn-1.1/CS.gram-.5.syn
%{_install_dir}/syn-1.1/CS.gram+.1.syn
%{_install_dir}/syn-1.1/CS.gram+.2.syn
%{_install_dir}/syn-1.1/CS.gram+.3.syn
%{_install_dir}/syn-1.1/CS.gram+.4.syn
%{_install_dir}/syn-1.1/CS.gram+.5.syn
%{_install_dir}/syn-1.1/euk.param
%{_install_dir}/syn-1.1/gram-.param
%{_install_dir}/syn-1.1/gram+.param
%{_install_dir}/syn-1.1/SP.euk.1.syn
%{_install_dir}/syn-1.1/SP.euk.2.syn
%{_install_dir}/syn-1.1/SP.euk.3.syn
%{_install_dir}/syn-1.1/SP.euk.4.syn
%{_install_dir}/syn-1.1/SP.euk.5.syn
%{_install_dir}/syn-1.1/SP.gram-.1.syn
%{_install_dir}/syn-1.1/SP.gram-.2.syn
%{_install_dir}/syn-1.1/SP.gram-.3.syn
%{_install_dir}/syn-1.1/SP.gram-.4.syn
%{_install_dir}/syn-1.1/SP.gram-.5.syn
%{_install_dir}/syn-1.1/SP.gram+.1.syn
%{_install_dir}/syn-1.1/SP.gram+.2.syn
%{_install_dir}/syn-1.1/SP.gram+.3.syn
%{_install_dir}/syn-1.1/SP.gram+.4.syn
%{_install_dir}/syn-1.1/SP.gram+.5.syn
%{_install_dir}/syn-2.0/CS.euk.1.syn
%{_install_dir}/syn-2.0/CS.euk.2.syn
%{_install_dir}/syn-2.0/CS.euk.3.syn
%{_install_dir}/syn-2.0/CS.euk.4.syn
%{_install_dir}/syn-2.0/CS.euk.5.syn
%{_install_dir}/syn-2.0/CS.gram-.1.syn
%{_install_dir}/syn-2.0/CS.gram-.2.syn
%{_install_dir}/syn-2.0/CS.gram-.3.syn
%{_install_dir}/syn-2.0/CS.gram-.4.syn
%{_install_dir}/syn-2.0/CS.gram-.5.syn
%{_install_dir}/syn-2.0/CS.gram+.1.syn
%{_install_dir}/syn-2.0/CS.gram+.2.syn
%{_install_dir}/syn-2.0/CS.gram+.3.syn
%{_install_dir}/syn-2.0/CS.gram+.4.syn
%{_install_dir}/syn-2.0/CS.gram+.5.syn
%{_install_dir}/syn-2.0/euk.param
%{_install_dir}/syn-2.0/gram-.param
%{_install_dir}/syn-2.0/gram+.param
%{_install_dir}/syn-2.0/SP.euk.1.syn
%{_install_dir}/syn-2.0/SP.euk.2.syn
%{_install_dir}/syn-2.0/SP.euk.3.syn
%{_install_dir}/syn-2.0/SP.euk.4.syn
%{_install_dir}/syn-2.0/SP.euk.5.syn
%{_install_dir}/syn-2.0/SP.gram-.1.syn
%{_install_dir}/syn-2.0/SP.gram-.2.syn
%{_install_dir}/syn-2.0/SP.gram-.3.syn
%{_install_dir}/syn-2.0/SP.gram-.4.syn
%{_install_dir}/syn-2.0/SP.gram-.5.syn
%{_install_dir}/syn-2.0/SP.gram+.1.syn
%{_install_dir}/syn-2.0/SP.gram+.2.syn
%{_install_dir}/syn-2.0/SP.gram+.3.syn
%{_install_dir}/syn-2.0/SP.gram+.4.syn
%{_install_dir}/syn-2.0/SP.gram+.5.syn
%{_install_dir}/syn/CS.euk.1.syn
%{_install_dir}/syn/CS.euk.2.syn
%{_install_dir}/syn/CS.euk.3.syn
%{_install_dir}/syn/CS.euk.4.syn
%{_install_dir}/syn/CS.euk.5.syn
%{_install_dir}/syn/CS.gram-.1.syn
%{_install_dir}/syn/CS.gram-.2.syn
%{_install_dir}/syn/CS.gram-.3.syn
%{_install_dir}/syn/CS.gram-.4.syn
%{_install_dir}/syn/CS.gram-.5.syn
%{_install_dir}/syn/CS.gram+.1.syn
%{_install_dir}/syn/CS.gram+.2.syn
%{_install_dir}/syn/CS.gram+.3.syn
%{_install_dir}/syn/CS.gram+.4.syn
%{_install_dir}/syn/CS.gram+.5.syn
%{_install_dir}/syn/euk.param
%{_install_dir}/syn/gram-.param
%{_install_dir}/syn/gram+.param
%{_install_dir}/syn/SP.euk.1.syn
%{_install_dir}/syn/SP.euk.2.syn
%{_install_dir}/syn/SP.euk.3.syn
%{_install_dir}/syn/SP.euk.4.syn
%{_install_dir}/syn/SP.euk.5.syn
%{_install_dir}/syn/SP.gram-.1.syn
%{_install_dir}/syn/SP.gram-.2.syn
%{_install_dir}/syn/SP.gram-.3.syn
%{_install_dir}/syn/SP.gram-.4.syn
%{_install_dir}/syn/SP.gram-.5.syn
%{_install_dir}/syn/SP.gram+.1.syn
%{_install_dir}/syn/SP.gram+.2.syn
%{_install_dir}/syn/SP.gram+.3.syn
%{_install_dir}/syn/SP.gram+.4.syn
%{_install_dir}/syn/SP.gram+.5.syn
%{_install_dir}/test/test.dat
%{_install_dir}/test/test.out
%{_install_dir}/test/test.ps
%{_install_dir}/test/test.seq
%{_install_dir}/test/test5.seq


%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/combine-hmm-plp.awk
%{_install_dir}/__bin__/combine-nn.awk
%{_install_dir}/__bin__/decodeanhmm_Linux
%{_install_dir}/__bin__/how_Linux
%{_install_dir}/__bin__/in2how+fasta
%{_install_dir}/__bin__/mergeoutput.awk
%{_install_dir}/__bin__/signalp
%{_install_dir}/__bin__/testhow
%{_install_dir}/__bin__/ReadMe


%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
