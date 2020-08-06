import os

from resolution.GEMStub import *
from resolution.CSCStub import *

## need to create directory structure - assume it does not exist yet
paths = [
    "plots",
    "plots/resolution",
    "plots/resolution/GEMStub",
    "plots/resolution/CSCStub",
]

for p in paths:
    if not os.path.exists(p):
        os.mkdir(p)

def makeResolutionPlots(plotter):
    CSCStub(plotter)
    #GEMStub(plotter)
