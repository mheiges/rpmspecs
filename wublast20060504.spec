%define pkg_base wu_blast

Summary: Washington University BLAST
Name: %{pkg_base}-%{version}
Version: 2.0MP_20060504
Release: 2%{?dist}
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
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
install -m 0755 -d %{install_dir}/filter
install -m 0755 -d %{install_dir}/matrix


cp -a filter %{install_dir}
cp -a matrix %{install_dir}

cp -d blastn %{install_dir}
cp -d blastp %{install_dir}
cp -d blastx %{install_dir}
cp -d BLOSUM62 %{install_dir}
cp -d pressdb %{install_dir}
cp -d setdb %{install_dir}
cp -d tblastn %{install_dir}
cp -d tblastx %{install_dir}

cp -p blasta %{install_dir}
cp -p COPYRIGHT %{install_dir}
cp -p FAQ-Indexing.html %{install_dir}
cp -p gb2fasta %{install_dir}
cp -p gt2fasta %{install_dir}
cp -p HISTORY %{install_dir}
cp -p LICENSE %{install_dir}
cp -p memfile %{install_dir}
cp -p Memory.html %{install_dir}
cp -p nrdb %{install_dir}
cp -p pam %{install_dir}
cp -p parameters.html %{install_dir}
cp -p patdb %{install_dir}
cp -p pir2fasta %{install_dir}
cp -p README.html %{install_dir}
cp -p sp2fasta %{install_dir}
cp -p sysblast.sample %{install_dir}
cp -p tabular.html %{install_dir}
cp -p wu-blastall %{install_dir}
cp -p wu-formatdb %{install_dir}
cp -p xdformat %{install_dir}
cp -p xdget %{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/blasta
ln -s %{ln_path}/blastn
ln -s %{ln_path}/blastp
ln -s %{ln_path}/blastx
ln -s %{ln_path}/gb2fasta
ln -s %{ln_path}/gt2fasta
ln -s %{ln_path}/memfile
ln -s %{ln_path}/nrdb
ln -s %{ln_path}/pam
ln -s %{ln_path}/patdb
ln -s %{ln_path}/pir2fasta
ln -s %{ln_path}/pressdb
ln -s %{ln_path}/setdb
ln -s %{ln_path}/sp2fasta
ln -s %{ln_path}/tblastn
ln -s %{ln_path}/tblastx
ln -s %{ln_path}/wu-blastall
ln -s %{ln_path}/wu-formatdb
ln -s %{ln_path}/xdformat
ln -s %{ln_path}/xdget

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
%dir %{install_dir}/filter
%dir %{install_dir}/matrix
%dir %{install_dir}/matrix/aa
%dir %{install_dir}/matrix/nt
%{install_dir}/blasta
%{install_dir}/blastn
%{install_dir}/blastp
%{install_dir}/blastx
%{install_dir}/BLOSUM62
%{install_dir}/COPYRIGHT
%{install_dir}/FAQ-Indexing.html
%{install_dir}/filter/dust
%{install_dir}/filter/nmerge
%{install_dir}/filter/nseg
%{install_dir}/filter/pmerge
%{install_dir}/filter/pseg
%{install_dir}/filter/README
%{install_dir}/filter/seg
%{install_dir}/filter/seg+xnu
%{install_dir}/filter/xnu
%{install_dir}/filter/xnu+seg
%{install_dir}/gb2fasta
%{install_dir}/gt2fasta
%{install_dir}/HISTORY
%{install_dir}/LICENSE
%{install_dir}/matrix/aa/blosum30
%{install_dir}/matrix/aa/BLOSUM30
%{install_dir}/matrix/aa/blosum35
%{install_dir}/matrix/aa/BLOSUM35
%{install_dir}/matrix/aa/blosum40
%{install_dir}/matrix/aa/BLOSUM40
%{install_dir}/matrix/aa/blosum45
%{install_dir}/matrix/aa/BLOSUM45
%{install_dir}/matrix/aa/blosum50
%{install_dir}/matrix/aa/BLOSUM50
%{install_dir}/matrix/aa/blosum55
%{install_dir}/matrix/aa/BLOSUM55
%{install_dir}/matrix/aa/blosum60
%{install_dir}/matrix/aa/BLOSUM60
%{install_dir}/matrix/aa/blosum62
%{install_dir}/matrix/aa/BLOSUM62
%{install_dir}/matrix/aa/blosum65
%{install_dir}/matrix/aa/BLOSUM65
%{install_dir}/matrix/aa/blosum70
%{install_dir}/matrix/aa/BLOSUM70
%{install_dir}/matrix/aa/blosum75
%{install_dir}/matrix/aa/BLOSUM75
%{install_dir}/matrix/aa/blosum80
%{install_dir}/matrix/aa/BLOSUM80
%{install_dir}/matrix/aa/blosum85
%{install_dir}/matrix/aa/BLOSUM85
%{install_dir}/matrix/aa/blosum90
%{install_dir}/matrix/aa/BLOSUM90
%{install_dir}/matrix/aa/blosum100
%{install_dir}/matrix/aa/BLOSUM100
%{install_dir}/matrix/aa/blosumn
%{install_dir}/matrix/aa/BLOSUMN
%{install_dir}/matrix/aa/dayhoff
%{install_dir}/matrix/aa/DAYHOFF
%{install_dir}/matrix/aa/gonnet
%{install_dir}/matrix/aa/GONNET
%{install_dir}/matrix/aa/identity
%{install_dir}/matrix/aa/IDENTITY
%{install_dir}/matrix/aa/match
%{install_dir}/matrix/aa/MATCH
%{install_dir}/matrix/aa/nuc.4.2
%{install_dir}/matrix/aa/NUC.4.2
%{install_dir}/matrix/aa/nuc.4.4
%{install_dir}/matrix/aa/NUC.4.4
%{install_dir}/matrix/aa/pam10
%{install_dir}/matrix/aa/PAM10
%{install_dir}/matrix/aa/pam20
%{install_dir}/matrix/aa/PAM20
%{install_dir}/matrix/aa/pam30
%{install_dir}/matrix/aa/PAM30
%{install_dir}/matrix/aa/pam40
%{install_dir}/matrix/aa/PAM40
%{install_dir}/matrix/aa/pam40.cdi
%{install_dir}/matrix/aa/PAM40.cdi
%{install_dir}/matrix/aa/pam50
%{install_dir}/matrix/aa/PAM50
%{install_dir}/matrix/aa/pam60
%{install_dir}/matrix/aa/PAM60
%{install_dir}/matrix/aa/pam70
%{install_dir}/matrix/aa/PAM70
%{install_dir}/matrix/aa/pam80
%{install_dir}/matrix/aa/PAM80
%{install_dir}/matrix/aa/pam80.cdi
%{install_dir}/matrix/aa/PAM80.cdi
%{install_dir}/matrix/aa/pam90
%{install_dir}/matrix/aa/PAM90
%{install_dir}/matrix/aa/pam100
%{install_dir}/matrix/aa/PAM100
%{install_dir}/matrix/aa/pam110
%{install_dir}/matrix/aa/PAM110
%{install_dir}/matrix/aa/pam120
%{install_dir}/matrix/aa/PAM120
%{install_dir}/matrix/aa/pam120.cdi
%{install_dir}/matrix/aa/PAM120.cdi
%{install_dir}/matrix/aa/pam130
%{install_dir}/matrix/aa/PAM130
%{install_dir}/matrix/aa/pam140
%{install_dir}/matrix/aa/PAM140
%{install_dir}/matrix/aa/pam150
%{install_dir}/matrix/aa/PAM150
%{install_dir}/matrix/aa/pam160
%{install_dir}/matrix/aa/PAM160
%{install_dir}/matrix/aa/pam160.cdi
%{install_dir}/matrix/aa/PAM160.cdi
%{install_dir}/matrix/aa/pam170
%{install_dir}/matrix/aa/PAM170
%{install_dir}/matrix/aa/pam180
%{install_dir}/matrix/aa/PAM180
%{install_dir}/matrix/aa/pam190
%{install_dir}/matrix/aa/PAM190
%{install_dir}/matrix/aa/pam200
%{install_dir}/matrix/aa/PAM200
%{install_dir}/matrix/aa/pam200.cdi
%{install_dir}/matrix/aa/PAM200.cdi
%{install_dir}/matrix/aa/pam210
%{install_dir}/matrix/aa/PAM210
%{install_dir}/matrix/aa/pam220
%{install_dir}/matrix/aa/PAM220
%{install_dir}/matrix/aa/pam230
%{install_dir}/matrix/aa/PAM230
%{install_dir}/matrix/aa/pam240
%{install_dir}/matrix/aa/PAM240
%{install_dir}/matrix/aa/pam250
%{install_dir}/matrix/aa/PAM250
%{install_dir}/matrix/aa/pam250.cdi
%{install_dir}/matrix/aa/PAM250.cdi
%{install_dir}/matrix/aa/pam260
%{install_dir}/matrix/aa/PAM260
%{install_dir}/matrix/aa/pam270
%{install_dir}/matrix/aa/PAM270
%{install_dir}/matrix/aa/pam280
%{install_dir}/matrix/aa/PAM280
%{install_dir}/matrix/aa/pam290
%{install_dir}/matrix/aa/PAM290
%{install_dir}/matrix/aa/pam300
%{install_dir}/matrix/aa/PAM300
%{install_dir}/matrix/aa/pam310
%{install_dir}/matrix/aa/PAM310
%{install_dir}/matrix/aa/pam320
%{install_dir}/matrix/aa/PAM320
%{install_dir}/matrix/aa/pam330
%{install_dir}/matrix/aa/PAM330
%{install_dir}/matrix/aa/pam340
%{install_dir}/matrix/aa/PAM340
%{install_dir}/matrix/aa/pam350
%{install_dir}/matrix/aa/PAM350
%{install_dir}/matrix/aa/pam360
%{install_dir}/matrix/aa/PAM360
%{install_dir}/matrix/aa/pam370
%{install_dir}/matrix/aa/PAM370
%{install_dir}/matrix/aa/pam380
%{install_dir}/matrix/aa/PAM380
%{install_dir}/matrix/aa/pam390
%{install_dir}/matrix/aa/PAM390
%{install_dir}/matrix/aa/pam400
%{install_dir}/matrix/aa/PAM400
%{install_dir}/matrix/aa/pam410
%{install_dir}/matrix/aa/PAM410
%{install_dir}/matrix/aa/pam420
%{install_dir}/matrix/aa/PAM420
%{install_dir}/matrix/aa/pam430
%{install_dir}/matrix/aa/PAM430
%{install_dir}/matrix/aa/pam440
%{install_dir}/matrix/aa/PAM440
%{install_dir}/matrix/aa/pam450
%{install_dir}/matrix/aa/PAM450
%{install_dir}/matrix/aa/pam460
%{install_dir}/matrix/aa/PAM460
%{install_dir}/matrix/aa/pam470
%{install_dir}/matrix/aa/PAM470
%{install_dir}/matrix/aa/pam480
%{install_dir}/matrix/aa/PAM480
%{install_dir}/matrix/aa/pam490
%{install_dir}/matrix/aa/PAM490
%{install_dir}/matrix/aa/pam500
%{install_dir}/matrix/aa/PAM500
%{install_dir}/matrix/aa/phat_t70_b66
%{install_dir}/matrix/aa/PHAT_T70_B66
%{install_dir}/matrix/aa/phat_t75_b73
%{install_dir}/matrix/aa/PHAT_T75_B73
%{install_dir}/matrix/aa/phat_t80_b78
%{install_dir}/matrix/aa/PHAT_T80_B78
%{install_dir}/matrix/aa/phat_t85_b82
%{install_dir}/matrix/aa/PHAT_T85_B82
%{install_dir}/matrix/nt/identity.4.2
%{install_dir}/matrix/nt/IDENTITY.4.2
%{install_dir}/matrix/nt/identity.4.4
%{install_dir}/matrix/nt/IDENTITY.4.4
%{install_dir}/matrix/nt/pupy.4.2
%{install_dir}/matrix/nt/PUPY.4.2
%{install_dir}/matrix/nt/pupy.4.4
%{install_dir}/matrix/nt/PUPY.4.4
%{install_dir}/matrix/README
%{install_dir}/memfile
%{install_dir}/Memory.html
%{install_dir}/nrdb
%{install_dir}/pam
%{install_dir}/parameters.html
%{install_dir}/patdb
%{install_dir}/pir2fasta
%{install_dir}/pressdb
%{install_dir}/README.html
%{install_dir}/setdb
%{install_dir}/sp2fasta
%{install_dir}/sysblast.sample
%{install_dir}/tabular.html
%{install_dir}/tblastn
%{install_dir}/tblastx
%{install_dir}/wu-blastall
%{install_dir}/wu-formatdb
%{install_dir}/xdformat
%{install_dir}/xdget

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/blasta
%{install_dir}/__bin__/blastn
%{install_dir}/__bin__/blastp
%{install_dir}/__bin__/blastx
%{install_dir}/__bin__/gb2fasta
%{install_dir}/__bin__/gt2fasta
%{install_dir}/__bin__/memfile
%{install_dir}/__bin__/nrdb
%{install_dir}/__bin__/pam
%{install_dir}/__bin__/patdb
%{install_dir}/__bin__/pir2fasta
%{install_dir}/__bin__/pressdb
%{install_dir}/__bin__/setdb
%{install_dir}/__bin__/sp2fasta
%{install_dir}/__bin__/tblastn
%{install_dir}/__bin__/tblastx
%{install_dir}/__bin__/wu-blastall
%{install_dir}/__bin__/wu-formatdb
%{install_dir}/__bin__/xdformat
%{install_dir}/__bin__/xdget


%changelog
* Tue Jan 31 2012 Mark Heiges <mheiges@uga.edu> 2.0MP_20060504-2
- add Provides
* Mon Jan 23 2012 Mark Heiges <mheiges@uga.edu> 2.0MP_20060504-1
- Initial release.
