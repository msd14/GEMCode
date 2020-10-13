import uproot
import matplotlib.pyplot as plt
from cuts_v2 import *

file = uproot.open("out_ana_phase2.ntuple.root")
print(file.keys())

events = file["MuonNtuplizer"]["FlatTree"]
sim_pt = events.array("sim_pt").flatten()
sim_charge = events.array("sim_charge").flatten()
sim_has_gem_pad = has_gem_pad(events)
sim_has_gem_csc = has_csc_lct(events)

## stuff for rates
csc_clct_bx = events.array("csc_clct_bx").flatten()
csc_alct_bx = events.array("csc_alct_bx").flatten()
csc_clct_bx_me11 = events.array("csc_clct_bx")

#print(len(csc_clct_bx[csc_clct_bx == 6csc_clct_bx == 7]))
print(len(csc_clct_bx[csc_clct_bx == 6]))
print(len(csc_clct_bx[csc_clct_bx == 7]))
print(len(csc_clct_bx[csc_clct_bx == 8]))
print(len(csc_clct_bx))

print(len(csc_alct_bx[csc_alct_bx == 2]))
print(len(csc_alct_bx[csc_alct_bx == 3]))
print(len(csc_alct_bx[csc_alct_bx == 4]))
print(len(csc_alct_bx))
