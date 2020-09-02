#include "GEMCode/GEMValidation/interface/Matchers/L1TkMuMatcher.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/normalizedPhi.h"

L1TkMuMatcher::L1TkMuMatcher(const edm::ParameterSet& ps, edm::ConsumesCollector&& iC)
{
  l1MuMatcher_.reset(new L1MuMatcher(ps, std::move(iC)));
  l1TrackMatcher_.reset(new L1TrackMatcher(ps, std::move(iC)));

  const auto& l1TkMuon = ps.getParameter<edm::ParameterSet>("l1TkMuon");
  minBXTkMuon_ = l1TkMuon.getParameter<int>("minBX");
  maxBXTkMuon_ = l1TkMuon.getParameter<int>("maxBX");
  verboseTkMuon_ = l1TkMuon.getParameter<int>("verbose");
  deltaRTkMuon_ = l1TkMuon.getParameter<double>("deltaR");
  runTkMuon_ = l1TkMuon.getParameter<bool>("run");

  l1TkMuonToken_ = iC.consumes<l1t::TkMuonCollection>(l1TkMuon.getParameter<edm::InputTag>("inputTag"));
}

void L1TkMuMatcher::init(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  l1MuMatcher_->init(iEvent, iSetup);
  l1TrackMatcher_->init(iEvent, iSetup);

  iEvent.getByToken(l1TkMuonToken_, l1TkMuonHandle_);
}

void
L1TkMuMatcher::clear()
{
  l1TkMuon_ = nullptr;
}


// do the matching
void L1TkMuMatcher::match(const SimTrack& t, const SimVertex& v)
{
  clear();

  l1MuMatcher_->match(t, v);
  l1TrackMatcher_->match(t, v);

  if (runTkMuon_)
    matchL1TkMuonToSimTrack(t, *l1TkMuonHandle_.product());
}

void
L1TkMuMatcher::matchL1TkMuonToSimTrack(const SimTrack& simtrack, const l1t::TkMuonCollection& tracks)
{
  // if (deltaRTkMuon_ < 0) {
  //   for (const auto& trk : tracks) {
  //     int bx = trk.BX();
  //     if ( bx < minBXTkMuon_ or bx > maxBXTkMuon_) continue;
  //     int nMatchingStubs = 0;
  //     int nMaxMatchingStubs = 0;
  //     if (verboseTkMuon_)
  //       std::cout <<"track BX "<< trk.BX()
  //                 <<  " pt "<< trk.Pt()
  //                 <<" eta "<< trk.Eta()
  //                 <<" phi "<< emtf::deg_to_rad(trk.Phi_glob())
  //                 <<" phi_local "<< emtf::deg_to_rad(trk.Phi_loc()) << std::endl;
  //     for (const auto& stub : trk.Hits()){
  //       const CSCCorrelatedLCTDigi& csc_stub = stub.CreateCSCCorrelatedLCTDigi();
  //       const CSCDetId& csc_id = stub.CSC_DetId();
  //       if (verboseTkMuon_)
  //         std::cout << "\tCSCDetId " << csc_id << " CSC stub "
  //                   << csc_stub << " available stubs in this chamber: "
  //                   << cscStubMatcher_->lctsInChamber(csc_id.rawId()).size() << std::endl;

  //       for (const auto& sim_stub: cscStubMatcher_->lctsInChamber(csc_id.rawId())){
  //         if (verboseTkMuon_)
  //           std::cout << "\tSIM " << csc_id << " " << sim_stub << std::endl;
  //         if (csc_stub == sim_stub) {
  //           nMatchingStubs++;
  //         }
  //       }
  //       if (nMatchingStubs>=2) {
  //         if (nMatchingStubs > nMaxMatchingStubs){
  //           l1TkMuon_.reset(new gem::TkMuon(trk));
  //           nMaxMatchingStubs = nMatchingStubs;
  //         }
  //       }
  //     }
  //   }
  // }
  // else {
  //   float mindRTkMuon = 10.0;
  //   for (const auto& trk : tracks) {
  //     if (verboseTkMuon_)
  //       std::cout <<"track BX "<< trk.BX()
  //                 <<  " pt "<< trk.Pt()
  //                 <<" eta "<< trk.Eta()
  //                 <<" phi "<< emtf::deg_to_rad(trk.Phi_glob())
  //                 <<" phi_local "<< emtf::deg_to_rad(trk.Phi_loc()) << std::endl;
  //     int bx = trk.BX();
  //     if ( bx < minBXTkMuon_ or bx > maxBXTkMuon_) continue;

  //     float dR = deltaR(float(simtrack.momentum().eta()), float(reco::reduceRange(simtrack.momentum().phi())),
  //                       trk.Eta(), reco::reduceRange(emtf::deg_to_rad(trk.Phi_glob())));

  //     if (verboseTkMuon_)
  //       std::cout <<"dR (track, sim) "<< dR <<" deltaRTkMuon_ "
  //                 << deltaRTkMuon_ << std::endl;
  //     if (dR < deltaRTkMuon_){
  //       if (dR < mindRTkMuon){
  //         mindRTkMuon = dR;
  //         l1TkMuon_.reset(new gem::TkMuon(trk));
  //         mindRTkMuon = dR;
  //       }
  //     }
  //   }
  // }
}
