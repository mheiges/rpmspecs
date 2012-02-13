%define _pkg_base ncbi_blast

Summary: BLAST finds regions of similarity between biological sequences
Name: %{_pkg_base}-%{version}
Version: 2.2.25
Release: 2%{?dist}
License: Custom/Academic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0:   ftp://ftp.ncbi.nlm.nih.gov/blast/executables/release/2.2.25/blast-2.2.25-x64-linux.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BLAST finds regions of similarity between biological sequences

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n blast-%{version}

%build

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
cp -a  bin                %{_pre_install_dir}
cp -a  data               %{_pre_install_dir}
cp -a  doc                %{_pre_install_dir}
cp -a  bin                %{_pre_install_dir}
cp     VERSION            %{_pre_install_dir}
 

%mfest_bin  bin/bl2seq            bl2seq
%mfest_bin  bin/blastall          blastall
%mfest_bin  bin/blastclust        blastclust
%mfest_bin  bin/blastpgp          blastpgp
%mfest_bin  bin/copymat           copymat
%mfest_bin  bin/fastacmd          fastacmd
%mfest_bin  bin/formatdb          formatdb
%mfest_bin  bin/formatrpsdb       formatrpsdb
%mfest_bin  bin/impala            impala
%mfest_bin  bin/makemat           makemat
%mfest_bin  bin/megablast         megablast
%mfest_bin  bin/rpsblast          rpsblast
%mfest_bin  bin/seedtop           seedtop

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root)

# for i in $(find * -type d ); do echo "%dir %{_install_dir}/$i"; done;
%dir %{_install_dir}
%dir %{_install_dir}/bin
%dir %{_install_dir}/data
%dir %{_install_dir}/doc

# for i in $(find . -type f -printf '%P\n'); do echo "%{_install_dir}/$i"; done;
%{_install_dir}/VERSION
%{_install_dir}/doc/bl2seq.html
%{_install_dir}/doc/index.html
%{_install_dir}/doc/formatrpsdb.html
%{_install_dir}/doc/blastclust.html
%{_install_dir}/doc/megablast.html
%{_install_dir}/doc/blastftp.html
%{_install_dir}/doc/filter.html
%{_install_dir}/doc/blastdb.html
%{_install_dir}/doc/web_blast.pl
%{_install_dir}/doc/history.html
%{_install_dir}/doc/fastacmd.html
%{_install_dir}/doc/impala.html
%{_install_dir}/doc/formatdb.html
%{_install_dir}/doc/blastpgp.html
%{_install_dir}/doc/netblast.html
%{_install_dir}/doc/blast.html
%{_install_dir}/doc/blastall.html
%{_install_dir}/doc/rpsblast.html
%{_install_dir}/doc/scoring.pdf
%{_install_dir}/data/humrep.fsa
%{_install_dir}/data/KSkyte.flt
%{_install_dir}/data/PAM70
%{_install_dir}/data/UniVec.nsq
%{_install_dir}/data/UniVec.nhr
%{_install_dir}/data/bstdt.val
%{_install_dir}/data/gc.val
%{_install_dir}/data/featdef.val
%{_install_dir}/data/ecnum_specific.txt
%{_install_dir}/data/KShopp.flt
%{_install_dir}/data/KSpcc.mat
%{_install_dir}/data/UniVec_Core.nhr
%{_install_dir}/data/seqcode.val
%{_install_dir}/data/UniVec_Core.nsq
%{_install_dir}/data/makerpt.prt
%{_install_dir}/data/KSpyr.flt
%{_install_dir}/data/sgmlbb.ent
%{_install_dir}/data/KSchoth.flt
%{_install_dir}/data/BLOSUM45
%{_install_dir}/data/KSgc.flt
%{_install_dir}/data/pubkey.enc
%{_install_dir}/data/ecnum_ambiguous.txt
%{_install_dir}/data/asn2ff.prt
%{_install_dir}/data/taxlist.txt
%{_install_dir}/data/objprt.prt
%{_install_dir}/data/UniVec_Core.nin
%{_install_dir}/data/lineages.txt
%{_install_dir}/data/sequin.hlp
%{_install_dir}/data/PAM30
%{_install_dir}/data/KSpur.flt
%{_install_dir}/data/BLOSUM62
%{_install_dir}/data/UniVec.nin
%{_install_dir}/data/KSat.flt
%{_install_dir}/data/BLOSUM80
%{_install_dir}/bin/seedtop
%{_install_dir}/bin/impala
%{_install_dir}/bin/megablast
%{_install_dir}/bin/blastall
%{_install_dir}/bin/blastpgp
%{_install_dir}/bin/fastacmd
%{_install_dir}/bin/formatdb
%{_install_dir}/bin/copymat
%{_install_dir}/bin/rpsblast
%{_install_dir}/bin/bl2seq
%{_install_dir}/bin/blastclust
%{_install_dir}/bin/makemat
%{_install_dir}/bin/formatrpsdb

%{_install_dir}/%{_manifest_file}

%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2.2.25-2
- use MANIFEST.EUPATH
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.