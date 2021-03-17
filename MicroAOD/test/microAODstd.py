import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggMicroAOD")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff") # gives deprecated message in 80X but still runs
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 100000 ) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

import os
### 2017 and 2018 files from David
#process.GlobalTag = GlobalTag(process.GlobalTag, '', '')
#process.source = cms.Source("PoolSource",
#                             fileNames=cms.untracked.vstring("file:/eos/cms/store/user/dsperka/ALP/GluGluHGG_125_102X.root"))
#                             fileNames=cms.untracked.vstring("file:/eos/cms/store/user/dsperka/GluGluHGG_125_106X_2017.root"))

### 30 GeV ggH files
process.source = cms.Source("PoolSource",
                             fileNames=cms.untracked.vstring(
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_0257c5a6af737179fdcaf872fd09c9c2.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_8476291f2e7b97042e7c8cd1c962962e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_0306a147aa95e90d5cd0a5426e6778f5.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_89b709c47d6b8dc6270cf62dd70b07fc.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_05eb6a4c6724edcb3ff56574148a7501.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_8b89cd9375a807c43d2ba25f2485f86c.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_07bbd0dc3ecc5d34b1ea17899d14b789.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_93b666a00e072294e7db41e039a4b74b.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_083b76845a8f38fe8ca9a0f14093f243.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_961cf9d88776a237eb6aba56739fedde.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_09b6e128ce410b8fdc781e48cfbaafb9.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_98aff55442d02f19c38ef8ec54338935.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_17ed51fa8a630dddbae51e32e6b14399.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9925a05daed8b5f6ad026a7b2b9aafd4.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_1adf5b04b7694e51f2c263c75d995263.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9925bf7b8d936ec9ed1d51fb30ee723b.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_1fe1c96cb2c8009b2e2a51450e747843.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9a604ebd295b661a11bacf99d212c71e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_1ff404efe601428072ad25704885a275.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9e23fd4e51a64c2341ab5f46233b27b3.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_23af5cd7be415c9d7ed5ade04c154f66.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9f59ef6a030d9a02af5d5124358b3ba1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_24e997dd937f8f48eaff255cfd3322c8.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_9faff0987e27cd10ee642371e621dba2.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_27d5260890f645399ed5b50c876d2856.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_a4e92034917e229134962210f4278ebc.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_2dd275c4226f7fe0c86615ae3891a48b.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_a6e327887d9b8884e836ef7c9d4e621b.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_2e9536ab86bc1ae0b76fcea105f418c1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_aa81248b02c6b405e53d0297fa6ded9e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3756018c2cba9695710d00341a546456.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_b1b08fbe3f84c14c5f6d66fc4caf9d75.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_377cf52de6c21d89448b1df6cae92724.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_b1efefd9feba9a0319d45e9d26f579d9.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3bba2cd0c36dc27af00d32d5a09c93c8.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_b639a9bd0813acb22c69ce19a909c406.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3d74c2d4f34e003f0101d9352bf63fd3.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_bf277d0f0887319a302845ed7f03429f.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3dd9c2d883e627eb52aaadafdbfd9710.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_bf889b0a60e9f05a241fa7c3e9b4723f.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3e0fa8a278486323e9ab1ad29ade07ff.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_bfb2f20546e9407ccf26527d659ab3a1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_3f9b899bc668b87d2f6b937cd85a8365.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_c1ffd34401e7bf4e6ce0b06d881cb921.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_41ec81e9812d7bfb510cba45f77f65e5.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_c454323e13df5cf946abd3298aecd247.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_42466b1b45f2696aff166a8ada8aac4d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_c6190f6a3bf7feed02650b633de46311.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_43412a95bc66d14b16c680bdde308ab2.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_cb468fdbb6108116358357f6417c3024.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_457188006821270728c48f9775ff94c1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_cbd8636fcb6847a1987357ef9cf8711f.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_483fd9856c623de31e240ae26cd61e75.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_ce4a8ed4127ae67993349cd598454769.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_48e539f4b9a9061954a5433e546d287e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_cf2a0f71aea6141996911e17f6a0f54c.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_48ec1e06f8d6d1de00202e9765b9ae4c.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d11ae085215e159e6b3ae6e66944b0c4.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_4f78f0e36c6a0af346d9bc1b36d03eb5.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d3c063973c2fad7ef6bf18378cc23a20.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_509cc155d50d2e4bfc6b6ce6b540c93d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d532cb5c06f5ab6dd384109fb3b2a63e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_512d8e38fc8de7c5b6281794785b6eee.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d7d690009f876c0199a7c95786514692.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5171377532430542db0b93961f24b8ac.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d855a67bb5b61642f3524b768a3673db.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_52260086506134eeb5625e2a38100d70.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_d9bbd7a608edf04051ca8492197f9aa8.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_54a660f4672b65a4f57457790c603d52.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_daf743afe50836d18d9dc608359dfaea.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5a1a013fe1907d7559862d67ac3c829f.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_db22ca67283e96f86956d83dc2c005c1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5b4ad934586e5359ce0ff84b9b18116f.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_df475528fcd8239b94599584fc1e66aa.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5b7e1b94c498d0fcaf2b910d225e0d6d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_dfb406c727431bc999da4ec580cec6d1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5c8dd32037e19f04073ed1933d095fde.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_e0e5ecb5ec66c583e29faed9e090045d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5e6ae3b6838f4721fecace29e17a6cb2.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_e0ea6f85d358304c90ef24b94ff69798.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_5f86e6c45313a8c80755d2075d950ef8.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_e3fe0d73ab0fe73beb9410a1af8df76a.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_659bc46923fea10f8d871ce02af96b22.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_e47bc1c9bd070b1f3830d86d64ead298.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_6a5b422e1ab4ef764160445cfc112838.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_e9124425fffffcb769f086e64fbb383e.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_6e37336d526beba1ad7b5d87aafaf1fe.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_f4bdf0e5c089ec5cdbf04b184dcd6a64.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_6e62e2c8c4e368b4b60492b3b269546d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_f5392df4196cc0269e2211e218b0fbc9.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_71fe5163cda1c064a4cb4982a74b8aee.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_f6bdc74a4a870e1d770e33be709ed46d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_72448ab8ddf8befb146ac924746bfd4d.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_f90b474886530127a974ddfcb242cef1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_747b5390141e9d3143a108b41d7d02a1.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_ff3d8612c7f3a459c7fcfa190a6e0f19.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_7564e72315da9d534127df0b9cc73473.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_ff7b6652c2fc5f5471b5f72954406cd8.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_766e421429599bbdaca2bfdb7c11dcac.root",
							     "file:/eos/cms/store/user/dsperka/ALP/ggh_m30/MiniAOD_ff9c337af02bb2c66a150580985089f5.root"))

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

### 2018 lowmass files
#process.source = cms.Source("PoolSource",
#                             fileNames=cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/1359F11B-F51C-4F47-8D70-8CFC55E77A64.root"))
#			     fileNames=cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/1359F11B-F51C-4F47-8D70-8CFC55E77A64.root",
#							      "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/9FE0ED7A-F7B7-6C46-A52D-AFE731096D0B.root",
#                                                             "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/7D3E00A4-254A-194C-9226-392CEB8262E6.root",
#                                                             "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/DD6AA8B9-3668-1D4B-AA19-1E7F54BB2353.root",
#                                                             "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/472FCFC6-82FE-0D47-88E1-D63B34113F13.root",
#                                                             "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/99B58FBC-E522-2A42-937D-7330BF9E3F9F.root",
#                                                             "/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/72D4635C-3780-6149-A13D-8C031F5CB943.root"))

### 2016
#process.GlobalTag = GlobalTag(process.GlobalTag, '', '')
#process.source = cms.Source("PoolSource",
#                             fileNames=cms.untracked.vstring("/store/mc/RunIISummer16MiniAODv3/VBFHToGG_M125_13TeV_amcatnlo_pythia8_v2/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/50000/38128C3C-892D-E911-AC8E-008CFA0087C4.root"))
#    process.GlobalTag = GlobalTag(process.GlobalTag,'80X_dataRun2_2016LegacyRepro_v4','')
#    process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2016B/SingleElectron/MINIAOD/07Aug17_ver1-v1/110000/0248293E-578B-E711-A639-44A842CFC9D9.root"))

### 2017
#process.GlobalTag = GlobalTag(process.GlobalTag,'','')
#process.source = cms.Source("PoolSource",
#                             fileNames=cms.untracked.vstring("/store/mc/RunIIFall17MiniAODv2/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0866D1A8-1941-E811-B61F-0CC47AF9B2E6.root"))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring('/store/mc/RunIISummer16MiniAODv2/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/024E4FA3-8BBC-E611-8E3D-00266CFFBE88.root'))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17MiniAOD/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/40000/4A2ACB0A-1BD9-E711-AF54-141877410316.root'))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17MiniAOD/GluGluToHHTo2B2G_node_SM_13TeV-madgraph/MINIAODSIM/94X_mc2017_realistic_v10-v1/00000/2E0E165D-8E05-E811-909C-FA163E80AE1F.root'))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring('file:/afs/cern.ch/user/s/sethzenz/work/public/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_94X_mc2017_realistic_v10-v1.root'))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIIFall17MiniAODv2/THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/6E58A5DD-BF43-E811-8946-0023AEEEB538.root"))

### 2018
    # process.GlobalTag = GlobalTag(process.GlobalTag,'100X_upgrade2018_realistic_v10','')
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2018B/DoubleMuon/MINIAOD/PromptReco-v1/000/317/080/00000/4E78B565-8464-E811-BF54-02163E01A0FC.root"))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v2/000/322/106/00000/9A1C4C91-1EB3-E811-A238-02163E0150CE.root"))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2018D/DoubleMuon/MINIAOD/PromptReco-v2/000/320/673/00000/0A83E8DF-EB97-E811-AE18-FA163E192E5D.root"))
    # process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10-v2/10000/F24C5C06-FF47-E811-9C2F-FA163EC3CAD1.root"))

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService")
process.RandomNumberGeneratorService.flashggRandomizedPhotons = cms.PSet(
          initialSeed = cms.untracked.uint32(16253245)
        )

#process.GlobalTag = GlobalTag(process.GlobalTag,'92X_upgrade2017_realistic_v10','')
#process.source.fileNames=cms.untracked.vstring("/store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10_ext1-v2/10000/00F9D855-E293-E711-B625-02163E014200.root")

# 2017 Data
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2017A/DoubleEG/MINIAOD/PromptReco-v2/000/296/173/00000/C24ABCFB-644C-E711-8A5E-02163E01A21C.root"))

# Legacy ReReco
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2016B/SingleElectron/MINIAOD/18Apr2017_ver1-v1/120000/40167FB6-6237-E711-934A-001E67E69E05.root"))

#Moriond17 MC
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISummer16MiniAODv2/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/024E4FA3-8BBC-E611-8E3D-00266CFFBE88.root"))

#80x reminiAOD data
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2016G/DoubleEG/MINIAOD/03Feb2017-v1/100000/002F14FF-D0EA-E611-952E-008CFA197AF4.root"))

#80x signal
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring16MiniAODv2/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext2-v1/10000/6A31A211-063B-E611-98EC-001E67F8F727.root")) # ggH 125 miniAODv2
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring16MiniAODv2/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_v2/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/267A1DB4-3D3B-E611-9AD2-003048C559C4.root")) # ttH 125 miniAODv2

#80x data
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2016B/DoubleEG/MINIAOD/PromptReco-v2/000/273/158/00000/1E5ABF54-E019-E611-AAED-02163E01293F.root")) # /DoubleEG/Run2016B-PromptReco-v2/MINIAOD

process.MessageLogger.cerr.threshold = 'ERROR' # can't get suppressWarning to work: disable all warnings for now
# process.MessageLogger.suppressWarning.extend(['SimpleMemoryCheck','MemoryCheck']) # this would have been better...

# Uncomment the following if you notice you have a memory leak
# This is a lightweight tool to digg further
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#                                        ignoreTotal = cms.untracked.int32(1),
#                                        monitorPssAndPrivate = cms.untracked.bool(True)
#                                       )

process.load("flashgg/MicroAOD/flashggMicroAODSequence_cff")

# NEEDED FOR ANYTHING PRIOR TO reMiniAOD
#process.weightsCount.pileupInfo = "addPileupInfo"

from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODDefaultOutputCommand
#process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('myMicroAODOutputFile_30GeV_dataset.root'),
process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('myMicroAODOutputFile_30GeV_allfiles.root'),
                               outputCommands = microAODDefaultOutputCommand
                               )

# All jets are now handled in MicroAODCustomize.py
# Switch from PFCHS to PUPPI with puppi=1 argument (both if puppi=2)

process.p = cms.Path(process.flashggMicroAODSequence)
process.e = cms.EndPath(process.out)

# Uncomment these lines to run the example commissioning module and send its output to root
#process.commissioning = cms.EDAnalyzer('flashggCommissioning',
#                                       PhotonTag=cms.untracked.InputTag('flashggPhotons'),
#                                       DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
#                                       VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices')
#)
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string("commissioningTree.root")
#)
#process.p *= process.commissioning

from flashgg.MicroAOD.MicroAODCustomize import customize
customize(process)

if "DY" in customize.datasetName or "SingleElectron" in customize.datasetName or "DoubleEG" in customize.datasetName or "EGamma" in customize.datasetName:
    customize.customizeHLT(process)

#open('dump.py', 'w').write(process.dumpPython())

