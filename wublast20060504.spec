%define _pkg_base wu_blast

Summary: Washington University BLAST
Name: %{_pkg_base}-%{version}
Version: 2.0MP_20060504
Release: 3%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

Provides: xdformat,blastn,blastp,blastx,tblastn,tblastx,setdb

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

# discontinued by vendor, rely on our archive
Source0: http://software.apidb.org/source/blast2.linux26-x64.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Washington University's BLAST implementation.
BLAST finds regions of similarity between biological sequences

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c %{name}

%build
# precompiled

%install
%{__rm} -rf %{buildroot}

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{_pre_install_dir}/filter
install -m 0755 -d %{_pre_install_dir}/matrix


cp -a filter %{_pre_install_dir}
cp -a matrix %{_pre_install_dir}

cp -d blastn %{_pre_install_dir}
cp -d blastp %{_pre_install_dir}
cp -d blastx %{_pre_install_dir}
cp -d BLOSUM62 %{_pre_install_dir}
cp -d pressdb %{_pre_install_dir}
cp -d setdb %{_pre_install_dir}
cp -d tblastn %{_pre_install_dir}
cp -d tblastx %{_pre_install_dir}

cp -p blasta %{_pre_install_dir}
cp -p COPYRIGHT %{_pre_install_dir}
cp -p FAQ-Indexing.html %{_pre_install_dir}
cp -p gb2fasta %{_pre_install_dir}
cp -p gt2fasta %{_pre_install_dir}
cp -p HISTORY %{_pre_install_dir}
cp -p LICENSE %{_pre_install_dir}
cp -p memfile %{_pre_install_dir}
cp -p Memory.html %{_pre_install_dir}
cp -p nrdb %{_pre_install_dir}
cp -p pam %{_pre_install_dir}
cp -p parameters.html %{_pre_install_dir}
cp -p patdb %{_pre_install_dir}
cp -p pir2fasta %{_pre_install_dir}
cp -p README.html %{_pre_install_dir}
cp -p sp2fasta %{_pre_install_dir}
cp -p sysblast.sample %{_pre_install_dir}
cp -p tabular.html %{_pre_install_dir}
cp -p wu-blastall %{_pre_install_dir}
cp -p wu-formatdb %{_pre_install_dir}
cp -p xdformat %{_pre_install_dir}
cp -p xdget %{_pre_install_dir}

%mfest_bin  blasta                              
%mfest_bin  blastn                              
%mfest_bin  blastp                              
%mfest_bin  blastx                              
%mfest_bin  gb2fasta                              
%mfest_bin  gt2fasta                              
%mfest_bin  memfile                              
%mfest_bin  nrdb                              
%mfest_bin  pam                              
%mfest_bin  patdb                              
%mfest_bin  pir2fasta                              
%mfest_bin  pressdb                              
%mfest_bin  setdb                              
%mfest_bin  sp2fasta                              
%mfest_bin  tblastn                              
%mfest_bin  tblastx                              
%mfest_bin  wu-blastall                              
%mfest_bin  wu-formatdb                              
%mfest_bin  xdformat                              
%mfest_bin  xdget                              


%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/filter
%dir %{_install_dir}/matrix
%dir %{_install_dir}/matrix/aa
%dir %{_install_dir}/matrix/nt
%{_install_dir}/blasta
%{_install_dir}/blastn
%{_install_dir}/blastp
%{_install_dir}/blastx
%{_install_dir}/BLOSUM62
%{_install_dir}/COPYRIGHT
%{_install_dir}/FAQ-Indexing.html
%{_install_dir}/filter/dust
%{_install_dir}/filter/nmerge
%{_install_dir}/filter/nseg
%{_install_dir}/filter/pmerge
%{_install_dir}/filter/pseg
%{_install_dir}/filter/README
%{_install_dir}/filter/seg
%{_install_dir}/filter/seg+xnu
%{_install_dir}/filter/xnu
%{_install_dir}/filter/xnu+seg
%{_install_dir}/gb2fasta
%{_install_dir}/gt2fasta
%{_install_dir}/HISTORY
%{_install_dir}/LICENSE
%{_install_dir}/matrix/aa/blosum30
%{_install_dir}/matrix/aa/BLOSUM30
%{_install_dir}/matrix/aa/blosum35
%{_install_dir}/matrix/aa/BLOSUM35
%{_install_dir}/matrix/aa/blosum40
%{_install_dir}/matrix/aa/BLOSUM40
%{_install_dir}/matrix/aa/blosum45
%{_install_dir}/matrix/aa/BLOSUM45
%{_install_dir}/matrix/aa/blosum50
%{_install_dir}/matrix/aa/BLOSUM50
%{_install_dir}/matrix/aa/blosum55
%{_install_dir}/matrix/aa/BLOSUM55
%{_install_dir}/matrix/aa/blosum60
%{_install_dir}/matrix/aa/BLOSUM60
%{_install_dir}/matrix/aa/blosum62
%{_install_dir}/matrix/aa/BLOSUM62
%{_install_dir}/matrix/aa/blosum65
%{_install_dir}/matrix/aa/BLOSUM65
%{_install_dir}/matrix/aa/blosum70
%{_install_dir}/matrix/aa/BLOSUM70
%{_install_dir}/matrix/aa/blosum75
%{_install_dir}/matrix/aa/BLOSUM75
%{_install_dir}/matrix/aa/blosum80
%{_install_dir}/matrix/aa/BLOSUM80
%{_install_dir}/matrix/aa/blosum85
%{_install_dir}/matrix/aa/BLOSUM85
%{_install_dir}/matrix/aa/blosum90
%{_install_dir}/matrix/aa/BLOSUM90
%{_install_dir}/matrix/aa/blosum100
%{_install_dir}/matrix/aa/BLOSUM100
%{_install_dir}/matrix/aa/blosumn
%{_install_dir}/matrix/aa/BLOSUMN
%{_install_dir}/matrix/aa/dayhoff
%{_install_dir}/matrix/aa/DAYHOFF
%{_install_dir}/matrix/aa/gonnet
%{_install_dir}/matrix/aa/GONNET
%{_install_dir}/matrix/aa/identity
%{_install_dir}/matrix/aa/IDENTITY
%{_install_dir}/matrix/aa/match
%{_install_dir}/matrix/aa/MATCH
%{_install_dir}/matrix/aa/nuc.4.2
%{_install_dir}/matrix/aa/NUC.4.2
%{_install_dir}/matrix/aa/nuc.4.4
%{_install_dir}/matrix/aa/NUC.4.4
%{_install_dir}/matrix/aa/pam10
%{_install_dir}/matrix/aa/PAM10
%{_install_dir}/matrix/aa/pam20
%{_install_dir}/matrix/aa/PAM20
%{_install_dir}/matrix/aa/pam30
%{_install_dir}/matrix/aa/PAM30
%{_install_dir}/matrix/aa/pam40
%{_install_dir}/matrix/aa/PAM40
%{_install_dir}/matrix/aa/pam40.cdi
%{_install_dir}/matrix/aa/PAM40.cdi
%{_install_dir}/matrix/aa/pam50
%{_install_dir}/matrix/aa/PAM50
%{_install_dir}/matrix/aa/pam60
%{_install_dir}/matrix/aa/PAM60
%{_install_dir}/matrix/aa/pam70
%{_install_dir}/matrix/aa/PAM70
%{_install_dir}/matrix/aa/pam80
%{_install_dir}/matrix/aa/PAM80
%{_install_dir}/matrix/aa/pam80.cdi
%{_install_dir}/matrix/aa/PAM80.cdi
%{_install_dir}/matrix/aa/pam90
%{_install_dir}/matrix/aa/PAM90
%{_install_dir}/matrix/aa/pam100
%{_install_dir}/matrix/aa/PAM100
%{_install_dir}/matrix/aa/pam110
%{_install_dir}/matrix/aa/PAM110
%{_install_dir}/matrix/aa/pam120
%{_install_dir}/matrix/aa/PAM120
%{_install_dir}/matrix/aa/pam120.cdi
%{_install_dir}/matrix/aa/PAM120.cdi
%{_install_dir}/matrix/aa/pam130
%{_install_dir}/matrix/aa/PAM130
%{_install_dir}/matrix/aa/pam140
%{_install_dir}/matrix/aa/PAM140
%{_install_dir}/matrix/aa/pam150
%{_install_dir}/matrix/aa/PAM150
%{_install_dir}/matrix/aa/pam160
%{_install_dir}/matrix/aa/PAM160
%{_install_dir}/matrix/aa/pam160.cdi
%{_install_dir}/matrix/aa/PAM160.cdi
%{_install_dir}/matrix/aa/pam170
%{_install_dir}/matrix/aa/PAM170
%{_install_dir}/matrix/aa/pam180
%{_install_dir}/matrix/aa/PAM180
%{_install_dir}/matrix/aa/pam190
%{_install_dir}/matrix/aa/PAM190
%{_install_dir}/matrix/aa/pam200
%{_install_dir}/matrix/aa/PAM200
%{_install_dir}/matrix/aa/pam200.cdi
%{_install_dir}/matrix/aa/PAM200.cdi
%{_install_dir}/matrix/aa/pam210
%{_install_dir}/matrix/aa/PAM210
%{_install_dir}/matrix/aa/pam220
%{_install_dir}/matrix/aa/PAM220
%{_install_dir}/matrix/aa/pam230
%{_install_dir}/matrix/aa/PAM230
%{_install_dir}/matrix/aa/pam240
%{_install_dir}/matrix/aa/PAM240
%{_install_dir}/matrix/aa/pam250
%{_install_dir}/matrix/aa/PAM250
%{_install_dir}/matrix/aa/pam250.cdi
%{_install_dir}/matrix/aa/PAM250.cdi
%{_install_dir}/matrix/aa/pam260
%{_install_dir}/matrix/aa/PAM260
%{_install_dir}/matrix/aa/pam270
%{_install_dir}/matrix/aa/PAM270
%{_install_dir}/matrix/aa/pam280
%{_install_dir}/matrix/aa/PAM280
%{_install_dir}/matrix/aa/pam290
%{_install_dir}/matrix/aa/PAM290
%{_install_dir}/matrix/aa/pam300
%{_install_dir}/matrix/aa/PAM300
%{_install_dir}/matrix/aa/pam310
%{_install_dir}/matrix/aa/PAM310
%{_install_dir}/matrix/aa/pam320
%{_install_dir}/matrix/aa/PAM320
%{_install_dir}/matrix/aa/pam330
%{_install_dir}/matrix/aa/PAM330
%{_install_dir}/matrix/aa/pam340
%{_install_dir}/matrix/aa/PAM340
%{_install_dir}/matrix/aa/pam350
%{_install_dir}/matrix/aa/PAM350
%{_install_dir}/matrix/aa/pam360
%{_install_dir}/matrix/aa/PAM360
%{_install_dir}/matrix/aa/pam370
%{_install_dir}/matrix/aa/PAM370
%{_install_dir}/matrix/aa/pam380
%{_install_dir}/matrix/aa/PAM380
%{_install_dir}/matrix/aa/pam390
%{_install_dir}/matrix/aa/PAM390
%{_install_dir}/matrix/aa/pam400
%{_install_dir}/matrix/aa/PAM400
%{_install_dir}/matrix/aa/pam410
%{_install_dir}/matrix/aa/PAM410
%{_install_dir}/matrix/aa/pam420
%{_install_dir}/matrix/aa/PAM420
%{_install_dir}/matrix/aa/pam430
%{_install_dir}/matrix/aa/PAM430
%{_install_dir}/matrix/aa/pam440
%{_install_dir}/matrix/aa/PAM440
%{_install_dir}/matrix/aa/pam450
%{_install_dir}/matrix/aa/PAM450
%{_install_dir}/matrix/aa/pam460
%{_install_dir}/matrix/aa/PAM460
%{_install_dir}/matrix/aa/pam470
%{_install_dir}/matrix/aa/PAM470
%{_install_dir}/matrix/aa/pam480
%{_install_dir}/matrix/aa/PAM480
%{_install_dir}/matrix/aa/pam490
%{_install_dir}/matrix/aa/PAM490
%{_install_dir}/matrix/aa/pam500
%{_install_dir}/matrix/aa/PAM500
%{_install_dir}/matrix/aa/phat_t70_b66
%{_install_dir}/matrix/aa/PHAT_T70_B66
%{_install_dir}/matrix/aa/phat_t75_b73
%{_install_dir}/matrix/aa/PHAT_T75_B73
%{_install_dir}/matrix/aa/phat_t80_b78
%{_install_dir}/matrix/aa/PHAT_T80_B78
%{_install_dir}/matrix/aa/phat_t85_b82
%{_install_dir}/matrix/aa/PHAT_T85_B82
%{_install_dir}/matrix/nt/identity.4.2
%{_install_dir}/matrix/nt/IDENTITY.4.2
%{_install_dir}/matrix/nt/identity.4.4
%{_install_dir}/matrix/nt/IDENTITY.4.4
%{_install_dir}/matrix/nt/pupy.4.2
%{_install_dir}/matrix/nt/PUPY.4.2
%{_install_dir}/matrix/nt/pupy.4.4
%{_install_dir}/matrix/nt/PUPY.4.4
%{_install_dir}/matrix/README
%{_install_dir}/memfile
%{_install_dir}/Memory.html
%{_install_dir}/nrdb
%{_install_dir}/pam
%{_install_dir}/parameters.html
%{_install_dir}/patdb
%{_install_dir}/pir2fasta
%{_install_dir}/pressdb
%{_install_dir}/README.html
%{_install_dir}/setdb
%{_install_dir}/sp2fasta
%{_install_dir}/sysblast.sample
%{_install_dir}/tabular.html
%{_install_dir}/tblastn
%{_install_dir}/tblastx
%{_install_dir}/wu-blastall
%{_install_dir}/wu-formatdb
%{_install_dir}/xdformat
%{_install_dir}/xdget

%{_install_dir}/%{_manifest_file}


%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2.0MP_20060504-3
- add MANIFEST.EUPATH
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu> 2.0MP_20060504-2
- add Provides
* Mon Jan 23 2012 Mark Heiges <mheiges@uga.edu> 2.0MP_20060504-1
- Initial release.
