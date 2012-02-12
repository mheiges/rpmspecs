%define _pkg_base cndsrc

Summary: Colin Dewey computational biology software
Name: %{_pkg_base}-%{version}
Version: 2010.04.23
Release: 1%{?dist}
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
%define _install_dir  %{buildroot}/%{prefix}/%{_software_topdir}/%{_pkg_base}/%{version}
%define bundle_bin_dir  %{_install_dir}/__bin__

make install prefix=%{_install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
install -m 0755 -d %{bundle_bin_dir}
%define ln_path ../%{_software_topdir}/%{_pkg_base}/%{version}/bin
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


%dir %{_install_dir}/__bin__
%{_install_dir}/__bin__/ReadMe
%{_install_dir}/__bin__/agpConsistent
%{_install_dir}/__bin__/agpReformat
%{_install_dir}/__bin__/agpReformat2
%{_install_dir}/__bin__/agpValidate
%{_install_dir}/__bin__/align2fa
%{_install_dir}/__bin__/anchors2fa
%{_install_dir}/__bin__/blat2hits
%{_install_dir}/__bin__/breakMap
%{_install_dir}/__bin__/breakpointMultipleAlignments
%{_install_dir}/__bin__/clustal2fa
%{_install_dir}/__bin__/clustalReformat
%{_install_dir}/__bin__/downloadGenbank
%{_install_dir}/__bin__/fa2align
%{_install_dir}/__bin__/fa2clustal
%{_install_dir}/__bin__/fa2line
%{_install_dir}/__bin__/fa2phylip
%{_install_dir}/__bin__/fa2sdb
%{_install_dir}/__bin__/faAlign
%{_install_dir}/__bin__/faAssemble
%{_install_dir}/__bin__/faConcat
%{_install_dir}/__bin__/faCount
%{_install_dir}/__bin__/faFilter
%{_install_dir}/__bin__/faFilterMasked
%{_install_dir}/__bin__/faFrag
%{_install_dir}/__bin__/faHardMask
%{_install_dir}/__bin__/faHead
%{_install_dir}/__bin__/faLen
%{_install_dir}/__bin__/faList
%{_install_dir}/__bin__/faMutate
%{_install_dir}/__bin__/faOrfs
%{_install_dir}/__bin__/faRandomSubset
%{_install_dir}/__bin__/faReformat
%{_install_dir}/__bin__/faRepeatMask
%{_install_dir}/__bin__/faReverseComplement
%{_install_dir}/__bin__/faReverseTranscribe
%{_install_dir}/__bin__/faShuffle
%{_install_dir}/__bin__/faSoftMask
%{_install_dir}/__bin__/faSort
%{_install_dir}/__bin__/faSplitRecs
%{_install_dir}/__bin__/faSubset
%{_install_dir}/__bin__/faTranscribe
%{_install_dir}/__bin__/faTranslate
%{_install_dir}/__bin__/faUnambiguous
%{_install_dir}/__bin__/faUnmask
%{_install_dir}/__bin__/faorfs2gff
%{_install_dir}/__bin__/filterBadGFF
%{_install_dir}/__bin__/findBadCDS
%{_install_dir}/__bin__/findBreakpoints
%{_install_dir}/__bin__/fixEnsembl
%{_install_dir}/__bin__/genbank2fa
%{_install_dir}/__bin__/genbank2fagff
%{_install_dir}/__bin__/genscan2gtf
%{_install_dir}/__bin__/getUCSC
%{_install_dir}/__bin__/getUCSCgtf
%{_install_dir}/__bin__/gff2anchors
%{_install_dir}/__bin__/gff2zff
%{_install_dir}/__bin__/gffFixFrames
%{_install_dir}/__bin__/gffGeneIDs
%{_install_dir}/__bin__/gffMap
%{_install_dir}/__bin__/gffOverlaps
%{_install_dir}/__bin__/gffReformat
%{_install_dir}/__bin__/gffRemoveOverlaps
%{_install_dir}/__bin__/gffSplit
%{_install_dir}/__bin__/gffTransform
%{_install_dir}/__bin__/gffUntransform
%{_install_dir}/__bin__/gridPoints
%{_install_dir}/__bin__/hmap2omap
%{_install_dir}/__bin__/intervalTransform
%{_install_dir}/__bin__/intervalUnion
%{_install_dir}/__bin__/likelihoods2posteriors
%{_install_dir}/__bin__/line2fa
%{_install_dir}/__bin__/links2agp
%{_install_dir}/__bin__/mafGenomes
%{_install_dir}/__bin__/mafReformat
%{_install_dir}/__bin__/mafSubset
%{_install_dir}/__bin__/mafTransform
%{_install_dir}/__bin__/makeAlignmentInput
%{_install_dir}/__bin__/makeBreakpointAlignmentInput
%{_install_dir}/__bin__/makeBreakpointGraph
%{_install_dir}/__bin__/makeConstraintGFFs
%{_install_dir}/__bin__/makeMavidConstraints
%{_install_dir}/__bin__/makeMercatorInput
%{_install_dir}/__bin__/map_draft
%{_install_dir}/__bin__/maskRepetitive
%{_install_dir}/__bin__/matchSegment
%{_install_dir}/__bin__/mavidAlignDirs
%{_install_dir}/__bin__/mercator
%{_install_dir}/__bin__/mfaScore
%{_install_dir}/__bin__/mfaSlice
%{_install_dir}/__bin__/mummer2matches
%{_install_dir}/__bin__/newickSubtree
%{_install_dir}/__bin__/newickTaxa
%{_install_dir}/__bin__/omap2coordinates
%{_install_dir}/__bin__/omap2hmap
%{_install_dir}/__bin__/omapTransform
%{_install_dir}/__bin__/overlapJoin
%{_install_dir}/__bin__/phits2constraints
%{_install_dir}/__bin__/phylipReformat
%{_install_dir}/__bin__/randSeq
%{_install_dir}/__bin__/randSeqs
%{_install_dir}/__bin__/randomIntegers
%{_install_dir}/__bin__/randomPermutation
%{_install_dir}/__bin__/randomPoints
%{_install_dir}/__bin__/randomizeLines
%{_install_dir}/__bin__/randomizeManyLines
%{_install_dir}/__bin__/recombinationLikelihood
%{_install_dir}/__bin__/recombinationLikelihoods
%{_install_dir}/__bin__/recombinationPath
%{_install_dir}/__bin__/recombinationPolytope
%{_install_dir}/__bin__/recombinationStateSetList
%{_install_dir}/__bin__/repeatmaskerReformat
%{_install_dir}/__bin__/rotateTabDelim
%{_install_dir}/__bin__/runAugustus
%{_install_dir}/__bin__/runGeneid
%{_install_dir}/__bin__/runGenscan
%{_install_dir}/__bin__/runSnap
%{_install_dir}/__bin__/sdb2fa
%{_install_dir}/__bin__/sdbAssemble
%{_install_dir}/__bin__/sdbDisassemble
%{_install_dir}/__bin__/sdbExport
%{_install_dir}/__bin__/sdbList
%{_install_dir}/__bin__/sliceAlignment
%{_install_dir}/__bin__/spacesToTabs
%{_install_dir}/__bin__/stats
%{_install_dir}/__bin__/ucsc2gtf
%{_install_dir}/__bin__/vertexCones
%{_install_dir}/__bin__/vertexNormals
%{_install_dir}/__bin__/vertexPosteriors
%{_install_dir}/__bin__/vertexStateSetLists
%{_install_dir}/__bin__/zff2gtf


%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.
