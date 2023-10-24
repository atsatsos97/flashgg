#include "RooRealVar.h"
#include "RooConstVar.h"
#include "RooArgList.h"
#include "RooDataSet.h"
#include "RooDataHist.h"
#include "RooGaussian.h"
#include "RooPolynomial.h"
#include "RooKeysPdf.h"
#include "RooNDKeysPdf.h"
#include "RooProdPdf.h"
#include "RooWorkspace.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TLegend.h"
#include "TH1.h"
#include "RooPlot.h"
#include <TROOT.h> 
#include <iostream>
#include <vector>
#include <string>

using namespace RooFit;
 
void phoIdMinMax_kernelestimation_pfFilter()
{
  // [1] INPUT FILE WITH HISTOGRAMS TO FIT SIGNAL and BACKGROUND
  TFile* file = NULL;
  file=TFile::Open("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/histoFakePdf_gJets_040_4080_skimmed.root");
  //file=TFile::Open("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_all_merged_MinMaxPhoId.root");
  //file=TFile::Open("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_040_4080_merged_PromptFakeFilter.root");

  if (!file || file->IsZombie()) {
    std::cerr << "Error: Unable to open the ROOT file." << std::endl;
    return 1; // Return an error code to indicate failure.
  }

  TTree* tree = (TTree*)file->Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_0");
  
  TH1D* h_minIDMVA = new TH1D("h_minIDMVA", "h_minIDMVA", 38, -0.9, 1);
  TH1D* h_maxIDMVA = new TH1D("h_maxIDMVA", "h_maxIDMVA", 38, -0.9, 1);
  //TH1D* h_minIDMVA = new TH1D("h_minIDMVA", "h_minIDMVA", 38, -0.9, 1);
  //TH1D* h_maxIDMVA = new TH1D("h_maxIDMVA", "h_maxIDMVA", 38, -0.9, 1);

  tree->Draw("dipho_minIDMVA>>h_minIDMVA","dipho_minIDMVA <=1.0","goff");
  tree->Draw("dipho_maxIDMVA>>h_maxIDMVA","dipho_maxIDMVA <=1.0","goff");

  if (!h_minIDMVA || !h_maxIDMVA) {
    std::cerr << "Error: Unable to retrieve histograms from the file." << std::endl;
    return 1; // Return an error code to indicate failure.
  }

  // Get the total number of events in the TTree
  Long64_t nEntries = tree->GetEntries();
  float min_maxPhoId = -0.7;
  float max_maxPhoId = -0.3;
  // Convert the double to a string
  std::string min_maxPhoIdStr = std::to_string(min_maxPhoId);
  std::string max_maxPhoIdStr = std::to_string(max_maxPhoId);

  // Variables to hold branch values
  Float_t dipho_minIDMVA;
  Float_t dipho_maxIDMVA;
  
  // Connect TBranches to variables
  tree->SetBranchAddress("dipho_minIDMVA", &dipho_minIDMVA);
  tree->SetBranchAddress("dipho_maxIDMVA", &dipho_maxIDMVA);
  
  // Loop over the events in the TTree
  for (Long64_t ev = 0; ev < nEntries; ev++) {
    //std::cout << "Event " << ev << std::endl;
    tree->GetEntry(ev);
    //std::cout << "dipho_maxIDMVA " << dipho_maxIDMVA << std::endl;
    if (dipho_maxIDMVA >= min_maxPhoId && dipho_maxIDMVA < min_maxPhoId)
      {
	// ----------------------------------------------------                                                           
	// Generating a fake pdf for each maximum photon ID bin                                                              
	// ----------------------------------------------------                                                              
	RooRealVar dipho_minIDMVA("dipho_minIDMVA", "dipho_minIDMVA", -0.9, 1);
	RooRealVar dipho_maxIDMVA("dipho_maxIDMVA", "dipho_maxIDMVA", -0.9, 1);
	//dipho_minIDMVA.setBins(95);
	//dipho_maxIDMVA.setBins(95);
	dipho_minIDMVA.setBins(38);
	dipho_maxIDMVA.setBins(38);
	
	// Import unbinned data from a TTree branch
	// ----------------------------------------
	RooDataSet* data_dipho_minIDMVA = new RooDataSet("data_dipho_minIDMVA","data_dipho_minIDMVA",tree,dipho_minIDMVA);
	RooDataSet* data_dipho_maxIDMVA = new RooDataSet("data_dipho_maxIDMVA","data_dipho_maxIDMVA",tree,dipho_maxIDMVA);
	
	RooPlot *frame0 = dipho_minIDMVA.frame(Title("Minimum photon ID (1D fake PDF)"));
	//data_dipho_minIDMVA->plotOn(frame0, Binning(95));
	data_dipho_minIDMVA->plotOn(frame0, Binning(38));
	
	RooPlot *frame1 = dipho_maxIDMVA.frame(Title("Maximum photon ID (1D fake PDF)"));
	//data_dipho_maxIDMVA->plotOn(frame1, Binning(95));
	data_dipho_maxIDMVA->plotOn(frame1, Binning(38));
	
	RooKeysPdf kestML_minPhoId("kestML_minPhoId", "kestML_minPhoId", dipho_minIDMVA, *data_dipho_minIDMVA, RooKeysPdf::MirrorLeft);
	RooKeysPdf kestML_maxPhoId("kestML_minPhoId", "kestML_maxPhoId", dipho_maxIDMVA, *data_dipho_maxIDMVA, RooKeysPdf::MirrorLeft);
	kestML_minPhoId.plotOn(frame0, LineWidth(3), LineColor(kCyan+2));
	kestML_maxPhoId.plotOn(frame1, LineWidth(3), LineColor(kCyan+2));
	/*RooKeysPdf kestML2_minPhoId("kestML2_minPhoId", "kestML2_minPhoId", dipho_minIDMVA, *data_dipho_minIDMVA, RooKeysPdf::MirrorLeft, 2);
	  RooKeysPdf kestML2_maxPhoId("kestML2_minPhoId", "kestML2_maxPhoId", dipho_maxIDMVA, *data_dipho_maxIDMVA, RooKeysPdf::MirrorLeft, 2);
	  RooKeysPdf kestML08_minPhoId("kestML08_minPhoId", "kestML08_minPhoId", dipho_minIDMVA, *data_dipho_minIDMVA, RooKeysPdf::MirrorLeft, 0.8);
	  RooKeysPdf kestML08_maxPhoId("kestML08_minPhoId", "kestML08_maxPhoId", dipho_maxIDMVA, *data_dipho_maxIDMVA, RooKeysPdf::MirrorLeft, 0.8);
	  RooKeysPdf kestML05_minPhoId("kestML05_minPhoId", "kestML05_minPhoId", dipho_minIDMVA, *data_dipho_minIDMVA, RooKeysPdf::MirrorLeft, 0.5);
	  RooKeysPdf kestML05_maxPhoId("kestML05_minPhoId", "kestML05_maxPhoId", dipho_maxIDMVA, *data_dipho_maxIDMVA, RooKeysPdf::MirrorLeft, 0.5);
	  kestML2_minPhoId.plotOn(frame0, LineWidth(3), LineStyle(kDashed), LineColor(kMagenta-7));
	  kestML2_maxPhoId.plotOn(frame1, LineWidth(3), LineStyle(kDashed), LineColor(kMagenta-7));
	  kestML08_minPhoId.plotOn(frame0, LineWidth(3), LineStyle(kDashed), LineColor(kAzure-4));
	  kestML08_maxPhoId.plotOn(frame1, LineWidth(3), LineStyle(kDashed), LineColor(kAzure-4));
	  kestML05_minPhoId.plotOn(frame0, LineWidth(3), LineStyle(kDashed), LineColor(kOrange-3));
	  kestML05_maxPhoId.plotOn(frame1, LineWidth(3), LineStyle(kDashed), LineColor(kOrange-3));
	*/
	
	TCanvas *c_min = new TCanvas("phoIdMin_kernelestimation", "phoIdMin_kernelestimation", 1000, 1000);
	c_min->cd();
	c_min->SetLeftMargin(2.0);
	frame0->GetYaxis()->SetTitleOffset(1.6);
	frame0->GetXaxis()->SetTitle("Minimum #gamma ID");
	frame0->Draw();
	TLegend *leg_min = new TLegend(0.2,0.6,0.8,0.88);
	leg_min->SetFillColor(kWhite);
	leg_min->SetLineColor(kWhite);
	TLegendEntry *entry1 = leg_min->AddEntry("kestML_minPhoId","Kernel estimation: mirror left","L");
	entry1->SetLineColor(kCyan+2);
	//TLegendEntry *entry2 = leg_min->AddEntry("kestML2_minPhoId","Kernel estimation: mirror left, bw 2","L");
	//TLegendEntry *entry3 = leg_min->AddEntry("kestML08_minPhoId","Kernel estimation: mirror left, bw 0.8","L");
	//TLegendEntry *entry4 = leg_min->AddEntry("kestML05_minPhoId","Kernel estimation: mirror left, bw 0.5","L");
	//entry2->SetLineColor(kMagenta-7);
	//entry3->SetLineColor(kAzure-4);
	//entry4->SetLineColor(kOrange-3);
	leg_min->Draw("same");
	c_min->SaveAs(Form("/eos/user/e/elfontan/www/LowMassDiPhoton/diphotonBDT/testing_reweighting/2D_fakePDF_kernelEstimation/1Dpdf_MinPhoId_gJetsPFfilter_%s_%s.root", min_maxPhoIdStr.c_str(), max_maxPhoIdStr.c_str()));  

	TCanvas *c_max = new TCanvas("phoIdMax_kernelestimation", "phoIdMax_kernelestimation", 1000, 1000);
	c_max->cd();
	c_max->SetLeftMargin(2.0);
	frame1->GetYaxis()->SetTitleOffset(1.6);
	frame1->GetXaxis()->SetTitle("Maximum #gamma ID");
	frame1->Draw();
	leg_min->Draw("same");
	c_max->SaveAs(Form("/eos/user/e/elfontan/www/LowMassDiPhoton/diphotonBDT/testing_reweighting/2D_fakePDF_kernelEstimation/1Dpdf_MaxPhoId_gJetsPFfilter_%s_%s.root", min_maxPhoIdStr.c_str(), max_maxPhoIdStr.c_str()));  
	
	//------------------------
	// Save into ROOWorkspace
	//------------------------
	RooWorkspace w_MinMaxPhoId("w_MinMaxPhoId", "");
	w_MinMaxPhoId.import(*data_dipho_minIDMVA);
	w_MinMaxPhoId.import(*data_dipho_maxIDMVA);
	w_MinMaxPhoId.import(kestML_minPhoId);
	w_MinMaxPhoId.import(kestML_maxPhoId);
	//w_MinMaxPhoId.writeToFile("KernelEstimation/w_ML_inclusive.root");
	w_MinMaxPhoId.writeToFile(Form("KernelEstimation/w_ML_maxPhoId_%s_%s.root", min_maxPhoIdStr.c_str(), max_maxPhoIdStr.c_str()));
    }
  }
}

//std::vector<std::string> list_maxphoid_names = {
//						 "m0p65", "m0p55", "m0p45", "m0p35", "m0p25", "m0p15", "m0p05", "p0p05", "p0p15",
//						 "p0p25", "p0p35", "p0p45", "p0p55", "p0p65", "p0p75", "p0p85", "p0p95"};
// std::vector<double> list_lower = {-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};
// std::vector<double> list_upper = {-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
