%define _pkg_base consed

Summary: A graphical tool for DNA sequence finishing
Name: %{_pkg_base}-%{version}
Version: 20.0
Release: 4%{?dist}
License: GPL
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

# website restricted to 128.192.75.112
# locally cached at http://software.apidb.org/source/consed_20_linux.tar.gz
Source0: http://bozeman.mbt.washington.edu/consed/distributions/20.0/consed_linux.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A graphical tool for DNA sequence finishing

%prep
%eupa_validate_workflow_pkg_name
%setup -q -c %{name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%define bundle_profile_dir  %{_pre_install_dir}/__profile__

install -m 0755 -d %{_pre_install_dir}
install -m 0755 -d %{bundle_profile_dir}

install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify
install -m 0755 -d %{_pre_install_dir}/selectRegions
install -m 0755 -d %{_pre_install_dir}/selectRegions/phdball_dir
install -m 0755 -d %{_pre_install_dir}/selectRegions/edit_dir
install -m 0755 -d %{_pre_install_dir}/selectRegions/solexa_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly/phdball_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0755 -d %{_pre_install_dir}/standard
install -m 0755 -d %{_pre_install_dir}/standard/chromat_dir
install -m 0755 -d %{_pre_install_dir}/standard/phd_dir
install -m 0755 -d %{_pre_install_dir}/standard/chromats_to_add
install -m 0755 -d %{_pre_install_dir}/standard/edit_dir
install -m 0755 -d %{_pre_install_dir}/assembly_view
install -m 0755 -d %{_pre_install_dir}/assembly_view/chromat_dir
install -m 0755 -d %{_pre_install_dir}/assembly_view/phd_dir
install -m 0755 -d %{_pre_install_dir}/assembly_view/edit_dir
install -m 0755 -d %{_pre_install_dir}/misc
install -m 0755 -d %{_pre_install_dir}/selectRegionsAnswer
install -m 0755 -d %{_pre_install_dir}/selectRegionsAnswer/phdball_dir
install -m 0755 -d %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0755 -d %{_pre_install_dir}/selectRegionsAnswer/solexa_dir
install -m 0755 -d %{_pre_install_dir}/454_newbler
install -m 0755 -d %{_pre_install_dir}/454_newbler/sff_dir
install -m 0755 -d %{_pre_install_dir}/454_newbler/chromat_dir
install -m 0755 -d %{_pre_install_dir}/454_newbler/phd_dir
install -m 0755 -d %{_pre_install_dir}/454_newbler/phdball_dir
install -m 0755 -d %{_pre_install_dir}/454_newbler/edit_dir
install -m 0755 -d %{_pre_install_dir}/contributions
install -m 0755 -d %{_pre_install_dir}/solexa_example
install -m 0755 -d %{_pre_install_dir}/solexa_example/phd_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example/phdball_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example/edit_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example/solexa_dir
install -m 0755 -d %{_pre_install_dir}/align454reads
install -m 0755 -d %{_pre_install_dir}/align454reads/sff_dir
install -m 0755 -d %{_pre_install_dir}/align454reads/chromat_dir
install -m 0755 -d %{_pre_install_dir}/align454reads/phd_dir
install -m 0755 -d %{_pre_install_dir}/align454reads/phdball_dir
install -m 0755 -d %{_pre_install_dir}/align454reads/edit_dir
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/phd_dir
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/phd_dir
install -m 0755 -d %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0755 -d %{_pre_install_dir}/scripts
install -m 0755 -d %{_pre_install_dir}/autofinish
install -m 0755 -d %{_pre_install_dir}/autofinish/chromat_dir
install -m 0755 -d %{_pre_install_dir}/autofinish/phd_dir
install -m 0755 -d %{_pre_install_dir}/autofinish/edit_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Ace_answer
install -m 0755 -d %{_pre_install_dir}/phaster2Ace_answer/phdball_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example_answer
install -m 0755 -d %{_pre_install_dir}/solexa_example_answer/phd_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example_answer/phdball_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example_answer/edit_dir
install -m 0755 -d %{_pre_install_dir}/solexa_example_answer/solexa_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Ace
install -m 0755 -d %{_pre_install_dir}/phaster2Ace/phdball_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0755 -d %{_pre_install_dir}/polyphred
install -m 0755 -d %{_pre_install_dir}/polyphred/chromat_dir
install -m 0755 -d %{_pre_install_dir}/polyphred/poly_dir
install -m 0755 -d %{_pre_install_dir}/polyphred/phd_dir
install -m 0755 -d %{_pre_install_dir}/polyphred/edit_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly_answer
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly_answer/phdball_dir
install -m 0755 -d %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0755 -d %{_pre_install_dir}/align454reads_answer
install -m 0755 -d %{_pre_install_dir}/align454reads_answer/sff_dir
install -m 0755 -d %{_pre_install_dir}/align454reads_answer/chromat_dir
install -m 0755 -d %{_pre_install_dir}/align454reads_answer/phd_dir
install -m 0755 -d %{_pre_install_dir}/align454reads_answer/phdball_dir
install -m 0755 -d %{_pre_install_dir}/align454reads_answer/edit_dir


# renaming and setting execute only perms
install -m 0711 consed_linux64bit %{_pre_install_dir}/consed

install -m 0755 scripts/ace2Fasta.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/ace2Oligos.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/add454Reads.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/addReads2Consed.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/addSolexaReads.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/alignSolexaReads2Refs.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/amplifyTranscripts.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/countEditedBases.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/determineReadTypes.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/fasta2Ace.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/fasta2Phd.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/fasta2PhdBall.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/filter454Reads.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/findSequenceMatchesForConsed.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/fixContigEnd.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/lib2Phd.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/makePhdBall.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/orderPrimerPairs.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/phaster2Ace.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/phaster2Miniassembly.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/phd2Ace.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/phredPhrap %{_pre_install_dir}/scripts
# see $bUsingPolyPhred in phredPhrap for explanation of this symlink
ln %{_pre_install_dir}/scripts/phredPhrap %{_pre_install_dir}/scripts/polyphredPhrap
install -m 0755 scripts/removeReads %{_pre_install_dir}/scripts
install -m 0755 scripts/revertToUneditedRead %{_pre_install_dir}/scripts
install -m 0755 scripts/selectRegions.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/tagRepeats.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/testSocket.perl %{_pre_install_dir}/scripts
install -m 0755 scripts/transferConsensusTags.perl %{_pre_install_dir}/scripts
install -m 0755 contributions/ace2fof %{_pre_install_dir}/contributions
install -m 0755 contributions/ace2OligosWithComments.perl %{_pre_install_dir}/contributions
install -m 0755 contributions/aceContigs2Phds.perl %{_pre_install_dir}/contributions
install -m 0755 contributions/acestatus.pl %{_pre_install_dir}/contributions
install -m 0755 contributions/export_cons %{_pre_install_dir}/contributions
install -m 0755 contributions/mergeAces.perl %{_pre_install_dir}/contributions
install -m 0755 contributions/recover_consensus_tags %{_pre_install_dir}/contributions
install -m 0755 contributions/revert_fof %{_pre_install_dir}/contributions

install -m 0644 20.0_announcement.txt %{_pre_install_dir}
install -m 0644 454_newbler/edit_dir/454Contigs.ace.1 %{_pre_install_dir}/454_newbler/edit_dir
install -m 0644 454_newbler/edit_dir/454Contigs.ace.1.091026.110917.fasta %{_pre_install_dir}/454_newbler/edit_dir
install -m 0644 454_newbler/edit_dir/454Contigs.ace.1.aview %{_pre_install_dir}/454_newbler/edit_dir
install -m 0644 454_newbler/phdball_dir/phd.ball.1 %{_pre_install_dir}/454_newbler/phdball_dir
install -m 0644 454_newbler/sff_dir/pairedreads.sff %{_pre_install_dir}/454_newbler/sff_dir
install -m 0644 align454reads_answer/edit_dir/reference.ace %{_pre_install_dir}/align454reads_answer/edit_dir
install -m 0644 align454reads_answer/edit_dir/reference.ace.1 %{_pre_install_dir}/align454reads_answer/edit_dir
install -m 0644 align454reads_answer/edit_dir/reference.fa %{_pre_install_dir}/align454reads_answer/edit_dir
install -m 0644 align454reads_answer/edit_dir/sff.fof %{_pre_install_dir}/align454reads_answer/edit_dir
install -m 0644 align454reads_answer/phdball_dir/phd.ball.1 %{_pre_install_dir}/align454reads_answer/phdball_dir
install -m 0644 align454reads_answer/phdball_dir/phd.ball.2 %{_pre_install_dir}/align454reads_answer/phdball_dir
install -m 0644 align454reads_answer/sff_dir/newreads.sff %{_pre_install_dir}/align454reads_answer/sff_dir
install -m 0644 align454reads_answer/sff_dir/reads.sff %{_pre_install_dir}/align454reads_answer/sff_dir
install -m 0644 align454reads/edit_dir/reference.fa %{_pre_install_dir}/align454reads/edit_dir
install -m 0644 align454reads/edit_dir/sff.fof %{_pre_install_dir}/align454reads/edit_dir
install -m 0644 align454reads/sff_dir/newreads.sff %{_pre_install_dir}/align454reads/sff_dir
install -m 0644 align454reads/sff_dir/reads.sff %{_pre_install_dir}/align454reads/sff_dir
install -m 0644 assembly_view/edit_dir/.consedrc %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/.consedrc_mini %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/assembly_view.030319.170348.fasta %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/assembly_view.030319.170348.fasta.log %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/assembly_view.fasta.screen.ace.1 %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/assembly_view.fasta.screen.ace.1.aview %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/doNotShowInAssemblyView.fof %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/edit_dir/fragSizes.txt %{_pre_install_dir}/assembly_view/edit_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q102.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q124.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q124.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q126.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q126.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q131.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q131.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q134.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q144.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q144.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q148.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q148.x1r1p24_e150.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q148.x1u1_e133.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q148.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q149.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q149.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q156.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q161.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q161.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q192.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q192.x1r1p30_e173.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q192.x1r1p33_e178.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q192.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q203.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q203.x1r2p46_e234.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q203.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q206.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q206.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q207.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q207.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q210.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q211.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q212.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q212.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q215.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q215.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q232.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q243.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q243.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q247.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q265.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q267.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q267.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q270.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q270.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q277.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q277.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q279.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q282.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q282.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q287.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q287.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q293.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q293.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q305.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q307.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q307.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q322.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q351.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q351.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q352.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q352.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q362.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q362.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q363.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q370.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q378.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q378.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q379.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q379.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q381.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q381.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q403.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q403.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q405.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q405.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q407.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q407.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q409.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q409.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q415.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q415.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q423.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q423.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q426.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q426.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q427.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q441.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q441.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q444.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q444.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q452.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q452.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q469.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q469.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q472.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q472.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q474.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q474.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q479.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q479.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q482.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q482.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q488.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q488.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q494.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp02q494.x1r1p17_e87.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q210.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q220.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q222.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q222.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q226.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q233.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q240.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q245.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q251.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q251.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q256.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q256.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q266.x1r1p14_e79.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q266.y1u1_e195.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q266.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q268.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q268.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q275.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q275.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q283.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q288.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q288.y3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q307.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q312.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q318.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q329.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q330.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q330.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q335.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q335.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q350.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q350.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q357.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q357.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q364.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q364.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q364.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q368.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q380.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q380.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q380.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q387.x4.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q387.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q393.x5.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp03q393.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q104.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q104.y1u1_e134.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q104.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q110.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q110.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q112.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q112.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q136.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q136.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q137.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q137.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q138.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q138.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q141.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q142.x1u2_e247.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q142.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q145.x1r1p12_e70.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q145.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q145.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q155.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q155.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q171.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q171.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q179.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q180.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q180.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q202.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q206.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q206.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q207.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q207.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q214.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q214.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q219.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q219.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q222.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q222.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q224.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q234.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q237.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q239.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q239.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q241.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q241.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q246.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q246.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q254.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q257.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q257.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q260.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q260.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q295.y1u1_e21.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q317.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q317.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q328.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q331.x1u1_e146.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q331.y1u1_e137.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q331.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q332.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q339.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q343.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q347.y1u1_e193.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q347.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q350.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q372.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q375.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q385.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q390.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q409.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q422.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q429.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q429.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q451.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q451.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q458.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q458.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q464.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q472.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a1_fp04q483.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q105.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q108.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q108.x1r1p12_e69.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q108.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q116.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q116.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q116.y1u1_e143.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q117.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q117.x1r2p51_e249.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q117.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q127.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q127.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q150.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q150.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q152.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q152.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q167.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q167.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q178.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q187.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q187.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q189.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q201.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q201.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q208.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q210.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q210.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q217.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q217.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q219.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q219.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q220.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q220.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q226.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q226.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q227.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q227.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q233.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q233.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q246.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q246.y1u1_e75.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q263.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q263.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q268.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q268.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q268.y1u1_e65.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q273.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q273.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q283.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q283.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q284.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q286.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q334.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q334.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q339.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q339.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q345.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q345.y1u1_e139.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q345.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q348.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q348.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q363.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q365.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q365.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q367.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q367.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q374.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q374.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q379.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q379.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q390.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q390.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q404.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q404.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q405.x1u1_e61.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q405.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q405.y1u1_e62.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q405.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q409.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q409.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q420.x1u1_e136.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q420.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q420.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q421.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q421.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q424.x1u1_e80.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q424.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q424.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q425.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q425.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q441.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q441.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q443.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q443.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q453.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q453.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q455.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q455.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q461.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q461.y1u1_e135.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q461.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q464.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q464.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q471.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q471.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q474.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q474.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q477.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q477.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q480.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q480.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q482.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q482.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q484.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q484.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q485.x3.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp01q485.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q105.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q105.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q107.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q107.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q110.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q110.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q112.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q112.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q124.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q124.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q126.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q126.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q134.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q134.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q143.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q144.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q145.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q145.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q147.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q147.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q150.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q150.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q161.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q165.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q173.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q173.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q175.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q175.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q177.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q177.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q187.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q187.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q188.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q189.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q189.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q209.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q210.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q210.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q214.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q222.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q222.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q231.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q231.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q234.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q234.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q238.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q238.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q240.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q240.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q242.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q242.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q243.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q243.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q248.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q248.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q250.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q253.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q253.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q264.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q264.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q266.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q266.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q268.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q268.x1u1_e131.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q268.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q273.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q289.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q290.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q290.x1r2p46_e235.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q290.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q291.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q291.x1r1p25_e153.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q291.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q291.y1u1_e142.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q294.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q295.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q309.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q309.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q314.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q314.y1u1_e64.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q319.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q319.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q321.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q321.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q331.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q336.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q336.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q344.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q344.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q347.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q349.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q349.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q354.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q354.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q358.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q358.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q359.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q359.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q360.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q360.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q363.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q369.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q369.x1r2p51_e248.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q369.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q370.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q370.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q375.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q375.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q381.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q381.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q386.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q386.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q388.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q388.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q419.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q419.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q425.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q425.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q427.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q427.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q428.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q428.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q430.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q430.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q435.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q435.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q438.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q438.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q440.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q440.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q444.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q444.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q445.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q445.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q445.y1u1_e140.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q446.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q446.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q451.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q451.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q464.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q464.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q465.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q465.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q475.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q475.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q480.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q480.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q483.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q483.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q488.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q488.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp02q494.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q102.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q104.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q107.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q108.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q112.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q119.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q126.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q127.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q127.x1u1_e132.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q127.y1u1_e129.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q133.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q136.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q138.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q138.y1u1_e128.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q146.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q152.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q153.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q156.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q159.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q161.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q164.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q171.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q172.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q173.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q177.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q177.x1r2p62_e291.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q177.y1u2_e289.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q183.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q187.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q189.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q210.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q210.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q211.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q211.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q212.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q212.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q216.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q216.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q218.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q218.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q218.y1u1_e138.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q225.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q225.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q227.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q227.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q229.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q238.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q238.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q238.y1u1_e67.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q275.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q275.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q280.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q280.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q284.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q284.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q286.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q286.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q287.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q287.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q293.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q293.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q303.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q306.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q315.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q338.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q338.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q341.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q341.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q342.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q342.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q342.y1u1_e66.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q343.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q343.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q344.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q344.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q346.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q346.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q349.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q349.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q350.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q350.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q355.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q355.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q368.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q368.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q368.y1u1_e81.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q370.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q370.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q372.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q372.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q376.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q376.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q378.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q378.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q379.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q379.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q380.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q382.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q382.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q383.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q383.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q386.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q386.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q392.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q392.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q403.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q403.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q404.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q404.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q405.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q405.x1u1_e130.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q405.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q407.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q407.x1u1_e182.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q409.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q409.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q413.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q413.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q415.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q415.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q416.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q418.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q418.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q419.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q419.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q423.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q423.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q432.y1u2_e254.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q433.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q433.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q436.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q436.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q437.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q437.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q445.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q445.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q455.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q455.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q457.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q457.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q459.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q459.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q462.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q462.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q465.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q465.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q469.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q474.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q474.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q483.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q483.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q485.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q485.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q488.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q489.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q489.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q493.x1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q493.x1r1p28_e160.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp03q493.y1.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q103.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q103.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q107.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q107.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q114.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q114.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q121.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q121.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q122.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q122.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q125.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q125.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q132.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q132.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q133.x1u1_e141.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q133.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q133.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q142.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q142.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q146.x1r1p15_e83.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q146.x1u1_e82.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q146.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q146.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q149.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q149.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q151.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q151.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q160.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q160.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q166.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q166.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q169.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q169.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q170.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q170.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q171.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q171.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q172.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q172.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q175.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q182.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q182.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q202.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q202.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q210.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q210.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q211.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q211.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q216.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q216.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q219.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q219.y1u1_e145.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q219.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q226.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q229.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q229.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q234.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q234.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q243.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q243.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q253.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q253.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q256.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q256.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q265.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q265.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q273.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q273.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q274.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q274.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q282.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q282.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q286.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q286.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q291.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q293.x2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q293.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q294.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 assembly_view/phd_dir/djs736a2_fp04q296.y2.phd.1 %{_pre_install_dir}/assembly_view/phd_dir
install -m 0644 autofinish/edit_dir/.consedrc.bu %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish_to_alu.cross %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.contigs %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.contigs.log %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.log %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.ace.1 %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.contigs %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.contigs.qual %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.log %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.problems %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.problems.qual %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.qual %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.singlets %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fasta.screen.view %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.fof %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinish.newtags %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autofinishNewChromats.fof %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autoPCRAmplify.fof %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autoPCRAmplify.txt %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/autoPCRAmplify2.txt %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/edit_dir/librariesInfo.txt_hide %{_pre_install_dir}/autofinish/edit_dir
install -m 0644 autofinish/phd_dir/djs228_168.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_331.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_426.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_433.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_434.s3.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_441.s3.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_474.s2.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_481.s2.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_523.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_539.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_560.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_671.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_671.s2.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_715.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_844.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_891.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_892.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1013.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1029.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1033.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1034.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1051.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1094.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1141.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1153.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1211.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1248.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1273.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1331.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1336.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1343.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1418.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1422.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1680.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1740.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1777.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1803.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1919.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_1929.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2019.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2078.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2083.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2116.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2151.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2222.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2273.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2282.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2338.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2346.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2390.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2417.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2436.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2529.s2.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2632.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2659.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2664.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2714.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2751.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2813.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2854.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2862.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2894.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2912.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2933.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_2949.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_3085.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autofinish/phd_dir/djs228_3196.s1.phd.1 %{_pre_install_dir}/autofinish/phd_dir
install -m 0644 autoPCRAmplify_answer/.consedrc %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.ace %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.ace.081205.113938.out %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.fasta %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.cross %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.fasta %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.fasta.log %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/autoPCRAmplify.fof %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/autoPCRAmplify.txt %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/phd_dir/AC004019.C22.4.mRNA.primerRegion.phd.1 %{_pre_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/phd_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.ace %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.ace.081205.113938.out %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.fasta %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.cross %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.fasta %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.fasta.log %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/autoPCRAmplify.fof %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/autoPCRAmplify.txt %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
install -m 0644 autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/phd_dir/AP000527.C22.6.mRNA.primerRegion.phd.1 %{_pre_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/phd_dir
install -m 0644 autoPCRAmplify_answer/brian.fa %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/failures.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/primers_sorted.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/primers_unsorted_shorter.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/primers_unsorted.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/primers081205.fasta %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/to_order.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify_answer/transcripts_filename.txt %{_pre_install_dir}/autoPCRAmplify_answer
install -m 0644 autoPCRAmplify/brian.fa %{_pre_install_dir}/autoPCRAmplify
install -m 0644 misc/filter454Reads.fa %{_pre_install_dir}/misc
install -m 0644 misc/primerCloneScreen.seq %{_pre_install_dir}/misc
install -m 0644 misc/primerSubcloneScreen.seq %{_pre_install_dir}/misc
install -m 0644 misc/repeats.fasta %{_pre_install_dir}/misc
install -m 0644 misc/sffLinkers.fa %{_pre_install_dir}/misc
install -m 0644 misc/singleVectorForRestrictionDigest.fasta %{_pre_install_dir}/misc
install -m 0644 misc/vector.seq %{_pre_install_dir}/misc
install -m 0644 phaster2Ace_answer/edit_dir/chr1.fa %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/fake_genome.fof %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/matrix.txt %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/myAce.ace %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/phaster.fof %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/phaster.phout %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/references.100819_095609.fa %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/references.ace %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/edit_dir/snps.txt %{_pre_install_dir}/phaster2Ace_answer/edit_dir
install -m 0644 phaster2Ace_answer/phdball_dir/phd.ball.1 %{_pre_install_dir}/phaster2Ace_answer/phdball_dir
install -m 0644 phaster2Ace_answer/phdball_dir/phd.ball.2 %{_pre_install_dir}/phaster2Ace_answer/phdball_dir
install -m 0644 phaster2Ace/edit_dir/chr1.fa %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0644 phaster2Ace/edit_dir/fake_genome.fof %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0644 phaster2Ace/edit_dir/phaster.fof %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0644 phaster2Ace/edit_dir/phaster.phout %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0644 phaster2Ace/edit_dir/snps.txt %{_pre_install_dir}/phaster2Ace/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/.consedrc %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/4_102.uncalibrated.clusters.phout %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/chrA.fa %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/fake_genome.fof %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/myAce.ace %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/phaster_output.fof %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/edit_dir/snps.txt %{_pre_install_dir}/phaster2Miniassembly_answer/edit_dir
install -m 0644 phaster2Miniassembly_answer/phdball_dir/phd.ball.1 %{_pre_install_dir}/phaster2Miniassembly_answer/phdball_dir
install -m 0644 phaster2Miniassembly_answer/phdball_dir/phd.ball.2 %{_pre_install_dir}/phaster2Miniassembly_answer/phdball_dir
install -m 0644 phaster2Miniassembly/edit_dir/4_102.uncalibrated.clusters.phout %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0644 phaster2Miniassembly/edit_dir/chrA.fa %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0644 phaster2Miniassembly/edit_dir/fake_genome.fof %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0644 phaster2Miniassembly/edit_dir/phaster_output.fof %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0644 phaster2Miniassembly/edit_dir/snps.txt %{_pre_install_dir}/phaster2Miniassembly/edit_dir
install -m 0644 polyphred/chromat_dir/ca-9.r %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/ca-9.s %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/ca-21.s %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/ca-22.r %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/ca-22.s %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/ca-23.s %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/va-1.x %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/va-13.x %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/va-16.x %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/chromat_dir/va-23.x %{_pre_install_dir}/polyphred/chromat_dir
install -m 0644 polyphred/edit_dir/core %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2_to_alu.cross %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.contigs %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.contigs.log %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.log %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.ace.1 %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.contigs %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.contigs.qual %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.log %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.polyphred.out %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.qual %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.singlets %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.fasta.screen.view %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.newtags %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.phrap.out %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/example2.screen.out %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/phd.fof %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/problem_reads %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/edit_dir/problem_reads.qual %{_pre_install_dir}/polyphred/edit_dir
install -m 0644 polyphred/phd_dir/ca-9.r.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/ca-9.s.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/ca-21.s.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/ca-22.r.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/ca-22.s.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/ca-23.s.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/va-1.x.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/va-13.x.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/va-16.x.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/phd_dir/va-23.x.phd.1 %{_pre_install_dir}/polyphred/phd_dir
install -m 0644 polyphred/poly_dir/ca-9.r.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/ca-9.s.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/ca-21.s.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/ca-22.r.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/ca-22.s.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/ca-23.s.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/va-1.x.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/va-13.x.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/va-16.x.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 polyphred/poly_dir/va-23.x.poly %{_pre_install_dir}/polyphred/poly_dir
install -m 0644 README.txt %{_pre_install_dir}
install -m 0644 selectRegions/edit_dir/ref.fa %{_pre_install_dir}/selectRegions/edit_dir
install -m 0644 selectRegions/edit_dir/refs.fof %{_pre_install_dir}/selectRegions/edit_dir
install -m 0644 selectRegions/edit_dir/regions.txt %{_pre_install_dir}/selectRegions/edit_dir
install -m 0644 selectRegions/edit_dir/solexa_files.fof %{_pre_install_dir}/selectRegions/edit_dir
install -m 0644 selectRegions/solexa_dir/solexa_reads.fastq %{_pre_install_dir}/selectRegions/solexa_dir
install -m 0644 selectRegionsAnswer/edit_dir/alignmentFile.081126_161722.cross.0 %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/my_alignments.fof %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/my_new_ace.ace.1 %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/my_new_ace.ace.2 %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/newAceFile.fof %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/ref.fa %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/refs.fof %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/regions.txt %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/edit_dir/solexa_files.fof %{_pre_install_dir}/selectRegionsAnswer/edit_dir
install -m 0644 selectRegionsAnswer/phdball_dir/phd.ball.1 %{_pre_install_dir}/selectRegionsAnswer/phdball_dir
install -m 0644 selectRegionsAnswer/phdball_dir/phd.ball.2 %{_pre_install_dir}/selectRegionsAnswer/phdball_dir
install -m 0644 selectRegionsAnswer/phdball_dir/phd.ball.3 %{_pre_install_dir}/selectRegionsAnswer/phdball_dir
install -m 0644 selectRegionsAnswer/solexa_dir/solexa_reads.fastq %{_pre_install_dir}/selectRegionsAnswer/solexa_dir
install -m 0644 solexa_example_answer/edit_dir/ref.ace %{_pre_install_dir}/solexa_example_answer/edit_dir
install -m 0644 solexa_example_answer/edit_dir/ref.ace.1 %{_pre_install_dir}/solexa_example_answer/edit_dir
install -m 0644 solexa_example_answer/edit_dir/ref.fa %{_pre_install_dir}/solexa_example_answer/edit_dir
install -m 0644 solexa_example_answer/edit_dir/solexa_files.fof %{_pre_install_dir}/solexa_example_answer/edit_dir
install -m 0644 solexa_example_answer/phdball_dir/phd.ball.1 %{_pre_install_dir}/solexa_example_answer/phdball_dir
install -m 0644 solexa_example_answer/phdball_dir/phd.ball.2 %{_pre_install_dir}/solexa_example_answer/phdball_dir
install -m 0644 solexa_example_answer/solexa_dir/solexa_reads.fastq %{_pre_install_dir}/solexa_example_answer/solexa_dir
install -m 0644 solexa_example/edit_dir/ref.fa %{_pre_install_dir}/solexa_example/edit_dir
install -m 0644 solexa_example/edit_dir/solexa_files.fof %{_pre_install_dir}/solexa_example/edit_dir
install -m 0644 solexa_example/solexa_dir/solexa_reads.fastq %{_pre_install_dir}/solexa_example/solexa_dir
install -m 0644 standard/chromat_dir/djs74-237.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-423.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-561.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-564.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-690.x1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-824.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-932.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-996.s2 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1180.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1432.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1532.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1802.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1803.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1861.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-1871.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2231.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2350.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2361.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2516.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2664.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2679.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2689.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-2931.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromat_dir/djs74-3174.s1 %{_pre_install_dir}/standard/chromat_dir
install -m 0644 standard/chromats_to_add/djs74-536.s2 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-568.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-649.x1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-867.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-1455.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-1465.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-2282.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-2712.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/chromats_to_add/djs74-2861.s1 %{_pre_install_dir}/standard/chromats_to_add
install -m 0644 standard/edit_dir/custom_navigation.nav %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/fragSizes.txt %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/reads_to_add.fof %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/reads_to_remove.fof %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard_to_alu.cross %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.030328.142354.fasta %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.030328.142354.fasta.log %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.contigs %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.contigs.log %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.log %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.ace.1 %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.ace.1.aview %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.contigs %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.contigs.qual %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.log %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.problems %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.problems.qual %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.qual %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.singlets %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.fasta.screen.view %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.newtags %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.phrap.out %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standard.screen.out %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/edit_dir/standardNewChromats.fof %{_pre_install_dir}/standard/edit_dir
install -m 0644 standard/phd_dir/djs74-237.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-423.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-423.s1.phd.2 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-561.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-564.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-690.x1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-824.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-932.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-996.s2.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1180.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1432.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1532.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1802.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1803.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1861.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-1871.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2231.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2350.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2361.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2516.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2664.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2679.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2689.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-2931.s1.phd.1 %{_pre_install_dir}/standard/phd_dir
install -m 0644 standard/phd_dir/djs74-3174.s1.phd.1 %{_pre_install_dir}/standard/phd_dir

cat <<EOF >  %{bundle_profile_dir}/%{_pkg_base}.sh
export CONSED_HOME=%{prefix}
EOF

%mfest_bin  consed
%mfest_bin  contributions/ace2OligosWithComments.perl     ace2OligosWithComments.perl
%mfest_bin  contributions/aceContigs2Phds.perl            aceContigs2Phds.perl
%mfest_bin  contributions/mergeAces.perl                  mergeAces.perl
%mfest_bin  scripts/phd2Ace.perl                          phd2Ace.perl
%mfest_bin  scripts/phredPhrap                            phredPhrap
%mfest_bin  scripts/polyphredPhrap                        polyphredPhrap
%mfest_bin  scripts/selectRegions.perl                    selectRegions.perl
%mfest_bin  scripts/ace2Fasta.perl                        ace2Fasta.perl
%mfest_bin  scripts/fixContigEnd.perl                     fixContigEnd.perl
%mfest_bin  scripts/makePhdBall.perl                      makePhdBall.perl
%mfest_bin  scripts/tagRepeats.perl                       tagRepeats.perl
%mfest_bin  scripts/amplifyTranscripts.perl               amplifyTranscripts.perl
%mfest_bin  scripts/lib2Phd.perl                          lib2Phd.perl
%mfest_bin  scripts/fasta2PhdBall.perl                    fasta2PhdBall.perl
%mfest_bin  scripts/testSocket.perl                       testSocket.perl
%mfest_bin  scripts/orderPrimerPairs.perl                 orderPrimerPairs.perl
%mfest_bin  scripts/transferConsensusTags.perl            transferConsensusTags.perl
%mfest_bin  scripts/filter454Reads.perl                   filter454Reads.perl
%mfest_bin  scripts/revertToUneditedRead                  revertToUneditedRead
%mfest_bin  scripts/removeReads                           removeReads
%mfest_bin  scripts/determineReadTypes.perl               determineReadTypes.perl
%mfest_bin  scripts/ace2Oligos.perl                       ace2Oligos.perl
%mfest_bin  scripts/addReads2Consed.perl                  addReads2Consed.perl
%mfest_bin  scripts/fasta2Phd.perl                        fasta2Phd.perl
%mfest_bin  scripts/phaster2Ace.perl                      phaster2Ace.perl
%mfest_bin  scripts/add454Reads.perl                      add454Reads.perl
%mfest_bin  scripts/countEditedBases.perl                 countEditedBases.perl
%mfest_bin  scripts/addSolexaReads.perl                   addSolexaReads.perl
%mfest_bin  scripts/fasta2Ace.perl                        fasta2Ace.perl
%mfest_bin  scripts/alignSolexaReads2Refs.perl            alignSolexaReads2Refs.perl
%mfest_bin  scripts/findSequenceMatchesForConsed.perl     findSequenceMatchesForConsed.perl
%mfest_bin  scripts/phaster2Miniassembly.perl             phaster2Miniassembly.perl
%mfest_profile   __profile__/%{_pkg_base}.sh %{_pkg_base}.sh


%post
cat <<EOF >  %{_post_install_dir}/__profile__/%{_pkg_base}.sh
export CONSED_HOME=$RPM_INSTALL_PREFIX0
EOF


%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/assembly_view
%dir %{_install_dir}/assembly_view/phd_dir
%dir %{_install_dir}/assembly_view/edit_dir
%dir %{_install_dir}/polyphred
%dir %{_install_dir}/polyphred/phd_dir
%dir %{_install_dir}/polyphred/edit_dir
%dir %{_install_dir}/polyphred/poly_dir
%dir %{_install_dir}/polyphred/chromat_dir
%dir %{_install_dir}/contributions
%dir %{_install_dir}/autoPCRAmplify_answer
%dir %{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion
%dir %{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/phd_dir
%dir %{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir
%dir %{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion
%dir %{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/phd_dir
%dir %{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir
%dir %{_install_dir}/phaster2Miniassembly
%dir %{_install_dir}/phaster2Miniassembly/edit_dir
%dir %{_install_dir}/standard
%dir %{_install_dir}/standard/phd_dir
%dir %{_install_dir}/standard/chromats_to_add
%dir %{_install_dir}/standard/edit_dir
%dir %{_install_dir}/standard/chromat_dir
%dir %{_install_dir}/phaster2Ace
%dir %{_install_dir}/phaster2Ace/edit_dir
%dir %{_install_dir}/phaster2Ace_answer
%dir %{_install_dir}/phaster2Ace_answer/edit_dir
%dir %{_install_dir}/phaster2Ace_answer/phdball_dir
%dir %{_install_dir}/misc
%dir %{_install_dir}/454_newbler
%dir %{_install_dir}/454_newbler/sff_dir
%dir %{_install_dir}/454_newbler/edit_dir
%dir %{_install_dir}/454_newbler/phdball_dir
%dir %{_install_dir}/scripts
%dir %{_install_dir}/selectRegionsAnswer
%dir %{_install_dir}/selectRegionsAnswer/solexa_dir
%dir %{_install_dir}/selectRegionsAnswer/edit_dir
%dir %{_install_dir}/selectRegionsAnswer/phdball_dir
%dir %{_install_dir}/solexa_example
%dir %{_install_dir}/solexa_example/solexa_dir
%dir %{_install_dir}/solexa_example/edit_dir
%dir %{_install_dir}/align454reads_answer
%dir %{_install_dir}/align454reads_answer/sff_dir
%dir %{_install_dir}/align454reads_answer/edit_dir
%dir %{_install_dir}/align454reads_answer/phdball_dir
%dir %{_install_dir}/align454reads
%dir %{_install_dir}/align454reads/sff_dir
%dir %{_install_dir}/align454reads/edit_dir
%dir %{_install_dir}/autofinish
%dir %{_install_dir}/autofinish/phd_dir
%dir %{_install_dir}/autofinish/edit_dir
%dir %{_install_dir}/solexa_example_answer
%dir %{_install_dir}/solexa_example_answer/solexa_dir
%dir %{_install_dir}/solexa_example_answer/edit_dir
%dir %{_install_dir}/solexa_example_answer/phdball_dir
%dir %{_install_dir}/selectRegions
%dir %{_install_dir}/selectRegions/solexa_dir
%dir %{_install_dir}/selectRegions/edit_dir
%dir %{_install_dir}/phaster2Miniassembly_answer
%dir %{_install_dir}/phaster2Miniassembly_answer/edit_dir
%dir %{_install_dir}/phaster2Miniassembly_answer/phdball_dir
%dir %{_install_dir}/autoPCRAmplify

%{_install_dir}/consed
%{_install_dir}/20.0_announcement.txt
%{_install_dir}/454_newbler/edit_dir/454Contigs.ace.1
%{_install_dir}/454_newbler/edit_dir/454Contigs.ace.1.091026.110917.fasta
%{_install_dir}/454_newbler/edit_dir/454Contigs.ace.1.aview
%{_install_dir}/454_newbler/phdball_dir/phd.ball.1
%{_install_dir}/454_newbler/sff_dir/pairedreads.sff
%{_install_dir}/align454reads_answer/edit_dir/reference.ace
%{_install_dir}/align454reads_answer/edit_dir/reference.ace.1
%{_install_dir}/align454reads_answer/edit_dir/reference.fa
%{_install_dir}/align454reads_answer/edit_dir/sff.fof
%{_install_dir}/align454reads_answer/phdball_dir/phd.ball.1
%{_install_dir}/align454reads_answer/phdball_dir/phd.ball.2
%{_install_dir}/align454reads_answer/sff_dir/newreads.sff
%{_install_dir}/align454reads_answer/sff_dir/reads.sff
%{_install_dir}/align454reads/edit_dir/reference.fa
%{_install_dir}/align454reads/edit_dir/sff.fof
%{_install_dir}/align454reads/sff_dir/newreads.sff
%{_install_dir}/align454reads/sff_dir/reads.sff
%{_install_dir}/assembly_view/edit_dir/.consedrc
%{_install_dir}/assembly_view/edit_dir/.consedrc_mini
%{_install_dir}/assembly_view/edit_dir/assembly_view.030319.170348.fasta
%{_install_dir}/assembly_view/edit_dir/assembly_view.030319.170348.fasta.log
%{_install_dir}/assembly_view/edit_dir/assembly_view.fasta.screen.ace.1
%{_install_dir}/assembly_view/edit_dir/assembly_view.fasta.screen.ace.1.aview
%{_install_dir}/assembly_view/edit_dir/doNotShowInAssemblyView.fof
%{_install_dir}/assembly_view/edit_dir/fragSizes.txt
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q102.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q124.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q124.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q126.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q126.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q131.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q131.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q134.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q144.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q144.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q148.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q148.x1r1p24_e150.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q148.x1u1_e133.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q148.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q149.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q149.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q156.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q161.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q161.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q192.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q192.x1r1p30_e173.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q192.x1r1p33_e178.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q192.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q203.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q203.x1r2p46_e234.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q203.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q206.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q206.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q207.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q207.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q210.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q211.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q212.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q212.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q215.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q215.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q232.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q243.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q243.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q247.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q265.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q267.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q267.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q270.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q270.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q277.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q277.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q279.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q282.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q282.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q287.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q287.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q293.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q293.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q305.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q307.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q307.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q322.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q351.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q351.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q352.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q352.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q362.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q362.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q363.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q370.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q378.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q378.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q379.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q379.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q381.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q381.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q403.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q403.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q405.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q405.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q407.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q407.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q409.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q409.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q415.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q415.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q423.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q423.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q426.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q426.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q427.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q441.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q441.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q444.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q444.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q452.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q452.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q469.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q469.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q472.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q472.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q474.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q474.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q479.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q479.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q482.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q482.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q488.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q488.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q494.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp02q494.x1r1p17_e87.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q210.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q220.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q222.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q222.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q226.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q233.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q240.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q245.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q251.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q251.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q256.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q256.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q266.x1r1p14_e79.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q266.y1u1_e195.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q266.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q268.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q268.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q275.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q275.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q283.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q288.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q288.y3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q307.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q312.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q318.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q329.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q330.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q330.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q335.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q335.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q350.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q350.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q357.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q357.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q364.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q364.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q364.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q368.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q380.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q380.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q380.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q387.x4.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q387.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q393.x5.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp03q393.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q104.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q104.y1u1_e134.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q104.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q110.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q110.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q112.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q112.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q136.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q136.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q137.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q137.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q138.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q138.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q141.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q142.x1u2_e247.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q142.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q145.x1r1p12_e70.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q145.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q145.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q155.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q155.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q171.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q171.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q179.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q180.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q180.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q202.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q206.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q206.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q207.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q207.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q214.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q214.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q219.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q219.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q222.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q222.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q224.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q234.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q237.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q239.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q239.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q241.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q241.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q246.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q246.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q254.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q257.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q257.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q260.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q260.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q295.y1u1_e21.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q317.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q317.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q328.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q331.x1u1_e146.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q331.y1u1_e137.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q331.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q332.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q339.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q343.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q347.y1u1_e193.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q347.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q350.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q372.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q375.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q385.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q390.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q409.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q422.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q429.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q429.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q451.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q451.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q458.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q458.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q464.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q472.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a1_fp04q483.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q105.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q108.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q108.x1r1p12_e69.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q108.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q116.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q116.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q116.y1u1_e143.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q117.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q117.x1r2p51_e249.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q117.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q127.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q127.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q150.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q150.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q152.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q152.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q167.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q167.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q178.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q187.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q187.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q189.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q201.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q201.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q208.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q210.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q210.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q217.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q217.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q219.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q219.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q220.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q220.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q226.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q226.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q227.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q227.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q233.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q233.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q246.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q246.y1u1_e75.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q263.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q263.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q268.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q268.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q268.y1u1_e65.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q273.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q273.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q283.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q283.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q284.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q286.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q334.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q334.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q339.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q339.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q345.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q345.y1u1_e139.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q345.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q348.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q348.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q363.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q365.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q365.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q367.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q367.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q374.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q374.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q379.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q379.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q390.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q390.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q404.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q404.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q405.x1u1_e61.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q405.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q405.y1u1_e62.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q405.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q409.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q409.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q420.x1u1_e136.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q420.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q420.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q421.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q421.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q424.x1u1_e80.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q424.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q424.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q425.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q425.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q441.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q441.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q443.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q443.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q453.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q453.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q455.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q455.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q461.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q461.y1u1_e135.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q461.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q464.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q464.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q471.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q471.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q474.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q474.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q477.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q477.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q480.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q480.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q482.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q482.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q484.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q484.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q485.x3.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp01q485.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q105.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q105.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q107.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q107.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q110.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q110.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q112.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q112.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q124.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q124.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q126.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q126.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q134.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q134.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q143.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q144.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q145.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q145.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q147.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q147.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q150.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q150.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q161.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q165.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q173.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q173.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q175.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q175.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q177.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q177.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q187.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q187.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q188.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q189.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q189.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q209.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q210.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q210.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q214.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q222.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q222.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q231.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q231.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q234.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q234.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q238.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q238.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q240.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q240.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q242.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q242.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q243.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q243.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q248.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q248.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q250.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q253.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q253.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q264.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q264.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q266.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q266.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q268.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q268.x1u1_e131.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q268.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q273.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q289.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q290.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q290.x1r2p46_e235.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q290.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q291.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q291.x1r1p25_e153.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q291.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q291.y1u1_e142.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q294.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q295.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q309.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q309.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q314.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q314.y1u1_e64.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q319.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q319.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q321.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q321.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q331.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q336.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q336.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q344.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q344.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q347.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q349.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q349.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q354.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q354.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q358.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q358.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q359.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q359.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q360.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q360.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q363.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q369.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q369.x1r2p51_e248.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q369.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q370.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q370.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q375.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q375.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q381.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q381.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q386.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q386.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q388.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q388.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q419.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q419.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q425.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q425.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q427.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q427.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q428.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q428.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q430.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q430.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q435.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q435.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q438.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q438.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q440.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q440.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q444.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q444.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q445.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q445.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q445.y1u1_e140.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q446.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q446.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q451.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q451.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q464.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q464.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q465.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q465.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q475.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q475.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q480.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q480.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q483.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q483.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q488.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q488.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp02q494.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q102.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q104.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q107.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q108.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q112.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q119.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q126.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q127.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q127.x1u1_e132.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q127.y1u1_e129.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q133.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q136.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q138.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q138.y1u1_e128.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q146.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q152.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q153.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q156.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q159.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q161.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q164.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q171.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q172.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q173.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q177.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q177.x1r2p62_e291.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q177.y1u2_e289.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q183.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q187.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q189.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q210.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q210.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q211.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q211.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q212.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q212.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q216.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q216.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q218.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q218.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q218.y1u1_e138.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q225.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q225.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q227.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q227.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q229.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q238.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q238.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q238.y1u1_e67.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q275.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q275.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q280.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q280.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q284.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q284.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q286.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q286.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q287.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q287.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q293.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q293.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q303.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q306.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q315.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q338.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q338.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q341.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q341.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q342.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q342.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q342.y1u1_e66.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q343.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q343.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q344.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q344.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q346.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q346.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q349.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q349.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q350.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q350.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q355.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q355.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q368.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q368.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q368.y1u1_e81.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q370.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q370.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q372.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q372.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q376.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q376.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q378.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q378.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q379.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q379.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q380.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q382.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q382.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q383.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q383.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q386.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q386.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q392.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q392.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q403.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q403.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q404.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q404.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q405.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q405.x1u1_e130.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q405.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q407.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q407.x1u1_e182.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q409.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q409.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q413.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q413.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q415.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q415.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q416.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q418.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q418.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q419.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q419.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q423.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q423.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q432.y1u2_e254.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q433.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q433.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q436.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q436.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q437.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q437.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q445.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q445.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q455.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q455.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q457.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q457.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q459.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q459.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q462.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q462.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q465.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q465.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q469.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q474.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q474.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q483.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q483.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q485.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q485.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q488.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q489.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q489.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q493.x1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q493.x1r1p28_e160.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp03q493.y1.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q103.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q103.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q107.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q107.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q114.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q114.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q121.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q121.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q122.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q122.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q125.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q125.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q132.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q132.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q133.x1u1_e141.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q133.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q133.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q142.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q142.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q146.x1r1p15_e83.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q146.x1u1_e82.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q146.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q146.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q149.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q149.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q151.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q151.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q160.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q160.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q166.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q166.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q169.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q169.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q170.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q170.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q171.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q171.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q172.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q172.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q175.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q182.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q182.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q202.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q202.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q210.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q210.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q211.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q211.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q216.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q216.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q219.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q219.y1u1_e145.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q219.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q226.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q229.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q229.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q234.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q234.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q243.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q243.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q253.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q253.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q256.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q256.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q265.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q265.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q273.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q273.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q274.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q274.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q282.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q282.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q286.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q286.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q291.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q293.x2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q293.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q294.y2.phd.1
%{_install_dir}/assembly_view/phd_dir/djs736a2_fp04q296.y2.phd.1
%{_install_dir}/autofinish/edit_dir/.consedrc.bu
%{_install_dir}/autofinish/edit_dir/autofinish_to_alu.cross
%{_install_dir}/autofinish/edit_dir/autofinish.contigs
%{_install_dir}/autofinish/edit_dir/autofinish.contigs.log
%{_install_dir}/autofinish/edit_dir/autofinish.fasta
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.log
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.ace.1
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.contigs
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.contigs.qual
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.log
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.problems
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.problems.qual
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.qual
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.singlets
%{_install_dir}/autofinish/edit_dir/autofinish.fasta.screen.view
%{_install_dir}/autofinish/edit_dir/autofinish.fof
%{_install_dir}/autofinish/edit_dir/autofinish.newtags
%{_install_dir}/autofinish/edit_dir/autofinishNewChromats.fof
%{_install_dir}/autofinish/edit_dir/autoPCRAmplify.fof
%{_install_dir}/autofinish/edit_dir/autoPCRAmplify.txt
%{_install_dir}/autofinish/edit_dir/autoPCRAmplify2.txt
%{_install_dir}/autofinish/edit_dir/librariesInfo.txt_hide
%{_install_dir}/autofinish/phd_dir/djs228_168.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_331.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_426.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_433.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_434.s3.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_441.s3.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_474.s2.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_481.s2.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_523.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_539.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_560.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_671.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_671.s2.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_715.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_844.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_891.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_892.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1013.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1029.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1033.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1034.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1051.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1094.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1141.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1153.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1211.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1248.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1273.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1331.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1336.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1343.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1418.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1422.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1680.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1740.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1777.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1803.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1919.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_1929.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2019.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2078.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2083.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2116.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2151.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2222.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2273.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2282.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2338.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2346.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2390.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2417.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2436.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2529.s2.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2632.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2659.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2664.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2714.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2751.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2813.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2854.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2862.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2894.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2912.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2933.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_2949.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_3085.s1.phd.1
%{_install_dir}/autofinish/phd_dir/djs228_3196.s1.phd.1
%{_install_dir}/autoPCRAmplify_answer/.consedrc
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.ace
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.ace.081205.113938.out
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.fasta
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.cross
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.fasta
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/AC004019.C22.4.mRNA.primerRegion.primers.fasta.log
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/autoPCRAmplify.fof
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/edit_dir/autoPCRAmplify.txt
%{_install_dir}/autoPCRAmplify_answer/AC004019.C22.4.mRNA.primerRegion/phd_dir/AC004019.C22.4.mRNA.primerRegion.phd.1
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.ace
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.ace.081205.113938.out
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.fasta
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.cross
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.fasta
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/AP000527.C22.6.mRNA.primerRegion.primers.fasta.log
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/autoPCRAmplify.fof
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/edit_dir/autoPCRAmplify.txt
%{_install_dir}/autoPCRAmplify_answer/AP000527.C22.6.mRNA.primerRegion/phd_dir/AP000527.C22.6.mRNA.primerRegion.phd.1
%{_install_dir}/autoPCRAmplify_answer/brian.fa
%{_install_dir}/autoPCRAmplify_answer/failures.txt
%{_install_dir}/autoPCRAmplify_answer/primers_sorted.txt
%{_install_dir}/autoPCRAmplify_answer/primers_unsorted_shorter.txt
%{_install_dir}/autoPCRAmplify_answer/primers_unsorted.txt
%{_install_dir}/autoPCRAmplify_answer/primers081205.fasta
%{_install_dir}/autoPCRAmplify_answer/to_order.txt
%{_install_dir}/autoPCRAmplify_answer/transcripts_filename.txt
%{_install_dir}/autoPCRAmplify/brian.fa
%{_install_dir}/contributions/ace2fof
%{_install_dir}/contributions/ace2OligosWithComments.perl
%{_install_dir}/contributions/aceContigs2Phds.perl
%{_install_dir}/contributions/acestatus.pl
%{_install_dir}/contributions/export_cons
%{_install_dir}/contributions/mergeAces.perl
%{_install_dir}/contributions/recover_consensus_tags
%{_install_dir}/contributions/revert_fof
%{_install_dir}/misc/filter454Reads.fa
%{_install_dir}/misc/primerCloneScreen.seq
%{_install_dir}/misc/primerSubcloneScreen.seq
%{_install_dir}/misc/repeats.fasta
%{_install_dir}/misc/sffLinkers.fa
%{_install_dir}/misc/singleVectorForRestrictionDigest.fasta
%{_install_dir}/misc/vector.seq
%{_install_dir}/phaster2Ace_answer/edit_dir/chr1.fa
%{_install_dir}/phaster2Ace_answer/edit_dir/fake_genome.fof
%{_install_dir}/phaster2Ace_answer/edit_dir/matrix.txt
%{_install_dir}/phaster2Ace_answer/edit_dir/myAce.ace
%{_install_dir}/phaster2Ace_answer/edit_dir/phaster.fof
%{_install_dir}/phaster2Ace_answer/edit_dir/phaster.phout
%{_install_dir}/phaster2Ace_answer/edit_dir/references.100819_095609.fa
%{_install_dir}/phaster2Ace_answer/edit_dir/references.ace
%{_install_dir}/phaster2Ace_answer/edit_dir/snps.txt
%{_install_dir}/phaster2Ace_answer/phdball_dir/phd.ball.1
%{_install_dir}/phaster2Ace_answer/phdball_dir/phd.ball.2
%{_install_dir}/phaster2Ace/edit_dir/chr1.fa
%{_install_dir}/phaster2Ace/edit_dir/fake_genome.fof
%{_install_dir}/phaster2Ace/edit_dir/phaster.fof
%{_install_dir}/phaster2Ace/edit_dir/phaster.phout
%{_install_dir}/phaster2Ace/edit_dir/snps.txt
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/.consedrc
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/4_102.uncalibrated.clusters.phout
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/chrA.fa
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/fake_genome.fof
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/myAce.ace
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/phaster_output.fof
%{_install_dir}/phaster2Miniassembly_answer/edit_dir/snps.txt
%{_install_dir}/phaster2Miniassembly_answer/phdball_dir/phd.ball.1
%{_install_dir}/phaster2Miniassembly_answer/phdball_dir/phd.ball.2
%{_install_dir}/phaster2Miniassembly/edit_dir/4_102.uncalibrated.clusters.phout
%{_install_dir}/phaster2Miniassembly/edit_dir/chrA.fa
%{_install_dir}/phaster2Miniassembly/edit_dir/fake_genome.fof
%{_install_dir}/phaster2Miniassembly/edit_dir/phaster_output.fof
%{_install_dir}/phaster2Miniassembly/edit_dir/snps.txt
%{_install_dir}/polyphred/chromat_dir/ca-9.r
%{_install_dir}/polyphred/chromat_dir/ca-9.s
%{_install_dir}/polyphred/chromat_dir/ca-21.s
%{_install_dir}/polyphred/chromat_dir/ca-22.r
%{_install_dir}/polyphred/chromat_dir/ca-22.s
%{_install_dir}/polyphred/chromat_dir/ca-23.s
%{_install_dir}/polyphred/chromat_dir/va-1.x
%{_install_dir}/polyphred/chromat_dir/va-13.x
%{_install_dir}/polyphred/chromat_dir/va-16.x
%{_install_dir}/polyphred/chromat_dir/va-23.x
%{_install_dir}/polyphred/edit_dir/core
%{_install_dir}/polyphred/edit_dir/example2_to_alu.cross
%{_install_dir}/polyphred/edit_dir/example2.contigs
%{_install_dir}/polyphred/edit_dir/example2.contigs.log
%{_install_dir}/polyphred/edit_dir/example2.fasta
%{_install_dir}/polyphred/edit_dir/example2.fasta.log
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.ace.1
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.contigs
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.contigs.qual
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.log
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.polyphred.out
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.qual
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.singlets
%{_install_dir}/polyphred/edit_dir/example2.fasta.screen.view
%{_install_dir}/polyphred/edit_dir/example2.newtags
%{_install_dir}/polyphred/edit_dir/example2.phrap.out
%{_install_dir}/polyphred/edit_dir/example2.screen.out
%{_install_dir}/polyphred/edit_dir/phd.fof
%{_install_dir}/polyphred/edit_dir/problem_reads
%{_install_dir}/polyphred/edit_dir/problem_reads.qual
%{_install_dir}/polyphred/phd_dir/ca-9.r.phd.1
%{_install_dir}/polyphred/phd_dir/ca-9.s.phd.1
%{_install_dir}/polyphred/phd_dir/ca-21.s.phd.1
%{_install_dir}/polyphred/phd_dir/ca-22.r.phd.1
%{_install_dir}/polyphred/phd_dir/ca-22.s.phd.1
%{_install_dir}/polyphred/phd_dir/ca-23.s.phd.1
%{_install_dir}/polyphred/phd_dir/va-1.x.phd.1
%{_install_dir}/polyphred/phd_dir/va-13.x.phd.1
%{_install_dir}/polyphred/phd_dir/va-16.x.phd.1
%{_install_dir}/polyphred/phd_dir/va-23.x.phd.1
%{_install_dir}/polyphred/poly_dir/ca-9.r.poly
%{_install_dir}/polyphred/poly_dir/ca-9.s.poly
%{_install_dir}/polyphred/poly_dir/ca-21.s.poly
%{_install_dir}/polyphred/poly_dir/ca-22.r.poly
%{_install_dir}/polyphred/poly_dir/ca-22.s.poly
%{_install_dir}/polyphred/poly_dir/ca-23.s.poly
%{_install_dir}/polyphred/poly_dir/va-1.x.poly
%{_install_dir}/polyphred/poly_dir/va-13.x.poly
%{_install_dir}/polyphred/poly_dir/va-16.x.poly
%{_install_dir}/polyphred/poly_dir/va-23.x.poly
%{_install_dir}/README.txt
%{_install_dir}/scripts/ace2Fasta.perl
%{_install_dir}/scripts/ace2Oligos.perl
%{_install_dir}/scripts/add454Reads.perl
%{_install_dir}/scripts/addReads2Consed.perl
%{_install_dir}/scripts/addSolexaReads.perl
%{_install_dir}/scripts/alignSolexaReads2Refs.perl
%{_install_dir}/scripts/amplifyTranscripts.perl
%{_install_dir}/scripts/countEditedBases.perl
%{_install_dir}/scripts/determineReadTypes.perl
%{_install_dir}/scripts/fasta2Ace.perl
%{_install_dir}/scripts/fasta2Phd.perl
%{_install_dir}/scripts/fasta2PhdBall.perl
%{_install_dir}/scripts/filter454Reads.perl
%{_install_dir}/scripts/findSequenceMatchesForConsed.perl
%{_install_dir}/scripts/fixContigEnd.perl
%{_install_dir}/scripts/lib2Phd.perl
%{_install_dir}/scripts/makePhdBall.perl
%{_install_dir}/scripts/orderPrimerPairs.perl
%{_install_dir}/scripts/phaster2Ace.perl
%{_install_dir}/scripts/phaster2Miniassembly.perl
%{_install_dir}/scripts/phd2Ace.perl
%{_install_dir}/scripts/phredPhrap
%{_install_dir}/scripts/polyphredPhrap
%{_install_dir}/scripts/removeReads
%{_install_dir}/scripts/revertToUneditedRead
%{_install_dir}/scripts/selectRegions.perl
%{_install_dir}/scripts/tagRepeats.perl
%{_install_dir}/scripts/testSocket.perl
%{_install_dir}/scripts/transferConsensusTags.perl
%{_install_dir}/selectRegions/edit_dir/ref.fa
%{_install_dir}/selectRegions/edit_dir/refs.fof
%{_install_dir}/selectRegions/edit_dir/regions.txt
%{_install_dir}/selectRegions/edit_dir/solexa_files.fof
%{_install_dir}/selectRegions/solexa_dir/solexa_reads.fastq
%{_install_dir}/selectRegionsAnswer/edit_dir/alignmentFile.081126_161722.cross.0
%{_install_dir}/selectRegionsAnswer/edit_dir/my_alignments.fof
%{_install_dir}/selectRegionsAnswer/edit_dir/my_new_ace.ace.1
%{_install_dir}/selectRegionsAnswer/edit_dir/my_new_ace.ace.2
%{_install_dir}/selectRegionsAnswer/edit_dir/newAceFile.fof
%{_install_dir}/selectRegionsAnswer/edit_dir/ref.fa
%{_install_dir}/selectRegionsAnswer/edit_dir/refs.fof
%{_install_dir}/selectRegionsAnswer/edit_dir/regions.txt
%{_install_dir}/selectRegionsAnswer/edit_dir/solexa_files.fof
%{_install_dir}/selectRegionsAnswer/phdball_dir/phd.ball.1
%{_install_dir}/selectRegionsAnswer/phdball_dir/phd.ball.2
%{_install_dir}/selectRegionsAnswer/phdball_dir/phd.ball.3
%{_install_dir}/selectRegionsAnswer/solexa_dir/solexa_reads.fastq
%{_install_dir}/solexa_example_answer/edit_dir/ref.ace
%{_install_dir}/solexa_example_answer/edit_dir/ref.ace.1
%{_install_dir}/solexa_example_answer/edit_dir/ref.fa
%{_install_dir}/solexa_example_answer/edit_dir/solexa_files.fof
%{_install_dir}/solexa_example_answer/phdball_dir/phd.ball.1
%{_install_dir}/solexa_example_answer/phdball_dir/phd.ball.2
%{_install_dir}/solexa_example_answer/solexa_dir/solexa_reads.fastq
%{_install_dir}/solexa_example/edit_dir/ref.fa
%{_install_dir}/solexa_example/edit_dir/solexa_files.fof
%{_install_dir}/solexa_example/solexa_dir/solexa_reads.fastq
%{_install_dir}/standard/chromat_dir/djs74-237.s1
%{_install_dir}/standard/chromat_dir/djs74-423.s1
%{_install_dir}/standard/chromat_dir/djs74-561.s1
%{_install_dir}/standard/chromat_dir/djs74-564.s1
%{_install_dir}/standard/chromat_dir/djs74-690.x1
%{_install_dir}/standard/chromat_dir/djs74-824.s1
%{_install_dir}/standard/chromat_dir/djs74-932.s1
%{_install_dir}/standard/chromat_dir/djs74-996.s2
%{_install_dir}/standard/chromat_dir/djs74-1180.s1
%{_install_dir}/standard/chromat_dir/djs74-1432.s1
%{_install_dir}/standard/chromat_dir/djs74-1532.s1
%{_install_dir}/standard/chromat_dir/djs74-1802.s1
%{_install_dir}/standard/chromat_dir/djs74-1803.s1
%{_install_dir}/standard/chromat_dir/djs74-1861.s1
%{_install_dir}/standard/chromat_dir/djs74-1871.s1
%{_install_dir}/standard/chromat_dir/djs74-2231.s1
%{_install_dir}/standard/chromat_dir/djs74-2350.s1
%{_install_dir}/standard/chromat_dir/djs74-2361.s1
%{_install_dir}/standard/chromat_dir/djs74-2516.s1
%{_install_dir}/standard/chromat_dir/djs74-2664.s1
%{_install_dir}/standard/chromat_dir/djs74-2679.s1
%{_install_dir}/standard/chromat_dir/djs74-2689.s1
%{_install_dir}/standard/chromat_dir/djs74-2931.s1
%{_install_dir}/standard/chromat_dir/djs74-3174.s1
%{_install_dir}/standard/chromats_to_add/djs74-536.s2
%{_install_dir}/standard/chromats_to_add/djs74-568.s1
%{_install_dir}/standard/chromats_to_add/djs74-649.x1
%{_install_dir}/standard/chromats_to_add/djs74-867.s1
%{_install_dir}/standard/chromats_to_add/djs74-1455.s1
%{_install_dir}/standard/chromats_to_add/djs74-1465.s1
%{_install_dir}/standard/chromats_to_add/djs74-2282.s1
%{_install_dir}/standard/chromats_to_add/djs74-2712.s1
%{_install_dir}/standard/chromats_to_add/djs74-2861.s1
%{_install_dir}/standard/edit_dir/custom_navigation.nav
%{_install_dir}/standard/edit_dir/fragSizes.txt
%{_install_dir}/standard/edit_dir/reads_to_add.fof
%{_install_dir}/standard/edit_dir/reads_to_remove.fof
%{_install_dir}/standard/edit_dir/standard_to_alu.cross
%{_install_dir}/standard/edit_dir/standard.030328.142354.fasta
%{_install_dir}/standard/edit_dir/standard.030328.142354.fasta.log
%{_install_dir}/standard/edit_dir/standard.contigs
%{_install_dir}/standard/edit_dir/standard.contigs.log
%{_install_dir}/standard/edit_dir/standard.fasta
%{_install_dir}/standard/edit_dir/standard.fasta.log
%{_install_dir}/standard/edit_dir/standard.fasta.screen
%{_install_dir}/standard/edit_dir/standard.fasta.screen.ace.1
%{_install_dir}/standard/edit_dir/standard.fasta.screen.ace.1.aview
%{_install_dir}/standard/edit_dir/standard.fasta.screen.contigs
%{_install_dir}/standard/edit_dir/standard.fasta.screen.contigs.qual
%{_install_dir}/standard/edit_dir/standard.fasta.screen.log
%{_install_dir}/standard/edit_dir/standard.fasta.screen.problems
%{_install_dir}/standard/edit_dir/standard.fasta.screen.problems.qual
%{_install_dir}/standard/edit_dir/standard.fasta.screen.qual
%{_install_dir}/standard/edit_dir/standard.fasta.screen.singlets
%{_install_dir}/standard/edit_dir/standard.fasta.screen.view
%{_install_dir}/standard/edit_dir/standard.newtags
%{_install_dir}/standard/edit_dir/standard.phrap.out
%{_install_dir}/standard/edit_dir/standard.screen.out
%{_install_dir}/standard/edit_dir/standardNewChromats.fof
%{_install_dir}/standard/phd_dir/djs74-237.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-423.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-423.s1.phd.2
%{_install_dir}/standard/phd_dir/djs74-561.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-564.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-690.x1.phd.1
%{_install_dir}/standard/phd_dir/djs74-824.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-932.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-996.s2.phd.1
%{_install_dir}/standard/phd_dir/djs74-1180.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1432.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1532.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1802.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1803.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1861.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-1871.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2231.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2350.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2361.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2516.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2664.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2679.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2689.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-2931.s1.phd.1
%{_install_dir}/standard/phd_dir/djs74-3174.s1.phd.1
%{_install_dir}/__profile__/%{_pkg_base}.sh

%{_install_dir}/%{_manifest_file}

%dir %{_install_dir}/__profile__
%{_install_dir}/__profile__/%{_pkg_base}.sh



%changelog
* Fri Feb 24 2012 Mark Heiges <mheiges@uga.edu> 20.0-4
- fix profile in MANIFEST
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 20.0-3
- use MANIFEST.EUPATH
* Tue Feb 7 2012 Mark Heiges <mheiges@uga.edu> 20.0-2
- add consed.sh profile
- add polyphredPhrap symlink
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
