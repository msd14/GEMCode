from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen, kBlack

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
    xTitle = "Generator muon p_{T} [GeV]"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genpt
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(20,0,100)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetGridx(1)
    c.SetGridy(2)
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(1.0)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    denom_cut = AND(ok_eta(1.2, 2.4), ok_2_csc_lcts())

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, denom_cut, ok_emtf(20), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, denom_cut, ok_emtf(15), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, denom_cut, ok_emtf(10), "same", kGreen+1)
    h4 = draw_geff(plotter.tree, title, h_bins, toPlot, denom_cut, ok_emtf(5), "same", kOrange+1)
    h5 = draw_geff(plotter.tree, title, h_bins, toPlot, denom_cut, ok_emtf(0), "same", kBlack)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.AddEntry(h2, "EMTF, p_{T} > 15 GeV","l")
    leg.AddEntry(h3, "EMTF, p_{T} > 10 GeV","l")
    leg.AddEntry(h4, "EMTF, p_{T} > 5 GeV","l")
    leg.AddEntry(h5, "EMTF, p_{T} > 0 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF_pt_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFEta(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "Generator muon |#eta|"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(%s)"%(geneta)
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(20,1.2,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetGridx(1)
    c.SetGridy(2)
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(1.0)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    denom_cut = AND(ok_eta(1.2, 2.4), ok_2_csc_lcts())

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>20")), ok_emtf(20), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>15")), ok_emtf(15), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>10")), ok_emtf(10), "same", kGreen+1)
    h4 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>5")), ok_emtf(5), "same", kOrange+1)
    h5 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>3")), ok_emtf(0), "same", kBlack)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.AddEntry(h2, "EMTF, p_{T} > 15 GeV","l")
    leg.AddEntry(h3, "EMTF, p_{T} > 10 GeV","l")
    leg.AddEntry(h4, "EMTF, p_{T} > 5 GeV","l")
    leg.AddEntry(h5, "EMTF, p_{T} > 0 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF_eta_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFEta2(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "Generator muon |#eta|"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = geneta
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(20,-2.4,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetGridx(1)
    c.SetGridy(2)
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(1.0)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    denom_cut = AND(ok_eta(1.2, 2.4), ok_2_csc_lcts())

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>20")), ok_emtf(20), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>15")), ok_emtf(15), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>10")), ok_emtf(10), "same", kGreen+1)
    h4 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>5")), ok_emtf(5), "same", kOrange+1)
    h5 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>3")), ok_emtf(0), "same", kBlack)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.AddEntry(h2, "EMTF, p_{T} > 15 GeV","l")
    leg.AddEntry(h3, "EMTF, p_{T} > 10 GeV","l")
    leg.AddEntry(h4, "EMTF, p_{T} > 5 GeV","l")
    leg.AddEntry(h5, "EMTF, p_{T} > 0 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF2_eta_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def EMTFPhi(plotter):

    ## variables for the plot
    topTitle = ""
    xTitle = "Generator muon #phi"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genphi
    subdirectory = "efficiency/L1Mu/"

    h_bins = "(20,-3.2,3.2)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetGridx(1)
    c.SetGridy(2)
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(1.0)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    denom_cut = AND(ok_eta(1.2, 2.4), ok_2_csc_lcts())

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>20")), ok_emtf(20), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>15")), ok_emtf(15), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>10")), ok_emtf(10), "same", kGreen+1)
    h4 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>5")), ok_emtf(5), "same", kOrange+1)
    h5 = draw_geff(plotter.tree, title, h_bins, toPlot, AND(denom_cut, TCut("GenParticle.pt>3")), ok_emtf(0), "same", kBlack)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "EMTF, p_{T} > 20 GeV","l")
    leg.AddEntry(h2, "EMTF, p_{T} > 15 GeV","l")
    leg.AddEntry(h3, "EMTF, p_{T} > 10 GeV","l")
    leg.AddEntry(h4, "EMTF, p_{T} > 5 GeV","l")
    leg.AddEntry(h5, "EMTF, p_{T} > 0 GeV","l")
    leg.Draw("same");

    c.Print("%sEff_EMTF_phi_Pt20_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg



def L1Mu(plotter):
    EMTFPt(plotter)
    EMTFEta(plotter)
    EMTFEta2(plotter)
    EMTFPhi(plotter)
