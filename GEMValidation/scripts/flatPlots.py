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

print(sim_has_gem_pad)
print(sim_has_gem_csc)
print(sim_has_gem_csc * sim_has_gem_pad)
print(sim_pt * sim_has_gem_csc * sim_has_gem_pad)
print(sim_pt)


#print(data)
'''
```
In [47]: ak.num(has_gem1) > 0
Out[47]: <Array [True, True, True, ... False, False] type='1722 * bool'>

In [48]: has_gem1 = ak.flatten(has_gem, axis=1)
``
'''
