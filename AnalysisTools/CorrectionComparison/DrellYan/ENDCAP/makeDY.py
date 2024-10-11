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

#DYMC
DY = TFile("/eos/home-a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Sep2024_DataBDT_DYtoLL/MergedRoot/allZee.root","READ")
DY_t0 = DY.Get("tagsDumper/trees/DYToLL_13TeV_UntaggedTag_0")

#Create histograms
DY_all = TH1F("DY_all","DY_all",nbins,binlow,binhigh)
DY_all.Sumw2()

DY_alluncorr = TH1F("DY_alluncorr","DY_alluncorr",nbins,binlow,binhigh)
DY_alluncorr.Sumw2()

#Weighted: abs(weight)*(CMS_hgg_mass>0)
#Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
DY_t0.Draw(var+">>DY_all","weight*(CMS_hgg_mass>80 && CMS_hgg_mass<100 && abs(leadEta)>1.566 && abs(subleadEta)>1.566)","goff")
DY_t0.Draw(var+"_uncorr>>DY_alluncorr","weight*(CMS_hgg_mass>80 && CMS_hgg_mass<100 && abs(leadEta)>1.566 && abs(subleadEta)>1.566)","goff")

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

DY_all.SetLineColor(0)
DY_all.GetYaxis().SetTitle("Events Accepted")
DY_all.SaveAs("output/DY.root")

DY_alluncorr.SetLineColor(1)
DY_alluncorr.GetYaxis().SetTitle("Events Accepted")
DY_alluncorr.SaveAs("output/DY_uncorr.root")

print "DY: ",DY_all.Integral()
print "DY: ",DY_alluncorr.Integral()
