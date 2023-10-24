from ROOT import *
from array import array

# Obtain spline from smoothed histogram
file_minID = TFile("minid_gjetqcd.root", "READ")
h_minID_gj0 = file_minID.Get("gj0")
h_minID_qcd0 = file_minID.Get("qcd0")

h_minID = h_minID_gj0.Clone("h_minID")
h_minID.Add(h_minID_qcd0)

h_minID.GetXaxis().SetRangeUser(-0.9,1.0)
#h_minID.GetXaxis().SetRangeUser(-0.9,0.8)
h_minID.Smooth(1, "R")

spline_x = array('f')
spline_y = array('f')
fakePDF = TSpline3(h_minID)

#for j in range(0,1901):
#  nbin = -0.9+(0.001*j)
#  eval = fakePDF.Eval(nbin)
#  spline_x.append(nbin)
#  spline_y.append(eval)
#  print j, eval

check_spline = fakePDF.Eval(0.633)
print "Spline Eval at 0.633: ",check_spline

fakePDF.SaveAs("fake.C");
gROOT.LoadMacro("fake.C++");
fakePDF_reweight = TF1("fakePDF_reweight", "fake(x)",-0.9,1.0)
#fakePDF_reweight = TF1("fakePDF_reweight", "fake(x)",-0.9,0.8)
print "--> NUM: ", fakePDF_reweight.Integral(-0.7,1.0,0.000001)
print "--> DEN: ", fakePDF_reweight.Integral(-0.9,-0.7,0.000001)
print "--> ratio ", fakePDF_reweight.Integral(-0.7,1.0,0.000001)/fakePDF_reweight.Integral(-0.9,-0.7,0.000001)

#Grab data tree
oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/2018Data/2018EGamma.root", "read")
#oldfile = TFile("/eos/user/a/atsatsos/ULFlashGG_Files/UL18_Data_Lowmassxml_v1/output_EGamma_alesauva-UL2018_0-10_6_4-v0-Run2018-0123Merged-12Nov2019_UL2018-981b04a73c9458401b9ffd78fdd24189_USER.root", "read")
newfile = TFile("output_sideband.root","recreate")
newfile.mkdir("tagsDumper")
tagsDumper.cd()
tagsDumper.mkdir("trees")
trees.cd()

for x in range (0,1):
#for x in range (0,4):
  oldtree = oldfile.Get("tagsDumper/trees/Data_13TeV_UntaggedTag_"+str(x))
  nentries = oldtree.GetEntries()

  dipho_leadIDMVA = array('f',[0.])
  dipho_subleadIDMVA = array('f',[0.])
  weight = array('f',[0.])
  event = array('I',[0])
  oldtree.SetBranchAddress("dipho_leadIDMVA",dipho_leadIDMVA)
  oldtree.SetBranchAddress("dipho_subleadIDMVA",dipho_subleadIDMVA)
  oldtree.SetBranchAddress("weight",weight)
  oldtree.SetBranchAddress("event",event)
  
  nEvents_SB = 0
  nEvents_presel = 0

  newtree = oldtree.CloneTree(0)
  for i in range(nentries):
    #if (i == 1000): break
    if (i%10000==0): print i,nentries
    oldtree.GetEntry(i)
    
    #print "Original minID is = \t", min(dipho_leadIDMVA[0],dipho_subleadIDMVA[0])
    #print "Original maxID is = \t", max(dipho_leadIDMVA[0],dipho_subleadIDMVA[0])
 
    #if event is in sideband and also blinded
    if (min(dipho_leadIDMVA[0],dipho_subleadIDMVA[0])<-0.7 and max(dipho_leadIDMVA[0],dipho_subleadIDMVA[0])>-0.7 and event[0]%20 == 0): 
      nEvents_SB+=1
      #reweight the event
      reweight = fakePDF_reweight.Integral(-0.7,max(dipho_leadIDMVA[0],dipho_subleadIDMVA[0]),0.000001)/fakePDF_reweight.Integral(-0.9,-0.7,0.000001)

      #generate and assign a new minimum ID
      fakePDF_minID = TF1("fakePDF_minID","fake(x)",-0.7,max(dipho_leadIDMVA[0],dipho_subleadIDMVA[0]))
      min_ID = fakePDF_minID.GetRandom()
      #print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Event in sideband = ", i
      #print "New minID is = \t", min_ID
      #print "### REWEIGHTING ###"
      #print "reweight NUM = ", fakePDF_reweight.Integral(-0.7,max(dipho_leadIDMVA[0],dipho_subleadIDMVA[0]),0.000001)
      #print "reweight DEN = ", fakePDF_reweight.Integral(-0.9,-0.7,0.000001) 
      #print "reweight TOT = ", reweight
      #print "###################"
      
      weight[0] = weight[0] * reweight
      #print "dipho_leadIDMVA[0] = ", dipho_leadIDMVA[0]
      #print "dipho_subleadIDMVA[0] = ", dipho_subleadIDMVA[0]

      if (dipho_leadIDMVA[0] < dipho_subleadIDMVA[0]):         
        dipho_leadIDMVA[0] = min_ID
      else:
        dipho_subleadIDMVA[0] = min_ID

      newtree.Fill()

    else:
      nEvents_presel+=1
      #print "@@@@@ NO SIDEBAND EVENT!"
    

  print "----------------------------------------------------"
  print "@@@@@ Total number of entries is = ", nentries
  print "@@@@@ nEvents in the sideband region = ", nEvents_SB
  print "@@@@@ nEvents in the preselec region = ", nEvents_presel
  print "----------------------------------------------------"
  newtree.AutoSave()

del oldfile
del newfile
