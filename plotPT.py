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

pt0 = TH1F("pt0","pt0",90,0,90)
pt0.Sumw2()

pt1 = TH1F("pt1","pt1",90,0,90)
pt1.Sumw2()

pt2 = TH1F("pt2","pt2",90,0,90)
pt2.Sumw2()

ptsig0 = TH1F("ptsig0","ptsig0",90,0,90)
ptsig0.Sumw2()

ptsig1 = TH1F("ptsig1","ptsig1",90,0,90)
ptsig1.Sumw2()

ptsig2 = TH1F("ptsig2","ptsig2",90,0,90)
ptsig2.Sumw2()

subpt0 = TH1F("subpt0","subpt0",90,0,90)
subpt0.Sumw2()

subpt1 = TH1F("subpt1","subpt1",90,0,90)
subpt1.Sumw2()

subpt2 = TH1F("subpt2","subpt2",90,0,90)
subpt2.Sumw2()

subptsig0 = TH1F("subptsig0","subptsig0",90,0,90)
subptsig0.Sumw2()

subptsig1 = TH1F("subptsig1","subptsig1",90,0,90)
subptsig1.Sumw2()

subptsig2 = TH1F("subptsig2","subptsig2",90,0,90)
subptsig2.Sumw2()

t0.Draw("leadPt>>pt0","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")
t1.Draw("leadPt>>pt1","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")
t2.Draw("leadPt>>pt2","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")

s0.Draw("leadPt>>ptsig0","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")
s1.Draw("leadPt>>ptsig1","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")
s2.Draw("leadPt>>ptsig2","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")

t0.Draw("subleadPt>>subpt0","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")
t1.Draw("subleadPt>>subpt1","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")
t2.Draw("subleadPt>>subpt2","CMS_hgg_mass>10 && CMS_hgg_mass<40 && event%10==0","goff")

s0.Draw("subleadPt>>subptsig0","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")
s1.Draw("subleadPt>>subptsig1","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")
s2.Draw("subleadPt>>subptsig2","CMS_hgg_mass>10 && CMS_hgg_mass<40","goff")

pt0.Add(pt1)
pt0.Add(pt2)

ptsig0.Add(ptsig1)
ptsig0.Add(ptsig2)

subpt0.Add(subpt1)
subpt0.Add(subpt2)

subptsig0.Add(subptsig1)
subptsig0.Add(subptsig2)

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",800,800)
c1.cd()

#pt0.SetLineColor(1)
#pt0.Scale(10.0)
#pt0.Draw("ehist")
#pt0.SetXTitle("pT")

ptsig0.SetLineColor(2)
#ptsig0.Scale(1.0*31950.0/16399.0)
ptsig0.Draw("ehistsame")
ptsig0.SetXTitle("pT")

leg = TLegend(0.7,0.8,0.88,0.88)
#leg.AddEntry(pt0,"Untagged Simone's Files")
leg.AddEntry(ptsig0,"Untagged 30GeV Sample")
leg.Draw("same")

c1.SaveAs("pt_file_sig.png")
c1.SaveAs("pt_file_sig.pdf")

c2 = TCanvas("c2","c2",800,800)
c2.cd()

#pt0.SetLineColor(1)
#pt0.Scale(10.0)
#pt0.Draw("ehist")
#pt0.SetXTitle("sub_pT")

subptsig0.SetLineColor(2)
#subptsig0.Scale(1.0*31950.0/16399.0)
subptsig0.Draw("ehistsame")
subptsig0.SetXTitle("sub_pT")

leg = TLegend(0.7,0.8,0.88,0.88)
#leg.AddEntry(pt0,"Untagged Simone's Files")
leg.AddEntry(ptsig0,"Untagged 30GeV Sample")
leg.Draw("same")

c2.SaveAs("subpt_file_sig.png")
c2.SaveAs("subpt_file_sig.pdf")

print ptsig0.Integral()
print subptsig0.Integral()

