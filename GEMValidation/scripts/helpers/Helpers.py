from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, TLatex, TEfficiency, SetOwnership
from cuts import *

#_______________________________________________________________________________
def drawCSCLabel(title, x=0.17, y=0.35, font_size=0.):
    tex = TLatex(x, y,title)
    if font_size > 0.:
      tex.SetTextSize(font_size)
      tex.SetTextSize(0.05)
      tex.SetNDC()
      tex.Draw()
      return tex


#_______________________________________________________________________________
def drawEtaLabel(minEta, maxEta, x=0.17, y=0.35, font_size=0.):
    tex = TLatex(x, y,"%.2f < |#eta| < %.2f"%(minEta,maxEta))
    if font_size > 0.:
      tex.SetTextSize(font_size)
      tex.SetTextSize(0.05)
      tex.SetNDC()
      tex.Draw()
      return tex


#_______________________________________________________________________________
def drawPuLabel(pu, x=0.17, y=0.35, font_size=0.):
    tex = TLatex(x, y,"<PU> = %d"%(pu))
    if font_size > 0.:
      tex.SetTextSize(font_size)
      tex.SetTextSize(0.05)
      tex.SetNDC()
      tex.Draw()
      return tex


#_______________________________________________________________________________
def draw_1D(t, title, h_bins, to_draw, extra_cut, opt = "",
             color = kBlue, marker_st = 20):

    nBins  = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    num = TH1F("num", "", nBins, minBin, maxBin)
    t.Draw(to_draw + ">>num", extra_cut, "goff")

    num.SetLineWidth(2)
    num.SetLineColor(color)
    num.SetMarkerStyle(marker_st)
    num.SetMarkerColor(color)
    num.SetMarkerSize(.5)

    SetOwnership(num, False)
    return num


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
