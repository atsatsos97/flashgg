from ROOT import *
from array import array

#Grab data tree
#oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_040_merged.root", "read")
#oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_all_merged.root", "read")
newfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_4080_merged_PromptFakeFilter_10k.root","recreate")
#oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_80InfHigh_merged.root", "read")
#newfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_80InfHigh_merged_40k.root","recreate")
#oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_80InfLow_merged.root", "read")
#newfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_80InfLow_merged_40k.root","recreate")
#oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_4080_merged.root", "read")
#newfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_4080_merged_40k.root","recreate")
oldfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/gJets_4080_merged_PromptFakeFilter.root", "read")
#newfile = TFile("/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/gJets/skimmed_gJets_4080_merged_PromptFakeFilter.root","recreate")
newfile.mkdir("tagsDumper")
tagsDumper.cd()
tagsDumper.mkdir("trees")
trees.cd()

for x in range (0,1): #change if trees are sorted into categories
  #oldtree = oldfile.Get("tagsDumper/trees/mgg_bkg_13TeV_UntaggedTag_"+str(x))
  oldtree = oldfile.Get("tagsDumper/trees/gjets_promptfake_13TeV_UntaggedTag_"+str(x))
  nentries = oldtree.GetEntries()
  nentries = 10000

  #leadMatchType = array('f',[0.])
  #subleadMatchType = array('f',[0.])
  dipho_lead_prompt = array('f',[0.])
  #dipho_sulead_prompt = array('f',[0.])
  dipho_sublead_prompt = array('f',[0.])
  dipho_leadIDMVA = array('f',[0.])
  dipho_subleadIDMVA = array('f',[0.])
  event = array('I',[0])
  weight = array('f',[0])
  #oldtree.SetBranchAddress("leadMatchType",leadMatchType)
  #oldtree.SetBranchAddress("subleadMatchType",subleadMatchType)
  oldtree.SetBranchAddress("dipho_lead_prompt",dipho_lead_prompt)
  oldtree.SetBranchAddress("dipho_sublead_prompt",dipho_sublead_prompt)
  #oldtree.SetBranchAddress("dipho_sulead_prompt",dipho_sulead_prompt)
  oldtree.SetBranchAddress("dipho_leadIDMVA",dipho_leadIDMVA)
  oldtree.SetBranchAddress("dipho_subleadIDMVA",dipho_subleadIDMVA)
  oldtree.SetBranchAddress("event",event)
  oldtree.SetBranchAddress("weight",weight)

  dipho_minIDMVA = array('f',[0.])
  dipho_maxIDMVA = array('f',[0.])
  newtree = TTree("gjets_promptfake_13TeV_UntaggedTag_"+str(x),"gjets_promptfake_13TeV_UntaggedTag_"+str(x))
  newtree.Branch('event', event, 'event/I')
  newtree.Branch('weight', weight, 'weight/F')
  #newtree.Branch('leadMatchType', leadMatchType, 'leadMatchType/F')
  #newtree.Branch('subleadMatchType', subleadMatchType, 'subleadMatchType/F')
  newtree.Branch('dipho_lead_prompt', dipho_lead_prompt, 'dipho_lead_prompt/F')
  #newtree.Branch('dipho_sublead_prompt', dipho_sulead_prompt, 'dipho_sublead_prompt/F')
  newtree.Branch('dipho_sublead_prompt', dipho_sublead_prompt, 'dipho_sublead_prompt/F')
  newtree.Branch('dipho_leadIDMVA', dipho_leadIDMVA, 'dipho_leadIDMVA/F')
  newtree.Branch('dipho_subleadIDMVA', dipho_subleadIDMVA, 'dipho_subleadIDMVA/F')
  newtree.Branch('dipho_minIDMVA', dipho_minIDMVA, 'dipho_minIDMVA/F')
  newtree.Branch('dipho_maxIDMVA', dipho_maxIDMVA, 'dipho_maxIDMVA/F')
  newtree.SetBranchAddress("event",event)
  newtree.SetBranchAddress("weight",weight)
  #newtree.SetBranchAddress("leadMatchType",leadMatchType)
  #newtree.SetBranchAddress("subleadMatchType",subleadMatchType)
  newtree.SetBranchAddress("dipho_lead_prompt",dipho_lead_prompt)
  newtree.SetBranchAddress("dipho_sublead_prompt",dipho_sublead_prompt)
  newtree.SetBranchAddress("dipho_leadIDMVA",dipho_leadIDMVA)
  newtree.SetBranchAddress("dipho_subleadIDMVA",dipho_subleadIDMVA)
  newtree.SetBranchAddress("dipho_minIDMVA",dipho_minIDMVA)
  newtree.SetBranchAddress("dipho_maxIDMVA",dipho_maxIDMVA)

  for i in range(nentries):
    if (i%1000==0): print(i,nentries)
    oldtree.GetEntry(i)
    if (dipho_leadIDMVA[0] < dipho_subleadIDMVA[0]):
      dipho_minIDMVA[0] = dipho_leadIDMVA[0]
      dipho_maxIDMVA[0] = dipho_subleadIDMVA[0]
    else:
      dipho_minIDMVA[0] = dipho_subleadIDMVA[0]
      dipho_maxIDMVA[0] = dipho_leadIDMVA[0]
    newtree.Fill()
  newtree.AutoSave()

del oldfile
del newfile
