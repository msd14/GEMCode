from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen

from helpers.cuts import *
from helpers.Helpers import *
from helpers.stations import *

gStyle.SetTitleStyle(0)
gStyle.SetTitleAlign(13) ##coord in top left
gStyle.SetTitleX(0.)
gStyle.SetTitleY(1.)
gStyle.SetTitleW(1)
gStyle.SetTitleH(0.058)
gStyle.SetTitleBorderSize(0)

gStyle.SetPadLeftMargin(0.126)
gStyle.SetPadRightMargin(0.04)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadBottomMargin(0.13)
gStyle.SetOptStat(0)
gStyle.SetMarkerStyle(1)

def EMTFPt(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "True muon p_{T} [GeV]"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "pt"
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(50,0,100)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(0.9, 2.4), ok_emtf(20), "same", kBlue)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF_pt_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFEta(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "True muon |#eta|"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(30,0.9,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(0.9, 2.4), ok_emtf(20), "same", kBlue)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF_eta_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFEta2(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "True muon |#eta|"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "eta"
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(50,-2.4,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(0.9, 2.4), ok_emtf(20), "same", kBlue)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF2_eta_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFPhi(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "True muon #phi"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "phi"
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(64,-3.2,3.2)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(0.9, 2.4), ok_emtf(20), "same", kBlue)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF2_phi_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg



def L1Mu(plotter):
    EMTFPt(plotter)
    EMTFEta(plotter)
    EMTFEta2(plotter)
    EMTFPhi(plotter)
