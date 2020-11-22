# -*- coding: utf-8 -*-
#CRAB configuration to do processing of Monte Carlo. Inputs a dataset from previous step of processing chain.
#Note: Filenames in psetName must match filenames of input dataset.

from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMu_Run3_Pt1to50OneOverPt_noPU_10M'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC' #'Analysis' #(If youhave an input dataset)
config.JobType.psetName = 'SingleMu_GEN_SIM.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1
#config.JobType.maxMemoryMB = 3000   #Use approx (1+1*ncores)GB

config.Data.inputDBS = 'phys03'  #'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
config.Data.totalUnits = 10000000
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_SingleMu_Run3_Pt1to50OneOverPt_noPU_10M'
config.Data.outputPrimaryDataset = 'SingleMu_Run3_Pt1to50OneOverPt_noPU_10M'

config.Site.storageSite = 'T3_US_FNALLPC' 
