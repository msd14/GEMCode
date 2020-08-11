# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2bis.py --filein file:step3.root --fileout file:step2bis.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic --step L1 --geometry DB:Extended --era Run3 --python_filename step2bis_L1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C10_cff import Phase2C10

process = cms.Process('ReL1',Phase2C10)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/FE5B56BE-AECE-4F45-B66F-E5FE1B8CC760.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/FA1B16F1-2326-4946-8C12-F141E3ED7722.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/F743F89A-904A-FB47-BD64-B1B5FECF5977.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/F4D40CBA-0F0A-AD44-9BEA-2923168A6888.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/F393F18A-1806-E347-9039-B92946FA2D6B.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/F1A6B357-5AC2-7A40-A6CF-24CFC09106C2.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/EFBCA1BA-B1C5-B746-B5C8-6432332C44E6.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/EB2F5ACB-30F6-B547-B170-1E93B2D1ABE8.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E9618BC1-82A3-AF4A-A974-6304CF3060A1.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E88883FC-B6C5-194B-88A0-16EB8F3C3896.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E86D585E-E786-744D-AA1C-7833DD36DC2B.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E67758BE-6251-B94B-ABB0-C4ED510891CD.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E1175AA8-9903-DE4D-9AA2-006F7012DCFB.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/E032530A-3081-6F42-B4DB-54DA530DDA8B.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/DF6FB165-CC74-E04C-A9DD-99F032CA68FC.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/DE3656AD-0C97-DB46-AC35-E59130069F27.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/DB806540-8009-E647-A497-B519FB682611.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/D73879DD-10E6-114F-8C52-E6E76AB3D213.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/D3C14F58-3D45-714B-8B6F-14FE7C2F7E5D.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/CD67BEFA-A3DA-8742-B7F7-35511F2078D5.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/C9947B62-11D9-F847-AEFA-15FDA7AAD4F8.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/C736391E-7C15-6240-8ECD-9D6520B443E6.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/BD4A10A2-7862-F542-9A15-AE3A4C4EDA70.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/B74F3827-AE2B-7E46-BC7D-DE7C81F9AED8.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/B64757F0-6BD4-1D4D-B1B2-5B8166793F0A.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/B47A6516-D815-844A-A1A9-F16082CB8105.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/B109E2A8-1E86-454B-B002-A47E853CDC2F.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/AEB1CEDE-4046-4446-86AC-94D3D4D10786.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A8D7A4C6-18B0-6C4E-B4BD-9BB5E0F8BFA7.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A7BAC248-6275-3848-9D6F-34DC9E20E74C.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A76E8B27-402B-A644-8203-094A1678E8D7.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A3FCA308-32A8-5948-AFD0-09DBE0FDB4F3.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A0B720AB-12B6-3746-A744-AD53FBE3D456.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/A06B0209-9128-7C4D-9F33-1DBE85F433B7.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/9F794253-B926-3B40-B5BA-573333ABA8DE.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/9E67504F-CA78-7541-B9F4-9DB685C1E87B.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/9B04930E-3BC3-C649-8A42-46AB42A25A6E.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/96C5DEEF-8AC9-464B-91C8-B3EE430DBCC4.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/966C64FF-1E81-BC48-83A7-FBBA4185DFDB.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/962D4DF9-24C5-A44E-9470-8CEBE255EF05.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/92892DBA-F001-5643-B612-EC007F8D4E06.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/923FCCBC-82CB-904E-887C-8C7BC81CDFB9.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/8D4AEC8E-F4FE-9440-97E9-908C498C6786.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/8CFCEB08-B2A3-AE47-ACD5-501A5955D0EC.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/8CB20580-7DB2-4C47-A87E-B703AB5B0846.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/8B687F87-9F8E-684A-A323-B309EB251301.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/892C3AAA-7E95-9B4F-B2B3-8FE25B55C6B9.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/8424807B-751F-E645-B00F-62628442B1F1.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/7DB70325-3A48-3A4D-9296-A4959220D155.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/71999205-2C50-9D49-8540-180D3EA2D88C.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/6D18B217-AA27-BF4E-9716-0B37B9804052.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/6C07C7AB-6538-784D-9C34-FC16B38B9927.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/6A519924-DED5-2047-BE85-1254C09E8476.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/64EAF39C-6BE6-2741-8029-4192B9BF9FE4.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/5AA6A995-0F1B-9C43-8191-B31BDD36D459.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/5A3AE99F-D988-8247-8227-47D6D4ADD704.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/581B918F-DDF5-F24E-95B6-52A5AAD6E310.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/5653C85F-AB24-EB49-99E5-3E6000E9474F.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/54BDAF02-B96F-904F-B751-77F2EBB72578.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/543F9F9E-2DD9-D849-83E8-9399A1558988.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/5037AF8F-9D98-0B4C-BD8E-21E286B4266F.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/4F2D6013-CE26-8742-ACB7-4D23AAB03934.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/4E237368-0524-6348-ABBC-AC10BECF48A2.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/476EB18E-FEA8-1A44-BF5B-F6F285253478.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/46DC105C-F8EE-6C40-8171-CBBAEFAAD830.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/45B8EED2-48BD-504C-8951-F85D749129F2.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/3AAD2FA3-22B9-764D-9DAF-2195DD2F8975.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/33CF6F03-3408-B34B-BB79-01D47BCED877.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/2E0F5C14-EFF6-9D4C-AEA8-B027C49FE0BF.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/2DA39EE9-1DDC-8B4A-9FD3-58D765ABC690.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/23057D38-26AD-B849-942B-4B2617232606.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/21F623D0-B5D9-CA40-8E59-2AA472F84815.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/2167ACCF-75D1-C04A-9480-95C6869C62C5.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/2131A721-AE66-6547-9B62-3B26BD3D5DCD.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/20148F2E-DBA0-A748-AFCB-2C0BD80E1E7A.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/1F345FFC-BB15-E84D-8227-FCBF4DB30654.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/1E5C150A-A14B-8545-95FF-A293A757864A.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/1B640F7A-1A0D-B445-9C66-BAD6EB1D5351.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/18B14BC8-A71F-F447-B9F3-93FE354DEA81.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/1785F909-B46B-4B43-9F72-4DB8FC9D49D4.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/15BBED38-8840-214F-9C7F-31D2F91484CA.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/1406224C-AEAB-884B-B23E-76671BDA0746.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/0F425345-33EB-1E41-B21D-F0B034BA6D61.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/0E025DDB-289E-A546-BCEB-FFFF8C147454.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/0B9A78A7-7574-6F48-83FF-1B6076862112.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/0A341DBF-A072-0A4D-85BD-4E1AC9459FFA.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/08B07345-E482-CD4C-91D0-40F3342D1B84.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/080A91EE-5B08-D64C-8BFC-C5BD844AC83A.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/043A1138-2438-8A47-9D36-AFFDE10C8451.root',
'/store/relval/CMSSW_11_0_0/RelValSingleMuFlatPt2To100/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/007E70B7-4A94-1941-9F1C-A7518E2E2492.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)


process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2bis.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-L1'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2bis_phase2_pu200.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

## keep all CSC trigger versions
process.FEVTDEBUGoutput.outputCommands.append('keep *_simCscTriggerPrimitiveDigis*_*_*')
process.FEVTDEBUGoutput.outputCommands.append('keep *_simEmtfDigis_*_*')

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')
#process.GlobalTag.globaltag = '110X_mcRun4_realistic_v2'

from GEMCode.GEMValidation.cscTriggerCustoms import addCSCTriggerRun3
process = addCSCTriggerRun3(process)

process.SimL1Emulator = cms.Sequence(
    #process.simMuonGEMPadDigis *
    # process.simMuonGEMPadDigiClusters *
    process.simCscTriggerPrimitiveDigis
    * process.simCscTriggerPrimitiveDigisRun3
    * process.simCscTriggerPrimitiveDigisRun3CCLUT
    * process.simEmtfDigis
)
#process.simMuonGEMPadDigis.InputCollection = "muonGEMDigis"

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(#process.raw2digi_step,
    process.L1simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

from GEMCode.GEMValidation.sampleProductionCustoms import dropNonMuonCollections
process = dropNonMuonCollections(process)
