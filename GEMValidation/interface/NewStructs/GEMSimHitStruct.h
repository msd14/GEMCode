#ifndef GEMCode_GEMValidation_MY_GEMSimHitStruct
#define GEMCode_GEMValidation_MY_GEMSimHitStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct GEMSimHitStruct {

    p_ints gem_sh_bx;
    p_ints gem_sh_keyhs;
    p_ints gem_sh_isodd;
    p_ints gem_sh_region;
    p_ints gem_sh_station;
    p_ints gem_sh_ring;
    p_ints gem_sh_chamber;
    p_ints gem_sh_tpid;
    p_ints gem_sh_nlayers;
    p_floats gem_sh_dphi;
    p_floats gem_sh_bend;
    p_floats gem_sh_phi;
    p_floats gem_sh_eta;
    p_floats gem_sh_perp;
    p_floats gem_sh_strip_l1;
    p_floats gem_sh_strip_l2;

    void init() {
      gem_sh_bx = new t_ints;
      gem_sh_keyhs = new t_ints;
      gem_sh_isodd = new t_ints;
      gem_sh_region = new t_ints;
      gem_sh_station = new t_ints;
      gem_sh_ring = new t_ints;
      gem_sh_chamber = new t_ints;
      gem_sh_tpid = new t_ints;
      gem_sh_nlayers = new t_ints;
      gem_sh_dphi = new t_floats;
      gem_sh_bend = new t_floats;
      gem_sh_phi = new t_floats;
      gem_sh_eta = new t_floats;
      gem_sh_perp = new t_floats;
      gem_sh_strip_l1 = new t_floats;
      gem_sh_strip_l2 = new t_floats;
    };

    void book(TTree* t) {
      t->Branch("gem_sh_bx", &gem_sh_bx);
      t->Branch("gem_sh_keyhs", &gem_sh_keyhs);
      t->Branch("gem_sh_isodd", &gem_sh_isodd);
      t->Branch("gem_sh_region", &gem_sh_region);
      t->Branch("gem_sh_station", &gem_sh_station);
      t->Branch("gem_sh_ring", &gem_sh_ring);
      t->Branch("gem_sh_chamber", &gem_sh_chamber);
      t->Branch("gem_sh_tpid", &gem_sh_tpid);
      t->Branch("gem_sh_nlayers", &gem_sh_nlayers);
      t->Branch("gem_sh_dphi", &gem_sh_dphi);
      t->Branch("gem_sh_bend", &gem_sh_bend);
      t->Branch("gem_sh_phi", &gem_sh_phi);
      t->Branch("gem_sh_eta", &gem_sh_eta);
      t->Branch("gem_sh_perp", &gem_sh_perp);
      t->Branch("gem_sh_strip_l1", &gem_sh_strip_l1);
      t->Branch("gem_sh_strip_l2", &gem_sh_strip_l2);
    }
  };
}  // namespace

#endif
