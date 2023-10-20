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
data = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_Data_Lowmassxml_v1/output_EGamma_alesauva-UL2018_0-10_6_4-v0-Run2018-12Nov2019_UL2018-981b04a73c9458401b9ffd78fdd24189_USER.root","READ")

#Obtain each class tree from each file
dat0 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
dat1 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_1")
dat2 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_2")
dat3 = data.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_3")

#Create histograms
data0 = TH1F("data0","data0",nbins,binlow,binhigh)
data0.Sumw2()
data1 = TH1F("data1","data1",nbins,binlow,binhigh)
data1.Sumw2()
data2 = TH1F("data2","data2",nbins,binlow,binhigh)
data2.Sumw2()
data3 = TH1F("data3","data3",nbins,binlow,binhigh)
data3.Sumw2()

#Sideband/Presel regions: CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7 && event%20==0
dat0.Draw(var+">>data0","CMS_hgg_mass>0 && event%20==0","goff")
dat1.Draw(var+">>data1","CMS_hgg_mass>0 && event%20==0","goff")
dat2.Draw(var+">>data2","CMS_hgg_mass>0 && event%20==0","goff")
dat3.Draw(var+">>data3","CMS_hgg_mass>0 && event%20==0","goff")

data0.Add(data1)
data0.Add(data2)
data0.Add(data3)

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1000)
c1.cd()
c1.SetBottomMargin(0.17)

data0.SetLineColor(1)
data0.Draw("ep")
data0.GetYaxis().SetTitle("Events/(GeV)")
data0.SaveAs("data.root")
