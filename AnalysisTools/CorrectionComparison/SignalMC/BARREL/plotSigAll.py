from ROOT import *
import CMS_lumi

#Argument Parser to input variable and range values
import argparse
def list_of_floats(arg):
    return list(map(float, arg.split(',')))
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='name of variable as x-axis label')
parser.add_argument('--label', type=str, help='end of file name to indicate which variable is used')
parser.add_argument('--binning', type=list_of_floats, help='number of bins,low range,high range')
args = parser.parse_args()

nbins = int(args.binning[0])
binlow = args.binning[1]
binhigh = args.binning[2]
var = args.name
lbl = args.label

#Obtain histogram files
ggh30 = TFile("output/ggh_30_sig.root","READ")
gghuncorr30 = TFile("output/ggh_30_siguncorr.root","READ")
ggh50 = TFile("output/ggh_50_sig.root","READ")
gghuncorr50 = TFile("output/ggh_50_siguncorr.root","READ")
ggh70 = TFile("output/ggh_70_sig.root","READ")
gghuncorr70 = TFile("output/ggh_70_siguncorr.root","READ")

#Create histograms for data, background, and signal, as well as stacked histo for all backgrounds
sig30 = ggh30.Get("ggh_all")
sig30uncorr = gghuncorr30.Get("ggh_alluncorr")
sig50 = ggh50.Get("ggh_all")
sig50uncorr = gghuncorr50.Get("ggh_alluncorr")
sig70 = ggh70.Get("ggh_all")
sig70uncorr = gghuncorr70.Get("ggh_alluncorr")

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()
c1.SetLeftMargin(0.11)
c1.SetBottomMargin(0.17)

sig70.SetXTitle(var)
sig70.GetXaxis().SetTitleSize(25)
sig70.GetXaxis().SetTitleFont(43)
sig70.GetXaxis().SetTitleOffset(1.9)
sig70.GetXaxis().SetLabelFont(43)
sig70.GetXaxis().SetLabelSize(25)
sig70.GetXaxis().SetLabelOffset(0.02)

sig70.GetYaxis().SetTitle("Events")
sig70.GetYaxis().SetTitleSize(25)
sig70.GetYaxis().SetTitleFont(43)
sig70.GetYaxis().SetTitleOffset(1.25)
sig70.GetYaxis().SetLabelFont(43)
sig70.GetYaxis().SetLabelSize(25)

sig70.SetLineColor(kTeal+3)
sig70.SetLineWidth(2)
sig70.Draw("histsame")

sig70uncorr.SetLineColor(kTeal-5)
sig70uncorr.SetLineWidth(2)
sig70uncorr.SetLineStyle(2)
sig70uncorr.Draw("histsame")

sig50.SetLineColor(kAzure)
sig50.SetLineWidth(2)
sig50.Draw("histsame")

sig50uncorr.SetLineColor(kAzure-4)
sig50uncorr.SetLineWidth(2)
sig50uncorr.SetLineStyle(2)
sig50uncorr.Draw("histsame")

sig30.SetLineColor(kViolet-6)
sig30.SetLineWidth(2)
sig30.Draw("histsame")

sig30uncorr.SetLineColor(kViolet-2)
sig30uncorr.SetLineWidth(2)
sig30uncorr.SetLineStyle(2)
sig30uncorr.Draw("histsame")

if ("PhotonIso" in lbl): leg = TLegend(0.53,0.65,0.88,0.85)
elif ("Sieip" in lbl): leg = TLegend(0.58,0.65,0.88,0.85)
else: leg = TLegend(0.18,0.65,0.53,0.85)
leg.SetBorderSize(0)
leg.SetHeader("Barrel |#eta|<1.4442","C")
leg.AddEntry(sig30,"CQR Corrected ggH 30 GeV")
leg.AddEntry(sig30uncorr,"Uncorrected ggH 30 GeV")
leg.AddEntry(sig50,"CQR Corrected ggH 50 GeV")
leg.AddEntry(sig50uncorr,"Uncorrected ggH 50 GeV")
leg.AddEntry(sig70,"CQR Corrected ggH 70 GeV")
leg.AddEntry(sig70uncorr,"Uncorrected ggH 70 GeV")
leg.Draw("same")

c1.Update()
c1.cd()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = " Preliminary Simulation"
CMS_lumi.lumi_sqrtS     = " 2018 (13 TeV)"
CMS_lumi.cmsTextSize    = 0.5
CMS_lumi.lumiTextSize   = 0.35
CMS_lumi.extraOverCmsTextSize = 0.75
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(c1, 0, 0)
c1.Update()

c1.SaveAs("/eos/user/a/atsatsos/www/SigMCDistributions_JUN2024/Sig_"+lbl+"_EB.png")
c1.SaveAs("/eos/user/a/atsatsos/www/SigMCDistributions_JUN2024/Sig_"+lbl+"_EB.pdf")
