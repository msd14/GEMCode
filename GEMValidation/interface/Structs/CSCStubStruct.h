#ifndef GEMCode_GEMValidation_CSCStubStruct
#define GEMCode_GEMValidation_CSCStubStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace gem {

  struct CSCStubStruct {

    static const int nStations = 11;

    // bools
    bool has_clct_odd[nStations];
    bool has_alct_odd[nStations];
    bool has_lct_odd[nStations];

    bool has_clct_even[nStations];
    bool has_alct_even[nStations];
    bool has_lct_even[nStations];

    // ints
    int bx_lct_odd[nStations];
    int bx_alct_odd[nStations];
    int bx_clct_odd[nStations];
    int bx_lct_even[nStations];
    int bx_alct_even[nStations];
    int bx_clct_even[nStations];

    int hs_clct_odd[nStations];
    int hs_clct_even[nStations];

    int qs_clct_odd[nStations];
    int qs_clct_even[nStations];

    int es_clct_odd[nStations];
    int es_clct_even[nStations];

    int hs_lct_odd[nStations];
    int hs_lct_even[nStations];

    int qs_lct_odd[nStations];
    int qs_lct_even[nStations];

    int es_lct_odd[nStations];
    int es_lct_even[nStations];

    int wg_alct_odd[nStations];
    int wg_alct_even[nStations];

    int pattern_clct_odd[nStations];
    int pattern_clct_even[nStations];

    int wg_lct_odd[nStations];
    int wg_lct_even[nStations];

    int chamber_lct_odd[nStations];
    int chamber_lct_even[nStations];

    int bend_lct_odd[nStations];
    int bend_lct_even[nStations];

    int passdphi_odd[nStations];
    int passdphi_even[nStations];

    int quality_clct_odd[nStations];
    int quality_clct_even[nStations];
    int quality_alct_odd[nStations];
    int quality_alct_even[nStations];
    int quality_lct_odd[nStations];
    int quality_lct_even[nStations];

    int lct_type[nStations];

    // floats
    float phi_lct_odd[nStations];
    float phi_lct_even[nStations];
    float eta_lct_odd[nStations];
    float eta_lct_even[nStations];
    float dphi_lct_odd[nStations];
    float dphi_lct_even[nStations];
    float chi2_lct_odd[nStations];
    float chi2_lct_even[nStations];

    float perp_lct_odd[nStations];
    float perp_lct_even[nStations];

    // bending resolution
    float slope_clct_odd[nStations];
    float slope_clct_even[nStations];

    float fslope_clct_odd[nStations];
    float fslope_clct_even[nStations];

    float dslope_clct_odd[nStations];
    float dslope_clct_even[nStations];

    // floating point strip in hs, qs or es precision
    float ffhs_clct_odd[nStations];
    float ffhs_clct_even[nStations];

    float fhs_clct_odd[nStations];
    float fhs_clct_even[nStations];

    float fqs_clct_odd[nStations];
    float fqs_clct_even[nStations];

    float fes_clct_odd[nStations];
    float fes_clct_even[nStations];

    float delta_ffhs_clct_odd[nStations];
    float delta_ffhs_clct_even[nStations];

    float delta_fhs_clct_odd[nStations];
    float delta_fhs_clct_even[nStations];

    float delta_fqs_clct_odd[nStations];
    float delta_fqs_clct_even[nStations];

    float delta_fes_clct_odd[nStations];
    float delta_fes_clct_even[nStations];

    // new stuff
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
     mplct_tpid = new t_ints;

      for (unsigned i = 0 ; i < nStations; i++) {

        has_alct_even[i] = 0;
        has_clct_even[i] = 0;
        has_lct_even[i] = 0;
        has_alct_odd[i] = 0;
        has_clct_odd[i] = 0;
        has_lct_odd[i] = 0;

        chamber_lct_odd[i] = -1;
        chamber_lct_even[i] = -1;

        bend_lct_odd[i] = -9;
        bend_lct_even[i] = -9;
        dphi_lct_odd[i] = -9;
        dphi_lct_even[i] = -9;

        bx_lct_odd[i] = -9;
        bx_lct_even[i] = -9;

        hs_lct_odd[i] = 0;
        hs_lct_even[i] = 0;

        qs_lct_odd[i] = 0;
        qs_lct_even[i] = 0;

        es_lct_odd[i] = 0;
        es_lct_even[i] = 0;

        hs_clct_odd[i] = 0;
        hs_clct_even[i] = 0;

        qs_clct_odd[i] = 0;
        qs_clct_even[i] = 0;

        es_clct_odd[i] = 0;
        es_clct_even[i] = 0;

        ffhs_clct_odd[i] = -9;
        ffhs_clct_even[i] = -9;

        fhs_clct_odd[i] = -9;
        fhs_clct_even[i] = -9;

        fqs_clct_odd[i] = -9;
        fqs_clct_even[i] = -9;

        fes_clct_odd[i] = -9;
        fes_clct_even[i] = -9;

        delta_ffhs_clct_odd[i] = -9.;
        delta_ffhs_clct_even[i] = -9.;

        delta_fhs_clct_odd[i] = -9.;
        delta_fhs_clct_even[i] = -9.;

        delta_fqs_clct_odd[i] = -9.;
        delta_fqs_clct_even[i] = -9.;

        delta_fes_clct_odd[i] = -9.;
        delta_fes_clct_even[i] = -9.;

        wg_alct_odd[i] = -1;
        wg_alct_even[i] = -1;

        wg_lct_odd[i] = -1;
        wg_lct_even[i] = -1;

        eta_lct_odd[i] = -9.;
        eta_lct_even[i] = -9.;

        phi_lct_odd[i] = -9.;
        phi_lct_even[i] = -9.;

        chi2_lct_odd[i] = -99999;
        chi2_lct_even[i] = -99999;

        passdphi_odd[i] = 0;
        passdphi_even[i] = 0;

        perp_lct_odd[i] = -1;
        perp_lct_even[i] = -1;

        quality_clct_odd[i] = -1;
        quality_clct_even[i] = -1;
        quality_alct_odd[i] = -1;
        quality_alct_even[i] = -1;
        quality_lct_odd[i] = -1;
        quality_lct_even[i] = -1;

        bx_clct_odd[i] = -9;
        bx_clct_even[i] = -9;
        bx_alct_odd[i] = -9;
        bx_alct_even[i] = -9;

        lct_type[i] = -1;

        dslope_clct_odd[i] = -9;
        dslope_clct_even[i] = -9;

        slope_clct_odd[i] = -9;
        slope_clct_even[i] = -9;

        fslope_clct_odd[i] = -9;
        fslope_clct_even[i] = -9;

        pattern_clct_odd[i] = -9;
        pattern_clct_even[i] = -9;
      }
    };

    void clear() {
      alct_bx->clear();
      alct_wg->clear();
      alct_isodd->clear();
      alct_region->clear();
      alct_station->clear();
      alct_ring->clear();
      alct_chamber->clear();
      alct_quality->clear();
      alct_tpid->clear();

      clct_bx->clear();
      clct_hs->clear();
      clct_qs->clear();
      clct_es->clear();
      clct_isodd->clear();
      clct_region->clear();
      clct_station->clear();
      clct_ring->clear();
      clct_chamber->clear();
      clct_quality->clear();
      clct_pattern->clear();
      clct_tpid->clear();

      lct_bx->clear();
      lct_wg->clear();
      lct_hs->clear();
      lct_qs->clear();
      lct_es->clear();
      lct_isodd->clear();
      lct_region->clear();
      lct_station->clear();
      lct_ring->clear();
      lct_chamber->clear();
      lct_quality->clear();
      lct_pattern->clear();
      lct_tpid->clear();

      mplct_bx->clear();
      mplct_wg->clear();
      mplct_hs->clear();
      mplct_qs->clear();
      mplct_es->clear();
      mplct_isodd->clear();
      mplct_region->clear();
      mplct_station->clear();
      mplct_ring->clear();
      mplct_chamber->clear();
      mplct_quality->clear();
      mplct_pattern->clear();
      mplct_tpid->clear();
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
      t->Branch("mplct_tpid", &mplct_tpid);

      t->Branch("has_clct_odd", has_clct_odd, "has_clct_odd[11]/O");
      t->Branch("has_alct_odd", has_alct_odd, "has_alct_odd[11]/O");
      t->Branch("has_lct_odd", has_lct_odd, "has_lct_odd[11]/O");

      t->Branch("has_clct_even", has_clct_even, "has_clct_even[11]/O");
      t->Branch("has_alct_even", has_alct_even, "has_alct_even[11]/O");
      t->Branch("has_lct_even", has_lct_even, "has_lct_even[11]/O");


      t->Branch("bx_clct_odd", bx_clct_odd, "bx_clct_odd[11]/I");
      t->Branch("bx_clct_even", bx_clct_even, "bx_clct_even[11]/I");

      t->Branch("pattern_clct_odd", pattern_clct_odd, "pattern_clct_odd[11]/I");
      t->Branch("pattern_clct_even", pattern_clct_even, "pattern_clct_even[11]/I");

      t->Branch("quality_clct_odd", quality_clct_odd, "quality_clct_odd[11]/I");
      t->Branch("quality_clct_even", quality_clct_even, "quality_clct_even[11]/I");
      t->Branch("quality_alct_odd", quality_alct_odd, "quality_alct_odd[11]/I");
      t->Branch("quality_alct_even", quality_alct_even, "quality_alct_even[11]/I");
      t->Branch("quality_lct_odd", quality_lct_odd, "quality_lct_odd[11]/I");
      t->Branch("quality_lct_even", quality_lct_even, "quality_lct_even[11]/I");

      t->Branch("bx_alct_odd", bx_alct_odd, "bx_alct_odd[11]/I");
      t->Branch("bx_alct_even", bx_alct_even, "bx_alct_even[11]/I");

      t->Branch("chamber_lct_odd", chamber_lct_odd, "chamber_lct_odd[11]/I");
      t->Branch("chamber_lct_even", chamber_lct_even, "chamber_lct_even[11]/I");

      t->Branch("bend_lct_odd", bend_lct_odd, "bend_lct_odd[11]/I");
      t->Branch("bend_lct_even", bend_lct_even, "bend_lct_even[11]/I");

      t->Branch("bx_lct_odd", bx_lct_odd, "bx_lct_odd[11]/I");
      t->Branch("bx_lct_even", bx_lct_even, "bx_lct_even[11]/I");

      t->Branch("hs_lct_odd", hs_lct_odd, "hs_lct_odd[11]/I");
      t->Branch("hs_lct_even", hs_lct_even, "hs_lct_even[11]/I");

      t->Branch("qs_lct_odd", qs_lct_odd, "qs_lct_odd[11]/I");
      t->Branch("qs_lct_even", qs_lct_even, "qs_lct_even[11]/I");

      t->Branch("es_lct_odd", es_lct_odd, "es_lct_odd[11]/I");
      t->Branch("es_lct_even", es_lct_even, "es_lct_even[11]/I");

      t->Branch("hs_clct_odd", hs_clct_odd, "hs_clct_odd[11]/I");
      t->Branch("hs_clct_even", hs_clct_even, "hs_clct_even[11]/I");

      t->Branch("qs_clct_odd", qs_clct_odd, "qs_clct_odd[11]/I");
      t->Branch("qs_clct_even", qs_clct_even, "qs_clct_even[11]/I");

      t->Branch("es_clct_odd", es_clct_odd, "es_clct_odd[11]/I");
      t->Branch("es_clct_even", es_clct_even, "es_clct_even[11]/I");

      t->Branch("ffhs_clct_odd", ffhs_clct_odd, "ffhs_clct_odd[11]/F");
      t->Branch("ffhs_clct_even", ffhs_clct_even, "ffhs_clct_even[11]/F");

      t->Branch("fhs_clct_odd", fhs_clct_odd, "fhs_clct_odd[11]/F");
      t->Branch("fhs_clct_even", fhs_clct_even, "fhs_clct_even[11]/F");

      t->Branch("fqs_clct_odd", fqs_clct_odd, "fqs_clct_odd[11]/F");
      t->Branch("fqs_clct_even", fqs_clct_even, "fqs_clct_even[11]/F");

      t->Branch("fes_clct_odd", fes_clct_odd, "fes_clct_odd[11]/F");
      t->Branch("fes_clct_even", fes_clct_even, "fes_clct_even[11]/F");

      t->Branch("delta_ffhs_clct_odd", delta_ffhs_clct_odd, "delta_ffhs_clct_odd[11]/F");
      t->Branch("delta_ffhs_clct_even", delta_ffhs_clct_even, "delta_ffhs_clct_even[11]/F");

      t->Branch("delta_fhs_clct_odd", delta_fhs_clct_odd, "delta_fhs_clct_odd[11]/F");
      t->Branch("delta_fhs_clct_even", delta_fhs_clct_even, "delta_fhs_clct_even[11]/F");

      t->Branch("delta_fqs_clct_odd", delta_fqs_clct_odd, "delta_fqs_clct_odd[11]/F");
      t->Branch("delta_fqs_clct_even", delta_fqs_clct_even, "delta_fqs_clct_even[11]/F");

      t->Branch("delta_fes_clct_odd", delta_fes_clct_odd, "delta_fes_clct_odd[11]/F");
      t->Branch("delta_fes_clct_even", delta_fes_clct_even, "delta_fes_clct_even[11]/F");

      t->Branch("wg_alct_odd", wg_alct_odd, "wg_alct_odd[11]/I");
      t->Branch("wg_alct_even", wg_alct_even, "wg_alct_even[11]/I");

      t->Branch("wg_lct_odd", wg_lct_odd, "wg_lct_odd[11]/I");
      t->Branch("wg_lct_even", wg_lct_even, "wg_lct_even[11]/I");

      t->Branch("perp_lct_odd", perp_lct_odd, "perp_lct_odd[11]/F");
      t->Branch("perp_lct_even", perp_lct_even, "perp_lct_even[11]/F");

      t->Branch("eta_lct_odd", eta_lct_odd, "eta_lct_odd[11]/F");
      t->Branch("eta_lct_even", eta_lct_even, "eta_lct_even[11]/F");

      t->Branch("phi_lct_odd", phi_lct_odd, "phi_lct_odd[11]/F");
      t->Branch("phi_lct_even", phi_lct_even, "phi_lct_even[11]/F");

      t->Branch("dphi_lct_odd", dphi_lct_odd, "dphi_lct_odd[11]/F");
      t->Branch("dphi_lct_even", dphi_lct_even, "dphi_lct_even[11]/F");

      t->Branch("chi2_lct_odd", chi2_lct_odd, "chi2_lct_odd[11]/F");
      t->Branch("chi2_lct_even", chi2_lct_even, "chi2_lct_even[11]/F");

      t->Branch("passdphi_odd", passdphi_odd, "passdphi_odd[11]/F");
      t->Branch("passdphi_even", passdphi_even, "passdphi_even[11]/F");

      t->Branch("lct_type", lct_type, "lct_type[11]/I");

      t->Branch("dslope_clct_odd", dslope_clct_odd, "dslope_clct_odd[11]/F");
      t->Branch("dslope_clct_even", dslope_clct_even, "dslope_clct_even[11]/F");

      t->Branch("slope_clct_odd", slope_clct_odd, "slope_clct_odd[11]/F");
      t->Branch("slope_clct_even", slope_clct_even, "slope_clct_even[11]/F");

      t->Branch("fslope_clct_odd", fslope_clct_odd, "fslope_clct_odd[11]/F");
      t->Branch("fslope_clct_even", fslope_clct_even, "fslope_clct_even[11]/F");
    }
  };
}  // namespace

#endif
