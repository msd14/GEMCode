import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Modifier_phase2_muon_cff import phase2_muon

# the analyzer configuration
from GEMCode.GEMValidation.simTrackMatching_cfi import simTrackPSet
GEMCSCAnalyzer = cms.EDAnalyzer(
    "GEMCSCAnalyzer",
    simTrackPSet,
    runSim = cms.bool(True),
    runDigi = cms.bool(True),
    runStub = cms.bool(True),
    runL1 = cms.bool(True),
    runReco = cms.bool(False),
    verbose = cms.untracked.int32(0),
    minNHitsChamberGEMSimHit = cms.int32(1),
    minNHitsChamberCSCSimHit = cms.int32(3),
    minNHitsChamberCSCDigi = cms.int32(4),
    minNHitsChamberGEMDigi = cms.int32(1),
    minNHitsChamberCSCStub = cms.int32(3),

    positionLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat0_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat1_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat2_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat3_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat4_v1.txt"
    ),

    positionFloatLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat0_float_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat1_float_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat2_float_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat3_float_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePosOffsetLUT_pat4_float_v1.txt"
    ),

    slopeLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodeSlopeLUT_pat0_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodeSlopeLUT_pat1_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodeSlopeLUT_pat2_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodeSlopeLUT_pat3_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodeSlopeLUT_pat4_v1.txt"
    ),

    patternConversionLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePatternConversionLUT_pat0_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePatternConversionLUT_pat1_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePatternConversionLUT_pat2_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePatternConversionLUT_pat3_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CSCComparatorCodePatternConversionLUT_pat4_v1.txt"
    ),
)

GEMCSCAnalyzer.simTrack.minEta = 0.9
GEMCSCAnalyzer.simTrack.maxEta = 2.4
GEMCSCAnalyzer.simTrack.minPt = 3
GEMCSCAnalyzer.gemSimHit.verbose = 0
GEMCSCAnalyzer.gemStripDigi.verbose = 0
GEMCSCAnalyzer.gemStripDigi.matchDeltaStrip = 2
GEMCSCAnalyzer.gemPadDigi.verbose = 0
GEMCSCAnalyzer.gemCoPadDigi.verbose = 0
GEMCSCAnalyzer.gemPadCluster.verbose = 0
GEMCSCAnalyzer.cscComparatorDigi.verbose = 0
GEMCSCAnalyzer.cscWireDigi.verbose = 0
GEMCSCAnalyzer.cscALCT.verbose = 0
GEMCSCAnalyzer.cscCLCT.verbose = 0
GEMCSCAnalyzer.cscLCT.verbose = 0
GEMCSCAnalyzer.cscLCT.addGhostLCTs = cms.bool(True)

phase2_muon.toModify(process.GEMCSCAnalyzer, l1Track = dict(run = cms.bool(True) ) )
phase2_muon.toModify(process.GEMCSCAnalyzer, l1TkMuon = dict(run = cms.bool(True) ) )
