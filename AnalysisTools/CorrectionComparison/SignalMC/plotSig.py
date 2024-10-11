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
parser.add_argument('--mass', type=str, help='mass point to plot')
args = parser.parse_args()

nbins = int(args.binning[0])
binlow = args.binning[1]
binhigh = args.binning[2]
var = args.name
lbl = args.label
mass = args.mass

#Obtain histogram files
ggh = TFile("output/ggh_"+mass+"_sig.root","READ")
gghuncorr = TFile("output/ggh_"+mass+"_siguncorr.root","READ")

#Create histograms for data, background, and signal, as well as stacked histo for all backgrounds
sig = ggh.Get("ggh_all")
siguncorr = gghuncorr.Get("ggh_alluncorr")

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()

#c1.SetLeftMargin(0.11)
#c1.SetBottomMargin(0.17)

pad1 = TPad("pad1","pad1", 0, 0.35, 1, 1.0)
pad1.Draw()
pad1.cd()
#pad1.SetLogy()
pad1.SetBottomMargin(0.)
pad1.SetLeftMargin(0.11)

sig.GetXaxis().SetLabelSize(0)

sig.GetYaxis().SetTitle("Events")
sig.GetYaxis().SetTitleSize(25)
sig.GetYaxis().SetTitleFont(43)
sig.GetYaxis().SetTitleOffset(1.25)
sig.GetYaxis().SetLabelFont(43)
sig.GetYaxis().SetLabelSize(25)

sig.SetLineColor(kAzure)
sig.SetLineWidth(2)
sig.Draw("histsame")

siguncorr.SetLineColor(kAzure-4)
siguncorr.SetLineWidth(2)
siguncorr.SetLineStyle(2)
siguncorr.Draw("histsame")

if ("PhotonIso" in lbl or "Sieie" in lbl): leg = TLegend(0.53,0.70,0.88,0.85)
elif ("Sieip" in lbl): leg = TLegend(0.58,0.70,0.88,0.85)
else: leg = TLegend(0.18,0.70,0.53,0.85)
leg.SetBorderSize(0)
leg.AddEntry(sig,"CQR Corrected ggH "+mass+" GeV")
leg.AddEntry(siguncorr,"Uncorrected ggH "+mass+" GeV")
leg.Draw("same")

c1.Update()
c1.cd()

pad2 = TPad("pad2","pad2", 0, 0.05, 1, 0.35)
pad2.SetGridy()
pad2.Draw()
pad2.cd()
pad2.SetTopMargin(0.)
pad2.SetBottomMargin(0.17)
pad2.SetLeftMargin(0.11)

rp = TH1F(sig.Clone("rp")) #clone the data
rp.SetLineColor(kBlack)
rp.SetMinimum(0.5)
rp.SetMaximum(2.)
rp.SetStats(0)
rp.Divide(siguncorr)   #divide by MC
rp.SetMarkerStyle(24)
rp.SetTitle("") 

rp.SetYTitle("Corr/Uncorr")
rp.GetYaxis().SetNdivisions(505)
rp.GetYaxis().SetTitleSize(25)
rp.GetYaxis().SetTitleFont(43)
rp.GetYaxis().SetTitleOffset(2.25)
rp.GetYaxis().SetLabelFont(43)
rp.GetYaxis().SetLabelSize(25)

rp.SetXTitle(var)
rp.GetXaxis().SetTitleSize(25)
rp.GetXaxis().SetTitleFont(43)
rp.GetXaxis().SetTitleOffset(1.9)
rp.GetXaxis().SetLabelFont(43)
rp.GetXaxis().SetLabelSize(25)
rp.GetXaxis().SetLabelOffset(0.02)

rp.Draw("ep")

c1.Update()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = " Preliminary Simulation"
CMS_lumi.lumi_sqrtS     = mass+" GeV, 2018 (13 TeV)"
CMS_lumi.cmsTextSize    = 0.5
CMS_lumi.lumiTextSize   = 0.35
CMS_lumi.extraOverCmsTextSize = 0.75
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(pad1, 0, 0)
c1.Update()

c1.SaveAs("/eos/user/a/atsatsos/www/SigMCDistributions_JUN2024/Sig_"+lbl+"_"+mass+"GeV.png")
c1.SaveAs("/eos/user/a/atsatsos/www/SigMCDistributions_JUN2024/Sig_"+lbl+"_"+mass+"GeV.pdf")

print("GGH Corr: ",sig.Integral())
print("GGH Uncorr: ",siguncorr.Integral())
