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

#Bkg from 40 to 80 GeV
mgg = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_DiPhoton_4080.root","READ")
gj = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_GJet_4080.root","READ")
qcd = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/output_QCD_4080.root","READ")

mggt0 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
gjt0 = gj.Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_0")
qcdt0 = qcd.Get("tagsDumper/trees/qcd_fakefake_13TeV_UntaggedTag_0")

#Create histograms as well as stacked histo for all backgrounds
mgg4080 = TH1F("mgg4080","mgg4080",nbins,binlow,binhigh)
mgg4080.Sumw2()
gj4080 = TH1F("gj4080","gj4080",nbins,binlow,binhigh)
gj4080.Sumw2()
qcd4080 = TH1F("qcd4080","qcd4080",nbins,binlow,binhigh)
qcd4080.Sumw2()

#Weighted: abs(weight)*(CMS_hgg_mass>0)
#Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
mggt0.Draw(var+">>mgg4080","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")
gjt0.Draw(var+">>gj4080","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")
qcdt0.Draw(var+">>qcd4080","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

mgg4080.SetFillColor(kRed)
mgg4080.SetLineColor(kBlack)
mgg4080.GetYaxis().SetTitle("Events Accepted")
mgg4080.SaveAs("output/mgg_4080.root")

gj4080.SetFillColor(kBlue)
gj4080.SetLineColor(kBlack)
gj4080.GetYaxis().SetTitle("Events Accepted")
gj4080.SaveAs("output/gj_4080.root")

qcd4080.SetFillColor(kYellow)
qcd4080.SetLineColor(kBlack)
qcd4080.GetYaxis().SetTitle("Events Accepted")
qcd4080.SaveAs("output/qcd_4080.root")

print("MGG: ",mgg4080.Integral())
print("GJet: ",gj4080.Integral())
print("QCD: ",qcd4080.Integral())
