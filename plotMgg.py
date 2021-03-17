from ROOT import *

#f = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_70GeV_allsimonefiles_trees_2018/output_EGamma_spigazzi-Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-Run2018D-22Jan2019-v2-dc8e5fb301bfbf2559680ca888829f0c_USER.root","READ")
#f = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_30GeV_allsimonefiles_trees_2018/output_EGamma_spigazzi-Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-Run2018D-22Jan2019-v2-dc8e5fb301bfbf2559680ca888829f0c_USER.root","READ")
f = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_fullrange_allsimonefiles_trees_2018/output_EGamma_spigazzi-Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-Run2018D-22Jan2019-v2-dc8e5fb301bfbf2559680ca888829f0c_USER.root","READ")

g = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_30GeV_allfiles_trees_2018/output_GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_USER_0.root")
#g = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_GluGluHM70_trees_2018/output_GluGluHToGG_M70_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_USER_0.root")

t0 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
t1 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
t2 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")

s0 = g.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
s1 = g.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
s2 = g.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")


mass0 = TH1F("mass0","mass0",120,0,60)
#mass0 = TH1F("mass0","mass0",120,60,110)
mass0.Sumw2()

mass1 = TH1F("mass1","mass1",120,0,60)
#mass1 = TH1F("mass1","mass1",120,60,110)
mass1.Sumw2()

mass2 = TH1F("mass2","mass2",120,0,60)
#mass2 = TH1F("mass2","mass2",120,60,110)
mass2.Sumw2()

data0 = TH1F("data0","data0",120,0,60)
#data0 = TH1F("data0","data0",120,60,110)
data0.Sumw2()

data1 = TH1F("data1","data1",120,0,60)
#data1 = TH1F("data1","data1",120,60,110)
data1.Sumw2()

data2 = TH1F("data2","data2",120,0,60)
#data2 = TH1F("data2","data2",120,60,110)
data2.Sumw2()

mass0.SetMaximum(20500)
mass0.SetMinimum(0)
data0.SetMaximum(20500)
data0.SetMinimum(0)

mass1.SetMaximum(20500)
mass1.SetMinimum(0)
data1.SetMaximum(20500)
data1.SetMinimum(0)

mass2.SetMaximum(20500)
mass2.SetMinimum(0)
data2.SetMaximum(20500)
data2.SetMinimum(0)

t0.Draw("CMS_hgg_mass>>data0","CMS_hgg_mass>0 && event%10==0","goff")
t1.Draw("CMS_hgg_mass>>data1","CMS_hgg_mass>0 && event%10==0","goff")
t2.Draw("CMS_hgg_mass>>data2","CMS_hgg_mass>0 && event%10==0","goff")
s0.Draw("CMS_hgg_mass>>mass0","CMS_hgg_mass>0","goff")
s1.Draw("CMS_hgg_mass>>mass1","CMS_hgg_mass>0","goff")
s2.Draw("CMS_hgg_mass>>mass2","CMS_hgg_mass>0","goff")

print "30 Background 0: ",data0.Integral()
#print "70 Background 0: ",data0.Integral()
print "30 Background 1: ",data1.Integral()
#print "70 Background 1: ",data1.Integral()
print "30 Background 2: ",data2.Integral()
#print "70 Background 2: ",data2.Integral()
print "30 Signal 0: ",mass0.Integral()
#print "70 Signal 0: ",mass0.Integral()
print "30 Signal 1: ",mass1.Integral()
#print "70 Signal 1: ",mass1.Integral()
print "30 Signal 2: ",mass2.Integral()
#print "70 Signal 2: ",mass2.Integral()

#mass0.Add(mass1)
#mass0.Add(mass2)

#data0.Add(data1)
#data0.Add(data2)

print "30 Background: ",data0.Integral()
#print "70 Background: ",data0.Integral()
print "30 Signal: ",mass0.Integral()
#print "70 Signal: ",mass0.Integral()

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",800,800)
c1.cd()

data0.SetLineColor(1)
data0.Scale(10.0)
data0.Draw("ehist")
data0.SetXTitle("CMS_Hgg_mass")
data0.SaveAs("histogramtest_70.root")

mass0.SetLineColor(2)
mass0.Scale(1.0*31950.0/16399.0)
#mass0.Scale(1.0*31950.0/104906.0)
mass0.Draw("ehistsame")
mass0.SetXTitle("CMS_Hgg_mass")
mass0.SaveAs("histogramtest_sig_70.root")

leg = TLegend(0.7,0.8,0.88,0.88)
leg.AddEntry(data0,"Untagged Simone's Files")
leg.AddEntry(mass0,"Untagged 30GeV Sample")
leg.Draw("same")

c1.SaveAs("mass_file_30.png")
c1.SaveAs("mass_file_30.pdf")

print "30 Background: ",data0.Integral()
print "30 Signal after norm: ",mass0.Integral()
