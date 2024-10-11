from ROOT import *
import CMS_lumi
import numpy as np

#Plot ROC Histograms using integrals of signal and background to compute efficiencies
mca_Asimov15 = TGraph()
mca_Asimov20 = TGraph()
mca_Asimov30 = TGraph()
mca_Asimov40 = TGraph()
mca_Asimov45 = TGraph()
mca_Asimov50 = TGraph()
mca_Asimov55 = TGraph()
mca_Asimov60 = TGraph()
mca_Asimov70 = TGraph()

#nEvents = [102177.0, 102829.0, 100223.0, 100752.0, 99832.0, 190139.0]
#nEvents_sign = [49044.96, 47301.34, 48107.04, 56421.12, 59899.2, 117886.18]
#gen = [1832.06, 1345.64, 1003.56, 775.896, 614.566, 505.814] #can be assigned negatively to events

mass = [15,20,30,40,45,50,55,60,70]

for i in mass:
#  m = (i-20)/10
  sig_mca = []
  bkg_mca = []
  sigeff_mca = []
  bkgrej_mca = []
  mva_mca = []
  asimov_mca = []

  #Obtain MVA histogram files for signal at different mass points and background at different sliding windows
  mca_sigfile = TFile("output/pnr"+str(i)+".root","READ")
  mca_sighist = mca_sigfile.Get("pnrr")
  mca_sigeffden = mca_sighist.Integral()

  mca_bkgfile = TFile("output/pnr"+str(i)+"data.root","READ")
  mca_bkghist = mca_bkgfile.Get("pnrr")
  mca_bkgrejden = mca_bkghist.Integral()

  nbins = 2000

#  lumi_diff = nEvents[m]/nEvents_sign[m]
#  eff = mca_sigeffden * lumi_diff/(1.06 * gen[m] * 1000.0)
  eff = mca_sigeffden/(1.06 * 1000.0)
  print " "
  print "Mass: ",i
  print "Event Efficiency: ", eff

  for j in range(0,nbins):
    mca_sigeffnum = mca_sighist.Integral(j,nbins)
    mca_bkgrejnum = mca_bkghist.Integral(j,nbins)
    mca_sigeff = mca_sigeffnum/mca_sigeffden
    mca_bkgrej = 1.0-(mca_bkgrejnum/mca_bkgrejden)

    sig_mca.append(mca_sigeffnum)
    bkg_mca.append(mca_bkgrejnum)
    sigeff_mca.append(mca_sigeff)
    bkgrej_mca.append(mca_bkgrej)
    mva = (j-1000)*0.001

    mca_sigeffnumscale = mca_sigeffnum*54400.0*eff/mca_sigeffden

    if (mca_bkgrejnum != 0.0): asimov = np.sqrt(2*((mca_sigeffnumscale+mca_bkgrejnum)*np.log(1+mca_sigeffnumscale/mca_bkgrejnum)-mca_sigeffnumscale))
    else: asimov = 0.0
    mva_mca.append(mva)
    asimov_mca.append(asimov)

    if (j >= 1000 and i==15): mca_Asimov15.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==20): mca_Asimov20.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==30): mca_Asimov30.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==40): mca_Asimov40.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==45): mca_Asimov45.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==50): mca_Asimov50.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==55): mca_Asimov55.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==60): mca_Asimov60.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs
    if (j >= 1000 and i==70): mca_Asimov70.SetPoint(j-1000, mva, asimov) #Use only if working with parametric NNs

#Now we draw it out
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c1 = TCanvas("c1","c1",1200,1200)
c1.cd()
c1.SetBottomMargin(0.11)
c1.SetLeftMargin(0.11)

mca_Asimov70.SetLineColor(kViolet-2)
mca_Asimov70.SetLineWidth(2)
mca_Asimov70.Draw("AL")

mca_Asimov70.GetXaxis().SetTitle("NN Score")
mca_Asimov70.GetXaxis().SetTitleSize(35)
mca_Asimov70.GetXaxis().SetTitleFont(43)
mca_Asimov70.GetXaxis().SetTitleOffset(1.5)
mca_Asimov70.GetXaxis().SetLabelFont(43)
mca_Asimov70.GetXaxis().SetLabelSize(35)
mca_Asimov70.GetXaxis().SetLabelOffset(0.02)

mca_Asimov70.GetYaxis().SetTitle("Approx. Asimov Significance")
mca_Asimov70.GetYaxis().SetTitleSize(35)
mca_Asimov70.GetYaxis().SetTitleFont(43)
mca_Asimov70.GetYaxis().SetTitleOffset(1.5)
mca_Asimov70.GetYaxis().SetLabelFont(43)
mca_Asimov70.GetYaxis().SetLabelSize(35)

mca_Asimov60.SetLineColor(kAzure-2)
mca_Asimov60.SetLineWidth(2)
mca_Asimov60.Draw("L")

mca_Asimov55.SetLineColor(kCyan+1)
mca_Asimov55.SetLineWidth(2)
mca_Asimov55.Draw("L")

mca_Asimov50.SetLineColor(kTeal+3)
mca_Asimov50.SetLineWidth(2)
mca_Asimov50.Draw("L")

mca_Asimov45.SetLineColor(kGreen+1)
mca_Asimov45.SetLineWidth(2)
mca_Asimov45.Draw("L")

mca_Asimov40.SetLineColor(kYellow+1)
mca_Asimov40.SetLineWidth(2)
mca_Asimov40.Draw("L")

mca_Asimov30.SetLineColor(kOrange-3)
mca_Asimov30.SetLineWidth(2)
mca_Asimov30.Draw("L")

mca_Asimov20.SetLineColor(kRed)
mca_Asimov20.SetLineWidth(2)
mca_Asimov20.Draw("L")

mca_Asimov15.SetLineColor(kPink+9)
mca_Asimov15.SetLineWidth(2)
mca_Asimov15.Draw("L")

cat01 = TLine(0.8,0,0.8,12.0)
cat01.SetLineColor(28)
cat01.SetLineWidth(3)
cat01.SetLineStyle(2)
cat01.Draw("same")

cat12 = TLine(0.6,0,0.6,12.0)
cat12.SetLineColor(28)
cat12.SetLineWidth(3)
cat12.SetLineStyle(2)
cat12.Draw("same")

#cat23 = TLine(0.5,0,0.5,12.0)
#cat23.SetLineColor(28)
#cat23.SetLineWidth(3)
#cat23.SetLineStyle(2)
#cat23.Draw("same")

#cat34 = TLine(0.64,0,0.64,12.0)
#cat34.SetLineColor(28)
#cat34.SetLineWidth(3)
#cat34.SetLineStyle(2)
#cat34.Draw("same")

leg = TLegend(0.74,0.65,0.86,0.89)
leg.SetTextSize(0.025)
leg.SetBorderSize(0)
leg.AddEntry(mca_Asimov15,"15 GeV")
leg.AddEntry(mca_Asimov20,"20 GeV")
leg.AddEntry(mca_Asimov30,"30 GeV")
leg.AddEntry(mca_Asimov40,"40 GeV")
leg.AddEntry(mca_Asimov45,"45 GeV")
leg.AddEntry(mca_Asimov50,"50 GeV")
leg.AddEntry(mca_Asimov55,"55 GeV")
leg.AddEntry(mca_Asimov60,"60 GeV")
leg.AddEntry(mca_Asimov70,"70 GeV")
leg.AddEntry(cat01,"Cat. Bounds")
leg.Draw("same")

c1.Update()

#CMS lumi stuff
CMS_lumi.writeExtraText = True
CMS_lumi.extraText      = " Preliminary"
CMS_lumi.lumi_sqrtS     = "2018 (13 TeV)"
CMS_lumi.cmsTextSize    = 0.5
CMS_lumi.lumiTextSize   = 0.4
CMS_lumi.extraOverCmsTextSize = 0.75
CMS_lumi.relPosX = 0.12
CMS_lumi.CMS_lumi(c1, 0, 0)
c1.Update()

c1.cd()
c1.SaveAs("output/AsimovAll.png")
c1.SaveAs("output/AsimovAll.pdf")
