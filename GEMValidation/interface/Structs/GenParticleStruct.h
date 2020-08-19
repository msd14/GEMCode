#ifndef GEMCode_GEMValidation_GenParticleStruct
#define GEMCode_GEMValidation_GenParticleStruct

#include "TTree.h"
#include <vector>

namespace gem {

  struct GenParticleStruct {
    float pt, eta, phi, pz, dxy;
    int charge;
    int endcap;
    int pdgid;

    // new stuff
    std::vector<float>* gen_pt;
    std::vector<float>* gen_eta;
    std::vector<float>* gen_phi;
    std::vector<int>*   gen_charge;
    std::vector<float>* gen_dxy;
    std::vector<float>* gen_d0;
    std::vector<float>* gen_z0;
    std::vector<float>* gen_d0_prod;
    std::vector<float>* gen_z0_prod;
    std::vector<int>*   gen_pdgid;

    void init() {
      pt = 0.;
      phi = 0.;
      eta = -9.;
      dxy = -999.;
      charge = -9;
      endcap = -9;
      pdgid = -9999;

      gen_pt      = new std::vector<float>;
      gen_eta     = new std::vector<float>;
      gen_phi     = new std::vector<float>;
      gen_dxy     = new std::vector<float>;
      gen_d0      = new std::vector<float>;
      gen_z0      = new std::vector<float>;
      gen_d0_prod = new std::vector<float>;
      gen_z0_prod = new std::vector<float>;
      gen_pdgid   = new std::vector<int>;
      gen_charge  = new std::vector<int>;
    };

    void clear() {
      gen_pt->clear();
      gen_eta->clear();
      gen_phi->clear();
      gen_dxy->clear();
      gen_d0->clear();
      gen_z0->clear();
      gen_d0_prod->clear();
      gen_z0_prod->clear();
      gen_pdgid->clear();
      gen_charge->clear();
    }

    void book(TTree* t) {
      t->Branch("pt", &pt);
      t->Branch("pz", &pz);
      t->Branch("eta", &eta);
      t->Branch("dxy", &dxy);
      t->Branch("phi", &phi);
      t->Branch("charge", &charge);
      t->Branch("endcap", &endcap);
      t->Branch("pdgid", &pdgid);

      t->Branch("tp_pt",     &gen_pt);
      t->Branch("tp_eta",    &gen_eta);
      t->Branch("tp_phi",    &gen_phi);
      t->Branch("tp_dxy",    &gen_dxy);
      t->Branch("tp_d0",     &gen_d0);
      t->Branch("tp_z0",     &gen_z0);
      t->Branch("tp_d0_prod",     &gen_d0_prod);
      t->Branch("tp_z0_prod",     &gen_z0_prod);
      t->Branch("tp_pdgid",       &gen_pdgid);
      t->Branch("tp_charge",      &gen_charge);
    }
  };
}  // namespace

#endif
