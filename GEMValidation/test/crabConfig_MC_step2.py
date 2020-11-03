# -*- coding: utf-8 -*-
#CRAB configuration to do processing of Monte Carlo. Inputs a dataset from previous step of processing chain.
#Note: Filenames in psetName must match filenames of input dataset.

from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Mu_FlatPt1to1000-pythia8-gun_MiniAOD-NoPU_110X_DIGI_L1-Run3CCLUT'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000   #Use approx (1+1*ncores)GB

#4M OneOverPt 1-10GeV NoPU
#config.Data.inputDataset = '/SingleMu_Run3_Pt1to10OneOverPt_noPU/madecaro-CRAB3_SingleMu_Run3_Pt1to10OneOverPt_noPU-2caf3e30aab5fb9c0e61f8f435dd00c9/USER'

#15M FlatPt 1GeV - 1TeV NoPU
config.Data.inputDataset = '/Mu_FlatPt1to1000-pythia8-gun/Run3Winter20DRMiniAOD-NoPU_110X_mcRun3_2021_realistic_v6-v3/GEN-SIM-RAW'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 570 #~12M events (1.7TB)
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_Mu_FlatPt1to1000-pythia8-gun_MiniAOD-NoPU_110X__DIGI_L1-Run3CCLUT'

config.Site.storageSite = 'T3_US_FNALLPC'

 
