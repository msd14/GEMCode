#ifndef GEMCode_GEMValidation_MY_SimTrackStruct
#define GEMCode_GEMValidation_MY_SimTrackStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct SimTrackStruct {
    p_floats sim_pt;
    p_floats sim_px;
    p_floats sim_py;
    p_floats sim_pz;
    p_floats sim_eta;
    p_floats sim_phi;
    p_ints   sim_charge;
    p_floats sim_dxy;
    p_floats sim_vx;
    p_floats sim_vy;
    p_floats sim_vz;
    p_floats sim_d0;
    p_floats sim_z0;
    p_floats sim_d0_prod;
    p_floats sim_z0_prod;
    p_ints   sim_pdgid;

    p_ints sim_id_gem_sh;
    p_ints sim_id_gem_dg;
    p_ints sim_id_gem_pad;
    p_ints sim_id_gem_copad;
    p_ints sim_id_gem_cluster;

    p_ints sim_id_csc_sh;
    p_ints sim_id_csc_wire;
    p_ints sim_id_csc_strip;
    p_ints sim_id_csc_clct;
    p_ints sim_id_csc_alct;
    p_ints sim_id_csc_lct;
    p_ints sim_id_csc_mplct;

    p_ints sim_id_emtf_track;
    p_ints sim_id_emtf_cand;
    p_ints sim_id_l1mu;
    p_ints sim_id_l1track;
    p_ints sim_id_l1trackmu;

    void init() {
      sim_pt      = new t_floats;
      sim_px      = new t_floats;
      sim_py      = new t_floats;
      sim_pz      = new t_floats;
      sim_eta     = new t_floats;
      sim_phi     = new t_floats;
      sim_dxy     = new t_floats;
      sim_vx     = new t_floats;
      sim_vy     = new t_floats;
      sim_vz     = new t_floats;
      sim_d0      = new t_floats;
      sim_z0      = new t_floats;
      sim_d0_prod = new t_floats;
      sim_z0_prod = new t_floats;
      sim_pdgid   = new t_ints;
      sim_charge  = new t_ints;

      sim_id_gem_sh  = new t_ints;
      sim_id_gem_dg  = new t_ints;
      sim_id_gem_pad  = new t_ints;
      sim_id_gem_copad  = new t_ints;
      sim_id_gem_cluster  = new t_ints;

      sim_id_csc_sh  = new t_ints;
      sim_id_csc_wire  = new t_ints;
      sim_id_csc_strip  = new t_ints;
      sim_id_csc_clct  = new t_ints;
      sim_id_csc_alct  = new t_ints;
      sim_id_csc_lct  = new t_ints;
      sim_id_csc_mplct  = new t_ints;

      sim_id_emtf_track  = new t_ints;
      sim_id_emtf_cand  = new t_ints;
      sim_id_l1mu  = new t_ints;
      sim_id_l1track  = new t_ints;
      sim_id_l1trackmu  = new t_ints;
    };

    void book(TTree* t) {
      t->Branch("sim_pt",     &sim_pt);
      t->Branch("sim_px",     &sim_px);
      t->Branch("sim_py",     &sim_py);
      t->Branch("sim_pz",     &sim_pz);
      t->Branch("sim_eta",    &sim_eta);
      t->Branch("sim_phi",    &sim_phi);
      t->Branch("sim_dxy",    &sim_dxy);
      t->Branch("sim_vx",    &sim_vx);
      t->Branch("sim_vy",    &sim_vy);
      t->Branch("sim_vz",    &sim_vz);
      t->Branch("sim_d0",     &sim_d0);
      t->Branch("sim_z0",     &sim_z0);
      t->Branch("sim_d0_prod",     &sim_d0_prod);
      t->Branch("sim_z0_prod",     &sim_z0_prod);
      t->Branch("sim_pdgid",       &sim_pdgid);
      t->Branch("sim_charge",      &sim_charge);
    }
  };
}  // namespace

#endif
