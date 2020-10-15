import awkward1 as ak
import uproot4
import matplotlib.pyplot as plt
from cuts_v2 import *
from objects import getObjects, id_to_station

mycache = {}

tree = uproot4.open("out_ana_phase2.ntuple.root")["MuonNtuplizer"]["FlatTree"].arrays(array_cache=mycache)

csc_clct, csc_alct, csc_lct, gem_cluster, emtftrack,l1mu = getObjects(tree)

## number of events (get from tree)
numberOfTotalEvents = 18000.

## Number of bunches
numberOfBunches = 2760.

## LHC bunch frequency
lhcFrequency = 11.246

## Effective LHC rate
rate = numberOfBunches * lhcFrequency

## normalization
normalization = rate / numberOfTotalEvents

## Rates per chamber type
alct_trigger_rate = []
clct_trigger_rate = []
lct_trigger_rate = []
alct_daq_rate = []
clct_daq_rate = []
lct_daq_rate = []

gem_trigger_rate = []
gem_daq_rate = []

## trigger rates for each station
for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_alct.bx==3) &
            (csc_alct.station == station) &
            (csc_alct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("Trigger Rate for ALCT for CSC station = %d, ring = %d (BX3): %f kHz"%(station, ring, objectRate))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_clct.bx==7) &
            (csc_clct.station == station) &
            (csc_clct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("Trigger Rate for CLCT for CSC station = %d, ring = %d (BX7): %f kHz"%(station, ring, objectRate))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_lct.bx==8) &
            (csc_lct.station == station) &
            (csc_lct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("Trigger Rate for LCT for CSC station = %d, ring = %d (BX8): %f kHz"%(station, ring, objectRate))


## DAQ rates!!!
for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_alct.bx==3 | csc_alct.bx==2 | csc_alct.bx==1 | csc_alct.bx==4 | csc_alct.bx==5) &
            (csc_alct.station == station) &
            (csc_alct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("DAQ Rate for ALCT for CSC station = %d, ring = %d: %f kHz"%(station, ring, objectRate))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_clct.bx==7 | csc_clct.bx==6 | csc_clct.bx==8 | csc_clct.bx==5 | csc_clct.bx==9 | csc_clct.bx==4 | csc_clct.bx==10) &
            (csc_clct.station == station) &
            (csc_clct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("DAQ Rate for CLCT for CSC station = %d, ring = %d: %f kHz"%(station, ring, objectRate))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_lct.bx==8 | csc_lct.bx==7 | csc_lct.bx==6 | csc_lct.bx==5 | csc_lct.bx==9 | csc_lct.bx==10 | csc_lct.bx==11) &
            (csc_lct.station == station) &
            (csc_lct.ring == ring))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("DAQ Rate for LCT for CSC station = %d, ring = %d: %f kHz"%(station, ring, objectRate))


## GEM cluster rates
for station in range(0,2):
    cuts = ((gem_cluster.bx == 0) &
            (gem_cluster.station == station) &
            (gem_cluster.ring == 1))
    ak.to_list(cuts)
    passEvents = ak.sum(cuts)
    objectRate = passEvents * normalization
    print("Trigger Cluster Rate for GEM station = %d, ring = %d: %f kHz"%(station, ring, objectRate))

"""
Plots needed
- alct rate per chamber type
- lct rate per chamber type
- anode/cathode pretrigger rate per chamber type
- alct rate per chamber
- lct rate per chamber

with/without CCLUT enabled

- Same plots for DAQ rates

- Same plots for Run-3 and Phase-2 (PU200) with recent HGCal
"""
