%define _pkg_base signalp

Summary: SignalP predicts the presence and location of signal peptide cleavage sites in amino acid sequences
Name: %{_pkg_base}-%{version}
Version: 3.0
Release: 2%{?dist}
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

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{_pre_install_dir}/syn-2.0
install -m 0755 -d %{_pre_install_dir}/how
install -m 0755 -d %{_pre_install_dir}/hmm
install -m 0755 -d %{_pre_install_dir}/syn-1.0
install -m 0755 -d %{_pre_install_dir}/syn-1.1
install -m 0755 -d %{_pre_install_dir}/mod
install -m 0755 -d %{_pre_install_dir}/tmp
install -m 0755 -d %{_pre_install_dir}/bin
install -m 0755 -d %{_pre_install_dir}/test
install -m 0755 -d %{_pre_install_dir}/syn

install -m 0711 signalp %{_pre_install_dir}
install -m 0711 how/how_Linux %{_pre_install_dir}/how
install -m 0711 hmm/decodeanhmm_Linux %{_pre_install_dir}/hmm
install -m 0711 bin/combine-hmm-plp.awk %{_pre_install_dir}/bin
install -m 0711 bin/mergeoutput.awk %{_pre_install_dir}/bin
install -m 0711 bin/testhow %{_pre_install_dir}/bin
install -m 0711 bin/combine-nn.awk %{_pre_install_dir}/bin
install -m 0711 bin/in2how+fasta %{_pre_install_dir}/bin

install -m 0444 signalp-3.0.readme %{_pre_install_dir}
install -m 0444 syn-2.0/CS.euk.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/euk.param %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/gram+.param %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.3.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/gram-.param %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.1.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.euk.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram-.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.euk.4.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram+.2.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/SP.gram+.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-2.0/CS.gram-.5.syn %{_pre_install_dir}/syn-2.0
install -m 0444 syn-1.0/CS.euk.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/euk.param %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/gram+.param %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.3.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/gram-.param %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.1.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.euk.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram-.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.euk.4.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram+.2.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/SP.gram+.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.0/CS.gram-.5.syn %{_pre_install_dir}/syn-1.0
install -m 0444 syn-1.1/CS.euk.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/euk.param %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/gram+.param %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.3.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/gram-.param %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.1.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.euk.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram-.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.euk.4.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram+.2.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/SP.gram+.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 syn-1.1/CS.gram-.5.syn %{_pre_install_dir}/syn-1.1
install -m 0444 mod/V.gram+.1.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.euk.4.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram+.4.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.euk.1.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram-.4.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram-.1.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.euk.2.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram-.2.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.euk.3.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.euk.5.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram-.5.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram+.5.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram+.2.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram+.3.bsmod %{_pre_install_dir}/mod
install -m 0444 mod/V.gram-.3.bsmod %{_pre_install_dir}/mod
install -m 0444 test/test5.seq %{_pre_install_dir}/test
install -m 0444 test/test.ps %{_pre_install_dir}/test
install -m 0444 test/test.seq %{_pre_install_dir}/test
install -m 0444 test/test.out %{_pre_install_dir}/test
install -m 0444 test/test.dat %{_pre_install_dir}/test
install -m 0444 syn/CS.euk.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram+.5.syn %{_pre_install_dir}/syn
install -m 0444 syn/euk.param %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram-.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/gram+.param %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram-.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram+.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram-.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram+.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.euk.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.euk.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.euk.5.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram-.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram+.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.euk.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram+.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram+.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram-.5.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram+.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.euk.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram+.3.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram-.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/gram-.param %{_pre_install_dir}/syn
install -m 0444 syn/SP.euk.5.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram-.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.euk.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram-.1.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.euk.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram-.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.euk.4.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram+.2.syn %{_pre_install_dir}/syn
install -m 0444 syn/SP.gram+.5.syn %{_pre_install_dir}/syn
install -m 0444 syn/CS.gram-.5.syn %{_pre_install_dir}/syn

%mfest_bin  signalp
%mfest_bin  how/how_Linux                 how_Linux
%mfest_bin  hmm/decodeanhmm_Linux         decodeanhmm_Linux
%mfest_bin  bin/combine-hmm-plp.awk       combine-hmm-plp.awk
%mfest_bin  bin/mergeoutput.awk           mergeoutput.awk
%mfest_bin  bin/testhow                   testhow
%mfest_bin  bin/combine-nn.awk            combine-nn.awk
%mfest_bin  bin/in2how+fasta              in2how+fasta


%post
mkdir -p $RPM_INSTALL_PREFIX0/tmp/%{_pkg_base}
chmod 1777 $RPM_INSTALL_PREFIX0/tmp/%{_pkg_base}

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
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

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 3.0-2
- add MANIFEST.EUPATH
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
