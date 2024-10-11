from ROOT import *
import CMS_lumi
import numpy as np

#Plot ROC Histograms using integrals of signal and background to compute efficiencies
for i in range(10,75,5):
  lm_ROC = TGraph()
  pnr_ROC = TGraph()

  lm_Int = TGraph()
  pnr_Int = TGraph()

  lm_ROC.SetPoint(0,1.0,0.0)
  pnr_ROC.SetPoint(0,1.0,0.0)

  lm_Int.SetPoint(0,1.0,0.0)
  pnr_Int.SetPoint(0,1.0,0.0)

  #Obtain MVA histogram files for signal at different mass points and background at different sliding windows
  lm_sigfile = TFile("output/pnr"+str(i)+".root","READ")
  pnr_sigfile = TFile("output_eval30GeV/pnr"+str(i)+".root","READ")

  lm_sighist = lm_sigfile.Get("pnrr")
  pnr_sighist = pnr_sigfile.Get("pnrr")

  lm_sigeffden = lm_sighist.Integral()
  pnr_sigeffden = pnr_sighist.Integral()

  lm_bkgfile = TFile("output/pnr"+str(i)+"data.root","READ")
  pnr_bkgfile = TFile("output_eval30GeV/pnr"+str(i)+"data.root","READ")

  lm_bkghist = lm_bkgfile.Get("pnrr")
  pnr_bkghist = pnr_bkgfile.Get("pnrr")

  lm_bkgrejden = lm_bkghist.Integral()
  pnr_bkgrejden = pnr_bkghist.Integral()

  nbins = 2000

  for j in range(0,nbins+1):
    lm_sigeffnum = lm_sighist.Integral(j,nbins)
    lm_bkgrejnum = lm_bkghist.Integral(j,nbins)
    lm_sigeff = lm_sigeffnum/lm_sigeffden
    lm_bkgrej = 1.0-(lm_bkgrejnum/lm_bkgrejden)
    lm_ROC.SetPoint(j+1, lm_sigeff,lm_bkgrej)
    lm_Int.SetPoint(j+1, lm_sigeff,lm_bkgrej)

    pnr_sigeffnum = pnr_sighist.Integral(j,nbins)
    pnr_bkgrejnum = pnr_bkghist.Integral(j,nbins)
    pnr_sigeff = pnr_sigeffnum/pnr_sigeffden
    pnr_bkgrej = 1.0-(pnr_bkgrejnum/pnr_bkgrejden)
    pnr_ROC.SetPoint(j+1, pnr_sigeff,pnr_bkgrej)
    pnr_Int.SetPoint(j+1, pnr_sigeff,pnr_bkgrej)

  lm_Int.SetPoint(nbins+2,0.0,0.0)
  pnr_Int.SetPoint(nbins+2,0.0,0.0)

  #Now we draw it out
  gStyle.SetOptStat(0)
  gStyle.SetOptTitle(0)

  c1 = TCanvas("c1","c1",1600,1600)
  c1.cd()
  c1.SetBottomMargin(0.11)
  c1.SetLeftMargin(0.11)

  lm_ROC.SetLineColor(kViolet-2)
  lm_ROC.SetLineWidth(3)
  lm_ROC.Draw("AL")

  lm_ROC.GetXaxis().SetTitle("Signal Efficiency")
  lm_ROC.GetXaxis().SetTitleSize(40)
  lm_ROC.GetXaxis().SetTitleFont(43)
  lm_ROC.GetXaxis().SetTitleOffset(1.2)
  lm_ROC.GetXaxis().SetLabelFont(43)
  lm_ROC.GetXaxis().SetLabelSize(30)
  lm_ROC.GetXaxis().SetLabelOffset(0.013)

  lm_ROC.GetYaxis().SetTitle("Background Rejection")
  lm_ROC.GetYaxis().SetTitleSize(40)
  lm_ROC.GetYaxis().SetTitleFont(43)
  lm_ROC.GetYaxis().SetTitleOffset(1.2)
  lm_ROC.GetYaxis().SetLabelFont(43)
  lm_ROC.GetYaxis().SetLabelSize(30)
  lm_ROC.GetYaxis().SetLabelOffset(0.013)

  pnr_ROC.SetLineColor(kAzure-2)
  pnr_ROC.SetLineWidth(3)
  pnr_ROC.Draw("L")

  leg = TLegend(0.15,0.15,0.65,0.40)
  leg.SetHeader(str(i)+" GeV Mass Hypothesis","C")
  leg.SetTextSize(0.032)
  leg.SetBorderSize(0)
  leg.AddEntry(lm_ROC,"Current PNN AUC = "+str(round(lm_Int.Integral(),3)))
  leg.AddEntry(pnr_ROC,"PNN Evaluated at 30 GeV AUC = "+str(round(pnr_Int.Integral(),3)))
  leg.Draw("same")

  c1.Update()

#CMS lumi stuff
#  CMS_lumi.writeExtraText = True
#  CMS_lumi.extraText      = "  Preliminary"
#  CMS_lumi.lumi_sqrtS     = "2018 (13 TeV)"
#  CMS_lumi.cmsTextSize    = 0.5
#  CMS_lumi.lumiTextSize   = 0.4
#  CMS_lumi.extraOverCmsTextSize = 0.80
#  CMS_lumi.relPosX = 0.12
#  CMS_lumi.CMS_lumi(c1, 0, 0)
#  c1.Update()

  c1.cd()
  c1.SaveAs("output_eval30GeV/ROC_M"+str(i)+"_PNN30Comp.png")
  c1.SaveAs("output_eval30GeV/ROC_M"+str(i)+"_PNN30Comp.pdf")
