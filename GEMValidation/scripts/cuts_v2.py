from ROOT import TH1F, TEfficiency, SetOwnership
import numpy as np
import awkward1 as ak

# functions operate on awkward arrays

def has_gem_pad(my_tree):
    return has_object(my_tree, "sim_id_gem_pad")

def has_gem_copad(my_tree):
    return has_object(my_tree, "sim_id_gem_copad")

def has_gem_cluster(my_tree):
    return has_object(my_tree, "sim_id_gem_cluster")

def has_csc_alct(my_tree):
    return has_object(my_tree, "sim_id_csc_alct")

def has_csc_clct(my_tree):
    return has_object(my_tree, "sim_id_csc_clct")

def has_csc_lct(my_tree):
    return has_object(my_tree, "sim_id_csc_lct")

def has_csc_mplct(my_tree):
    return has_object(my_tree, "sim_id_csc_mplct")

def has_emtf_track(my_tree):
    return has_object(my_tree, "sim_id_emtf_track")

def has_emtf_cand(my_tree):
    return has_object(my_tree, "sim_id_emtf_cand")

def has_l1mu(my_tree):
    return has_object(my_tree, "sim_id_l1mu")

def has_object(my_tree, objstring):
    obj_array = my_tree.array(objstring)
    obj_array = ak.flatten(obj_array, axis=1)
    has_obj = ak.num(obj_array) > 0
    return has_obj


## convert 1D array to histogram
def efficiency(denominator, num_cut, bins):
    numerator = denominator * num_cut
    th1_denom = TH1F("denom","denom", bins, np.array(denominator))
    th1_num = TH1F("num","num", bins, np.array(numerator))

#_______________________________________________________________________________
def draw_geff(t, title, h_bins, to_draw, den_cut, extra_num_cut,
              opt = "", color = kBlue, marker_st = 1, marker_sz = 1.):
    """Make an efficiency plot"""

    ## total numerator selection cut
    num_cut = AND(den_cut,extra_num_cut)

    ## PyROOT works a little different than ROOT when you are plotting
    ## histograms directly from tree. Hence, this work-around
    nBins  = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    num = TH1F("num", "", nBins, minBin, maxBin)
    den = TH1F("den", "", nBins, minBin, maxBin)

    t.Draw(to_draw + ">>num", num_cut, "goff")
    t.Draw(to_draw + ">>den", den_cut, "goff")

    debug = False
    if debug:
        print "Denominator cut", den_cut, den.GetEntries()
        print "Numerator cut", num_cut, num.GetEntries()

    ## check if the number of passed entries larger than total entries
    doConsistencyCheck = False
    if doConsistencyCheck:
        for i in range(0,nBins):
            print i, num.GetBinContent(i), den.GetBinContent(i)
            if num.GetBinContent(i) > den.GetBinContent(i):
                print ">>>Error: passed entries > total entries"

    eff = TEfficiency(num, den)

    ## plotting options
    if not "same" in opt:
        num.Reset()
        num.GetYaxis().SetRangeUser(0.0,1.1)
        num.SetStats(0)
        num.SetTitle(title)
        num.Draw()

    eff.SetLineWidth(2)
    eff.SetLineColor(color)
    eff.SetMarkerStyle(marker_st)
    eff.SetMarkerColor(color)
    eff.SetMarkerSize(marker_sz)
    eff.Draw(opt + " same")

    SetOwnership(eff, False)
    return eff
