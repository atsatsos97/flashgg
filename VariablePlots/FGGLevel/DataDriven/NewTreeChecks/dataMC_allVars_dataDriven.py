from ROOT import *
import CMS_lumi
import ROOT, array, random, copy
from ROOT import TCanvas, TFile, TH1, TH1F, TF1, gSystem, TChain
import ROOT, array, CMSGraphics, CMS_lumi, random, copy
from ROOT import TFile, TTree, TList
from collections import OrderedDict
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

# ----------------------
# Obtain histogram files
# ----------------------
data = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/2018Data/2018EGamma.root","READ") #Data with unweighted events, both regions
sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/kest/output_sideband_multiKest1D_lowerBw_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
#sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/2D_kest/output_sideband_multiKest1D_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
#sideband = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/reweighting/2D_kest/output_sideband_PF_kest1D_AllChunks.root","READ") #Sideband tree with reweight - replaces gjet and QCD
mgg040 = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG0to40_v2/output_DiPhotonJetsBox_M0_40-Sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_DiphotonMass0to40_v04062023-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-3fc41d6a5cdc2b7d1e5534c778de39cd_USER.root","READ")
mgg4080 = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG40to80_v2/output_DiPhotonJetsBox_M40_80-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG40to80_v1-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")
mgg80inf = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_BkgMC_MGG80toInf_v2/output_DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa_atsatsos-UL18_VLowMassDiphoton_BkgMC_MGG80toInf_v2-v0-v0-RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2-bf7acd40472d4982996c4dd60309cd6d_USER.root","READ")


# Get trees and create histograms for data
# ----------------------------------------
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


var_list = ["dipho_lead_ptoM", "dipho_sublead_ptoM", "dipho_leadEta", "dipho_subleadEta", "cosphi", "dipho_leadIDMVA", "dipho_subleadIDMVA", "sigmaMrvoM", "sigmaMwvoM", "vtxprob"]
label_list = ["Leading photon p_{T}", "Subleading photon p_{T}", "Leading photon #eta", "Sublead photon #eta", "cosphi", "Lead IDMVA", "Sublead IDMVA", "#sigma_{RV}/m_{#gamma#gamma}", "sigma_{WV}/m_{#gamma#gamma}", "Vtx probability"]

#histo_sbb0_list = {}
#histo_sba0_list = {}
#histo_pre0_list = {}
#histo_mgg0_list = {}

histo_sbb0_list = OrderedDict()
histo_sba0_list = OrderedDict()
histo_pre0_list = OrderedDict()
histo_mgg0_list = OrderedDict()

# Create a dictionary to store the binning information for each variable
binning_info = {
    var_list[0]: (100, 0., 4.), #dipho_lead_ptoM
    var_list[1]: (100, 0., 4.), #"dipho_sublead_ptoM
    var_list[2]: (60, -3., 3.), #dipho_leadEta 
    var_list[3]: (60, -3., 3.), #dipho_subleadEta
    var_list[4]: (30, 0.0, 1.0), #cosphi
    var_list[5]: (100, -1.,1.), #dipho_leadIDMVA 
    var_list[6]: (100, -1.,1.), #dipho_subleadIDMVA
    var_list[7]: (50, 0., 0.05), #sigmaMrvoM
    var_list[8]: (50, 0., 0.05), #sigmaMwvoM
    var_list[9]: (50, 0.9, 1.0) #vtxprob
}

#nbins = [100, 100, 60, 60, 30, 100, 100, 50, 50, 100]
#xlow = [0., 0., -3., -3., -0.5, -1., -1., 0., 0., 0.95]
#xhigh = [4., 4., 3., 3., 1., 1., 1., 0.05, 0.05, 1.01]


for variable in var_list:
    nbins, xlow, xhigh = binning_info[variable]
    print("var_list[i]", variable)
    print("nbins = ", nbins)
    print("xlow = ", xlow)
    print("xhigh = ", xhigh)
    histo_sbb0_list[variable + "_sbb0"] = TH1F("h_" + variable + "_sbb0", "h_" + variable + "_sbb0", nbins, xlow, xhigh)
    histo_sba0_list[variable + "_sba0"] = TH1F("h_" + variable + "_sba0", "h_" + variable + "_sba0" , nbins, xlow, xhigh)
    histo_pre0_list[variable + "_pre0"] = TH1F("h_" + variable + "_pre0", "h_" + variable + "_pre0", nbins, xlow, xhigh)
    histo_mgg0_list[variable + "_mgg0"] = TH1F("h_" + variable + "_mgg0", "h_" + variable + "_mgg0", nbins, xlow, xhigh)

    # Fill the histograms
    # Fill the histograms
    sb0.Draw(variable + ">>h_" + variable + "_sbb0", "(CMS_hgg_mass>0 && event%20==0)", "goff")
    sb0.Draw(variable + ">>h_" + variable + "_sba0", "abs(weight)*(CMS_hgg_mass>0 && event%20==0)", "goff")
    #dat0.Draw(variable + ">>h_" + variable + "_pre0", "CMS_hgg_mass>0 && event%20==0", "goff")

    #mgg040_0.Draw(variable + ">>h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg040_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg040_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg040_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")

    #mgg4080_0.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg4080_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg4080_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg4080_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")

    #mgg80inf_0.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg80inf_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg80inf_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")
    #mgg80inf_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0)", "goff")

    dat0.Draw(variable + ">>h_" + variable + "_pre0", "CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7 && event%20==0", "goff")

    mgg040_0.Draw(variable + ">>h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg040_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg040_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg040_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")

    mgg4080_0.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg4080_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg4080_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg4080_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")

    mgg80inf_0.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg80inf_1.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg80inf_2.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    mgg80inf_3.Draw(variable + ">>+h_" + variable + "_mgg0", "abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)", "goff")
    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>> FILLED HISTOS")

#print(">>>>>>>>>>>>>>>>>>>>>>>>>> SBB0")
#print(histo_sbb0_list)
#print(">>>>>>>>>>>>>>>>>>>>>>>>>> SBA0")
#print(histo_sba0_list)
#print(">>>>>>>>>>>>>>>>>>>>>>>>>> PRE0")
#print(histo_pre0_list)
#print(">>>>>>>>>>>>>>>>>>>>>>>>>> MGG0")
#print(histo_mgg0_list)

#for i in range(len(histo_sbb0_list)):
for variable in var_list:
    print(variable)
    #MC Scaling
    sbb0 = histo_sbb0_list[variable + "_sbb0"]
    sba0 = histo_sba0_list[variable + "_sba0"]
    pre0 = histo_pre0_list[variable + "_pre0"]
    mgg0 = histo_mgg0_list[variable + "_mgg0"]
    bkg0 = THStack("bkg0","bkg0")

    #print("sbb0", sbb0)
    #print("sba0", sba0)
    #print("pre0", pre0)
    #print("mgg0", mgg0)
    
    mgg0.Scale(1.3*54.40/20.0)
    
    sbb0.SetMaximum(1.2*pre0.GetMaximum())
    sba0.SetMaximum(1.2*pre0.GetMaximum())
    pre0.SetMaximum(1.2*pre0.GetMaximum())
    mgg0.SetMaximum(1.2*pre0.GetMaximum())
    bkg0.SetMaximum(1.2*pre0.GetMaximum())

    #Now we draw it out
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)

    canvasname = "c_"+variable
    c1 = TCanvas(canvasname,canvasname,1200,1200)
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
    
    sba0.GetXaxis().SetLabelSize(0)
    
    sba0.GetYaxis().SetTitle("Events")
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
    bkg0.Draw("histo")
    
    pre0.SetLineWidth(2)
    pre0.SetLineColorAlpha(kBlack,0.8)
    #pre0.SetLineColorAlpha(kOrange+9,0.8)
    pre0.Draw("epsame")
    
    sbb0.SetLineColor(kOrange-1)
    sbb0.SetLineWidth(2)
    sbb0.Draw("histosame")
        
    leg = TLegend(0.3,0.5,0.75,0.88)
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
    
    rp.SetXTitle(variable)
    #rp.SetXTitle(label_list[i])
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
    c1.SaveAs(outputdir+"/"+variable+".png")
    c1.SaveAs(outputdir+"/"+variable+".pdf")
    
    print("MGG: ", mgg0.Integral())
    print("Reweight: ", sba0.Integral())
    print("Preselect: ", pre0.Integral())
    print("Unweighted Sideband:", sbb0.Integral())
