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

#Signal MC using ggH
masses = ["30","50","70"]
color = 0
for i in masses:
  color+=1

  ggh = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Mar2024_DataBDT_AllMC_SigExtIncluded/ggh_M"+i+".root","READ")

  ggh_t0 = ggh.Get("tagsDumper/trees/ggh_"+i+"_13TeV_UntaggedTag_0")

  #Create histograms
  ggh_all = TH1F("ggh_all","ggh_all",nbins,binlow,binhigh)
  ggh_all.Sumw2()

  ggh_alluncorr = TH1F("ggh_alluncorr","ggh_alluncorr",nbins,binlow,binhigh)
  ggh_alluncorr.Sumw2()

  #Weighted: abs(weight)*(CMS_hgg_mass>0)
  #Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
  ggh_t0.Draw(var+">>ggh_all","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")
  ggh_t0.Draw(var+"_uncorr>>ggh_alluncorr","weight*(CMS_hgg_mass>0 && CMS_hgg_mass<80)","goff")

  gStyle.SetOptStat(0)
  gStyle.SetOptTitle(0)

  ggh_all.SetLineColor(color)
  ggh_all.GetYaxis().SetTitle("Events Accepted")
  ggh_all.SaveAs("output/ggh_"+i+"_sig.root")

  ggh_alluncorr.SetLineColor(color+1)
  ggh_alluncorr.GetYaxis().SetTitle("Events Accepted")
  ggh_alluncorr.SaveAs("output/ggh_"+i+"_siguncorr.root")

  print i+" GeV: ",ggh_all.Integral()
  print i+" GeV: ",ggh_alluncorr.Integral()
