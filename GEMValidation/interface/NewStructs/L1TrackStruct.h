#ifndef GEMCode_GEMValidation_MY_L1TrackStruct
#define GEMCode_GEMValidation_MY_L1TrackStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct L1TrackStruct {

    p_floats l1track_pt;
    p_floats l1track_eta;
    p_floats l1track_phi;
    p_ints   l1track_charge;
    p_ints   l1track_bx;
    p_ints   l1track_tpid;

    p_floats l1trackmuon_pt;
    p_floats l1trackmuon_eta;
    p_floats l1trackmuon_phi;
    p_ints   l1trackmuon_charge;
    p_ints   l1trackmuon_bx;
    p_ints   l1trackmuon_tpid;

    void init() {
      l1track_pt = new t_floats;
      l1track_eta = new t_floats;
      l1track_phi = new t_floats;
      l1track_charge = new t_ints;
      l1track_bx = new t_ints;

      l1trackmuon_pt = new t_floats;
      l1trackmuon_eta = new t_floats;
      l1trackmuon_phi = new t_floats;
      l1trackmuon_charge = new t_ints;
      l1trackmuon_bx = new t_ints;
    };

    void clear(){
      l1track_pt->clear();
      l1track_eta->clear();
      l1track_phi->clear();
      l1track_charge->clear();
      l1track_bx->clear();

      l1trackmuon_pt->clear();
      l1trackmuon_eta->clear();
      l1trackmuon_phi->clear();
      l1trackmuon_charge->clear();
      l1trackmuon_bx->clear();
    }

    void book(TTree* t) {
      t->Branch("l1track_pt", &l1track_pt);
      t->Branch("l1track_eta", &l1track_eta);
      t->Branch("l1track_phi", &l1track_phi);
      t->Branch("l1track_charge", &l1track_charge);
      t->Branch("l1track_bx", &l1track_bx);
      t->Branch("l1track_tpid", &l1track_tpid);

      t->Branch("l1trackmuon_pt", &l1trackmuon_pt);
      t->Branch("l1trackmuon_eta", &l1trackmuon_eta);
      t->Branch("l1trackmuon_phi", &l1trackmuon_phi);
      t->Branch("l1trackmuon_charge", &l1trackmuon_charge);
      t->Branch("l1trackmuon_bx", &l1trackmuon_bx);
      t->Branch("l1trackmuon_tpid", &l1trackmuon_tpid);
    }
  };
}  // namespace

#endif
