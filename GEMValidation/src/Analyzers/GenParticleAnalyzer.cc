#include "GEMCode/GEMValidation/interface/Analyzers/GenParticleAnalyzer.h"

GenParticleAnalyzer::GenParticleAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  const auto& gen = conf.getParameter<edm::ParameterSet>("genParticle");
  verbose_ = gen.getParameter<int>("verbose");
  run_ = gen.getParameter<bool>("run");

  inputToken_ = iC.consumes<reco::GenParticleCollection>(gen.getParameter<edm::InputTag>("inputTag"));
}

void GenParticleAnalyzer::init(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  iEvent.getByToken(inputToken_, genParticlesHandle_);
}

void GenParticleAnalyzer::setMatcher(const GenParticleMatcher& match_sh)
{
  match_.reset(new GenParticleMatcher(match_sh));
}

void GenParticleAnalyzer::analyze(TreeManager& tree)
{
  // genparticle properties
  tree.genParticle().pt = match_->getMatch()->pt();
  tree.genParticle().pz = match_->getMatch()->pz();
  tree.genParticle().phi = match_->getMatch()->phi();
  tree.genParticle().eta = match_->getMatch()->eta();
  tree.genParticle().charge = match_->getMatch()->charge();
  tree.genParticle().endcap = (tree.genParticle().eta > 0.) ? 1 : -1;
  tree.genParticle().pdgid = match_->getMatch()->pdgId();
}
