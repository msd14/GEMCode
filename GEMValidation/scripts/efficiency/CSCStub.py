from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen

from helpers.cuts import *
from helpers.Helpers import *
from helpers.stations import *
from style.tdrstyle import *
import style.CMS_lumi as CMS_lumi
from style.canvas import newCanvas

topTitle = ""
xTitle = "Generated muon |#eta|"
yTitle = "Efficiency"
subdirectory = "efficiency/CSCStub/"
title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

setTDRStyle()

iPeriod = 0
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12

def CSCALCT(plotter):

    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_alct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "ALCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCALCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h1, leg, csc


def CSCCLCT(plotter):

    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct(st), "same",kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "CLCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc


def CSCLCT(plotter):

    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_lct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2


def GEMCSCLCT(plotter):

    toPlot = "TMath::Abs(eta)"

    for st in [0,5]:

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        gemst = 1
        if st==5:
            gemst = 2

        ok_alct_clct = ok_csc_clct(st) and ok_csc_alct(st) and ok_gem_pad(gemst)
        ok_alct_gem = ok_csc_alct(st) and ok_gem_copad(gemst)
        ok_clct_gem = ok_csc_clct(st) and ok_gem_copad(gemst)

        ok_any_combination = ok_alct_clct or ok_alct_gem or ok_clct_gem

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_any_combination, "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_GEMCSCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2


def MultipleCSCLCTPt(plotter):

    xTitle = "Generated muon p_{T} [GeV]"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genpt

    h_bins = "(20,0,100)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.05)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_pt_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def MultipleCSCLCTEta(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    h_bins = "(20,1.2,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_eta_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg

def MultipleCSCLCTPhi(plotter):

    ## variables for the plot
    xTitle = "Generated muon #phi"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genphi

    h_bins = "(20,-3.2,3.2)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.2,0.2,.5,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_phi_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def CSCStub(plotter):
    CSCALCT(plotter)
    CSCCLCT(plotter)
    CSCLCT(plotter)
    GEMCSCLCT(plotter)

    MultipleCSCLCTPt(plotter)
    MultipleCSCLCTEta(plotter)
    MultipleCSCLCTPhi(plotter)
