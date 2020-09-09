#include "GEMCode/GEMValidation/interface/Analyzers/SimTrackAnalyzer.h"

SimTrackAnalyzer::SimTrackAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
}

void SimTrackAnalyzer::init()
{
}

void SimTrackAnalyzer::analyze(TreeManager& tree, const SimTrack& t, const SimVertex& v)
{
  // simtrack properties
  tree.simTrack().pt = t.momentum().pt();
  tree.simTrack().px = t.momentum().px();
  tree.simTrack().py = t.momentum().py();
  tree.simTrack().pz = t.momentum().pz();
  tree.simTrack().phi = t.momentum().phi();
  tree.simTrack().eta = t.momentum().eta();
  tree.simTrack().charge = t.charge();
  tree.simTrack().endcap = (tree.simTrack().eta > 0.) ? 1 : -1;
  tree.simTrack().pdgid = t.type();

  tree.simTrack().vx = v.position().x();
  tree.simTrack().vy = v.position().y();
  tree.simTrack().vz = v.position().z();
}
