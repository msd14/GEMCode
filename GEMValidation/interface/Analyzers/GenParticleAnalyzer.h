#ifndef GEMCode_GEMValidation_GenParticleAnalyzer_h
#define GEMCode_GEMValidation_GenParticleAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class GenParticleAnalyzer
{
public:

  // constructor
  GenParticleAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~GenParticleAnalyzer() {}

  void init(const edm::Event& iEvent, const edm::EventSetup& iSetup);

  void setMatcher(const GenParticleMatcher& match_sh);

  // initialize the event
  void analyze(TreeManager& tree);

 private:
  std::unique_ptr<GenParticleMatcher> match_;

};

#endif
