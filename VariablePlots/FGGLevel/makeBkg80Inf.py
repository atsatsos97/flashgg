from ROOT import *
import math

#Argument Parser to input variable and range values
import argparse
def list_of_floats(arg):
    return list(map(float, arg.split(',')))
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='name of variable in tree')
parser.add_argument('--binning', type=list_of_floats, help='number of bins,low range,high range')
args = parser.parse_args()

nbins = int(args.binning[0])
binlow = args.binning[1]
binhigh = args.binning[2]
var = args.name

#Bkg from 80 to Inf GeV
mgg = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2//output_DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")
gjLow = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2//output_GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v4-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
gjHigh = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2//output_GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
qcdLow = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2//output_QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
qcdHigh = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2//output_QCD_Pt-40ToInf_DoubleEMEnriched_MGG-80ToInf_TuneCP5_13TeV-pythia8_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")

mggt0 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
mggt1 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
mggt2 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
mggt3 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

gjt0 = gjLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
gjt1 = gjLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
gjt2 = gjLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
gjt3 = gjLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

gju0 = gjHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
gju1 = gjHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
gju2 = gjHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
gju3 = gjHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

qcdt0 = qcdLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
qcdt1 = qcdLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
qcdt2 = qcdLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
qcdt3 = qcdLow.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

qcdu0 = qcdHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
qcdu1 = qcdHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
qcdu2 = qcdHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
qcdu3 = qcdHigh.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

#Create histograms as well as stacked histo for all backgrounds
mgg0 = TH1F("mgg0","mgg0",nbins,binlow,binhigh)
mgg0.Sumw2()
mgg1 = TH1F("mgg1","mgg1",nbins,binlow,binhigh)
mgg1.Sumw2()
mgg2 = TH1F("mgg2","mgg2",nbins,binlow,binhigh)
mgg2.Sumw2()
mgg3 = TH1F("mgg3","mgg3",nbins,binlow,binhigh)
mgg3.Sumw2()

gjl0 = TH1F("gjl0","gjl0",nbins,binlow,binhigh)
gjl0.Sumw2()
gjl1 = TH1F("gjl1","gjl1",nbins,binlow,binhigh)
gjl1.Sumw2()
gjl2 = TH1F("gjl2","gjl2",nbins,binlow,binhigh)
gjl2.Sumw2()
gjl3 = TH1F("gjl3","gjl3",nbins,binlow,binhigh)
gjl3.Sumw2()

gj0 = TH1F("gj0","gj0",nbins,binlow,binhigh)
gj0.Sumw2()
gj1 = TH1F("gj1","gj1",nbins,binlow,binhigh)
gj1.Sumw2()
gj2 = TH1F("gj2","gj2",nbins,binlow,binhigh)
gj2.Sumw2()
gj3 = TH1F("gj3","gj3",nbins,binlow,binhigh)
gj3.Sumw2()

qcdl0 = TH1F("qcdl0","qcdl0",nbins,binlow,binhigh)
qcdl0.Sumw2()
qcdl1 = TH1F("qcdl1","qcdl1",nbins,binlow,binhigh)
qcdl1.Sumw2()
qcdl2 = TH1F("qcdl2","qcdl2",nbins,binlow,binhigh)
qcdl2.Sumw2()
qcdl3 = TH1F("qcdl3","qcdl3",nbins,binlow,binhigh)
qcdl3.Sumw2()

qcd0 = TH1F("qcd0","qcd0",nbins,binlow,binhigh)
qcd0.Sumw2()
qcd1 = TH1F("qcd1","qcd1",nbins,binlow,binhigh)
qcd1.Sumw2()
qcd2 = TH1F("qcd2","qcd2",nbins,binlow,binhigh)
qcd2.Sumw2()
qcd3 = TH1F("qcd3","qcd3",nbins,binlow,binhigh)
qcd3.Sumw2()

mgg80inf = TH1F("mgg80inf","mgg80inf",nbins,binlow,binhigh)
mgg80inf.Sumw2()
gjl80inf = TH1F("gjl80inf","gjl80inf",nbins,binlow,binhigh)
gjl80inf.Sumw2()
gj80inf = TH1F("gj80inf","gj80inf",nbins,binlow,binhigh)
gj80inf.Sumw2()
qcdl80inf = TH1F("qcdl80inf","qcdl80inf",nbins,binlow,binhigh)
qcdl80inf.Sumw2()
qcd80inf = TH1F("qcd80inf","qcd80inf",nbins,binlow,binhigh)
qcd80inf.Sumw2()


#Weighted: abs(weight)*(CMS_hgg_mass>0)
#Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
mggt0.Draw(var+">>mgg0","abs(weight)*(CMS_hgg_mass>0)","goff")
mggt1.Draw(var+">>mgg1","abs(weight)*(CMS_hgg_mass>0)","goff")
mggt2.Draw(var+">>mgg2","abs(weight)*(CMS_hgg_mass>0)","goff")
mggt3.Draw(var+">>mgg3","abs(weight)*(CMS_hgg_mass>0)","goff")

gjt0.Draw(var+">>gjl0","abs(weight)*(CMS_hgg_mass>0)","goff")
gjt1.Draw(var+">>gjl1","abs(weight)*(CMS_hgg_mass>0)","goff")
gjt2.Draw(var+">>gjl2","abs(weight)*(CMS_hgg_mass>0)","goff")
gjt3.Draw(var+">>gjl3","abs(weight)*(CMS_hgg_mass>0)","goff")

gju0.Draw(var+">>gj0","abs(weight)*(CMS_hgg_mass>0)","goff")
gju1.Draw(var+">>gj1","abs(weight)*(CMS_hgg_mass>0)","goff")
gju2.Draw(var+">>gj2","abs(weight)*(CMS_hgg_mass>0)","goff")
gju3.Draw(var+">>gj3","abs(weight)*(CMS_hgg_mass>0)","goff")

qcdt0.Draw(var+">>qcdl0","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdt1.Draw(var+">>qcdl1","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdt2.Draw(var+">>qcdl2","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdt3.Draw(var+">>qcdl3","abs(weight)*(CMS_hgg_mass>0)","goff")

qcdu0.Draw(var+">>qcd0","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdu1.Draw(var+">>qcd1","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdu2.Draw(var+">>qcd2","abs(weight)*(CMS_hgg_mass>0)","goff")
qcdu3.Draw(var+">>qcd3","abs(weight)*(CMS_hgg_mass>0)","goff")

mgg80inf.Add(mgg0)
mgg80inf.Add(mgg1)
mgg80inf.Add(mgg2)
mgg80inf.Add(mgg3)

gjl80inf.Add(gjl0)
gjl80inf.Add(gjl1)
gjl80inf.Add(gjl2)
gjl80inf.Add(gjl3)

gj80inf.Add(gj0)
gj80inf.Add(gj1)
gj80inf.Add(gj2)
gj80inf.Add(gj3)

qcdl80inf.Add(qcdl0)
qcdl80inf.Add(qcdl1)
qcdl80inf.Add(qcdl2)
qcdl80inf.Add(qcdl3)

qcd80inf.Add(qcd0)
qcd80inf.Add(qcd1)
qcd80inf.Add(qcd2)
qcd80inf.Add(qcd3)

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,800)
c1.cd()

mgg80inf.SetFillColor(kRed)
mgg80inf.SetLineColor(kBlack)
mgg80inf.GetYaxis().SetTitle("Events Accepted")
mgg80inf.SaveAs("DataDriven/bkg_histos/mgg_80inf.root")

gj80inf.SetFillColor(kBlue)
gj80inf.SetLineColor(kBlack)
gj80inf.GetYaxis().SetTitle("Events Accepted")
gj80inf.SaveAs("DataDriven/bkg_histos/gj_80inf.root")

gjl80inf.SetFillColor(kBlue)
gjl80inf.SetLineColor(kBlack)
gjl80inf.GetYaxis().SetTitle("Events Accepted")
gjl80inf.SaveAs("DataDriven/bkg_histos/gj_low_80inf.root")

qcd80inf.SetFillColor(kYellow)
qcd80inf.SetLineColor(kBlack)
qcd80inf.GetYaxis().SetTitle("Events Accepted")
qcd80inf.SaveAs("DataDriven/bkg_histos/qcd_80inf.root")

qcdl80inf.SetFillColor(kYellow)
qcdl80inf.SetLineColor(kBlack)
qcdl80inf.GetYaxis().SetTitle("Events Accepted")
qcdl80inf.SaveAs("DataDriven/bkg_histos/qcd_low_80inf.root")

print("MGG: ",mgg80inf.Integral())
print("GJet: ",gj80inf.Integral())
print("GJetL: ",gjl80inf.Integral())
print("QCD: ",qcd80inf.Integral())
print("QCDL: ",qcdl80inf.Integral())
