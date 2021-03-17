from ROOT import *

f = TFile("/afs/cern.ch/work/a/atsatsos/CMSSW_10_5_0/src/flashgg/Systematics/test/test_fullrange_allsimonefiles_trees_2018/output_EGamma_spigazzi-Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-Run2018D-22Jan2019-v2-dc8e5fb301bfbf2559680ca888829f0c_USER.root","READ")

t0 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
t1 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
t2 = f.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")

sens = THStack("sens","")

data0 = TH1F("data0","data0",230,5,120)
data0.Sumw2()
data0.SetFillColor(kGreen)
data1 = TH1F("data1","data1",230,5,120)
data1.Sumw2()
data1.SetFillColor(kBlue)
data2 = TH1F("data2","data2",230,5,120)
data2.Sumw2()
data2.SetFillColor(kViolet)

t0.Draw("CMS_hgg_mass>>data0","CMS_hgg_mass>0 && event%10==0","goff")
t1.Draw("CMS_hgg_mass>>data1","CMS_hgg_mass>0 && event%10==0","goff")
t2.Draw("CMS_hgg_mass>>data2","CMS_hgg_mass>0 && event%10==0","goff")

print "Background 0: ",data0.Integral()
print "Background 1: ",data1.Integral()
print "Background 2: ",data2.Integral()

data0.Scale(10.0)
data1.Scale(10.0)
data2.Scale(10.0)

sens.Add(data0)
sens.Add(data1)
sens.Add(data2)

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",800,800)
c1.cd()

sens.Draw()

leg = TLegend(0.7,0.8,0.88,0.88)
leg.AddEntry(sens,"Untagged Simone's Files")
leg.Draw()

c1.SaveAs("data_sensitivities.png")
c1.SaveAs("data_sensitivities.pdf")

print "30 Background: ",data0.Integral()
