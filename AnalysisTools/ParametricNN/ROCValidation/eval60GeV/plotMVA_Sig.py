from ROOT import *
import CMS_lumi

for i in range(10,75,5):
  #Signal
  lmf = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/NewReleaseFiles/Feb2024_LowMassBDT_MassHypInput/ggh_M"+str(i)+".root","READ")
#  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/out_ggH_M"+str(i)+"_newSamples.root","READ")
#  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat/out_ggH_M"+str(i)+"_newSamplesFlat.root","READ")
  pnrf = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NTUPLES_May2024/nearest_flat_evaluateAt60GeV/out_ggH_M"+str(i)+"_newSamplesFlat.root","READ")

  lmt0 = lmf.Get("tagsDumper/trees/ggh_"+str(i)+"_13TeV_UntaggedTag_0")
  pnrt0 = pnrf.Get("tagsDumper/trees/ggh_"+str(i)+"_13TeV_UntaggedTag_0")

  #Create histograms
  lmr = TH1F("lmr","lmr",2000,-1.0,1.0)
  lmr.Sumw2()
  pnrr = TH1F("pnrr","pnrr",2000,-1.0,1.0)
  pnrr.Sumw2()

  lm = TH1F("lm","lm",80,-1.0,1.0)
  lm.Sumw2()
  pnr = TH1F("pnr","pnr",80,-1.0,1.0)
  pnr.Sumw2()

  #Weighted: weight*(CMS_hgg_mass>0)
  lmt0.Draw("diphoMVA>>lm","weight*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  pnrt0.Draw("NNScore>>pnr","weight*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  lmt0.Draw("diphoMVA>>lmr","weight*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")
  pnrt0.Draw("NNScore>>pnrr","weight*(CMS_hgg_mass>0 && min(dipho_leadIDMVA,dipho_subleadIDMVA)>-0.7)","goff")

  lmr.SaveAs("output/lm"+str(i)+".root")
  pnrr.SaveAs("output/pnr"+str(i)+".root")

  #Now we draw it out
  gStyle.SetOptStat(0)
  gStyle.SetOptTitle(0)

  c1 = TCanvas("c1","c1",1200,1200)
  c1.cd()
  c1.SetBottomMargin(0.11)
  c1.SetLeftMargin(0.11)

  lm.SetLineColor(kViolet-2)
  lm.SetLineWidth(2)
  lm.Draw("histsame")

  lm.SetXTitle("Diphoton MVA")
  lm.GetXaxis().SetTitleSize(25)
  lm.GetXaxis().SetTitleFont(43)
  lm.GetXaxis().SetTitleOffset(2.0)
  lm.GetXaxis().SetLabelFont(43)
  lm.GetXaxis().SetLabelSize(25)
  lm.GetXaxis().SetLabelOffset(0.02)

  lm.GetYaxis().SetTitle("Events")
  lm.GetYaxis().SetTitleSize(25)
  lm.GetYaxis().SetTitleFont(43)
  lm.GetYaxis().SetTitleOffset(2.25)
  lm.GetYaxis().SetLabelFont(43)
  lm.GetYaxis().SetLabelSize(25)

  pnr.SetLineColor(kAzure-2)
  pnr.SetLineWidth(2)
  pnr.Draw("histsame")

  pnr.SetXTitle("Diphoton MVA")
  pnr.GetXaxis().SetTitleSize(25)
  pnr.GetXaxis().SetTitleFont(43)
  pnr.GetXaxis().SetTitleOffset(2.0)
  pnr.GetXaxis().SetLabelFont(43)
  pnr.GetXaxis().SetLabelSize(25)
  pnr.GetXaxis().SetLabelOffset(0.02)

  pnr.GetYaxis().SetTitle("Events")
  pnr.GetYaxis().SetTitleSize(25)
  pnr.GetYaxis().SetTitleFont(43)
  pnr.GetYaxis().SetTitleOffset(2.25)
  pnr.GetYaxis().SetLabelFont(43)
  pnr.GetYaxis().SetLabelSize(25)

  leg = TLegend(0.2,0.6,0.45,0.8)
  leg.SetTextSize(0.018)
  leg.SetBorderSize(0)
  leg.AddEntry(lm,"Lowmass BDT")
  leg.AddEntry(pnr,"Parametric NN")
  leg.Draw("same")

  c1.Update()
  c1.cd()

#CMS lumi stuff
  CMS_lumi.writeExtraText = True
  CMS_lumi.extraText      = "Preliminary"
  CMS_lumi.lumi_sqrtS     = "13 TeV"
  CMS_lumi.cmsTextSize    = 0.4
  CMS_lumi.lumiTextSize   = 0.3
  CMS_lumi.extraOverCmsTextSize = 0.75
  CMS_lumi.relPosX = 0.12
  CMS_lumi.CMS_lumi(c1, 0, 0)
  c1.Update()

  c1.SaveAs("output/DiphoMVA_ggh"+str(i)+".png")
  c1.SaveAs("output/DiphoMVA_ggh"+str(i)+".pdf")

  print "Lowmass BDT "+str(i)+": ",lm.Integral()
  print "Parametric NN "+str(i)+": ",pnr.Integral()
