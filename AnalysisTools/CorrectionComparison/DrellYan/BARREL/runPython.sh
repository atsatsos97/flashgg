mkdir output

varNames=("dipho_lead_sieie" "dipho_sublead_sieie" "dipho_leadR9" "dipho_subleadR9" "dipho_lead_phoiso" "dipho_sublead_phoiso" "dipho_lead_sieip" "dipho_sublead_sieip" "dipho_lead_s4ratio" "dipho_sublead_s4ratio" "dipho_lead_etawidth" "dipho_sublead_etawidth" "dipho_lead_phiwidth" "dipho_sublead_phiwidth")
graphNames=("Lead #sigma_{i#etai#eta}" "Sublead #sigma_{i#etai#eta}" "Lead R_{9}" "Sublead R_{9}" "Lead Photon Isolation" "Sublead Photon Isolation" "Lead #sigma_{i#etai#phi}" "Sublead #sigma_{i#etai#phi}" "Lead S_{4}" "Sublead S_{4}" "Lead #eta Width" "Sublead #eta Width" "Lead #phi Width" "Sublead #phi Width")
lblNames=("LeadSieie" "SubleadSieie" "LeadR9" "SubleadR9" "LeadPhotonIso" "SubleadPhotonIso" "LeadSieip" "SubleadSieip" "LeadS4Ratio" "SubleadS4Ratio" "LeadEtaWidth" "SubleadEtaWidth" "LeadPhiWidth" "SubleadPhiWidth")
binRanges=("120,0.,0.015" "120,0.,0.015" "140,0.4,1.1" "140,0.4,1.1" "100,0.,5." "100,0.,5." "100,-0.0001,0.0001" "100,-0.0001,0.0001" "140,0.4,1.1" "140,0.4,1.1" "120,0.0,0.03" "120,0.0,0.03" "100,0.0,0.1" "100,0.0,0.1")

for i in ${!varNames[@]}; do
  python makeDY.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python plotDY.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]}
  echo "$i ${varNames[$i]} is done"
done
