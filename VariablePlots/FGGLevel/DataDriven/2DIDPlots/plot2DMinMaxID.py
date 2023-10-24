from ROOT import *
import CMS_lumi

isMC = True
isGJet = False
isQCD = True
isSideband = False

#Overall histo
minmax_0 = TH2F("minmax_0","minmax_0",50,-1,1,50,-1,1)
minmax_0.Sumw2()

if (isMC):
  if(isGJet):
    print "GJet Background"
    file040 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG0to40_v1/output_GJet_Pt-20toInf_DoubleEMEnriched_MGG-2to40_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_PhotonJetMass2to40_v05252023-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file4080 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG40to80_v2/output_GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG40to80_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file80InfLow = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v3/output_GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v4-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file80InfHigh = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v3/output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
  elif(isQCD):
    print "QCD Background"
    file040 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG0to40_v1/output_QCD_Pt-30toInf_DoubleEMEnriched_MGG-5to40_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_QCDMass5to40_v05252023-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file4080 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG40to80_v2/output_QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG40to80_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file80InfLow = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v3/output_QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file80InfHigh = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v3/output_QCD_Pt-40ToInf_DoubleEMEnriched_MGG-80ToInf_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
  else:
    print "Diphoton Background"
    file040 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG0to40_v1/output_DiPhotonJetsBox_M0_40-Sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_DiphotonMass0to40_v04062023-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
    file4080 = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG40to80_v2/output_DiPhotonJetsBox_M40_80-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG40to80_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")
    file80InfLow = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/Systematics/test/UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v3/output_DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")

  #Background MC
  tree040_0 = file040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
  tree040_1 = file040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
  tree040_2 = file040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
  tree040_3 = file040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

  tree4080_0 = file4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
  tree4080_1 = file4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
  tree4080_2 = file4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
  tree4080_3 = file4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

  tree80InfLow_0 = file80InfLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
  tree80InfLow_1 = file80InfLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
  tree80InfLow_2 = file80InfLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
  tree80InfLow_3 = file80InfLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

  if(isGJet or isQCD):
    tree80InfHigh_0 = file80InfHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
    tree80InfHigh_1 = file80InfHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
    tree80InfHigh_2 = file80InfHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
    tree80InfHigh_3 = file80InfHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

  minmax040_0 = TH2F("minmax040_0","minmax040_0",50,-1,1,50,-1,1)
  minmax040_0.Sumw2()
  minmax040_1 = TH2F("minmax040_1","minmax040_1",50,-1,1,50,-1,1)
  minmax040_1.Sumw2()
  minmax040_2 = TH2F("minmax040_2","minmax040_2",50,-1,1,50,-1,1)
  minmax040_2.Sumw2()
  minmax040_3 = TH2F("minmax040_3","minmax040_3",50,-1,1,50,-1,1)
  minmax040_3.Sumw2()

  minmax4080_0 = TH2F("minmax4080_0","minmax4080_0",50,-1,1,50,-1,1)
  minmax4080_0.Sumw2()
  minmax4080_1 = TH2F("minmax4080_1","minmax4080_1",50,-1,1,50,-1,1)
  minmax4080_1.Sumw2()
  minmax4080_2 = TH2F("minmax4080_2","minmax4080_2",50,-1,1,50,-1,1)
  minmax4080_2.Sumw2()
  minmax4080_3 = TH2F("minmax4080_3","minmax4080_3",50,-1,1,50,-1,1)
  minmax4080_3.Sumw2()

  minmax80InfLow_0 = TH2F("minmax80InfLow_0","minmax80InfLow_0",50,-1,1,50,-1,1)
  minmax80InfLow_0.Sumw2()
  minmax80InfLow_1 = TH2F("minmax80InfLow_1","minmax80InfLow_1",50,-1,1,50,-1,1)
  minmax80InfLow_1.Sumw2()
  minmax80InfLow_2 = TH2F("minmax80InfLow_2","minmax80InfLow_2",50,-1,1,50,-1,1)
  minmax80InfLow_2.Sumw2()
  minmax80InfLow_3 = TH2F("minmax80InfLow_3","minmax80InfLow_3",50,-1,1,50,-1,1)
  minmax80InfLow_3.Sumw2()

  if(isGJet or isQCD):
    minmax80InfHigh_0 = TH2F("minmax80InfHigh_0","minmax80InfHigh_0",50,-1,1,50,-1,1)
    minmax80InfHigh_0.Sumw2()
    minmax80InfHigh_1 = TH2F("minmax80InfHigh_1","minmax80InfHigh_1",50,-1,1,50,-1,1)
    minmax80InfHigh_1.Sumw2()
    minmax80InfHigh_2 = TH2F("minmax80InfHigh_2","minmax80InfHigh_2",50,-1,1,50,-1,1)
    minmax80InfHigh_2.Sumw2()
    minmax80InfHigh_3 = TH2F("minmax80InfHigh_3","minmax80InfHigh_3",50,-1,1,50,-1,1)
    minmax80InfHigh_3.Sumw2()

  tree040_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax040_0","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree040_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax040_1","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree040_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax040_2","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree040_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax040_3","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  tree4080_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax4080_0","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree4080_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax4080_1","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree4080_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax4080_2","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree4080_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax4080_3","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  tree80InfLow_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfLow_0","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree80InfLow_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfLow_1","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree80InfLow_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfLow_2","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  tree80InfLow_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfLow_3","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  if(isGJet or isQCD):
    tree80InfHigh_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfHigh_0","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
    tree80InfHigh_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfHigh_1","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
    tree80InfHigh_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfHigh_2","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
    tree80InfHigh_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax80InfHigh_3","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  minmax040_0.Add(minmax040_1)
  minmax040_0.Add(minmax040_2)
  minmax040_0.Add(minmax040_3)

  minmax4080_0.Add(minmax4080_1)
  minmax4080_0.Add(minmax4080_2)
  minmax4080_0.Add(minmax4080_3)

  minmax80InfLow_0.Add(minmax80InfLow_1)
  minmax80InfLow_0.Add(minmax80InfLow_2)
  minmax80InfLow_0.Add(minmax80InfLow_3)

  minmax_0.Add(minmax040_0)
  minmax_0.Add(minmax4080_0)
  minmax_0.Add(minmax80InfLow_0)

  if(isGJet or isQCD):
    minmax80InfHigh_0.Add(minmax80InfHigh_1)
    minmax80InfHigh_0.Add(minmax80InfHigh_2)
    minmax80InfHigh_0.Add(minmax80InfHigh_3)

    minmax_0.Add(minmax80InfHigh_0)

else:
  if(isSideband):
    print "Data Sideband"
    file = TFile("/afs/cern.ch/work/a/atsatsos/ULLowmassFGG/CMSSW_10_6_8/src/flashgg/VariablePlots/FGGLevel/DataDriven/output_sideband.root","READ")

    tree_0 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
    tree_1 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
    tree_2 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")
    tree_3 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_3")

    minmax_1 = TH2F("minmax_1","minmax_1",50,-1,1,50,-1,1)
    minmax_1.Sumw2()
    minmax_2 = TH2F("minmax_2","minmax_2",50,-1,1,50,-1,1)
    minmax_2.Sumw2()
    minmax_3 = TH2F("minmax_3","minmax_3",50,-1,1,50,-1,1)
    minmax_3.Sumw2()

    tree_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_0","(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_1","(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_2","(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_3","(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")

    minmax_0.Add(minmax_1)
    minmax_0.Add(minmax_2)
    minmax_0.Add(minmax_3)
  else:
    print "Data Preselection"
    file = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_Data_Lowmassxml_v1/output_EGamma_alesauva-UL2018_0-10_6_4-v0-Run2018-12Nov2019_UL2018-981b04a73c9458401b9ffd78fdd24189_USER.root","READ")

    tree_0 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
    tree_1 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
    tree_2 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")
    tree_3 = file.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_3")

    minmax_1 = TH2F("minmax_1","minmax_1",50,-1,1,50,-1,1)
    minmax_1.Sumw2()
    minmax_2 = TH2F("minmax_2","minmax_2",50,-1,1,50,-1,1)
    minmax_2.Sumw2()
    minmax_3 = TH2F("minmax_3","minmax_3",50,-1,1,50,-1,1)
    minmax_3.Sumw2()

    tree_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_0","(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_1","(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_2","(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")
    tree_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA):max(dipho_leadIDMVA,dipho_subleadIDMVA)>>minmax_3","(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0)","goff")

    minmax_0.Add(minmax_1)
    minmax_0.Add(minmax_2)
    minmax_0.Add(minmax_3)

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,800)
c1.cd()
gPad.SetLogz()
c1.SetBottomMargin(0.17)
c1.SetLeftMargin(0.11)

minmax_0.GetYaxis().SetTitle("Min #gamma ID")
minmax_0.GetYaxis().SetTitleSize(30)
minmax_0.GetYaxis().SetTitleFont(43)
minmax_0.GetYaxis().SetTitleOffset(1.5)
minmax_0.GetYaxis().SetLabelFont(43)
minmax_0.GetYaxis().SetLabelSize(25)
minmax_0.GetYaxis().SetLabelOffset(0.02)

minmax_0.GetXaxis().SetTitle("Max #gamma ID")
minmax_0.GetXaxis().SetTitleSize(30)
minmax_0.GetXaxis().SetTitleFont(43)
minmax_0.GetXaxis().SetTitleOffset(1.75)
minmax_0.GetXaxis().SetLabelFont(43)
minmax_0.GetXaxis().SetLabelSize(25)
minmax_0.GetXaxis().SetLabelOffset(0.02)

minmax_0.Draw("colz")

c1.Update()
if (isMC):
  CMS_lumi.writeExtraText = True
  CMS_lumi.extraText      = "Preliminary Simulation"
  CMS_lumi.lumi_sqrtS     = "13 TeV"
  CMS_lumi.cmsTextSize    = 0.6
  CMS_lumi.lumiTextSize   = 0.46
  CMS_lumi.extraOverCmsTextSize = 0.753
  CMS_lumi.relPosX = 0.12
  CMS_lumi.CMS_lumi(c1, 0, 0)
  c1.Update()
  if(isGJet):
    minmax_0.SaveAs("GJet_MinMaxIDMVA.root")
    c1.SaveAs("GJet_MinMaxIDMVA.png")
    c1.SaveAs("GJet_MinMaxIDMVA.pdf")
  elif(isQCD):
    minmax_0.SaveAs("QCD_MinMaxIDMVA.root")
    c1.SaveAs("QCD_MinMaxIDMVA.png")
    c1.SaveAs("QCD_MinMaxIDMVA.pdf")
  else:
    minmax_0.SaveAs("Dipho_MinMaxIDMVA.root")
    c1.SaveAs("Dipho_MinMaxIDMVA.png")
    c1.SaveAs("Dipho_MinMaxIDMVA.pdf")
else:
  CMS_lumi.writeExtraText = True
  CMS_lumi.extraText      = "Preliminary"
  CMS_lumi.lumi_sqrtS     = "2.9 fb^{-1} (13 TeV)"
  CMS_lumi.cmsTextSize    = 0.6
  CMS_lumi.lumiTextSize   = 0.46
  CMS_lumi.extraOverCmsTextSize = 0.753
  CMS_lumi.relPosX = 0.12
  CMS_lumi.CMS_lumi(c1, 0, 0)
  c1.Update()
  if(isSideband):
    minmax_0.SaveAs("DataSideband_MinMaxIDMVA_Reweighted.root")
    c1.SaveAs("DataSideband_MinMaxIDMVA_Reweighted.png")
    c1.SaveAs("DataSideband_MinMaxIDMVA_Reweighted.pdf")
  else:
    minmax_0.SaveAs("DataPresel_MinMaxIDMVA.root")
    c1.SaveAs("DataPresel_MinMaxIDMVA.png")
    c1.SaveAs("DataPresel_MinMaxIDMVA.pdf")
