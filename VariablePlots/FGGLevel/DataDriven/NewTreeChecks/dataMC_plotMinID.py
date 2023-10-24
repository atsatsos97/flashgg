from ROOT import *
import CMS_lumi
import ROOT, array, random, copy
from ROOT import TCanvas, TFile, TH1, TH1F, TF1, gSystem, TChain
import ROOT, array, CMSGraphics, CMS_lumi, random, copy
from ROOT import TFile, TTree, TList
import argparse
import sys
import os

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)

argparser = argparse.ArgumentParser(description='Parser used for non default arguments', formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=True)
argparser.add_argument('--outdir', dest='outdir', default='./', help='Output dir')
argparser.add_argument('--minV', dest='minV', default='-0.9', help='Minimum Value for maxPhoId')
argparser.add_argument('--maxV', dest='maxV', default='1.0', help='Maximum Value for maxPhoId')

args = argparser.parse_args()
outputdir = args.outdir
minValue = args.minV
maxValue = args.maxV

#Obtain histogram files
data = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/2018Data/2018EGamma.root","READ") #Data with unweighted events, both regions
sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/kest/output_sideband_multiKest1D_lowerBw_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
#sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/2D_kest/output_sideband_multiKest1D_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
#sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/2D_kest/output_sideband_PF_kest1D_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
mgg040 = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG0to40_v2/output_DiPhotonJetsBox_M0_40-Sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_DiphotonMass0to40_v04062023-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
mgg4080 = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG40to80_v2/output_DiPhotonJetsBox_M40_80-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG40to80_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")
mgg80inf = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2/output_DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")


#Get trees and create histograms for data
dat0 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
sb0 = sideband.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")

mgg040_0 = mgg040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
mgg040_1 = mgg040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
mgg040_2 = mgg040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
mgg040_3 = mgg040.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")
mgg4080_0 = mgg4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
mgg4080_1 = mgg4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
mgg4080_2 = mgg4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
mgg4080_3 = mgg4080.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")
mgg80inf_0 = mgg80inf.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
mgg80inf_1 = mgg80inf.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_1")
mgg80inf_2 = mgg80inf.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_2")
mgg80inf_3 = mgg80inf.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_3")

# Previously tested nBins 68
sbb0 = TH1F("sbb0","sbb0",38,-0.7,1) #Max ID in sideband before reweight
sbb0.Sumw2()
sba0 = TH1F("sba0","sba0",38,-0.7,1) #Max ID in sideband after reweight - replaces GJet and QCD
sba0.Sumw2()
pre0 = TH1F("pre0","pre0",38,-0.7,1) #Max ID in preselection region
pre0.Sumw2()
mgg0l = TH1F("mgg0l","mgg0l",38,-0.7,1) #Diphoton MC in preselection region
mgg0l.Sumw2()
mgg0m = TH1F("mgg0m","mgg0m",38,-0.7,1) #Diphoton MC in preselection region
mgg0m.Sumw2()
mgg0h = TH1F("mgg0h","mgg0h",38,-0.7,1) #Diphoton MC in preselection region
mgg0h.Sumw2()
mgg0 = TH1F("mgg0","mgg0",38,-0.7,1) #Diphoton MC in preselection region
mgg0.Sumw2()
bkg0 = THStack("bkg0","bkg0")

sbb0.SetMaximum(35000)
sba0.SetMaximum(35000)
pre0.SetMaximum(35000)
mgg0.SetMaximum(35000)
bkg0.SetMaximum(35000)

#Sideband/Presel regions: CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7 && event%20==0
# -----------------------------------------------------------------------------------------------------
#sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sbb0","CMS_hgg_mass>0","goff")
#sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sbb0","CMS_hgg_mass>0 && event%17==0","goff")
sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sbb0","CMS_hgg_mass>0 && event%20==0","goff")

#sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sba0","abs(weight)*(CMS_hgg_mass>0)","goff")
#sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sba0","abs(weight)*(CMS_hgg_mass>0 && event%17==0)","goff")
sb0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>sba0","abs(weight)*(CMS_hgg_mass>0 && event%20==0)","goff")

dat0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>pre0","CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0","goff")

mgg040_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>mgg0l","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg040_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0l","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg040_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0l","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg040_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0l","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

mgg4080_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>mgg0m","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg4080_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0m","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg4080_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0m","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg4080_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0m","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

mgg80inf_0.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>mgg0h","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg80inf_1.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0h","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg80inf_2.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0h","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
mgg80inf_3.Draw("min(dipho_leadIDMVA,dipho_subleadIDMVA)>>+mgg0h","abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

mgg0.Add(mgg0l)
mgg0.Add(mgg0m)
mgg0.Add(mgg0h)

#MC Scaling
mgg0.Scale(1.3*54.40/20.0)

#Now we draw it out                                                                                                                          
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()
#c1.SetLeftMargin(0.15)                                                                                                          

#upper plot pad - Data histos                                                                                                       
pad1 = TPad("pad1","pad1", 0, 0.36, 1, 1.0)
pad1.Draw()
pad1.cd()
#pad1.SetLogy()                                                                                                                    
pad1.SetBottomMargin(0.01)
pad1.SetLeftMargin(1.9)

sba0.Scale(1.21)
sba0.SetLineColor(kYellow-7)
sba0.SetFillColorAlpha(kYellow-7,0.8)
sba0.SetLineWidth(2)

sba0.GetYaxis().SetTitle("Events/0.05")
sba0.GetYaxis().SetTitleSize(25)
sba0.GetYaxis().SetTitleFont(43)
sba0.GetYaxis().SetTitleOffset(2.25)
sba0.GetYaxis().SetLabelFont(43)
sba0.GetYaxis().SetLabelOffset(0.01)
sba0.GetYaxis().SetLabelSize(25)

mgg0.SetLineColor(kOrange-4)
mgg0.SetFillColorAlpha(kOrange-4,0.8)
mgg0.SetLineWidth(2)

bkg0.Add(mgg0)
bkg0.Add(sba0)
sba0.GetXaxis().SetLabelOffset(1.5)
mgg0.GetXaxis().SetLabelOffset(1.5)
sba0.GetXaxis().SetLabelSize(0)
mgg0.GetXaxis().SetLabelSize(0)
bkg0.Draw("histo")

pre0.SetLineWidth(2)
pre0.SetLineColorAlpha(kBlack,0.8)
#pre0.SetLineColorAlpha(kOrange+9,0.8)
pre0.GetXaxis().SetLabelSize(0)
pre0.Draw("epsame")

sbb0.SetLineColor(kOrange-1)
sbb0.SetLineWidth(2)
sbb0.GetXaxis().SetLabelSize(0)
sbb0.Draw("histosame")

leg = TLegend(0.2,0.5,0.7,0.88)
leg.AddEntry(sbb0,"Unweighted Sideband")
leg.AddEntry(sba0,"#gamma-jet and jet-jet (Reweighted Sideband)")
leg.AddEntry(mgg0,"Diphoton MC")
leg.AddEntry(pre0,"Preselection Region")
leg.SetLineWidth(0)
leg.Draw("same")

c1.Update()
c1.cd()

#lower plot pad - Ratio plot
pad2 = TPad("pad2","pad2", 0, 0.01, 1, 0.35)
pad2.SetGridy()
pad2.Draw()
pad2.cd()
pad2.SetTopMargin(0.)
pad2.SetBottomMargin(0.17)
pad2.SetLeftMargin(0.11)

#define ratio plot                                                                                                                              
rp = TH1F(pre0.Clone("rp")) #clone the preselection region                                                                                         
rp.SetLineColor(kBlack)
rp.SetMinimum(0.5)
rp.SetMaximum(1.9)
rp.SetStats(0)
rp.Divide(sba0+mgg0) #divide by sideband+mgg                                                                                                     
rp.SetMarkerStyle(24)
rp.SetTitle("")

rp.SetYTitle("Reweighted SB/Presel")
rp.GetYaxis().SetNdivisions(505)
rp.GetYaxis().SetTitleSize(25)
rp.GetYaxis().SetTitleFont(43)
rp.GetYaxis().SetTitleOffset(2.25)
rp.GetYaxis().SetLabelFont(43)
rp.GetYaxis().SetLabelSize(25)

rp.SetXTitle("Min #gamma ID MVA")
rp.GetXaxis().SetTitleSize(25)
rp.GetXaxis().SetTitleFont(43)
rp.GetXaxis().SetTitleOffset(3.9)
rp.GetXaxis().SetLabelFont(43)
rp.GetXaxis().SetLabelSize(25)
rp.GetXaxis().SetLabelOffset(0.02)

rp.Draw("ep")

c1.Update()
c1.cd()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = "Preliminary"
CMS_lumi.lumi_sqrtS     = "2.72 fb^{-1} (13 TeV)"
CMS_lumi.cmsTextSize    = 0.6
CMS_lumi.lumiTextSize   = 0.46
CMS_lumi.extraOverCmsTextSize = 0.75
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(pad1, 0, 0)

c1.Update()
#c1.SaveAs(outputdir+"/kest2D_Data_MaxIDComp.png")
#c1.SaveAs(outputdir+"/kest2D_Data_MaxIDComp.pdf")
c1.SaveAs(outputdir+"/multiKest1D_scaled1p21_lowerBw_5PercSB_Data_MinIDComp.png")
c1.SaveAs(outputdir+"/multiKest1D_scaled1p21_lowerBw_5PercSB_Data_MinIDComp.pdf")
#c1.SaveAs(outputdir+"/PF_5PercSB_kest1D_Data_MinIDComp.png")
#c1.SaveAs(outputdir+"/PF_5PercSB_kest1D_Data_MinIDComp.pdf")

print "MGG: ", mgg0.Integral()
print "Reweight: ", sba0.Integral()
print "Preselect: ", pre0.Integral()
print "Unweighted Sideband:", sbb0.Integral()
