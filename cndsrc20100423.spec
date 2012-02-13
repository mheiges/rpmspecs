%define _pkg_base cndsrc

Summary: Colin Dewey computational biology software
Name: %{_pkg_base}-%{version}
Version: 2010.04.23
Release: 2%{?dist}
License: GPLv3
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://www.biostat.wisc.edu/~cdewey/%{_software_topdir}/cndsrc-%{version}.tar.gz

# we can't specify this requirement because it's registered in the 
# system rpm database and this rpm may be installed as non-root
#Requires: python >= 2.3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Computational biology software by Colin Dewey, including mercator. 
parametricAlign is not included with this rpm.

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n cndsrc-%{version}

%build
# no Polymake installed so parametricAlign is not compiled.
make

%install
%{__rm} -rf %{buildroot}

make install prefix=%{_pre_install_dir}

%mfest_bin    bin/agpConsistent
%mfest_bin    bin/agpReformat
%mfest_bin    bin/agpReformat2
%mfest_bin    bin/agpValidate
%mfest_bin    bin/align2fa
%mfest_bin    bin/anchors2fa
%mfest_bin    bin/blat2hits
%mfest_bin    bin/breakMap
%mfest_bin    bin/breakpointMultipleAlignments
%mfest_bin    bin/clustal2fa
%mfest_bin    bin/clustalReformat
%mfest_bin    bin/downloadGenbank
%mfest_bin    bin/fa2align
%mfest_bin    bin/fa2clustal
%mfest_bin    bin/fa2line
%mfest_bin    bin/fa2phylip
%mfest_bin    bin/fa2sdb
%mfest_bin    bin/faAlign
%mfest_bin    bin/faAssemble
%mfest_bin    bin/faConcat
%mfest_bin    bin/faCount
%mfest_bin    bin/faFilter
%mfest_bin    bin/faFilterMasked
%mfest_bin    bin/faFrag
%mfest_bin    bin/faHardMask
%mfest_bin    bin/faHead
%mfest_bin    bin/faLen
%mfest_bin    bin/faList
%mfest_bin    bin/faMutate
%mfest_bin    bin/faOrfs
%mfest_bin    bin/faorfs2gff
%mfest_bin    bin/faRandomSubset
%mfest_bin    bin/faReformat
%mfest_bin    bin/faRepeatMask
%mfest_bin    bin/faReverseComplement
%mfest_bin    bin/faReverseTranscribe
%mfest_bin    bin/faShuffle
%mfest_bin    bin/faSoftMask
%mfest_bin    bin/faSort
%mfest_bin    bin/faSplitRecs
%mfest_bin    bin/faSubset
%mfest_bin    bin/faTranscribe
%mfest_bin    bin/faTranslate
%mfest_bin    bin/faUnambiguous
%mfest_bin    bin/faUnmask
%mfest_bin    bin/filterBadGFF
%mfest_bin    bin/findBadCDS
%mfest_bin    bin/findBreakpoints
%mfest_bin    bin/fixEnsembl
%mfest_bin    bin/genbank2fa
%mfest_bin    bin/genbank2fagff
%mfest_bin    bin/genscan2gtf
%mfest_bin    bin/getUCSC
%mfest_bin    bin/getUCSCgtf
%mfest_bin    bin/gff2anchors
%mfest_bin    bin/gff2zff
%mfest_bin    bin/gffFixFrames
%mfest_bin    bin/gffGeneIDs
%mfest_bin    bin/gffMap
%mfest_bin    bin/gffOverlaps
%mfest_bin    bin/gffReformat
%mfest_bin    bin/gffRemoveOverlaps
%mfest_bin    bin/gffSplit
%mfest_bin    bin/gffTransform
%mfest_bin    bin/gffUntransform
%mfest_bin    bin/gridPoints
%mfest_bin    bin/hmap2omap
%mfest_bin    bin/intervalTransform
%mfest_bin    bin/intervalUnion
%mfest_bin    bin/likelihoods2posteriors
%mfest_bin    bin/line2fa
%mfest_bin    bin/links2agp
%mfest_bin    bin/mafGenomes
%mfest_bin    bin/mafReformat
%mfest_bin    bin/mafSubset
%mfest_bin    bin/mafTransform
%mfest_bin    bin/makeAlignmentInput
%mfest_bin    bin/makeBreakpointAlignmentInput
%mfest_bin    bin/makeBreakpointGraph
%mfest_bin    bin/makeConstraintGFFs
%mfest_bin    bin/makeMavidConstraints
%mfest_bin    bin/makeMercatorInput
%mfest_bin    bin/map_draft
%mfest_bin    bin/maskRepetitive
%mfest_bin    bin/matchSegment
%mfest_bin    bin/mavidAlignDirs
%mfest_bin    bin/mercator
%mfest_bin    bin/mfaScore
%mfest_bin    bin/mfaSlice
%mfest_bin    bin/mummer2matches
%mfest_bin    bin/newickSubtree
%mfest_bin    bin/newickTaxa
%mfest_bin    bin/omap2coordinates
%mfest_bin    bin/omap2hmap
%mfest_bin    bin/omapTransform
%mfest_bin    bin/overlapJoin
%mfest_bin    bin/phits2constraints
%mfest_bin    bin/phylipReformat
%mfest_bin    bin/randomIntegers
%mfest_bin    bin/randomizeLines
%mfest_bin    bin/randomizeManyLines
%mfest_bin    bin/randomPermutation
%mfest_bin    bin/randomPoints
%mfest_bin    bin/randSeq
%mfest_bin    bin/randSeqs
%mfest_bin    bin/recombinationLikelihood
%mfest_bin    bin/recombinationLikelihoods
%mfest_bin    bin/recombinationPath
%mfest_bin    bin/recombinationPolytope
%mfest_bin    bin/recombinationStateSetList
%mfest_bin    bin/repeatmaskerReformat
%mfest_bin    bin/rotateTabDelim
%mfest_bin    bin/runAugustus
%mfest_bin    bin/runGeneid
%mfest_bin    bin/runGenscan
%mfest_bin    bin/runSnap
%mfest_bin    bin/sdb2fa
%mfest_bin    bin/sdbAssemble
%mfest_bin    bin/sdbDisassemble
%mfest_bin    bin/sdbExport
%mfest_bin    bin/sdbList
%mfest_bin    bin/sliceAlignment
%mfest_bin    bin/spacesToTabs
%mfest_bin    bin/stats
%mfest_bin    bin/ucsc2gtf
%mfest_bin    bin/vertexCones
%mfest_bin    bin/vertexNormals
%mfest_bin    bin/vertexPosteriors
%mfest_bin    bin/vertexStateSetLists
%mfest_bin    bin/zff2gtf

%post

%postun
%rm_pkg_base_dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_install_dir}
%dir %{_install_dir}/bin
%{_install_dir}/bin/AGP.py
%{_install_dir}/bin/AGP.pyc
%{_install_dir}/bin/AGP.pyo
%{_install_dir}/bin/BLAT.py
%{_install_dir}/bin/BLAT.pyc
%{_install_dir}/bin/BLAT.pyo
%{_install_dir}/bin/DB_MySQL.py
%{_install_dir}/bin/DB_MySQL.pyc
%{_install_dir}/bin/DB_MySQL.pyo
%{_install_dir}/bin/FASTA.py
%{_install_dir}/bin/FASTA.pyc
%{_install_dir}/bin/FASTA.pyo
%{_install_dir}/bin/GFF.py
%{_install_dir}/bin/GFF.pyc
%{_install_dir}/bin/GFF.pyo
%{_install_dir}/bin/GLADIS.py
%{_install_dir}/bin/GLADIS.pyc
%{_install_dir}/bin/GLADIS.pyo
%{_install_dir}/bin/Genome.py
%{_install_dir}/bin/Genome.pyc
%{_install_dir}/bin/Genome.pyo
%{_install_dir}/bin/SeqUtil.py
%{_install_dir}/bin/SeqUtil.pyc
%{_install_dir}/bin/SeqUtil.pyo
%{_install_dir}/bin/TabDelimited.py
%{_install_dir}/bin/TabDelimited.pyc
%{_install_dir}/bin/TabDelimited.pyo
%{_install_dir}/bin/ZFF.py
%{_install_dir}/bin/ZFF.pyc
%{_install_dir}/bin/ZFF.pyo
%{_install_dir}/bin/agpConsistent
%{_install_dir}/bin/agpReformat
%{_install_dir}/bin/agpReformat2
%{_install_dir}/bin/agpValidate
%{_install_dir}/bin/align2fa
%{_install_dir}/bin/anchors2fa
%{_install_dir}/bin/blat2hits
%{_install_dir}/bin/breakMap
%{_install_dir}/bin/breakpointMultipleAlignments
%{_install_dir}/bin/clustal2fa
%{_install_dir}/bin/clustalReformat
%{_install_dir}/bin/downloadGenbank
%{_install_dir}/bin/fa2align
%{_install_dir}/bin/fa2clustal
%{_install_dir}/bin/fa2line
%{_install_dir}/bin/fa2phylip
%{_install_dir}/bin/fa2sdb
%{_install_dir}/bin/faAlign
%{_install_dir}/bin/faAssemble
%{_install_dir}/bin/faConcat
%{_install_dir}/bin/faCount
%{_install_dir}/bin/faFilter
%{_install_dir}/bin/faFilterMasked
%{_install_dir}/bin/faFrag
%{_install_dir}/bin/faHardMask
%{_install_dir}/bin/faHead
%{_install_dir}/bin/faLen
%{_install_dir}/bin/faList
%{_install_dir}/bin/faMutate
%{_install_dir}/bin/faOrfs
%{_install_dir}/bin/faRandomSubset
%{_install_dir}/bin/faReformat
%{_install_dir}/bin/faRepeatMask
%{_install_dir}/bin/faReverseComplement
%{_install_dir}/bin/faReverseTranscribe
%{_install_dir}/bin/faShuffle
%{_install_dir}/bin/faSoftMask
%{_install_dir}/bin/faSort
%{_install_dir}/bin/faSplitRecs
%{_install_dir}/bin/faSubset
%{_install_dir}/bin/faTranscribe
%{_install_dir}/bin/faTranslate
%{_install_dir}/bin/faUnambiguous
%{_install_dir}/bin/faUnmask
%{_install_dir}/bin/faorfs2gff
%{_install_dir}/bin/filterBadGFF
%{_install_dir}/bin/findBadCDS
%{_install_dir}/bin/findBreakpoints
%{_install_dir}/bin/fixEnsembl
%{_install_dir}/bin/genbank2fa
%{_install_dir}/bin/genbank2fagff
%{_install_dir}/bin/genscan2gtf
%{_install_dir}/bin/getUCSC
%{_install_dir}/bin/getUCSCgtf
%{_install_dir}/bin/gff2anchors
%{_install_dir}/bin/gff2zff
%{_install_dir}/bin/gffFixFrames
%{_install_dir}/bin/gffGeneIDs
%{_install_dir}/bin/gffMap
%{_install_dir}/bin/gffOverlaps
%{_install_dir}/bin/gffReformat
%{_install_dir}/bin/gffRemoveOverlaps
%{_install_dir}/bin/gffSplit
%{_install_dir}/bin/gffTransform
%{_install_dir}/bin/gffUntransform
%{_install_dir}/bin/gridPoints
%{_install_dir}/bin/hmap2omap
%{_install_dir}/bin/html.py
%{_install_dir}/bin/html.pyc
%{_install_dir}/bin/html.pyo
%{_install_dir}/bin/interval.py
%{_install_dir}/bin/interval.pyc
%{_install_dir}/bin/interval.pyo
%{_install_dir}/bin/intervalTransform
%{_install_dir}/bin/intervalUnion
%{_install_dir}/bin/likelihoods2posteriors
%{_install_dir}/bin/line2fa
%{_install_dir}/bin/links2agp
%{_install_dir}/bin/mafGenomes
%{_install_dir}/bin/mafReformat
%{_install_dir}/bin/mafSubset
%{_install_dir}/bin/mafTransform
%{_install_dir}/bin/makeAlignmentInput
%{_install_dir}/bin/makeBreakpointAlignmentInput
%{_install_dir}/bin/makeBreakpointGraph
%{_install_dir}/bin/makeConstraintGFFs
%{_install_dir}/bin/makeMavidConstraints
%{_install_dir}/bin/makeMercatorInput
%{_install_dir}/bin/map_draft
%{_install_dir}/bin/maskRepetitive
%{_install_dir}/bin/matchSegment
%{_install_dir}/bin/mavidAlignDirs
%{_install_dir}/bin/mercator
%{_install_dir}/bin/mfaScore
%{_install_dir}/bin/mfaSlice
%{_install_dir}/bin/mummer2matches
%{_install_dir}/bin/newickSubtree
%{_install_dir}/bin/newickTaxa
%{_install_dir}/bin/omap2coordinates
%{_install_dir}/bin/omap2hmap
%{_install_dir}/bin/omapTransform
%{_install_dir}/bin/overlapJoin
%{_install_dir}/bin/phits2constraints
%{_install_dir}/bin/phylipReformat
%{_install_dir}/bin/randSeq
%{_install_dir}/bin/randSeqs
%{_install_dir}/bin/randomIntegers
%{_install_dir}/bin/randomPermutation
%{_install_dir}/bin/randomPoints
%{_install_dir}/bin/randomizeLines
%{_install_dir}/bin/randomizeManyLines
%{_install_dir}/bin/recombinationLikelihood
%{_install_dir}/bin/recombinationLikelihoods
%{_install_dir}/bin/recombinationPath
%{_install_dir}/bin/recombinationPolytope
%{_install_dir}/bin/recombinationStateSetList
%{_install_dir}/bin/repeatmaskerReformat
%{_install_dir}/bin/rotateTabDelim
%{_install_dir}/bin/runAugustus
%{_install_dir}/bin/runGeneid
%{_install_dir}/bin/runGenscan
%{_install_dir}/bin/runSnap
%{_install_dir}/bin/sdb2fa
%{_install_dir}/bin/sdbAssemble
%{_install_dir}/bin/sdbDisassemble
%{_install_dir}/bin/sdbExport
%{_install_dir}/bin/sdbList
%{_install_dir}/bin/sliceAlignment
%{_install_dir}/bin/spacesToTabs
%{_install_dir}/bin/stats
%{_install_dir}/bin/stats.py
%{_install_dir}/bin/stats.pyc
%{_install_dir}/bin/stats.pyo
%{_install_dir}/bin/ucsc2gtf
%{_install_dir}/bin/vertexCones
%{_install_dir}/bin/vertexNormals
%{_install_dir}/bin/vertexPosteriors
%{_install_dir}/bin/vertexStateSetLists
%{_install_dir}/bin/zff2gtf

%{_install_dir}/%{_manifest_file}



%changelog
* Sat Feb 11 2012 Mark Heiges <mheiges@uga.edu> 2010.04.23-2
- use MANIFEST.EUPATH
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
