#ifndef GEMCode_GEMValidation_MY_CSCDigiStruct
#define GEMCode_GEMValidation_MY_CSCDigiStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {
  /*
    "CSC_ME11", "CSC_ME1a", "CSC_ME1b", "CSC_ME12", "CSC_ME13",
    "CSC_ME21", "CSC_ME22", "CSC_ME31",
    "CSC_ME32", "CSC_ME41", "CSC_ME42"
  */

  struct CSCDigiStruct {

    // at least 4 wiregroups in a chamber!
    p_ints csc_wg_bx;
    p_ints csc_wg_keywg;
    p_ints csc_wg_isodd;
    p_ints csc_wg_region;
    p_ints csc_wg_station;
    p_ints csc_wg_ring;
    p_ints csc_wg_chamber;
    p_ints csc_wg_quality;
    p_ints csc_wg_tpid;

    p_ints csc_hs_bx;
    p_ints csc_hs_keyhs;
    p_ints csc_hs_isodd;
    p_ints csc_hs_region;
    p_ints csc_hs_station;
    p_ints csc_hs_ring;
    p_ints csc_hs_chamber;
    p_ints csc_hs_quality;
    p_ints csc_hs_tpid;

    void init() {
      csc_wg_bx = new t_ints;
      csc_wg_keywg = new t_ints;
      csc_wg_isodd = new t_ints;
      csc_wg_region = new t_ints;
      csc_wg_station = new t_ints;
      csc_wg_ring = new t_ints;
      csc_wg_chamber = new t_ints;
      csc_wg_quality = new t_ints;
      csc_wg_tpid = new t_ints;

      csc_hs_bx = new t_ints;
      csc_hs_keyhs = new t_ints;
      csc_hs_isodd = new t_ints;
      csc_hs_region = new t_ints;
      csc_hs_station = new t_ints;
      csc_hs_ring = new t_ints;
      csc_hs_chamber = new t_ints;
      csc_hs_quality = new t_ints;
      csc_hs_tpid = new t_ints;
    };

   void book(TTree* t) {
      t->Branch("csc_wg_bx", &csc_wg_bx);
      t->Branch("csc_wg_keywg", &csc_wg_keywg);
      t->Branch("csc_wg_isodd", &csc_wg_isodd);
      t->Branch("csc_wg_region", &csc_wg_region);
      t->Branch("csc_wg_station", &csc_wg_station);
      t->Branch("csc_wg_ring", &csc_wg_ring);
      t->Branch("csc_wg_chamber", &csc_wg_chamber);
      t->Branch("csc_wg_quality", &csc_wg_quality);
      t->Branch("csc_wg_tpid", &csc_wg_tpid);

      t->Branch("csc_hs_bx", &csc_hs_bx);
      t->Branch("csc_hs_keyhs", &csc_hs_keyhs);
      t->Branch("csc_hs_isodd", &csc_hs_isodd);
      t->Branch("csc_hs_region", &csc_hs_region);
      t->Branch("csc_hs_station", &csc_hs_station);
      t->Branch("csc_hs_ring", &csc_hs_ring);
      t->Branch("csc_hs_chamber", &csc_hs_chamber);
      t->Branch("csc_hs_quality", &csc_hs_quality);
      t->Branch("csc_hs_tpid", &csc_hs_tpid);
    }
  };  // namespace
}
#endif
