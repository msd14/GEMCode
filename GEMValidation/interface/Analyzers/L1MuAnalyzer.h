#ifndef GEMCode_GEMValidation_L1MuAnalyzer_h
#define GEMCode_GEMValidation_L1MuAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class L1MuAnalyzer
{
public:

  // constructor
  L1MuAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~L1MuAnalyzer() {}

  void setMatcher(const L1MuMatcher& match_sh);

  // initialize the event
  void analyze(TreeManager& tree);

 private:

  edm::EDGetTokenT<l1t::EMTFTrackCollection> emtfTrackToken_;
  edm::EDGetTokenT<l1t::RegionalMuonCandBxCollection> emtfCandToken_;
  edm::EDGetTokenT<l1t::MuonBxCollection> muonToken_;

  edm::Handle<l1t::EMTFTrackCollection> emtfTrackHandle_;
  edm::Handle<l1t::RegionalMuonCandBxCollection> emtfCandHandle_;
  edm::Handle<l1t::MuonBxCollection> muonHandle_;

  std::unique_ptr<L1MuMatcher> match_;
};

#endif
