import os

from efficiency.CSCSimHit import *
from efficiency.CSCDigi import *
from efficiency.CSCStub import *

from efficiency.GEMSimHit import *
from efficiency.GEMDigi import *
from efficiency.GEMStub import *
from efficiency.GEMRecHit import *

from efficiency.L1Mu import *

## need to create directory structure - assume it does not exist yet
paths = [
    "plots",
    "plots/efficiency",
    "plots/efficiency/GEMSimHit",
    "plots/efficiency/GEMDigi",
    "plots/efficiency/GEMStub",
    "plots/efficiency/CSCSimHit",
    "plots/efficiency/CSCDigi",
    "plots/efficiency/CSCStub",
    "plots/efficiency/L1Mu",
]

for p in paths:
    if not os.path.exists(p):
        os.mkdir(p)

def makeEfficiencyPlots(plotter):
    CSCSimHit(plotter)
    CSCDigi(plotter)
    CSCStub(plotter)
    GEMSimHit(plotter)
    GEMDigi(plotter)
    GEMStub(plotter)
    L1Mu(plotter)
