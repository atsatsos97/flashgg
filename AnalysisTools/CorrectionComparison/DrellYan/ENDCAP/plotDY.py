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
DY = TFile("output/DY.root","READ")
DYuncorr = TFile("output/DY_uncorr.root","READ")

#Create histograms for data, background, and signal, as well as stacked histo for all backgrounds
DYhist = DY.Get("DY_all")
DYhistuncorr = DYuncorr.Get("DY_alluncorr")

DYmax = DYhist.GetMaximum()
DYmaxuncorr = DYhistuncorr.GetMaximum()
DYhist.SetMaximum(1.2*max(DYmax,DYmaxuncorr))

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1600,1200)
c1.cd()
if ("PhotonIso" in lbl): c1.SetLogy()
c1.SetLeftMargin(0.11)
c1.SetBottomMargin(0.17)

DYhist.SetXTitle(var)
DYhist.GetXaxis().SetTitleSize(40)
DYhist.GetXaxis().SetTitleFont(43)
DYhist.GetXaxis().SetTitleOffset(1.9)
DYhist.GetXaxis().SetLabelFont(43)
DYhist.GetXaxis().SetLabelSize(40)
DYhist.GetXaxis().SetLabelOffset(0.02)

DYhist.GetYaxis().SetTitle("Events")
DYhist.GetYaxis().SetTitleSize(40)
DYhist.GetYaxis().SetTitleFont(43)
DYhist.GetYaxis().SetTitleOffset(1.25)
DYhist.GetYaxis().SetLabelFont(43)
DYhist.GetYaxis().SetLabelSize(40)

DYhist.SetLineColorAlpha(kGreen+2,0.7)
DYhist.SetLineWidth(2)
DYhist.Draw("histsame")

DYhistuncorr.SetLineColor(kRed-7)
DYhistuncorr.SetLineWidth(2)
DYhistuncorr.SetLineStyle(2)
DYhistuncorr.Draw("histsame")

if ("PhotonIso" in lbl or "Width" in lbl): leg = TLegend(0.53,0.70,0.88,0.85)
elif ("Sieip" in lbl): leg = TLegend(0.58,0.70,0.88,0.85)
else: leg = TLegend(0.18,0.70,0.53,0.85)
leg.SetHeader("Endcap |#eta|>1.566","C")
leg.SetBorderSize(0)
leg.AddEntry(DYhist,"CQR Corrected DY")
leg.AddEntry(DYhistuncorr,"Uncorrected DY")
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

c1.SaveAs("/eos/user/a/atsatsos/www/DYMCDistributions_SEP2024/DY_"+lbl+"_EE.png")
c1.SaveAs("/eos/user/a/atsatsos/www/DYMCDistributions_SEP2024/DY_"+lbl+"_EE.pdf")
