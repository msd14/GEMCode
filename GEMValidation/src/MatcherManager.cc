#include "GEMCode/GEMValidation/interface/MatcherManager.h"

MatcherManager::MatcherManager(const edm::ParameterSet& iPS, edm::ConsumesCollector&& iC) {
  genParticles_.reset(new GenParticleMatcher(iPS, std::move(iC)));
  l1Muons_.reset(new L1MuMatcher(iPS, std::move(iC)));
  l1Tracks_.reset(new L1TrackMatcher(iPS, std::move(iC)));
  me0_rechits_.reset(new ME0RecHitMatcher(iPS, std::move(iC)));
  // gem_rechits_.reset(new GEMRecHitMatcher(iPS, std::move(iC)));
}

void MatcherManager::init(const edm::Event& e, const edm::EventSetup& eventSetup) {
  genParticles_->init(e, eventSetup);
  l1Muons_->init(e, eventSetup);
  l1Tracks_->init(e, eventSetup);
  me0_rechits_->init(e, eventSetup);
  // gem_rechits_->init(e, eventSetup);
}

/// do the matching
void MatcherManager::match(const SimTrack& t, const SimVertex& v) {
  genParticles_->match(t, v);
  l1Muons_->match(t, v);
  l1Tracks_->match(t, v);
  me0_rechits_->match(t, v);
  // gem_rechits_->match(t, v);
}
