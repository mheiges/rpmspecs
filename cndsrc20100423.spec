%define pkg_base cndsrc

Summary: Colin Dewey computational biology software
Name: cndsrc20100423
Version: 2010.04.23
Release: 1%{?dist}
License: GPLv3
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://www.biostat.wisc.edu/~cdewey/software/cndsrc-%{version}.tar.gz

# we can't specify this requirement because it's registered in the 
# system rpm database and this rpm may be installed as non-root
#Requires: python >= 2.3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Computational biology software by Colin Dewey, including mercator. 
parametricAlign is not included with this rpm.

%prep
%setup -q -n cndsrc-%{version}

%build
# no Polymake installed so parametricAlign is not compiled.
make

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

make install prefix=%{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
install -m 0755 -d %{bundle_bin_dir}
%define ln_path ../software/%{pkg_base}/%{version}/bin
cd %{bundle_bin_dir}
ln -s %{ln_path}/agpConsistent
ln -s %{ln_path}/agpReformat
ln -s %{ln_path}/agpReformat2
ln -s %{ln_path}/agpValidate
ln -s %{ln_path}/align2fa
ln -s %{ln_path}/anchors2fa
ln -s %{ln_path}/blat2hits
ln -s %{ln_path}/breakMap
ln -s %{ln_path}/breakpointMultipleAlignments
ln -s %{ln_path}/clustal2fa
ln -s %{ln_path}/clustalReformat
ln -s %{ln_path}/downloadGenbank
ln -s %{ln_path}/fa2align
ln -s %{ln_path}/fa2clustal
ln -s %{ln_path}/fa2line
ln -s %{ln_path}/fa2phylip
ln -s %{ln_path}/fa2sdb
ln -s %{ln_path}/faAlign
ln -s %{ln_path}/faAssemble
ln -s %{ln_path}/faConcat
ln -s %{ln_path}/faCount
ln -s %{ln_path}/faFilter
ln -s %{ln_path}/faFilterMasked
ln -s %{ln_path}/faFrag
ln -s %{ln_path}/faHardMask
ln -s %{ln_path}/faHead
ln -s %{ln_path}/faLen
ln -s %{ln_path}/faList
ln -s %{ln_path}/faMutate
ln -s %{ln_path}/faOrfs
ln -s %{ln_path}/faorfs2gff
ln -s %{ln_path}/faRandomSubset
ln -s %{ln_path}/faReformat
ln -s %{ln_path}/faRepeatMask
ln -s %{ln_path}/faReverseComplement
ln -s %{ln_path}/faReverseTranscribe
ln -s %{ln_path}/faShuffle
ln -s %{ln_path}/faSoftMask
ln -s %{ln_path}/faSort
ln -s %{ln_path}/faSplitRecs
ln -s %{ln_path}/faSubset
ln -s %{ln_path}/faTranscribe
ln -s %{ln_path}/faTranslate
ln -s %{ln_path}/faUnambiguous
ln -s %{ln_path}/faUnmask
ln -s %{ln_path}/filterBadGFF
ln -s %{ln_path}/findBadCDS
ln -s %{ln_path}/findBreakpoints
ln -s %{ln_path}/fixEnsembl
ln -s %{ln_path}/genbank2fa
ln -s %{ln_path}/genbank2fagff
ln -s %{ln_path}/genscan2gtf
ln -s %{ln_path}/getUCSC
ln -s %{ln_path}/getUCSCgtf
ln -s %{ln_path}/gff2anchors
ln -s %{ln_path}/gff2zff
ln -s %{ln_path}/gffFixFrames
ln -s %{ln_path}/gffGeneIDs
ln -s %{ln_path}/gffMap
ln -s %{ln_path}/gffOverlaps
ln -s %{ln_path}/gffReformat
ln -s %{ln_path}/gffRemoveOverlaps
ln -s %{ln_path}/gffSplit
ln -s %{ln_path}/gffTransform
ln -s %{ln_path}/gffUntransform
ln -s %{ln_path}/gridPoints
ln -s %{ln_path}/hmap2omap
ln -s %{ln_path}/intervalTransform
ln -s %{ln_path}/intervalUnion
ln -s %{ln_path}/likelihoods2posteriors
ln -s %{ln_path}/line2fa
ln -s %{ln_path}/links2agp
ln -s %{ln_path}/mafGenomes
ln -s %{ln_path}/mafReformat
ln -s %{ln_path}/mafSubset
ln -s %{ln_path}/mafTransform
ln -s %{ln_path}/makeAlignmentInput
ln -s %{ln_path}/makeBreakpointAlignmentInput
ln -s %{ln_path}/makeBreakpointGraph
ln -s %{ln_path}/makeConstraintGFFs
ln -s %{ln_path}/makeMavidConstraints
ln -s %{ln_path}/makeMercatorInput
ln -s %{ln_path}/map_draft
ln -s %{ln_path}/maskRepetitive
ln -s %{ln_path}/matchSegment
ln -s %{ln_path}/mavidAlignDirs
ln -s %{ln_path}/mercator
ln -s %{ln_path}/mfaScore
ln -s %{ln_path}/mfaSlice
ln -s %{ln_path}/mummer2matches
ln -s %{ln_path}/newickSubtree
ln -s %{ln_path}/newickTaxa
ln -s %{ln_path}/omap2coordinates
ln -s %{ln_path}/omap2hmap
ln -s %{ln_path}/omapTransform
ln -s %{ln_path}/overlapJoin
ln -s %{ln_path}/phits2constraints
ln -s %{ln_path}/phylipReformat
ln -s %{ln_path}/randomIntegers
ln -s %{ln_path}/randomizeLines
ln -s %{ln_path}/randomizeManyLines
ln -s %{ln_path}/randomPermutation
ln -s %{ln_path}/randomPoints
ln -s %{ln_path}/randSeq
ln -s %{ln_path}/randSeqs
ln -s %{ln_path}/recombinationLikelihood
ln -s %{ln_path}/recombinationLikelihoods
ln -s %{ln_path}/recombinationPath
ln -s %{ln_path}/recombinationPolytope
ln -s %{ln_path}/recombinationStateSetList
ln -s %{ln_path}/repeatmaskerReformat
ln -s %{ln_path}/rotateTabDelim
ln -s %{ln_path}/runAugustus
ln -s %{ln_path}/runGeneid
ln -s %{ln_path}/runGenscan
ln -s %{ln_path}/runSnap
ln -s %{ln_path}/sdb2fa
ln -s %{ln_path}/sdbAssemble
ln -s %{ln_path}/sdbDisassemble
ln -s %{ln_path}/sdbExport
ln -s %{ln_path}/sdbList
ln -s %{ln_path}/sliceAlignment
ln -s %{ln_path}/spacesToTabs
ln -s %{ln_path}/stats
ln -s %{ln_path}/ucsc2gtf
ln -s %{ln_path}/vertexCones
ln -s %{ln_path}/vertexNormals
ln -s %{ln_path}/vertexPosteriors
ln -s %{ln_path}/vertexStateSetLists
ln -s %{ln_path}/zff2gtf


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
%dir %{install_dir}/bin
%{install_dir}/bin/AGP.py
%{install_dir}/bin/AGP.pyc
%{install_dir}/bin/AGP.pyo
%{install_dir}/bin/BLAT.py
%{install_dir}/bin/BLAT.pyc
%{install_dir}/bin/BLAT.pyo
%{install_dir}/bin/DB_MySQL.py
%{install_dir}/bin/DB_MySQL.pyc
%{install_dir}/bin/DB_MySQL.pyo
%{install_dir}/bin/FASTA.py
%{install_dir}/bin/FASTA.pyc
%{install_dir}/bin/FASTA.pyo
%{install_dir}/bin/GFF.py
%{install_dir}/bin/GFF.pyc
%{install_dir}/bin/GFF.pyo
%{install_dir}/bin/GLADIS.py
%{install_dir}/bin/GLADIS.pyc
%{install_dir}/bin/GLADIS.pyo
%{install_dir}/bin/Genome.py
%{install_dir}/bin/Genome.pyc
%{install_dir}/bin/Genome.pyo
%{install_dir}/bin/SeqUtil.py
%{install_dir}/bin/SeqUtil.pyc
%{install_dir}/bin/SeqUtil.pyo
%{install_dir}/bin/TabDelimited.py
%{install_dir}/bin/TabDelimited.pyc
%{install_dir}/bin/TabDelimited.pyo
%{install_dir}/bin/ZFF.py
%{install_dir}/bin/ZFF.pyc
%{install_dir}/bin/ZFF.pyo
%{install_dir}/bin/agpConsistent
%{install_dir}/bin/agpReformat
%{install_dir}/bin/agpReformat2
%{install_dir}/bin/agpValidate
%{install_dir}/bin/align2fa
%{install_dir}/bin/anchors2fa
%{install_dir}/bin/blat2hits
%{install_dir}/bin/breakMap
%{install_dir}/bin/breakpointMultipleAlignments
%{install_dir}/bin/clustal2fa
%{install_dir}/bin/clustalReformat
%{install_dir}/bin/downloadGenbank
%{install_dir}/bin/fa2align
%{install_dir}/bin/fa2clustal
%{install_dir}/bin/fa2line
%{install_dir}/bin/fa2phylip
%{install_dir}/bin/fa2sdb
%{install_dir}/bin/faAlign
%{install_dir}/bin/faAssemble
%{install_dir}/bin/faConcat
%{install_dir}/bin/faCount
%{install_dir}/bin/faFilter
%{install_dir}/bin/faFilterMasked
%{install_dir}/bin/faFrag
%{install_dir}/bin/faHardMask
%{install_dir}/bin/faHead
%{install_dir}/bin/faLen
%{install_dir}/bin/faList
%{install_dir}/bin/faMutate
%{install_dir}/bin/faOrfs
%{install_dir}/bin/faRandomSubset
%{install_dir}/bin/faReformat
%{install_dir}/bin/faRepeatMask
%{install_dir}/bin/faReverseComplement
%{install_dir}/bin/faReverseTranscribe
%{install_dir}/bin/faShuffle
%{install_dir}/bin/faSoftMask
%{install_dir}/bin/faSort
%{install_dir}/bin/faSplitRecs
%{install_dir}/bin/faSubset
%{install_dir}/bin/faTranscribe
%{install_dir}/bin/faTranslate
%{install_dir}/bin/faUnambiguous
%{install_dir}/bin/faUnmask
%{install_dir}/bin/faorfs2gff
%{install_dir}/bin/filterBadGFF
%{install_dir}/bin/findBadCDS
%{install_dir}/bin/findBreakpoints
%{install_dir}/bin/fixEnsembl
%{install_dir}/bin/genbank2fa
%{install_dir}/bin/genbank2fagff
%{install_dir}/bin/genscan2gtf
%{install_dir}/bin/getUCSC
%{install_dir}/bin/getUCSCgtf
%{install_dir}/bin/gff2anchors
%{install_dir}/bin/gff2zff
%{install_dir}/bin/gffFixFrames
%{install_dir}/bin/gffGeneIDs
%{install_dir}/bin/gffMap
%{install_dir}/bin/gffOverlaps
%{install_dir}/bin/gffReformat
%{install_dir}/bin/gffRemoveOverlaps
%{install_dir}/bin/gffSplit
%{install_dir}/bin/gffTransform
%{install_dir}/bin/gffUntransform
%{install_dir}/bin/gridPoints
%{install_dir}/bin/hmap2omap
%{install_dir}/bin/html.py
%{install_dir}/bin/html.pyc
%{install_dir}/bin/html.pyo
%{install_dir}/bin/interval.py
%{install_dir}/bin/interval.pyc
%{install_dir}/bin/interval.pyo
%{install_dir}/bin/intervalTransform
%{install_dir}/bin/intervalUnion
%{install_dir}/bin/likelihoods2posteriors
%{install_dir}/bin/line2fa
%{install_dir}/bin/links2agp
%{install_dir}/bin/mafGenomes
%{install_dir}/bin/mafReformat
%{install_dir}/bin/mafSubset
%{install_dir}/bin/mafTransform
%{install_dir}/bin/makeAlignmentInput
%{install_dir}/bin/makeBreakpointAlignmentInput
%{install_dir}/bin/makeBreakpointGraph
%{install_dir}/bin/makeConstraintGFFs
%{install_dir}/bin/makeMavidConstraints
%{install_dir}/bin/makeMercatorInput
%{install_dir}/bin/map_draft
%{install_dir}/bin/maskRepetitive
%{install_dir}/bin/matchSegment
%{install_dir}/bin/mavidAlignDirs
%{install_dir}/bin/mercator
%{install_dir}/bin/mfaScore
%{install_dir}/bin/mfaSlice
%{install_dir}/bin/mummer2matches
%{install_dir}/bin/newickSubtree
%{install_dir}/bin/newickTaxa
%{install_dir}/bin/omap2coordinates
%{install_dir}/bin/omap2hmap
%{install_dir}/bin/omapTransform
%{install_dir}/bin/overlapJoin
%{install_dir}/bin/phits2constraints
%{install_dir}/bin/phylipReformat
%{install_dir}/bin/randSeq
%{install_dir}/bin/randSeqs
%{install_dir}/bin/randomIntegers
%{install_dir}/bin/randomPermutation
%{install_dir}/bin/randomPoints
%{install_dir}/bin/randomizeLines
%{install_dir}/bin/randomizeManyLines
%{install_dir}/bin/recombinationLikelihood
%{install_dir}/bin/recombinationLikelihoods
%{install_dir}/bin/recombinationPath
%{install_dir}/bin/recombinationPolytope
%{install_dir}/bin/recombinationStateSetList
%{install_dir}/bin/repeatmaskerReformat
%{install_dir}/bin/rotateTabDelim
%{install_dir}/bin/runAugustus
%{install_dir}/bin/runGeneid
%{install_dir}/bin/runGenscan
%{install_dir}/bin/runSnap
%{install_dir}/bin/sdb2fa
%{install_dir}/bin/sdbAssemble
%{install_dir}/bin/sdbDisassemble
%{install_dir}/bin/sdbExport
%{install_dir}/bin/sdbList
%{install_dir}/bin/sliceAlignment
%{install_dir}/bin/spacesToTabs
%{install_dir}/bin/stats
%{install_dir}/bin/stats.py
%{install_dir}/bin/stats.pyc
%{install_dir}/bin/stats.pyo
%{install_dir}/bin/ucsc2gtf
%{install_dir}/bin/vertexCones
%{install_dir}/bin/vertexNormals
%{install_dir}/bin/vertexPosteriors
%{install_dir}/bin/vertexStateSetLists
%{install_dir}/bin/zff2gtf


%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/agpConsistent
%{install_dir}/__bin__/agpReformat
%{install_dir}/__bin__/agpReformat2
%{install_dir}/__bin__/agpValidate
%{install_dir}/__bin__/align2fa
%{install_dir}/__bin__/anchors2fa
%{install_dir}/__bin__/blat2hits
%{install_dir}/__bin__/breakMap
%{install_dir}/__bin__/breakpointMultipleAlignments
%{install_dir}/__bin__/clustal2fa
%{install_dir}/__bin__/clustalReformat
%{install_dir}/__bin__/downloadGenbank
%{install_dir}/__bin__/fa2align
%{install_dir}/__bin__/fa2clustal
%{install_dir}/__bin__/fa2line
%{install_dir}/__bin__/fa2phylip
%{install_dir}/__bin__/fa2sdb
%{install_dir}/__bin__/faAlign
%{install_dir}/__bin__/faAssemble
%{install_dir}/__bin__/faConcat
%{install_dir}/__bin__/faCount
%{install_dir}/__bin__/faFilter
%{install_dir}/__bin__/faFilterMasked
%{install_dir}/__bin__/faFrag
%{install_dir}/__bin__/faHardMask
%{install_dir}/__bin__/faHead
%{install_dir}/__bin__/faLen
%{install_dir}/__bin__/faList
%{install_dir}/__bin__/faMutate
%{install_dir}/__bin__/faOrfs
%{install_dir}/__bin__/faRandomSubset
%{install_dir}/__bin__/faReformat
%{install_dir}/__bin__/faRepeatMask
%{install_dir}/__bin__/faReverseComplement
%{install_dir}/__bin__/faReverseTranscribe
%{install_dir}/__bin__/faShuffle
%{install_dir}/__bin__/faSoftMask
%{install_dir}/__bin__/faSort
%{install_dir}/__bin__/faSplitRecs
%{install_dir}/__bin__/faSubset
%{install_dir}/__bin__/faTranscribe
%{install_dir}/__bin__/faTranslate
%{install_dir}/__bin__/faUnambiguous
%{install_dir}/__bin__/faUnmask
%{install_dir}/__bin__/faorfs2gff
%{install_dir}/__bin__/filterBadGFF
%{install_dir}/__bin__/findBadCDS
%{install_dir}/__bin__/findBreakpoints
%{install_dir}/__bin__/fixEnsembl
%{install_dir}/__bin__/genbank2fa
%{install_dir}/__bin__/genbank2fagff
%{install_dir}/__bin__/genscan2gtf
%{install_dir}/__bin__/getUCSC
%{install_dir}/__bin__/getUCSCgtf
%{install_dir}/__bin__/gff2anchors
%{install_dir}/__bin__/gff2zff
%{install_dir}/__bin__/gffFixFrames
%{install_dir}/__bin__/gffGeneIDs
%{install_dir}/__bin__/gffMap
%{install_dir}/__bin__/gffOverlaps
%{install_dir}/__bin__/gffReformat
%{install_dir}/__bin__/gffRemoveOverlaps
%{install_dir}/__bin__/gffSplit
%{install_dir}/__bin__/gffTransform
%{install_dir}/__bin__/gffUntransform
%{install_dir}/__bin__/gridPoints
%{install_dir}/__bin__/hmap2omap
%{install_dir}/__bin__/intervalTransform
%{install_dir}/__bin__/intervalUnion
%{install_dir}/__bin__/likelihoods2posteriors
%{install_dir}/__bin__/line2fa
%{install_dir}/__bin__/links2agp
%{install_dir}/__bin__/mafGenomes
%{install_dir}/__bin__/mafReformat
%{install_dir}/__bin__/mafSubset
%{install_dir}/__bin__/mafTransform
%{install_dir}/__bin__/makeAlignmentInput
%{install_dir}/__bin__/makeBreakpointAlignmentInput
%{install_dir}/__bin__/makeBreakpointGraph
%{install_dir}/__bin__/makeConstraintGFFs
%{install_dir}/__bin__/makeMavidConstraints
%{install_dir}/__bin__/makeMercatorInput
%{install_dir}/__bin__/map_draft
%{install_dir}/__bin__/maskRepetitive
%{install_dir}/__bin__/matchSegment
%{install_dir}/__bin__/mavidAlignDirs
%{install_dir}/__bin__/mercator
%{install_dir}/__bin__/mfaScore
%{install_dir}/__bin__/mfaSlice
%{install_dir}/__bin__/mummer2matches
%{install_dir}/__bin__/newickSubtree
%{install_dir}/__bin__/newickTaxa
%{install_dir}/__bin__/omap2coordinates
%{install_dir}/__bin__/omap2hmap
%{install_dir}/__bin__/omapTransform
%{install_dir}/__bin__/overlapJoin
%{install_dir}/__bin__/phits2constraints
%{install_dir}/__bin__/phylipReformat
%{install_dir}/__bin__/randSeq
%{install_dir}/__bin__/randSeqs
%{install_dir}/__bin__/randomIntegers
%{install_dir}/__bin__/randomPermutation
%{install_dir}/__bin__/randomPoints
%{install_dir}/__bin__/randomizeLines
%{install_dir}/__bin__/randomizeManyLines
%{install_dir}/__bin__/recombinationLikelihood
%{install_dir}/__bin__/recombinationLikelihoods
%{install_dir}/__bin__/recombinationPath
%{install_dir}/__bin__/recombinationPolytope
%{install_dir}/__bin__/recombinationStateSetList
%{install_dir}/__bin__/repeatmaskerReformat
%{install_dir}/__bin__/rotateTabDelim
%{install_dir}/__bin__/runAugustus
%{install_dir}/__bin__/runGeneid
%{install_dir}/__bin__/runGenscan
%{install_dir}/__bin__/runSnap
%{install_dir}/__bin__/sdb2fa
%{install_dir}/__bin__/sdbAssemble
%{install_dir}/__bin__/sdbDisassemble
%{install_dir}/__bin__/sdbExport
%{install_dir}/__bin__/sdbList
%{install_dir}/__bin__/sliceAlignment
%{install_dir}/__bin__/spacesToTabs
%{install_dir}/__bin__/stats
%{install_dir}/__bin__/ucsc2gtf
%{install_dir}/__bin__/vertexCones
%{install_dir}/__bin__/vertexNormals
%{install_dir}/__bin__/vertexPosteriors
%{install_dir}/__bin__/vertexStateSetLists
%{install_dir}/__bin__/zff2gtf


%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
