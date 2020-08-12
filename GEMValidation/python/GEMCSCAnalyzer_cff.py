import FWCore.ParameterSet.Config as cms

# the analyzer configuration
from GEMCode.GEMValidation.simTrackMatching_cfi import simTrackPSet
process.GEMCSCAnalyzer = cms.EDAnalyzer(
    "GEMCSCAnalyzer",
    simTrackPSet,
    runSim = cms.bool(True),
    runDigi = cms.bool(True),
    runStub = cms.bool(True),
    runL1 = cms.bool(True),
    runReco = cms.bool(False),
    verbose = cms.untracked.int32(1),
    minNHitsChamberGEMSimHit = cms.int32(1),
    minNHitsChamberCSCSimHit = cms.int32(3),
    minNHitsChamberCSCDigi = cms.int32(4),
    minNHitsChamberGEMDigi = cms.int32(1),
    minNHitsChamberCSCStub = cms.int32(3),
)

ana = process.GEMCSCAnalyzer
ana.simTrack.minEta = 0.9
ana.simTrack.maxEta = 2.4
ana.simTrack.minPt = 3
ana.gemSimHit.verbose = 0
ana.gemStripDigi.verbose = 0
ana.gemStripDigi.matchDeltaStrip = 2
ana.gemPadDigi.verbose = 0
ana.gemCoPadDigi.verbose = 0
ana.gemPadCluster.verbose = 0
ana.cscComparatorDigi.verbose = 0
ana.cscWireDigi.verbose = 0
ana.cscALCT.verbose = 0
ana.cscCLCT.verbose = 0
ana.cscLCT.verbose = 0
ana.cscLCT.addGhostLCTs = cms.bool(True)
