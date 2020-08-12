import FWCore.ParameterSet.Config as cms

def addCSCTriggerRun3(process):
    process.simEmtfDigis.CSCInput  = cms.InputTag('simCscTriggerPrimitiveDigis','MPCSORTED',"ReL1")

    ## Run-3 patterns
    process.simCscTriggerPrimitiveDigisRun3 = process.simCscTriggerPrimitiveDigis.clone()
    process.simCscTriggerPrimitiveDigisRun3.clctParam07.useRun3Patterns = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3.clctSLHC.useRun3Patterns = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3.clctSLHCME21.useRun3Patterns = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3.clctSLHCME3141.useRun3Patterns = cms.bool(True)

    ## Run-3 patterns with CCLUT
    process.simCscTriggerPrimitiveDigisRun3CCLUT = process.simCscTriggerPrimitiveDigisRun3.clone()
    process.simCscTriggerPrimitiveDigisRun3CCLUT.clctParam07.useComparatorCodes = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3CCLUT.clctSLHC.useComparatorCodes = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3CCLUT.clctSLHCME21.useComparatorCodes = cms.bool(True)
    process.simCscTriggerPrimitiveDigisRun3CCLUT.clctSLHCME3141.useComparatorCodes = cms.bool(True)
    return process

def addAnalysisRun3(process):

    ana = process.GEMCSCAnalyzer
    ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","ReL1")

    useUnpacked = False
    if useUnpacked:
        ana.gemStripDigi.inputTag = "muonGEMDigis"
        ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

    process.GEMCSCAnalyzerRun3 = process.GEMCSCAnalyzer.clone()
    anaRun3 = process.GEMCSCAnalyzerRun3
    anaRun3.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3","","ReL1")
    anaRun3.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3","","ReL1")
    anaRun3.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3","","ReL1")
    anaRun3.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3","MPCSORTED","ReL1")

    process.GEMCSCAnalyzerRun3CCLUT = process.GEMCSCAnalyzer.clone()
    anaCCLUT = process.GEMCSCAnalyzerRun3CCLUT
    anaCCLUT.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","MPCSORTED","ReL1")

    return process
