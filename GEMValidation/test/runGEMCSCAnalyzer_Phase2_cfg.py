import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C10_cff import Phase2C10

process = cms.Process('ANA',Phase2C10)

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('GEMCode.GEMValidation.GEMCSCAnalyzer_cff')

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
    debugModules = cms.untracked.vstring("GEMCSCAnalyzer")
)
"""
process.source = cms.Source(
  "PoolSource",
  fileNames = cms.untracked.vstring('file:step2bis_phase2.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-100) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana_phase2.root")
)

## global tag for upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# the analyzer configuration
ana = process.GEMCSCAnalyzer
ana.simTrack.minEta = 0.9
ana.simTrack.maxEta = 2.4
ana.simTrack.minPt = 2
ana.gemStripDigi.matchDeltaStrip = 2

from GEMCode.GEMValidation.cscTriggerCustoms import addAnalysisRun3
process = addAnalysisRun3(process)

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.p = cms.Path(
    process.GEMCSCAnalyzer *
    process.GEMCSCAnalyzerRun3CCLUT)

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
