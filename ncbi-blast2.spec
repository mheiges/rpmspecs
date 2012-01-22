%define pkg_base ncbi-blast

Summary: BLAST finds regions of similarity between biological sequences
Name: ncbi-blast2225
Version: 2.2.25
Release: 1%{?dist}
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
%setup -q -n blast-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
cp -a  bin                %{install_dir}
cp -a  data               %{install_dir}
cp -a  doc                %{install_dir}
cp -a  bin                %{install_dir}
cp     VERSION            %{install_dir}
 

# set up symlinks. These are broken as installed and should be copied to 
# a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active.
#
# for i in bin/*; do echo "ln -s %{ln_path}/$i"; done;
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/bin/bl2seq
ln -s %{ln_path}/bin/blastall
ln -s %{ln_path}/bin/blastclust
ln -s %{ln_path}/bin/blastpgp
ln -s %{ln_path}/bin/copymat
ln -s %{ln_path}/bin/fastacmd
ln -s %{ln_path}/bin/formatdb
ln -s %{ln_path}/bin/formatrpsdb
ln -s %{ln_path}/bin/impala
ln -s %{ln_path}/bin/makemat
ln -s %{ln_path}/bin/megablast
ln -s %{ln_path}/bin/rpsblast
ln -s %{ln_path}/bin/seedtop

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

%dir %{install_dir}/__bin__

# for i in $(find * -type d ); do echo "%dir %{install_dir}/$i"; done;
%dir %{install_dir}
%dir %{install_dir}/bin
%dir %{install_dir}/data
%dir %{install_dir}/doc

# for i in $(find . -type f -printf '%P\n'); do echo "%{install_dir}/$i"; done;
%{install_dir}/VERSION
%{install_dir}/doc/bl2seq.html
%{install_dir}/doc/index.html
%{install_dir}/doc/formatrpsdb.html
%{install_dir}/doc/blastclust.html
%{install_dir}/doc/megablast.html
%{install_dir}/doc/blastftp.html
%{install_dir}/doc/filter.html
%{install_dir}/doc/blastdb.html
%{install_dir}/doc/web_blast.pl
%{install_dir}/doc/history.html
%{install_dir}/doc/fastacmd.html
%{install_dir}/doc/impala.html
%{install_dir}/doc/formatdb.html
%{install_dir}/doc/blastpgp.html
%{install_dir}/doc/netblast.html
%{install_dir}/doc/blast.html
%{install_dir}/doc/blastall.html
%{install_dir}/doc/rpsblast.html
%{install_dir}/doc/scoring.pdf
%{install_dir}/data/humrep.fsa
%{install_dir}/data/KSkyte.flt
%{install_dir}/data/PAM70
%{install_dir}/data/UniVec.nsq
%{install_dir}/data/UniVec.nhr
%{install_dir}/data/bstdt.val
%{install_dir}/data/gc.val
%{install_dir}/data/featdef.val
%{install_dir}/data/ecnum_specific.txt
%{install_dir}/data/KShopp.flt
%{install_dir}/data/KSpcc.mat
%{install_dir}/data/UniVec_Core.nhr
%{install_dir}/data/seqcode.val
%{install_dir}/data/UniVec_Core.nsq
%{install_dir}/data/makerpt.prt
%{install_dir}/data/KSpyr.flt
%{install_dir}/data/sgmlbb.ent
%{install_dir}/data/KSchoth.flt
%{install_dir}/data/BLOSUM45
%{install_dir}/data/KSgc.flt
%{install_dir}/data/pubkey.enc
%{install_dir}/data/ecnum_ambiguous.txt
%{install_dir}/data/asn2ff.prt
%{install_dir}/data/taxlist.txt
%{install_dir}/data/objprt.prt
%{install_dir}/data/UniVec_Core.nin
%{install_dir}/data/lineages.txt
%{install_dir}/data/sequin.hlp
%{install_dir}/data/PAM30
%{install_dir}/data/KSpur.flt
%{install_dir}/data/BLOSUM62
%{install_dir}/data/UniVec.nin
%{install_dir}/data/KSat.flt
%{install_dir}/data/BLOSUM80
%{install_dir}/bin/seedtop
%{install_dir}/bin/impala
%{install_dir}/bin/megablast
%{install_dir}/bin/blastall
%{install_dir}/bin/blastpgp
%{install_dir}/bin/fastacmd
%{install_dir}/bin/formatdb
%{install_dir}/bin/copymat
%{install_dir}/bin/rpsblast
%{install_dir}/bin/bl2seq
%{install_dir}/bin/blastclust
%{install_dir}/bin/makemat
%{install_dir}/bin/formatrpsdb

#  for i in $(find . -type f -printf '%P\n'); do echo "%{install_dir}/__bin__/$i"; done;
%{install_dir}/__bin__/seedtop
%{install_dir}/__bin__/impala
%{install_dir}/__bin__/megablast
%{install_dir}/__bin__/blastall
%{install_dir}/__bin__/blastpgp
%{install_dir}/__bin__/fastacmd
%{install_dir}/__bin__/formatdb
%{install_dir}/__bin__/copymat
%{install_dir}/__bin__/rpsblast
%{install_dir}/__bin__/bl2seq
%{install_dir}/__bin__/blastclust
%{install_dir}/__bin__/makemat
%{install_dir}/__bin__/formatrpsdb

%changelog
* Fri Jan 20 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.