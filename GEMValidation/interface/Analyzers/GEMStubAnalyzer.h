#ifndef GEMCode_GEMValidation_GEMStubAnalyzer_h
#define GEMCode_GEMValidation_GEMStubAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class GEMStubAnalyzer
{
public:

  // constructor
  GEMStubAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~GEMStubAnalyzer() {}

  void setMatcher(const GEMDigiMatcher& match_sh);

  // initialize the event
  void analyze(TreeManager& tree);

 private:

  edm::EDGetTokenT<GEMPadDigiCollection> gemPadToken_;
  edm::EDGetTokenT<GEMPadDigiClusterCollection> gemClusterToken_;
  edm::EDGetTokenT<GEMCoPadDigiCollection> gemCoPadToken_;

  edm::Handle<GEMPadDigiCollection> gemPadsH_;
  edm::Handle<GEMPadDigiClusterCollection> gemClustersH_;
  edm::Handle<GEMCoPadDigiCollection> gemCoPadsH_;

  std::pair<GEMPadDigi, GlobalPoint>
  bestPad(const GEMDetId& id,
          const GEMPadDigiContainer& digis) const;

  std::pair<GEMCoPadDigi, GlobalPoint>
  bestCoPad(const GEMDetId& id,
            const GEMCoPadDigiContainer& digis) const;

  GlobalPoint
  meanPosition(const GEMDetId& id,
               const GEMPadDigiContainer& digis) const;

  GlobalPoint
  meanPosition(const GEMDetId& id,
               const GEMCoPadDigiContainer& digis) const;

  std::unique_ptr<GEMDigiMatcher> match_;
  int minNHitsChamber_;
};

#endif
