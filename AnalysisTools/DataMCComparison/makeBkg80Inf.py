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

#Bkg from 80 to Inf GeV
mgg = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_Oct2023/bkg_dipho/DiPhotonJetsBox_MGG80toInf.root","READ")
gjLow = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_Oct2023/bkg_gjets/GJets_MGG80toInf_low.root","READ")
gjHigh = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_Oct2023/bkg_gjets/GJets_MGG80toInf_high.root","READ")
qcdLow = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_Oct2023/bkg_qcd/QCD_MGG80toInf_low.root","READ")
qcdHigh = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_Oct2023/bkg_qcd/QCD_MGG80toInf_high.root","READ")

mggt0 = mgg.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_0")
gjt0 = gjLow.Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_0")
gju0 = gjHigh.Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_0")
qcdt0 = qcdLow.Get("tagsDumper/trees/qcd_fakefake_13TeV_UntaggedTag_0")
qcdu0 = qcdHigh.Get("tagsDumper/trees/qcd_fakefake_13TeV_UntaggedTag_0")

#Create histograms as well as stacked histo for all backgrounds
mgg80inf = TH1F("mgg80inf","mgg80inf",nbins,binlow,binhigh)
mgg80inf.Sumw2()
gjl80inf = TH1F("gjl80inf","gjl80inf",nbins,binlow,binhigh)
gjl80inf.Sumw2()
gj80inf = TH1F("gj80inf","gj80inf",nbins,binlow,binhigh)
gj80inf.Sumw2()
qcdl80inf = TH1F("qcdl80inf","qcdl80inf",nbins,binlow,binhigh)
qcdl80inf.Sumw2()
qcd80inf = TH1F("qcd80inf","qcd80inf",nbins,binlow,binhigh)
qcd80inf.Sumw2()


#Weighted: abs(weight)*(CMS_hgg_mass>0)
#Sideband/Presel regions: abs(weight)*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)<-0.7)
mggt0.Draw(var+">>mgg80inf","weight*(CMS_hgg_mass>0)","goff")
gjt0.Draw(var+">>gjl80inf","weight*(CMS_hgg_mass>0)","goff")
gju0.Draw(var+">>gj80inf","weight*(CMS_hgg_mass>0)","goff")
qcdt0.Draw(var+">>qcdl80inf","weight*(CMS_hgg_mass>0)","goff")
qcdu0.Draw(var+">>qcd80inf","weight*(CMS_hgg_mass>0)","goff")

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

mgg80inf.SetFillColor(kRed)
mgg80inf.SetLineColor(kBlack)
mgg80inf.GetYaxis().SetTitle("Events Accepted")
mgg80inf.SaveAs("output/mgg_80inf.root")

gj80inf.SetFillColor(kBlue)
gj80inf.SetLineColor(kBlack)
gj80inf.GetYaxis().SetTitle("Events Accepted")
gj80inf.SaveAs("output/gj_80inf.root")

gjl80inf.SetFillColor(kBlue)
gjl80inf.SetLineColor(kBlack)
gjl80inf.GetYaxis().SetTitle("Events Accepted")
gjl80inf.SaveAs("output/gj_low_80inf.root")

qcd80inf.SetFillColor(kYellow)
qcd80inf.SetLineColor(kBlack)
qcd80inf.GetYaxis().SetTitle("Events Accepted")
qcd80inf.SaveAs("output/qcd_80inf.root")

qcdl80inf.SetFillColor(kYellow)
qcdl80inf.SetLineColor(kBlack)
qcdl80inf.GetYaxis().SetTitle("Events Accepted")
qcdl80inf.SaveAs("output/qcd_low_80inf.root")

print("MGG: ",mgg80inf.Integral())
print("GJet: ",gj80inf.Integral())
print("GJetL: ",gjl80inf.Integral())
print("QCD: ",qcd80inf.Integral())
print("QCDL: ",qcdl80inf.Integral())
