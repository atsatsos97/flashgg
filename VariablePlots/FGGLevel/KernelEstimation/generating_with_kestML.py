from ROOT import *
import CMS_lumi
import ROOT, array, random, copy
from ROOT import TCanvas, TFile, TH1, TH1F, TF1, gSystem, TChain
import ROOT, array, CMSGraphics, CMS_lumi, random, copy
from ROOT import TFile, TTree, TList
import argparse
import sys
import os

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

argparser = argparse.ArgumentParser(description='Parser used for non default arguments', formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=True)
argparser.add_argument('--outdir', dest='outdir', default='./', help='Output dir')
argparser.add_argument('--maxid', dest='maxid', default='./', help='Output dir')

args = argparser.parse_args()
outputdir = args.outdir
maxphoid = args.maxid


# Open the file with the workspace
# --------------------------------
ws = TFile.Open("/afs/cern.ch/work/e/elfontan/private/DiPhotonAnalysis/Sep2023_flashGG/CMSSW_12_6_5/src/KernelEstimation/w_ML_inclusive.root")

# Load the workspace from the file
# --------------------------------
w = ws.Get("w_MinMaxPhoId")

if not w:
    print("Error: Could not load the workspace from the file.")
    exit(1)

# Retrieve the observable variable(s) and PDFs from the workspace
# ---------------------------------------------------------------
dipho_minIDMVA = w.var("dipho_minIDMVA")
dipho_maxIDMVA = w.var("dipho_maxIDMVA")
kestML = w.pdf("kestML_minPhoId")

if not (dipho_minIDMVA or dipho_maxIDMVA):
    print("Error: Observable 'dipho_minIDMVA' not found in the workspace.")
    exit(1)

if dipho_minIDMVA:
    print("Variable Name:", dipho_minIDMVA.GetName())
else:
    print("Variable dipho_minIDMVA not found in the workspace.")

if dipho_maxIDMVA:
    print("Variable Name:", dipho_maxIDMVA.GetName())
else:
    print("Variable dipho_maxIDMVA not found in the workspace.")

if not kestML:
    print("Error: PDF 'kestMLminPhoId' not found in the workspace.")
    exit(1)


# ----------------------------------------------------                           
# Generating a fake pdf for each maximum photon ID bin                                                
# ----------------------------------------------------                                                                       
list_maxphoid_names = ["m0p65","m0p55","m0p45","m0p35","m0p25","m0p15","m0p05","p0p05","p0p15","p0p25","p0p35","p0p45","p0p55","p0p65","p0p75","p0p85","p0p95"]
list_maxphoid_mean = [-0.65, -0.55, -0.45, -0.35, -0.25, -0.15, -0.05, 0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
list_maxphoid_min = [-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.00, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
list_maxphoid_max = [-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.00, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

fakePdfs = {}
outfile = TFile("histos_forReweighting/kestML_gJets040_4080/histofile_fakePdfs.root", "RECREATE")

for i in range(len(list_maxphoid_names)):
    # Create a unique name for each dataset
    dataset_name = f"data_kestML_{list_maxphoid_names[i]}"

    # Use the pdf to generate events
    # ------------------------------
    #dipho_maxIDMVA.setVal(float(list_maxphoid_mean[i]))
    #dipho_maxIDMVA.setConstant(True)
    dipho_minIDMVA.setConstant(False)
    data_kestML = kestML.generate(RooArgSet(dipho_minIDMVA), 200000) 
    data_kestML.SetName(dataset_name)
    
    # Store the dataset in the dictionary
    fakePdfs[dataset_name] = data_kestML    
    
    # Create and fill a histogram with the generated values
    # -----------------------------------------------------
    h_gendata_name = "h_gendata_kestML"+list_maxphoid_names[i]
    h_gendata_kestML = TH1F(h_gendata_name, "Generated Data kestML", 95, -0.9, 1.0)
    for h in range(data_kestML.numEntries()):
        minIDMVA = data_kestML.get(h).getRealValue("dipho_minIDMVA")
        h_gendata_kestML.Fill(minIDMVA)
        
    # Open a rootfile and save the histograms for the reweighting
    # -----------------------------------------------------------
    h_gendata_kestML.Write()

outfile.Close()

# Create and save new RooDataSets in a workspace
# ----------------------------------------------
ws = ROOT.RooWorkspace("w_fakePdfs")

# Import variables and PDF into the workspace
# -------------------------------------------
for dataset_name, data_kestML in fakePdfs.items():
    getattr(ws, 'import')(data_kestML)

getattr(ws, 'import')(kestML)
ws.Print()

# Print the workspace contents
# ----------------------------
ws.writeToFile("KernelEstimation/setFakePdfs_1dMirrorLeft.root")
#ws.writeToFile("KernelEstimation/setFakePdfs_"+list_maxphoid_names[i]+".root")
