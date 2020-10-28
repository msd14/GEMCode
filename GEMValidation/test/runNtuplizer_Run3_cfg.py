import FWCore.ParameterSet.Config as cms
#from Configuration.Eras.Era_Phase2C10_cff import Phase2C10
from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('ANA',Run3)

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')  #Phase-II Geometry cff
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')       #Run-3 Geometry cff
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('GEMCode.GEMValidation.MuonNtuplizer_cff')

"""
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring("debug"),
    debug = cms.untracked.PSet(
 #       extension = cms.untracked.string(".txt"),
        threshold = cms.untracked.string("DEBUG"),
        # threshold = cms.untracked.string("WARNING"),
        lineLength = cms.untracked.int32(132),
        noLineBreaks = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring("MuonNtuplizer")
)
"""
process.source = cms.Source(
  "PoolSource",
  fileNames = cms.untracked.vstring('/store/user/mdecaro/SingleMu_Run3_Pt1to10OneOverPt_noPU_40M/CRAB3_SingleMu_Run3_Pt1to10OneOverPt_noPU_GEN_SIM_DIGI_L1_40M/201027_144728/0000/step2_1.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root")
)

## global tag for upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '') #Phase-II Global Tag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '') #Run-3 Global Tag


# the analyzer configuration
ana = process.MuonNtuplizer
ana.simTrack.minEta = 1.2
ana.simTrack.maxEta = 2.4
ana.simTrack.minPt = 2
ana.verbose = 1
ana.gemStripDigi.matchDeltaStrip = 2
ana.cscLCT.addGhostLCTs = cms.bool(True)

ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","L1")
ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","L1")
ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","L1")
ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","L1")

useUnpacked = False
if useUnpacked:
    ana.gemStripDigi.inputTag = "muonGEMDigis"
    ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

process.MuonNtuplizerRun3CCLUT = process.MuonNtuplizer.clone()
process.MuonNtuplizerRun3CCLUT.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","L1")
process.MuonNtuplizerRun3CCLUT.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","L1")
process.MuonNtuplizerRun3CCLUT.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","L1")
process.MuonNtuplizerRun3CCLUT.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","MPCSORTED","L1")

process.options = cms.untracked.PSet( 
   wantSummary = cms.untracked.bool(True)
   #numberOfThreads = cms.untracked.uint32(8) 
)

process.p = cms.Path(
    process.MuonNtuplizer #*
#    process.MuonNtuplizerRun3CCLUT
)

## messages
print
#print 'Input files:'
print '----------------------------------------'
print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.TFileService.fileName
print
