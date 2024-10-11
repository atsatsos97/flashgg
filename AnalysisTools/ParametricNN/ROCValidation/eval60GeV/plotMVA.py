from ROOT import *
import CMS_lumi

lmdf = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Feb2024_LowMassBDT_MassHypInput/EGamma_Summer20UL.root","READ")
#pnrdf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/out_all2018Data_bkg_newSamples.root","READ")
#pnrdf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat/out_all2018Data_bkg_newSamplesFlat.root","READ")
pnrdf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat_evaluateAt60GeV/out_all2018Data_bkg_newSamplesFlat.root","READ")
lmdt0 = lmdf.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")
pnrdt0 = pnrdf.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_0")

for i in range(10,75,5):
  #Signal
  lmf = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Feb2024_LowMassBDT_MassHypInput/ggh_M"+str(i)+".root","READ")
#  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/out_ggH_M"+str(i)+"_newSamples.root","READ")
#  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat/out_ggH_M"+str(i)+"_newSamplesFlat.root","READ")
  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat_evaluateAt60GeV/out_ggH_M"+str(i)+"_newSamplesFlat.root","READ")

  lmt0 = lmf.Get("tagsDumper/trees/ggh_"+str(i)+"_13TeV_UntaggedTag_0")
  pnrt0 = pnrf.Get("tagsDumper/trees/ggh_"+str(i)+"_13TeV_UntaggedTag_0")

  #Create histograms
  lm = TH1F("lm","lm",80,-1.0,1.0)
  lm.Sumw2()
  pnr = TH1F("pnr","pnr",80,-1.0,1.0)
  pnr.Sumw2()

  lmd = TH1F("lmd","lmd",80,-1.0,1.0)
  lmd.Sumw2()
  pnrd = TH1F("pnrd","pnrd",80,-1.0,1.0)
  pnrd.Sumw2()

  #Weighted: weight*(CMS_hgg_mass>0)
  lmt0.Draw("diphoMVA>>lm","weight*(CMS_hgg_mass>0) && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7","goff")
  pnrt0.Draw("NNScore>>pnr","weight*(CMS_hgg_mass>0) && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7","goff")

  masslow = 0.9*i
  masshigh = 1.1*i

  #Weighted: weight*(CMS_hgg_mass>0)
  lmdt0.Draw("diphoMVA>>lmd","weight*(CMS_hgg_mass>"+str(masslow)+" && CMS_hgg_mass<"+str(masshigh)+") && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7","goff")
  pnrdt0.Draw("NNScore>>pnrd","weight*(CMS_hgg_mass>"+str(masslow)+" && CMS_hgg_mass<"+str(masshigh)+") && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7","goff")

  if (lm.Integral() != 0): lm.Scale(1.0/lm.Integral())
  if (lmd.Integral() != 0): lmd.Scale(1.0/lmd.Integral())
  if (pnr.Integral() != 0): pnr.Scale(1.0/pnr.Integral())
  if (pnrd.Integral() != 0): pnrd.Scale(1.0/pnrd.Integral())

  lmd.SetMaximum(1.0)

  #Now we draw it out
  #Lowmass: kTeal+5,+3
  #30 GeV Window: kAzure-2,-6
  #70 GeV: kViolet-2,-6
  #All GeV: kPink-2,-6
  gStyle.SetOptStat(0)
  gStyle.SetOptTitle(0)

  c1 = TCanvas("c1","c1",1200,1200)
  c1.cd()
  c1.SetBottomMargin(0.11)
  c1.SetLeftMargin(0.11)

  #Parametric NN: Nearest
  lmd.SetLineColor(kViolet-2)
  lmd.SetLineWidth(3)
  lmd.SetLineStyle(2)
  lmd.Draw("hist")

  lmd.SetXTitle("Diphoton MVA")
  lmd.GetXaxis().SetTitleSize(25)
  lmd.GetXaxis().SetTitleFont(43)
  lmd.GetXaxis().SetTitleOffset(2.0)
  lmd.GetXaxis().SetLabelFont(43)
  lmd.GetXaxis().SetLabelSize(25)
  lmd.GetXaxis().SetLabelOffset(0.02)

  lmd.GetYaxis().SetTitle("A.U.")
  lmd.GetYaxis().SetTitleSize(25)
  lmd.GetYaxis().SetTitleFont(43)
  lmd.GetYaxis().SetTitleOffset(2.25)
  lmd.GetYaxis().SetLabelFont(43)
  lmd.GetYaxis().SetLabelSize(25)

  lm.SetLineColor(kViolet-6)
  lm.SetLineWidth(2)
  lm.Draw("histsame")

  #Parametric NN: Random
  pnrd.SetLineColor(kAzure-2)
  pnrd.SetLineWidth(3)
  pnrd.SetLineStyle(2)
  pnrd.Draw("histsame")

  pnr.SetLineColor(kAzure-6)
  pnr.SetLineWidth(2)
  pnr.Draw("histsame")

  leg = TLegend(0.2,0.5,0.55,0.8)
  leg.SetBorderSize(0)
  leg.AddEntry(lm,"Lowmass BDT on Signal")
  leg.AddEntry(pnr,"Parametric NN on Signal")
  leg.AddEntry(lmd,"Lowmass BDT on Data")
  leg.AddEntry(pnrd,"Parametric NN on Data")
  leg.Draw("same")

  c1.Update()
  c1.cd()

  #CMS lumi stuff
  CMS_lumi.writeExtraText = True
  CMS_lumi.extraText      = "Preliminary"
  CMS_lumi.lumi_sqrtS     = str(i)+" GeV, 2018 (13 TeV)"
  CMS_lumi.cmsTextSize    = 0.4
  CMS_lumi.lumiTextSize   = 0.3
  CMS_lumi.extraOverCmsTextSize = 0.75
  CMS_lumi.relPosX = 0.12
  CMS_lumi.CMS_lumi(c1, 0, 0)
  c1.Update()

  c1.SaveAs("output/DiphoMVA_"+str(i)+".png")
  c1.SaveAs("output/DiphoMVA_"+str(i)+".pdf")

  print(pnr.Integral())
  print(pnrd.Integral())
