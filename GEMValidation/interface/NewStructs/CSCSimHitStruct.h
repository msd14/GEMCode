#ifndef GEMCode_GEMValidation_MY_CSCSimHitStruct
#define GEMCode_GEMValidation_MY_CSCSimHitStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct CSCSimHitStruct {

    static const int nStations = 11;

    p_ints csc_sh_bx;
    p_ints csc_sh_keyhs;
    p_ints csc_sh_isodd;
    p_ints csc_sh_region;
    p_ints csc_sh_station;
    p_ints csc_sh_ring;
    p_ints csc_sh_chamber;
    p_ints csc_sh_tpid;
    p_ints csc_sh_nlayers;
    p_floats csc_sh_dphi;
    p_floats csc_sh_bend;
    p_floats csc_sh_phi;
    p_floats csc_sh_eta;
    p_floats csc_sh_perp;
    p_floats csc_sh_phi_l1;
    p_floats csc_sh_phi_l6;
    p_floats csc_sh_strip_l1;
    p_floats csc_sh_strip_l6;

    void init() {

      csc_sh_bx = new t_ints;
      csc_sh_keyhs = new t_ints;
      csc_sh_isodd = new t_ints;
      csc_sh_region = new t_ints;
      csc_sh_station = new t_ints;
      csc_sh_ring = new t_ints;
      csc_sh_chamber = new t_ints;
      csc_sh_tpid = new t_ints;
      csc_sh_nlayers = new t_ints;
      csc_sh_dphi = new t_floats;
      csc_sh_bend = new t_floats;
      csc_sh_phi = new t_floats;
      csc_sh_eta = new t_floats;
      csc_sh_perp = new t_floats;
      csc_sh_phi_l1 = new t_floats;
      csc_sh_phi_l6 = new t_floats;
      csc_sh_strip_l1 = new t_floats;
      csc_sh_strip_l6 = new t_floats;
    };

    void book(TTree* t) {

      t->Branch("csc_sh_bx", &csc_sh_bx);
      t->Branch("csc_sh_keyhs", &csc_sh_keyhs);
      t->Branch("csc_sh_isodd", &csc_sh_isodd);
      t->Branch("csc_sh_region", &csc_sh_region);
      t->Branch("csc_sh_station", &csc_sh_station);
      t->Branch("csc_sh_ring", &csc_sh_ring);
      t->Branch("csc_sh_chamber", &csc_sh_chamber);
      t->Branch("csc_sh_tpid", &csc_sh_tpid);
      t->Branch("csc_sh_nlayers", &csc_sh_nlayers);
      t->Branch("csc_sh_dphi", &csc_sh_dphi);
      t->Branch("csc_sh_bend", &csc_sh_bend);
      t->Branch("csc_sh_phi", &csc_sh_phi);
      t->Branch("csc_sh_eta", &csc_sh_eta);
      t->Branch("csc_sh_perp", &csc_sh_perp);
      t->Branch("csc_sh_l1", &csc_sh_phi_l1);
      t->Branch("csc_sh_l6", &csc_sh_phi_l6);
      t->Branch("csc_sh_strip_l1", &csc_sh_strip_l1);
      t->Branch("csc_sh_strip_l6", &csc_sh_strip_l6);

    }
  };
}  // namespace

#endif
