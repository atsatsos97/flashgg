mkdir -p output

varNames=("dipho_mass" "leadPt" "subleadPt" "leadEta" "subleadEta" "dipho_pt" "dipho_sumpt" "diphoMVA" "dipho_leadIDMVA" "dipho_subleadIDMVA" "dipho_lead_ptoM" "dipho_sublead_ptoM" "dipho_leadEta" "dipho_subleadEta" "vtxprob" "cosphi" "dipho_lead_phoiso" "dipho_sublead_phoiso" "dipho_lead_sieie" "dipho_sublead_sieie" "sigmaMrvoM" "sigmaMwvoM" "dipho_lead_sigmaEoE" "dipho_sublead_sigmaEoE")
graphNames=("m_{#gamma#gamma}" "Lead p_{T}" "Sublead p_{T}" "Lead #eta" "Sublead #eta" "p^{T}_{#gamma#gamma}" "#Sigma p_{T}" "Diphoton MVA" "Lead #gamma ID MVA" "Sublead #gamma ID MVA" "Lead p_{T}/m_{#gamma#gamma}" "Sublead p_{T}/m_{#gamma#gamma}" "Diphoton Lead #eta" "Diphoton Sublead #eta" "p_{vtx}" "cos(#phi)" "Lead #gamma Isolation" "Sublead #gamma Isolation" "Lead #sigma_{i #eta i #eta}" "Sublead #sigma_{i #eta i #eta}" "#sigma_{RV}" "#sigma_{WV}" "Lead #sigma_{E}/E" "Sublead #sigma_{E}/E")
lblNames=("Mass" "LeadPt" "SubleadPt" "LeadEta" "SubleadEta" "DiphotonPt" "DiphotonSumPt" "DiphoMVA" "LeadIDMVA" "SubleadIDMVA" "LeadScaledPt" "SubleadScaledPt" "DiphoLeadEta" "DiphoSubleadEta" "VtxProb" "CosPhi" "LeadPhotonIso" "SubleadPhotonIso" "LeadSieie" "SubleadSieie" "SigmaRV" "SigmaWV" "LeadSigmaEoE" "SubleadSigmaEoE")
binRanges=("80,0.,80." "100,0.,400." "100,0.,400." "60,-3.,3." "60,-3.,3." "100,0.,600." "100,0.,400." "100,-1.,1." "100,-1.,1." "100,-1.,1." "100,0.,4." "100,0.,4." "60,-3.,3." "60,-3.,3." "101,0.,1.01" "50,-1.,1." "100,0.,4." "100,0.,4." "40,0.,0.04" "40,0.,0.04" "50,0.,0.05" "50,0.,0.05" "50,0.,0.05" "50,0.,0.05")

for i in ${!varNames[@]}; do
  python makeBkg040.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeBkg4080.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeData.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeSig.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python plotDataSigBkg.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]}
  python plotDataSigBkg_log.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]}
  echo "$i ${varNames[$i]} is done"
done
