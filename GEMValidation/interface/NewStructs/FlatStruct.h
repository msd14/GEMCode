#ifndef GEMCode_GEMValidation_FlatStruct
#define GEMCode_GEMValidation_FlatStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct GenParticleStruct {

    p_ints gen_charge;
    p_ints gen_pdgid;
    p_ints gen_tpid;
    p_floats gen_pt;
    p_floats gen_pz;
    p_floats gen_eta;
    p_floats gen_phi;
    p_floats gen_dxy;
    p_floats gen_d0;
    p_floats gen_z0;
    p_floats gen_d0_prod;
    p_floats gen_z0_prod;

    void init() {
      gen_charge = new t_ints;
      gen_pdgid = new t_ints;
      gen_tpid = new t_ints;
      gen_pt = new t_floats;
      gen_pz = new t_floats;
      gen_eta = new t_floats;
      gen_phi = new t_floats;
      gen_dxy = new t_floats;
      gen_d0 = new t_floats;
      gen_z0 = new t_floats;
      gen_d0_prod = new t_floats;
      gen_z0_prod = new t_floats;
    }

    void book(TTree* t) {
      t->Branch("gen_charge", &gen_charge);
      t->Branch("gen_pdgid", &gen_pdgid);
      t->Branch("gen_tpid", &gen_tpid);
      t->Branch("gen_pt", &gen_pt);
      t->Branch("gen_pz", &gen_pz);
      t->Branch("gen_eta", &gen_eta);
      t->Branch("gen_phi", &gen_phi);
      t->Branch("gen_dxy", &gen_dxy);
      t->Branch("gen_d0", &gen_d0);
      t->Branch("gen_z0", &gen_z0);
      t->Branch("gen_d0_prod", &gen_d0_prod);
      t->Branch("gen_z0_prod", &gen_z0_prod);
    }
  };

  struct SimTrackStruct {

    p_ints sim_charge;
    p_ints sim_pdgid;
    p_ints sim_tpid;
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
    p_floats sim_pt;
    p_floats sim_px;
    p_floats sim_py;
    p_floats sim_pz;
    p_floats sim_eta;
    p_floats sim_phi;
    p_floats sim_vx;
    p_floats sim_vy;
    p_floats sim_vz;
    p_floats sim_d0;
    p_floats sim_z0;
    p_floats sim_d0_prod;
    p_floats sim_z0_prod;

    void init() {
      sim_charge = new t_ints;
      sim_pdgid = new t_ints;
      sim_tpid = new t_ints;
      sim_id_gem_sh = new t_ints;
      sim_id_gem_dg = new t_ints;
      sim_id_gem_pad = new t_ints;
      sim_id_gem_copad = new t_ints;
      sim_id_gem_cluster = new t_ints;
      sim_id_csc_sh = new t_ints;
      sim_id_csc_wire = new t_ints;
      sim_id_csc_strip = new t_ints;
      sim_id_csc_clct = new t_ints;
      sim_id_csc_alct = new t_ints;
      sim_id_csc_lct = new t_ints;
      sim_id_csc_mplct = new t_ints;
      sim_id_emtf_track = new t_ints;
      sim_id_emtf_cand = new t_ints;
      sim_id_l1mu = new t_ints;
      sim_id_l1track = new t_ints;
      sim_id_l1trackmu = new t_ints;
      sim_pt = new t_floats;
      sim_px = new t_floats;
      sim_py = new t_floats;
      sim_pz = new t_floats;
      sim_eta = new t_floats;
      sim_phi = new t_floats;
      sim_vx = new t_floats;
      sim_vy = new t_floats;
      sim_vz = new t_floats;
      sim_d0 = new t_floats;
      sim_z0 = new t_floats;
      sim_d0_prod = new t_floats;
      sim_z0_prod = new t_floats;
    }

    void book(TTree* t) {
      t->Branch("sim_charge", &sim_charge);
      t->Branch("sim_pdgid", &sim_pdgid);
      t->Branch("sim_tpid", &sim_tpid);
      t->Branch("sim_id_gem_sh", &sim_id_gem_sh);
      t->Branch("sim_id_gem_dg", &sim_id_gem_dg);
      t->Branch("sim_id_gem_pad", &sim_id_gem_pad);
      t->Branch("sim_id_gem_copad", &sim_id_gem_copad);
      t->Branch("sim_id_gem_cluster", &sim_id_gem_cluster);
      t->Branch("sim_id_csc_sh", &sim_id_csc_sh);
      t->Branch("sim_id_csc_wire", &sim_id_csc_wire);
      t->Branch("sim_id_csc_strip", &sim_id_csc_strip);
      t->Branch("sim_id_csc_clct", &sim_id_csc_clct);
      t->Branch("sim_id_csc_alct", &sim_id_csc_alct);
      t->Branch("sim_id_csc_lct", &sim_id_csc_lct);
      t->Branch("sim_id_csc_mplct", &sim_id_csc_mplct);
      t->Branch("sim_id_emtf_track", &sim_id_emtf_track);
      t->Branch("sim_id_emtf_cand", &sim_id_emtf_cand);
      t->Branch("sim_id_l1mu", &sim_id_l1mu);
      t->Branch("sim_id_l1track", &sim_id_l1track);
      t->Branch("sim_id_l1trackmu", &sim_id_l1trackmu);
      t->Branch("sim_pt", &sim_pt);
      t->Branch("sim_px", &sim_px);
      t->Branch("sim_py", &sim_py);
      t->Branch("sim_pz", &sim_pz);
      t->Branch("sim_eta", &sim_eta);
      t->Branch("sim_phi", &sim_phi);
      t->Branch("sim_vx", &sim_vx);
      t->Branch("sim_vy", &sim_vy);
      t->Branch("sim_vz", &sim_vz);
      t->Branch("sim_d0", &sim_d0);
      t->Branch("sim_z0", &sim_z0);
      t->Branch("sim_d0_prod", &sim_d0_prod);
      t->Branch("sim_z0_prod", &sim_z0_prod);
    }
  };

  struct GEMSimHitStruct {

    p_ints gem_sh_bx;
    p_ints gem_sh_strip_l1;
    p_ints gem_sh_strip_l2;
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

    void init() {
      gem_sh_bx = new t_ints;
      gem_sh_strip_l1 = new t_ints;
      gem_sh_strip_l2 = new t_ints;
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
    }

    void book(TTree* t) {
      t->Branch("gem_sh_bx", &gem_sh_bx);
      t->Branch("gem_sh_strip_l1", &gem_sh_strip_l1);
      t->Branch("gem_sh_strip_l2", &gem_sh_strip_l2);
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
    }
  };

  struct CSCSimHitStruct {

    p_ints csc_sh_bx;
    p_ints csc_sh_keyhs;
    p_ints csc_sh_isodd;
    p_ints csc_sh_region;
    p_ints csc_sh_station;
    p_ints csc_sh_ring;
    p_ints csc_sh_chamber;
    p_ints csc_sh_tpid;
    p_ints csc_sh_nlayers;
    p_ints csc_sh_strip_l1;
    p_ints csc_sh_strip_l6;
    p_floats csc_sh_dphi;
    p_floats csc_sh_bend;
    p_floats csc_sh_phi;
    p_floats csc_sh_phi_l1;
    p_floats csc_sh_phi_l6;
    p_floats csc_sh_eta;
    p_floats csc_sh_perp;

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
      csc_sh_strip_l1 = new t_ints;
      csc_sh_strip_l6 = new t_ints;
      csc_sh_dphi = new t_floats;
      csc_sh_bend = new t_floats;
      csc_sh_phi = new t_floats;
      csc_sh_phi_l1 = new t_floats;
      csc_sh_phi_l6 = new t_floats;
      csc_sh_eta = new t_floats;
      csc_sh_perp = new t_floats;
    }

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
      t->Branch("csc_sh_strip_l1", &csc_sh_strip_l1);
      t->Branch("csc_sh_strip_l6", &csc_sh_strip_l6);
      t->Branch("csc_sh_dphi", &csc_sh_dphi);
      t->Branch("csc_sh_bend", &csc_sh_bend);
      t->Branch("csc_sh_phi", &csc_sh_phi);
      t->Branch("csc_sh_phi_l1", &csc_sh_phi_l1);
      t->Branch("csc_sh_phi_l6", &csc_sh_phi_l6);
      t->Branch("csc_sh_eta", &csc_sh_eta);
      t->Branch("csc_sh_perp", &csc_sh_perp);
    }
  };

  struct GEMDigiStruct {

    p_ints gem_digi_bx;
    p_ints gem_digi_strip;
    p_ints gem_digi_isodd;
    p_ints gem_digi_region;
    p_ints gem_digi_station;
    p_ints gem_digi_roll;
    p_ints gem_digi_layer;
    p_ints gem_digi_chamber;
    p_ints gem_digi_tpid;

    void init() {
      gem_digi_bx = new t_ints;
      gem_digi_strip = new t_ints;
      gem_digi_isodd = new t_ints;
      gem_digi_region = new t_ints;
      gem_digi_station = new t_ints;
      gem_digi_roll = new t_ints;
      gem_digi_layer = new t_ints;
      gem_digi_chamber = new t_ints;
      gem_digi_tpid = new t_ints;
    }

    void book(TTree* t) {
      t->Branch("gem_digi_bx", &gem_digi_bx);
      t->Branch("gem_digi_strip", &gem_digi_strip);
      t->Branch("gem_digi_isodd", &gem_digi_isodd);
      t->Branch("gem_digi_region", &gem_digi_region);
      t->Branch("gem_digi_station", &gem_digi_station);
      t->Branch("gem_digi_roll", &gem_digi_roll);
      t->Branch("gem_digi_layer", &gem_digi_layer);
      t->Branch("gem_digi_chamber", &gem_digi_chamber);
      t->Branch("gem_digi_tpid", &gem_digi_tpid);
    }
  };

  struct CSCDigiStruct {

    p_ints csc_strip_bx;
    p_ints csc_strip_keyhs;
    p_ints csc_strip_isodd;
    p_ints csc_strip_region;
    p_ints csc_strip_station;
    p_ints csc_strip_ring;
    p_ints csc_strip_quality;
    p_ints csc_strip_chamber;
    p_ints csc_strip_tpid;
    p_ints csc_wire_bx;
    p_ints csc_wire_keywg;
    p_ints csc_wire_isodd;
    p_ints csc_wire_region;
    p_ints csc_wire_station;
    p_ints csc_wire_ring;
    p_ints csc_wire_quality;
    p_ints csc_wire_chamber;
    p_ints csc_wire_tpid;

    void init() {
      csc_strip_bx = new t_ints;
      csc_strip_keyhs = new t_ints;
      csc_strip_isodd = new t_ints;
      csc_strip_region = new t_ints;
      csc_strip_station = new t_ints;
      csc_strip_ring = new t_ints;
      csc_strip_quality = new t_ints;
      csc_strip_chamber = new t_ints;
      csc_strip_tpid = new t_ints;
      csc_wire_bx = new t_ints;
      csc_wire_keywg = new t_ints;
      csc_wire_isodd = new t_ints;
      csc_wire_region = new t_ints;
      csc_wire_station = new t_ints;
      csc_wire_ring = new t_ints;
      csc_wire_quality = new t_ints;
      csc_wire_chamber = new t_ints;
      csc_wire_tpid = new t_ints;
    }

    void book(TTree* t) {
      t->Branch("csc_strip_bx", &csc_strip_bx);
      t->Branch("csc_strip_keyhs", &csc_strip_keyhs);
      t->Branch("csc_strip_isodd", &csc_strip_isodd);
      t->Branch("csc_strip_region", &csc_strip_region);
      t->Branch("csc_strip_station", &csc_strip_station);
      t->Branch("csc_strip_ring", &csc_strip_ring);
      t->Branch("csc_strip_quality", &csc_strip_quality);
      t->Branch("csc_strip_chamber", &csc_strip_chamber);
      t->Branch("csc_strip_tpid", &csc_strip_tpid);
      t->Branch("csc_wire_bx", &csc_wire_bx);
      t->Branch("csc_wire_keywg", &csc_wire_keywg);
      t->Branch("csc_wire_isodd", &csc_wire_isodd);
      t->Branch("csc_wire_region", &csc_wire_region);
      t->Branch("csc_wire_station", &csc_wire_station);
      t->Branch("csc_wire_ring", &csc_wire_ring);
      t->Branch("csc_wire_quality", &csc_wire_quality);
      t->Branch("csc_wire_chamber", &csc_wire_chamber);
      t->Branch("csc_wire_tpid", &csc_wire_tpid);
    }
  };

  struct GEMStubStruct {

    p_ints gem_pad_bx;
    p_ints gem_pad_pad;
    p_ints gem_pad_isodd;
    p_ints gem_pad_region;
    p_ints gem_pad_station;
    p_ints gem_pad_roll;
    p_ints gem_pad_layer;
    p_ints gem_pad_chamber;
    p_ints gem_pad_tpid;
    p_ints gem_copad_bx;
    p_ints gem_copad_pad;
    p_ints gem_copad_isodd;
    p_ints gem_copad_region;
    p_ints gem_copad_station;
    p_ints gem_copad_roll;
    p_ints gem_copad_layer;
    p_ints gem_copad_chamber;
    p_ints gem_copad_tpid;
    p_ints gem_cluster_bx;
    p_ints gem_cluster_pad;
    p_ints gem_cluster_isodd;
    p_ints gem_cluster_size;
    p_ints gem_cluster_region;
    p_ints gem_cluster_station;
    p_ints gem_cluster_roll;
    p_ints gem_cluster_layer;
    p_ints gem_cluster_chamber;
    p_ints gem_cluster_tpid;

    void init() {
      gem_pad_bx = new t_ints;
      gem_pad_pad = new t_ints;
      gem_pad_isodd = new t_ints;
      gem_pad_region = new t_ints;
      gem_pad_station = new t_ints;
      gem_pad_roll = new t_ints;
      gem_pad_layer = new t_ints;
      gem_pad_chamber = new t_ints;
      gem_pad_tpid = new t_ints;
      gem_copad_bx = new t_ints;
      gem_copad_pad = new t_ints;
      gem_copad_isodd = new t_ints;
      gem_copad_region = new t_ints;
      gem_copad_station = new t_ints;
      gem_copad_roll = new t_ints;
      gem_copad_layer = new t_ints;
      gem_copad_chamber = new t_ints;
      gem_copad_tpid = new t_ints;
      gem_cluster_bx = new t_ints;
      gem_cluster_pad = new t_ints;
      gem_cluster_isodd = new t_ints;
      gem_cluster_size = new t_ints;
      gem_cluster_region = new t_ints;
      gem_cluster_station = new t_ints;
      gem_cluster_roll = new t_ints;
      gem_cluster_layer = new t_ints;
      gem_cluster_chamber = new t_ints;
      gem_cluster_tpid = new t_ints;
    }

    void book(TTree* t) {
      t->Branch("gem_pad_bx", &gem_pad_bx);
      t->Branch("gem_pad_pad", &gem_pad_pad);
      t->Branch("gem_pad_isodd", &gem_pad_isodd);
      t->Branch("gem_pad_region", &gem_pad_region);
      t->Branch("gem_pad_station", &gem_pad_station);
      t->Branch("gem_pad_roll", &gem_pad_roll);
      t->Branch("gem_pad_layer", &gem_pad_layer);
      t->Branch("gem_pad_chamber", &gem_pad_chamber);
      t->Branch("gem_pad_tpid", &gem_pad_tpid);
      t->Branch("gem_copad_bx", &gem_copad_bx);
      t->Branch("gem_copad_pad", &gem_copad_pad);
      t->Branch("gem_copad_isodd", &gem_copad_isodd);
      t->Branch("gem_copad_region", &gem_copad_region);
      t->Branch("gem_copad_station", &gem_copad_station);
      t->Branch("gem_copad_roll", &gem_copad_roll);
      t->Branch("gem_copad_layer", &gem_copad_layer);
      t->Branch("gem_copad_chamber", &gem_copad_chamber);
      t->Branch("gem_copad_tpid", &gem_copad_tpid);
      t->Branch("gem_cluster_bx", &gem_cluster_bx);
      t->Branch("gem_cluster_pad", &gem_cluster_pad);
      t->Branch("gem_cluster_isodd", &gem_cluster_isodd);
      t->Branch("gem_cluster_size", &gem_cluster_size);
      t->Branch("gem_cluster_region", &gem_cluster_region);
      t->Branch("gem_cluster_station", &gem_cluster_station);
      t->Branch("gem_cluster_roll", &gem_cluster_roll);
      t->Branch("gem_cluster_layer", &gem_cluster_layer);
      t->Branch("gem_cluster_chamber", &gem_cluster_chamber);
      t->Branch("gem_cluster_tpid", &gem_cluster_tpid);
    }
  };

  struct CSCStubStruct {

    p_ints alct_bx;
    p_ints alct_wg;
    p_ints alct_isodd;
    p_ints alct_region;
    p_ints alct_station;
    p_ints alct_ring;
    p_ints alct_chamber;
    p_ints alct_quality;
    p_ints alct_tpid;
    p_ints clct_bx;
    p_ints clct_hs;
    p_ints clct_qs;
    p_ints clct_es;
    p_ints clct_isodd;
    p_ints clct_region;
    p_ints clct_station;
    p_ints clct_ring;
    p_ints clct_chamber;
    p_ints clct_quality;
    p_ints clct_pattern;
    p_ints clct_pattern_run3;
    p_ints clct_tpid;
    p_ints lct_bx;
    p_ints lct_wg;
    p_ints lct_hs;
    p_ints lct_qs;
    p_ints lct_es;
    p_ints lct_isodd;
    p_ints lct_region;
    p_ints lct_station;
    p_ints lct_ring;
    p_ints lct_chamber;
    p_ints lct_quality;
    p_ints lct_pattern;
    p_ints lct_pattern_run3;
    p_ints lct_tpid;
    p_ints mplct_bx;
    p_ints mplct_wg;
    p_ints mplct_hs;
    p_ints mplct_qs;
    p_ints mplct_es;
    p_ints mplct_isodd;
    p_ints mplct_region;
    p_ints mplct_station;
    p_ints mplct_ring;
    p_ints mplct_chamber;
    p_ints mplct_quality;
    p_ints mplct_pattern;
    p_ints mplct_pattern_run3;
    p_ints mplct_tpid;

    void init() {
      alct_bx = new t_ints;
      alct_wg = new t_ints;
      alct_isodd = new t_ints;
      alct_region = new t_ints;
      alct_station = new t_ints;
      alct_ring = new t_ints;
      alct_chamber = new t_ints;
      alct_quality = new t_ints;
      alct_tpid = new t_ints;
      clct_bx = new t_ints;
      clct_hs = new t_ints;
      clct_qs = new t_ints;
      clct_es = new t_ints;
      clct_isodd = new t_ints;
      clct_region = new t_ints;
      clct_station = new t_ints;
      clct_ring = new t_ints;
      clct_chamber = new t_ints;
      clct_quality = new t_ints;
      clct_pattern = new t_ints;
      clct_pattern_run3 = new t_ints;
      clct_tpid = new t_ints;
      lct_bx = new t_ints;
      lct_wg = new t_ints;
      lct_hs = new t_ints;
      lct_qs = new t_ints;
      lct_es = new t_ints;
      lct_isodd = new t_ints;
      lct_region = new t_ints;
      lct_station = new t_ints;
      lct_ring = new t_ints;
      lct_chamber = new t_ints;
      lct_quality = new t_ints;
      lct_pattern = new t_ints;
      lct_pattern_run3 = new t_ints;
      lct_tpid = new t_ints;
      mplct_bx = new t_ints;
      mplct_wg = new t_ints;
      mplct_hs = new t_ints;
      mplct_qs = new t_ints;
      mplct_es = new t_ints;
      mplct_isodd = new t_ints;
      mplct_region = new t_ints;
      mplct_station = new t_ints;
      mplct_ring = new t_ints;
      mplct_chamber = new t_ints;
      mplct_quality = new t_ints;
      mplct_pattern = new t_ints;
      mplct_pattern_run3 = new t_ints;
      mplct_tpid = new t_ints;
    }

    void book(TTree* t) {
      t->Branch("alct_bx", &alct_bx);
      t->Branch("alct_wg", &alct_wg);
      t->Branch("alct_isodd", &alct_isodd);
      t->Branch("alct_region", &alct_region);
      t->Branch("alct_station", &alct_station);
      t->Branch("alct_ring", &alct_ring);
      t->Branch("alct_chamber", &alct_chamber);
      t->Branch("alct_quality", &alct_quality);
      t->Branch("alct_tpid", &alct_tpid);
      t->Branch("clct_bx", &clct_bx);
      t->Branch("clct_hs", &clct_hs);
      t->Branch("clct_qs", &clct_qs);
      t->Branch("clct_es", &clct_es);
      t->Branch("clct_isodd", &clct_isodd);
      t->Branch("clct_region", &clct_region);
      t->Branch("clct_station", &clct_station);
      t->Branch("clct_ring", &clct_ring);
      t->Branch("clct_chamber", &clct_chamber);
      t->Branch("clct_quality", &clct_quality);
      t->Branch("clct_pattern", &clct_pattern);
      t->Branch("clct_pattern_run3", &clct_pattern_run3);
      t->Branch("clct_tpid", &clct_tpid);
      t->Branch("lct_bx", &lct_bx);
      t->Branch("lct_wg", &lct_wg);
      t->Branch("lct_hs", &lct_hs);
      t->Branch("lct_qs", &lct_qs);
      t->Branch("lct_es", &lct_es);
      t->Branch("lct_isodd", &lct_isodd);
      t->Branch("lct_region", &lct_region);
      t->Branch("lct_station", &lct_station);
      t->Branch("lct_ring", &lct_ring);
      t->Branch("lct_chamber", &lct_chamber);
      t->Branch("lct_quality", &lct_quality);
      t->Branch("lct_pattern", &lct_pattern);
      t->Branch("lct_pattern_run3", &lct_pattern_run3);
      t->Branch("lct_tpid", &lct_tpid);
      t->Branch("mplct_bx", &mplct_bx);
      t->Branch("mplct_wg", &mplct_wg);
      t->Branch("mplct_hs", &mplct_hs);
      t->Branch("mplct_qs", &mplct_qs);
      t->Branch("mplct_es", &mplct_es);
      t->Branch("mplct_isodd", &mplct_isodd);
      t->Branch("mplct_region", &mplct_region);
      t->Branch("mplct_station", &mplct_station);
      t->Branch("mplct_ring", &mplct_ring);
      t->Branch("mplct_chamber", &mplct_chamber);
      t->Branch("mplct_quality", &mplct_quality);
      t->Branch("mplct_pattern", &mplct_pattern);
      t->Branch("mplct_pattern_run3", &mplct_pattern_run3);
      t->Branch("mplct_tpid", &mplct_tpid);
    }
  };

  struct L1MuStruct {

    p_ints emtftrack_charge;
    p_ints emtftrack_bx;
    p_ints emtftrack_tpid;
    p_floats emtftrack_pt;
    p_floats emtftrack_eta;
    p_floats emtftrack_phi;
    p_ints emtfcand_charge;
    p_ints emtfcand_bx;
    p_ints emtfcand_tpid;
    p_floats emtfcand_pt;
    p_floats emtfcand_eta;
    p_floats emtfcand_phi;
    p_ints l1mu_charge;
    p_ints l1mu_bx;
    p_ints l1mu_tpid;
    p_floats l1mu_pt;
    p_floats l1mu_eta;
    p_floats l1mu_phi;

    void init() {
      emtftrack_charge = new t_ints;
      emtftrack_bx = new t_ints;
      emtftrack_tpid = new t_ints;
      emtftrack_pt = new t_floats;
      emtftrack_eta = new t_floats;
      emtftrack_phi = new t_floats;
      emtfcand_charge = new t_ints;
      emtfcand_bx = new t_ints;
      emtfcand_tpid = new t_ints;
      emtfcand_pt = new t_floats;
      emtfcand_eta = new t_floats;
      emtfcand_phi = new t_floats;
      l1mu_charge = new t_ints;
      l1mu_bx = new t_ints;
      l1mu_tpid = new t_ints;
      l1mu_pt = new t_floats;
      l1mu_eta = new t_floats;
      l1mu_phi = new t_floats;
    }

    void book(TTree* t) {
      t->Branch("emtftrack_charge", &emtftrack_charge);
      t->Branch("emtftrack_bx", &emtftrack_bx);
      t->Branch("emtftrack_tpid", &emtftrack_tpid);
      t->Branch("emtftrack_pt", &emtftrack_pt);
      t->Branch("emtftrack_eta", &emtftrack_eta);
      t->Branch("emtftrack_phi", &emtftrack_phi);
      t->Branch("emtfcand_charge", &emtfcand_charge);
      t->Branch("emtfcand_bx", &emtfcand_bx);
      t->Branch("emtfcand_tpid", &emtfcand_tpid);
      t->Branch("emtfcand_pt", &emtfcand_pt);
      t->Branch("emtfcand_eta", &emtfcand_eta);
      t->Branch("emtfcand_phi", &emtfcand_phi);
      t->Branch("l1mu_charge", &l1mu_charge);
      t->Branch("l1mu_bx", &l1mu_bx);
      t->Branch("l1mu_tpid", &l1mu_tpid);
      t->Branch("l1mu_pt", &l1mu_pt);
      t->Branch("l1mu_eta", &l1mu_eta);
      t->Branch("l1mu_phi", &l1mu_phi);
    }
  };
};

#endif
