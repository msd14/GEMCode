#include "GEMCode/GEMValidation/interface/Analyzers/L1TrackAnalyzer.h"

L1TrackAnalyzer::L1TrackAnalyzer(const edm::ParameterSet& conf)
{
}

void L1TrackAnalyzer::setMatcher(const L1TrackMatcher& match_sh)
{
  match_.reset(new L1TrackMatcher(match_sh));
}

void L1TrackAnalyzer::analyze(TreeManager& tree)
{
  const auto& track = match_->l1Track();
  const auto& muon = match_->l1TrackMuon();

  if (track != nullptr) {
    tree.l1track().has_L1Track = true;
    tree.l1track().L1Track_pt = track->momentum().perp();
    tree.l1track().L1Track_eta = track->momentum().eta();
    tree.l1track().L1Track_phi = track->momentum().barePhi();
  }

  if (muon != nullptr) {
    tree.l1track().has_L1TrackMuon = true;
    tree.l1track().L1TrackMuon_pt = muon->pt();
    tree.l1track().L1TrackMuon_eta = muon->eta();
    tree.l1track().L1TrackMuon_phi = muon->phi();
  }

  /*
    L1TrackTriggerVeto trkVeto2(cfg_, match_sh.eventSetup(), match_sh.event(), trackInputLabel_,
    etrk_[0].L1Mu_eta, normalizedPhi((float)etrk_[0].L1Mu_phi));
    etrk_[0].isL1LooseVeto  = trkVeto2.isLooseVeto();
    etrk_[0].isL1MediumVeto = trkVeto2.isMediumVeto();
    etrk_[0].isL1TightVeto  = trkVeto2.isTightVeto();
  */
}
