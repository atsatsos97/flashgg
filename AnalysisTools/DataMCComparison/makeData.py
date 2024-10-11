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

#Data
data = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/EGamma_All_Summer20UL.root","READ")

#Obtain each class tree from each file
dat0 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")

#Create histograms
data0 = TH1F("data0","data0",nbins,binlow,binhigh)
data0.Sumw2()

#Sideband/Presel regions: CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7 && event%20==0
dat0.Draw(var+">>data0","CMS_hgg_mass>0 && CMS_hgg_mass<80 && event%20==0","goff")

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

data0.SetLineColor(1)
data0.Draw("ep")
data0.GetYaxis().SetTitle("Accepted Events")
data0.SaveAs("output/data.root")
