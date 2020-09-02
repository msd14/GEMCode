#ifndef GEMCode_GEMValidation_L1TkMuMatcher_h
#define GEMCode_GEMValidation_L1TkMuMatcher_h

/**\class L1TkMuMatcher

 Description: Matching of tracks to l1tkmu

 Original Author:  "Sven Dildick"
*/

#include "DataFormats/L1TCorrelator/interface/TkMuon.h"
#include "DataFormats/L1TCorrelator/interface/TkMuonFwd.h"
#include "GEMCode/GEMValidation/interface/Matchers/L1TrackMatcher.h"
#include "GEMCode/GEMValidation/interface/Matchers/L1MuMatcher.h"

class L1TkMuMatcher
{
 public:
  /// constructor
  L1TkMuMatcher(edm::ParameterSet const& iPS, edm::ConsumesCollector&& iC);

  /// destructor
  ~L1TkMuMatcher() {}

  /// initialize the event
  void init(const edm::Event& e, const edm::EventSetup& eventSetup);

  /// do the matching
  void match(const SimTrack& t, const SimVertex& v);

  // return best matching tracks
  std::shared_ptr<l1t::TkMuon> l1TkMuon() const { return l1TkMuon_; }

  std::shared_ptr<L1TrackMatcher> l1TrackMatcher() { return l1TrackMatcher_; }
  std::shared_ptr<L1MuMatcher> l1MuMatcher() { return l1MuMatcher_; }

  void setL1TrackMatcher(std::shared_ptr<L1TrackMatcher> s) {l1TrackMatcher_ = s;}
  void setL1MuMatcher(std::shared_ptr<L1MuMatcher> s) {l1MuMatcher_ = s;}

 private:

  void clear();

  void matchL1TkMuonToSimTrack(const SimTrack& t, const l1t::TkMuonCollection&);

  edm::EDGetTokenT<l1t::TkMuonCollection> l1TkMuonToken_;

  edm::Handle<l1t::TkMuonCollection> l1TkMuonHandle_;

  std::shared_ptr<L1TrackMatcher> l1TrackMatcher_;
  std::shared_ptr<L1MuMatcher> l1MuMatcher_;

  int minBXTkMuon_, maxBXTkMuon_;
  int verboseTkMuon_;
  double deltaRTkMuon_;
  bool runTkMuon_;

  std::shared_ptr<l1t::TkMuon> l1TkMuon_;
};

#endif
