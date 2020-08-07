from ROOT import *
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
#ROOT.gErrorIgnoreLevel=1001

gemstations = [ [1,1], [2,1]]
gemlabel = {
    1 : {
        1 : {
            1 : ["pGE11","GE+1/1"]
        },
        2 : {
            1 : ["pGE21","GE+2/1"]
        },
    },
    2 : {
        1 : {
            1 : ["mGE11","GE-1/1"],
        },
        2 : {
            1 : ["mGE21","GE-2/1"]
        },
    },
    }

gROOT.SetBatch(1)
gStyle.SetStatStyle(0)
gStyle.SetOptStat("nemrou")

ch = TChain("Events")
fc = TFileCollection("dum")
fc.Add("step2bis_pu200.root")
#"/eos/uscms/store/user/dildick/RelValSingleMuFlatPt2To100/L1GEM_SingleMuPU200_11_1_X_v8_copadbx_revertclct_3layerclct/200731_202710/0000/*.root")
fc.Print()
ch.AddFileInfoList(fc.GetList())
#file = TFile("step2bis_pu200.root")
outputdirectory = "LCT_comparison_RelValSingleMuFlatPt2To100_PU200_CMSSW_11_2_X_20200806/"
tree = ch#.Get("Events")

gempaddigi = {
    0 : ["pad_", "pad",384,0,384],
    1 : ["bx_", "bx",16,-8,8],
    }

colors = [kRed, kBlue, kBlack, kGreen+2, kOrange+2, kPink+1, 28]

def yRanges(nCollections):
    yrange = 1.0-0.1
    ydelta = yrange/nCollections
    ymins = []
    ymaxs = []
    for d in range(0,nCollections):
        ymins.append(1.0-(1+d)*ydelta)
        ymaxs.append(1.0-d*ydelta)
    return ymins, ymaxs


def compareLCTs(collections, endcap, station, ring, variable, bxpar):

    nCollections = len(collections)
    ymins, ymaxs = yRanges(nCollections)

    var = gemcorrelatedlctdigi[variable][0]
    varstr = gemcorrelatedlctdigi[variable][1]
    varnbin = gemcorrelatedlctdigi[variable][2]
    varminbin = gemcorrelatedlctdigi[variable][3]
    varmaxbin = gemcorrelatedlctdigi[variable][4]

    extraCut = "pad >= 0"

    c = TCanvas("c","c",800,800)
    c.cd()

    def addCollection(collection, index):
        collection_substring = collection[len('GEMDetIdGEMPadDigiMuonDigiCollection_'):] + "_" + varstr + "_" + gemlabel[endcap][station][ring][0]
        hist = TH1D(collection_substring,"GEMCorrelatedLCTDigi " + varstr + " " +
                   gemlabel[endcap][station][ring][1] + "; " + varstr + "; Entries",varnbin,varminbin,varmaxbin)

        tree.Draw(collection + ".obj.data_.second." + var + ">>" + hist.GetName(),
                  collection + ".obj.data_.first.endcap() == %d && "%(endcap) +
                  collection + ".obj.data_.first.station()==%d && "%(station) +
                  collection + ".obj.data_.second." + extraCut)

        hist.SetLineColor(colors[index])

        if index==0:
            hist.Draw()
        else:
            hist.Draw("sames")
        gPad.Update()
        hist_st = hist.FindObject("stats");
        hist_st.SetY1NDC(ymins[index]);
        hist_st.SetY2NDC(ymaxs[index])
        hist_st.SetTextColor(colors[index]);
        SetOwnership(hist, False)
        SetOwnership(hist_st, False)
        return hist, hist_st

    def plotCollection(hist, stats, index):
        if index==0: hist.Draw()
        else:        hist.Draw("sames")
        stats.Draw("same")

    ## add the histograms and the stat boxes
    hists = []
    stats = []
    for i in range(0,nCollections):
        hist, stat = addCollection(collections[i],i)
        hists.append(hist)
        stats.append(stat)

    for i in range(0,nCollections):
        plotCollection(hists[i], stats[i], i)

    c.SaveAs(outputdirectory  + "comparison_lct_" + varstr + "_" + gemlabel[endcap][station][ring][0] + ".png")

def compareLCTsAll(collections):
    for i in range(0,12):
        for p in gemstations:
            compareLCTs(collections,1,p[0],p[1],i,-1)
        for p in gemstations:
            compareLCTs(collections,2,p[0],p[1],i,-1)

gem_collections = [
    'GEMDetIdGEMPadDigiMuonDigiCollection_simMuonGEMPadDigis__ReL1',
    'GEMDetIdGEMPadDigiMuonDigiCollection_simMuonGEMPadDigis__HLT',
]

compareLCTsAll(lct_collections)
