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
