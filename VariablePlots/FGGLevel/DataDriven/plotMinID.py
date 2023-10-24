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

argparser = argparse.ArgumentParser(description='Parser used for non default arguments', formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=True)
argparser.add_argument('--outdir', dest='outdir', default='./', help='Output dir')

args = argparser.parse_args()
outputdir = args.outdir


######################################################
# Obtain histogram files for GJets and QCD processes #
######################################################
# Note: the [0,40] GeV QCD sample is excluded

gjlow = TFile("bkg_histos/gj_040.root","READ")
gjmed = TFile("bkg_histos/gj_4080.root","READ")
gjhighlowpt = TFile("bkg_histos/gj_low_80inf.root","READ")
gjhigh = TFile("bkg_histos/gj_80inf.root","READ")

#qcdlow = TFile("bkg_histos/qcd_040.root","READ")
qcdmed = TFile("bkg_histos/qcd_4080.root","READ")
qcdhighlowpt = TFile("bkg_histos/qcd_low_80inf.root","READ")
qcdhigh = TFile("bkg_histos/qcd_80inf.root","READ")

#####################
# Create histograms # 
#####################
#for data, background, and signal, as well as stacked histo for all backgrounds

gjlow0 = gjlow.Get("gj040")
gjmed0 = gjmed.Get("gj4080")
gjhighlowpt0 = gjhighlowpt.Get("gjl80inf")
gjhigh0 = gjhigh.Get("gj80inf")

#qcdlow0 = qcdlow.Get("qcd040")
qcdmed0 = qcdmed.Get("qcd4080")
qcdhighlowpt0 = qcdhighlowpt.Get("qcdl80inf")
qcdhigh0 = qcdhigh.Get("qcd80inf")


print "qcdmed0", qcdmed0.Integral()
print "qcdhighlowpt0", qcdhighlowpt0.Integral()
print "qcdhigh0", qcdhigh0.Integral()

gj0 = TH1F("gj0","gj0",38,-0.9,1.0)
gj0.Sumw2()
qcd0 = TH1F("qcd0","qcd0",38,-0.9,1.0)
qcd0.Sumw2()
bkg0 = THStack()
#bkg0 = TH1F("bkg0","bkg0",38,-0.9,1)
#bkg0.Sumw2()

#Merge histograms from different mass ranges
gj0.Add(gjlow0)
gj0.Add(gjmed0)
gj0.Add(gjhighlowpt0)
gj0.Add(gjhigh0)
#qcd0.Add(qcdlow0)
qcd0.Add(qcdmed0)
qcd0.Add(qcdhighlowpt0)
qcd0.Add(qcdhigh0)

print "qcd0", qcd0.Integral()

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()

c1.SetBottomMargin(0.11)
c1.SetLeftMargin(0.11)

#bkg0.SetFillColorAlpha(kOrange-4,0.8)
#bkg0.SetLineColorAlpha(kOrange-4,0.8)

gj0.SetFillColorAlpha(kOrange-4,0.8)
gj0.SetLineColorAlpha(kOrange-4,0.8)
qcd0.SetFillColorAlpha(kYellow-7,0.8)
qcd0.SetLineColorAlpha(kYellow-7,0.8)

bkg0.Add(gj0)
bkg0.Add(qcd0)
bkg0.Draw("histo")

bkg0.GetXaxis().SetTitle("Min #gamma ID MVA")
bkg0.GetXaxis().SetTitleSize(25)
bkg0.GetXaxis().SetTitleFont(43)
bkg0.GetXaxis().SetTitleOffset(1.75)
bkg0.GetXaxis().SetLabelFont(43)
bkg0.GetXaxis().SetLabelOffset(0.01)
bkg0.GetXaxis().SetLabelSize(25)

bkg0.GetYaxis().SetTitle("Events")
bkg0.GetYaxis().SetTitleSize(25)
bkg0.GetYaxis().SetTitleFont(43)
bkg0.GetYaxis().SetTitleOffset(2.25)
bkg0.GetYaxis().SetLabelFont(43)
bkg0.GetYaxis().SetLabelOffset(0.01)
bkg0.GetYaxis().SetLabelSize(25)


leg = TLegend(0.65,0.75,0.88,0.88)
#leg.AddEntry(bkg0,"Events with 1+ jets")
leg.AddEntry(gj0,"#gamma-jet")
leg.AddEntry(qcd0,"jet-jet")
leg.SetLineWidth (0)
leg.Draw("same")

c1.Update()
c1.cd()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = " Simulation Preliminary"
CMS_lumi.lumi_sqrtS     = "13 TeV"
CMS_lumi.cmsTextSize    = 0.4
CMS_lumi.lumiTextSize   = 0.35
CMS_lumi.extraOverCmsTextSize = 0.8
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(c1, 0, 0)
c1.Update()

c1.SaveAs(outputdir+"MinIDMVA_GJetQCD40andUp_Stack.png")
c1.SaveAs(outputdir+"MinIDMVA_GJetQCD40andUp_Stack.pdf")

print("GJet: ",gj0.Integral())
print("QCD: ",qcd0.Integral())

outfile = TFile("minid_gjetqcd.root", "RECREATE")
outfile.cd()
gj0.Write()
qcd0.Write()
outfile.Close()
