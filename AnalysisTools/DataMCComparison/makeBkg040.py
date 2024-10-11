from ROOT import *

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

#Bkg from 0 to 40 GeV

#Background
mgg = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_DiPhoton_040.root","READ")
gj = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_GJet_040.root","READ")
qcd = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_QCD_040.root","READ")

mggt0 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
gjt0 = gj.Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_0")
qcdt0 = qcd.Get("tagsDumper/trees/qcd_fakefake_13TeV_UntaggedTag_0")

#Create histograms as well as stacked histo for all backgrounds
mgg040 = TH1F("mgg040","mgg040",nbins,binlow,binhigh)
mgg040.Sumw2()
gj040 = TH1F("gj040","gj040",nbins,binlow,binhigh)
gj040.Sumw2()
qcd040 = TH1F("qcd040","qcd040",nbins,binlow,binhigh)
qcd040.Sumw2()

#Weighted: abs(weight)*(CMS_hgg_mass>0)
#Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
mggt0.Draw(var+">>mgg040","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")
gjt0.Draw(var+">>gj040","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")
qcdt0.Draw(var+">>qcd040","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

mgg040.SetFillColor(kRed)
mgg040.SetLineColor(kBlack)
mgg040.GetYaxis().SetTitle("Events Accepted")
mgg040.SaveAs("output/mgg_040.root")

gj040.SetFillColor(kBlue)
gj040.SetLineColor(kBlack)
gj040.GetYaxis().SetTitle("Events Accepted")
gj040.SaveAs("output/gj_040.root")

qcd040.SetFillColor(kYellow)
qcd040.SetLineColor(kBlack)
qcd040.GetYaxis().SetTitle("Events Accepted")
qcd040.SaveAs("output/qcd_040.root")

print("MGG: ",mgg040.Integral())
print("GJet: ",gj040.Integral())
print("QCD: ",qcd040.Integral())
