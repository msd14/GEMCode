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
xTitle = "Resolution [strips]"
yTitle = "Entries"
subdirectory = "resolution/CSCStub/"
title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

setTDRStyle()

iPeriod = 0
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12

def CSCCLCT(plotter):

    for st in range(0,len(cscStations)):

        h_bins = "(100,-1.5,1.5)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(1000)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = "CSCStub.delta_fhs_clct_odd[%d]"%(st)
        toPlot2 = "CSCStub.delta_fqs_clct_odd[%d]"%(st)
        toPlot3 = "CSCStub.delta_fes_clct_odd[%d]"%(st)

        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)
        h2 = draw_1D(plotter.tree, title, h_bins, toPlot2, "", "same", kBlue)
        h3 = draw_1D(plotter.tree, title, h_bins, toPlot3, "", "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "1/2 strip","pl")
        leg.AddEntry(h2, "1/4 strip","pl")
        leg.AddEntry(h3, "1/8 strip","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sRes_CSCCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc, h1, h3


def CSCStub(plotter):
    CSCCLCT(plotter)
