import os

from resolution.GEMStub import *
from resolution.CSCStub import *

## need to create directory structure - assume it does not exist yet
def makeDir(plotter):
    base = plotter.baseDir + "/"
    analyzer = plotter.analyzer
    paths = [
        base,
        base + analyzer,
        base + analyzer + "/resolution",
        base + analyzer + "/resolution/GEMStub",
        base + analyzer + "/resolution/CSCStub",
    ]
    for p in paths:
        if not os.path.exists(p):
            os.mkdir(p)

def makeResolutionPlots(plotter):
    makeDir(plotter)
    CSCStub(plotter)
    GEMStub(plotter)

def makeResolutionComparisonPlots(plotter, plotter2):
    CSCPosResolutionComparison(plotter, plotter2)
    CSCBendResolutionComparison(plotter, plotter2)
