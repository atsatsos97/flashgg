from ROOT import *

gStyle.SetOptFit(1)
gStyle.SetOptStat(0)

c_spline = TCanvas("c_spline", "c_spline", 1200, 1000)
c_spline.cd()

file_minID = TFile("minid_gjetqcd.root", "READ")
h_minID_gj0 = file_minID.Get("gj0")
h_minID_qcd0 = file_minID.Get("qcd0")

h_minID_clone = h_minID_gj0.Clone("h_minID")
h_minID.Add(h_minID_qcd0)

h_minID.GetXaxis().SetRangeUser(-0.9,1.0)
#h_minID.GetXaxis().SetRangeUser(-0.9,0.8)

h_minID.Smooth(1, "R")
g_minID = TGraph()

for i in range(1,h_minID.GetNbinsX()+1): g_minID.SetPoint(i-1, h_minID.GetBinCenter(i), h_minID.GetBinContent(i))

check_spline = 0.0
g_spline = TGraph()

for i in range(0,1901):
  nbin = -0.9+(0.001*i)
  check_spline = g_minID.Eval(nbin, 0, "S")
  print nbin,"  ",check_spline
  g_spline.SetPoint(i,nbin,check_spline)

s = TSpline3(h_minID)
check_spline = s.Eval(0.633)
print "Spline Eval at 0.633: ",check_spline

h_minID_clone.GetXaxis().SetTitle("Minimum Photon ID")
h_minID_clone.GetYaxis().SetTitle("Events")
h_minID_clone.SetLineWidth(2)
h_minID_clone.SetLineColor(kRed-9)
h_minID_clone.SetFillColor(kRed-9)
h_minID_clone.Draw("HISTO")
h_minID_clone.SetTitle("Spline Fit of Minimum Photon ID")

g_spline.GetXaxis().SetTitle("Minimum Photon ID")
g_spline.GetYaxis().SetTitle("Events")
g_spline.SetLineWidth(2)
g_spline.SetLineColor(kAzure-2)
g_spline.SetMarkerColor(kAzure-2)
g_spline.Draw("L")
g_spline.SetTitle("Spline Fit of Minimum Photon ID")

g_spline.SaveAs("spline.root")
c_spline.SaveAs("MinID_Spline_GJetQCD40andUp_HistSmooth.png")
c_spline.SaveAs("MinID_Spline_GJetQCD40andUp_HistSmooth.pdf")
