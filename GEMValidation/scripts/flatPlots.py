import awkward1 as ak
import uproot4
import matplotlib.pyplot as plt
from cuts_v2 import *
from objects import getObjects, id_to_station

mycache = {}

tree = uproot4.open("out_ana_phase2.ntuple.root")["MuonNtuplizer"]["FlatTree"].arrays(array_cache=mycache)

csc_clct, csc_alct, csc_lct = getObjects(tree)

## rates for each station
for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_alct.bx==3) &
            (csc_alct.station == station) &
            (csc_alct.ring == ring))
    ak.to_list(cuts)
    print("number of csc_alct for CSC station = %d, ring = %d and bunch crossing is 3 is :"%(station, ring), ak.sum(cuts))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_clct.bx==7) &
            (csc_clct.station == station) &
            (csc_clct.ring == ring))
    ak.to_list(cuts)
    print("number of csc_clct for CSC station = %d, ring = %d and bunch crossing is 6 is :"%(station, ring), ak.sum(cuts))


for ids in range(0,9):
    station = id_to_station[ids][0]
    ring = id_to_station[ids][1]
    cuts = ((csc_lct.bx==8) &
            (csc_lct.station == station) &
            (csc_lct.ring == ring))
    ak.to_list(cuts)
    print("number of csc_lct for CSC station = %d, ring = %d and bunch crossing is 6 is :"%(station, ring), ak.sum(cuts))
