from ROOT import *
import CMS_lumi
import numpy as np

#Plot ROC Histograms using integrals of signal and background to compute efficiencies
mca_MVA = TGraph()
mca_SIG = TGraph()
mca_BKG = TGraph()

mca_MVA.SetMaximum(1.0)
mca_MVA.SetMinimum(0.0)
mca_SIG.SetMaximum(1.0)
mca_SIG.SetMinimum(0.0)
mca_BKG.SetMaximum(1.0)
mca_BKG.SetMinimum(0.0)

for i in range(10,75,5):
  sig_mca = []
  bkg_mca = []
  sigeff_mca = []
  bkgrej_mca = []
  mva_mca = []
  asimov_mca = []

  commonsigeff = 0.0
  commonbkgrej = 0.0
  commonmva = 0.0

  #Obtain MVA histogram files for signal at different mass points and background at different sliding windows
  mca_sigfile = TFile("output/pnr"+str(i)+".root","READ")
  mca_sighist = mca_sigfile.Get("pnrr")
  mca_sigeffden = mca_sighist.Integral()

  mca_bkgfile = TFile("output/pnr"+str(i)+"data.root","READ")
  mca_bkghist = mca_bkgfile.Get("pnrr")
  mca_bkgrejden = mca_bkghist.Integral()

  nbins = 2000

  for j in range(0,nbins):
      mca_sigeffnum = mca_sighist.Integral(j,nbins)
      mca_bkgrejnum = mca_bkghist.Integral(j,nbins)
      mca_sigeff = mca_sigeffnum/mca_sigeffden
      mca_bkgrej = 1.0-(mca_bkgrejnum/mca_bkgrejden)

      sig_mca.append(mca_sigeffnum)
      bkg_mca.append(mca_bkgrejnum)
      sigeff_mca.append(mca_sigeff)
      bkgrej_mca.append(mca_bkgrej)
      mva = j*0.001-1
      if (mca_bkgrejnum != 0.0): asimov = np.sqrt(2*((mca_sigeffnum+mca_bkgrejnum)*np.log(1+mca_sigeffnum/(mca_bkgrejnum))-mca_sigeffnum))
      else: asimov = 0.0
      mva_mca.append(mva)
      asimov_mca.append(asimov)

#      if (round(mva,3) == 0.780):
      if (round(mva,3) == 0.880):
        commonsigeff = mca_sigeff
        commonbkgrej = mca_bkgrej
        commonmva = mva

#      if (round(mva,3) == 0.880):
#        commonsigeff -= mca_sigeff
#        commonbkgrej += (1-mca_bkgrej)
#        commonmva += mva

  mca_MVA.SetPoint((i-10)/5, i, commonmva) #Use only if working with parametric NNs
  mca_SIG.SetPoint((i-10)/5, i, commonsigeff) #Use only if working with parametric NNs
  mca_BKG.SetPoint((i-10)/5, i, commonbkgrej) #Use only if working with parametric NNs

  print " "
  print "Mass: ",i
  print "MVA Response: ", commonmva
  print "Signal Eff.: ", commonsigeff
  print "Background Rej.: ", commonbkgrej

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()
c1.SetBottomMargin(0.11)
c1.SetLeftMargin(0.11)

mca_SIG.SetLineColor(kTeal+3)
mca_SIG.SetLineWidth(3)
mca_SIG.SetMarkerStyle(7)
mca_SIG.SetMarkerColor(kTeal+3)
mca_SIG.Draw("ALP")

mca_SIG.GetXaxis().SetTitle("Diphoton Mass [GeV]")
mca_SIG.GetXaxis().SetTitleSize(25)
mca_SIG.GetXaxis().SetTitleFont(43)
mca_SIG.GetXaxis().SetTitleOffset(1.5)
mca_SIG.GetXaxis().SetLabelFont(43)
mca_SIG.GetXaxis().SetLabelSize(25)
mca_SIG.GetXaxis().SetLabelOffset(0.02)

mca_SIG.GetYaxis().SetTitleSize(25)
mca_SIG.GetYaxis().SetTitleFont(43)
mca_SIG.GetYaxis().SetTitleOffset(1.5)
mca_SIG.GetYaxis().SetLabelFont(43)
mca_SIG.GetYaxis().SetLabelSize(25)

mca_BKG.SetLineColor(kPink-6)
mca_BKG.SetLineWidth(3)
mca_BKG.SetMarkerStyle(7)
mca_BKG.SetMarkerColor(kPink-6)
mca_BKG.Draw("LP")

leg = TLegend(0.5,0.5,0.8,0.65)
leg.SetTextSize(0.025)
leg.SetBorderSize(0)
leg.SetHeader("Category 0 (MVA Score > 0.88)","C")
#leg.SetHeader("Category 1 (0.78 < MVA Score < 0.88)","C")
leg.AddEntry(mca_SIG,"Signal Efficiency")
leg.AddEntry(mca_BKG,"Background Rejection")
leg.Draw("same")

c1.Update()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = "Preliminary"
CMS_lumi.lumi_sqrtS     = "2018 (13 TeV)"
CMS_lumi.cmsTextSize    = 0.4
CMS_lumi.lumiTextSize   = 0.3
CMS_lumi.extraOverCmsTextSize = 0.75
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(c1, 0, 0)
c1.Update()

c1.cd()
c1.SaveAs("output/ParaNN_EffCat0.png")
c1.SaveAs("output/ParaNN_EffCat0.pdf")
