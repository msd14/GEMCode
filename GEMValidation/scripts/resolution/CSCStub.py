## position resolution

## bending resolution CSC-only

## bending resolution GEM-CSC

from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen

from helpers.cuts import *
from helpers.Helpers import *
from helpers.stations import *
from style.tdrstyle import *
import style.CMS_lumi as CMS_lumi
from style.canvas import newCanvas

topTitle = ""
xTitle = "Strip_{L1T} - Strip_{SIM}"
yTitle = "Normalized"
subdirectory = "resolution/CSCStub/"
title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

setTDRStyle()

iPeriod = 0
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12

def CSCCLCTPos1(plotter):

    for st in range(0,len(cscStations)):

        h_bins = "(100,-1.5,1.5)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(0.08)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = delta_fhs_clct(st)
        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)

        h1.Scale(1./h1.GetEntries())
        #base.SetMaximum(h3.GetBinContent(h3.GetMaximumBin()) * 1.1)
        h1.Draw("histsame")

        leg = TLegend(0.15,0.6,.45,0.9, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "1/2 strip","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sRes_CSCCLCT_pos1_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del base, leg, csc, h1, c


def CSCCLCTPos(plotter):

    for st in range(0,len(cscStations)):

        h_bins = "(100,-1.5,1.5)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(0.08)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = delta_fhs_clct(st)
        toPlot2 = delta_fqs_clct(st)
        toPlot3 = delta_fes_clct(st)

        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)
        h2 = draw_1D(plotter.tree, title, h_bins, toPlot2, "", "same", kGreen+2)
        h3 = draw_1D(plotter.tree, title, h_bins, toPlot3, "", "same", kRed+1)

        #print h1.GetBinContent(h1.GetMaximumBin()), h1.GetMaximumBin(), h1.GetEntries()
        #print h2.GetBinContent(h2.GetMaximumBin()), h2.GetMaximumBin(), h2.GetEntries()
        #print h3.GetBinContent(h3.GetMaximumBin()), h3.GetMaximumBin(), h3.GetEntries()

        h1.Scale(1./h1.GetEntries())
        h2.Scale(1./h2.GetEntries())
        h3.Scale(1./h3.GetEntries())
        base.SetMaximum(h3.GetBinContent(h3.GetMaximumBin()) * 1.1)
        h1.Draw("histsame")
        h2.Draw("histsame")
        h3.Draw("histsame")

        leg = TLegend(0.15,0.6,.45,0.9, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "1/2 strip","pl")
        leg.AddEntry(h2, "1/4 strip","pl")
        leg.AddEntry(h3, "1/8 strip","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sRes_CSCCLCT_pos_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del base, h2, leg, csc, h1, h3, c


def CSCCLCTBend(plotter):

    xTitle = "Slope_{L1T} - Slope_{SIM} [Strips/layer]"
    yTitle = "Normalized"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(100,-2.,2.)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(0.08)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = delta_bend_clct(st)

        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)

        h1.Scale(1./h1.GetEntries())
        h1.Draw("histsame")

        leg = TLegend(0.15,0.6,.45,0.9, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "CLCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sRes_CSCCLCT_bend_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h1


def CSCStub(plotter):
    CSCCLCTPos(plotter)
    CSCCLCTPos1(plotter)
    CSCCLCTBend(plotter)
