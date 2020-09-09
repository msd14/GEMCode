#ifndef GEMCode_GEMValidation_CSCSimHitAnalyzer_h
#define GEMCode_GEMValidation_CSCSimHitAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class CSCSimHitAnalyzer
{
public:

  // constructor
  CSCSimHitAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~CSCSimHitAnalyzer() {}

  void setMatcher(const CSCSimHitMatcher& match_sh);

  // initialize the event
  void analyze(TreeManager& tree);

 private:
  edm::EDGetTokenT<edm::PSimHitContainer> simHitInput_;
  edm::Handle<edm::PSimHitContainer> simHitsH_;

  float
    //  std::pair<float,float>
    fitBendingPositionInChamber(unsigned int detid) const;

  std::shared_ptr<CSCSimHitMatcher> match_;
  int minNHitsChamber_;

  bool verbose_;
  edm::ParameterSet simHitPSet_;
};

#endif
