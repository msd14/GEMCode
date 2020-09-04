import FWCore.ParameterSet.Config as cms

me0HitPSet = cms.PSet(
    me0StripDigi = cms.PSet(
        verbose = cms.int32(0),
        inputTag = cms.InputTag("simMuonME0Digis"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
        matchDeltaStrip = cms.int32(1),
        run = cms.bool(False)
    ),
    me0PadDigi = cms.PSet(
        verbose = cms.int32(0),
        inputTag = cms.InputTag("simMuonME0PadDigis"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
        matchDeltaStrip = cms.int32(1),
        run = cms.bool(False)
    ),
    me0RecHit = cms.PSet(
        verbose = cms.int32(0),
        inputTag = cms.InputTag('me0RecHits'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
        run = cms.bool(False)
    ),
    me0Seg = cms.PSet(
        verbose = cms.int32(0),
        inputTag = cms.InputTag('me0Segments'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
        run = cms.bool(False)
    )
)
