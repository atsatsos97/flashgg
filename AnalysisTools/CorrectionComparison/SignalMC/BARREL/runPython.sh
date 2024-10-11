mkdir output

varNames=("dipho_lead_sieie" "dipho_sublead_sieie" "dipho_leadR9" "dipho_subleadR9" "dipho_lead_phoiso" "dipho_sublead_phoiso" "dipho_lead_sieip" "dipho_sublead_sieip" "dipho_lead_s4ratio" "dipho_sublead_s4ratio")
graphNames=("Lead #sigma_{i#etai#eta}" "Sublead #sigma_{i#etai#eta}" "Lead R_{9}" "Sublead R_{9}" "Lead Photon Isolation" "Sublead Photon Isolation" "Lead #sigma_{i#etai#phi}" "Sublead #sigma_{i#etai#phi}" "Lead S_{4}" "Sublead S_{4}")
lblNames=("LeadSieie" "SubleadSieie" "LeadR9" "SubleadR9" "LeadPhotonIso" "SubleadPhotonIso" "LeadSieip" "SubleadSieip" "LeadS4Ratio" "SubleadS4Ratio")
binRanges=("60,0.,0.015" "60,0.,0.015" "70,0.4,1.1" "70,0.4,1.1" "50,0.,5." "50,0.,5." "50,-0.0001,0.0001" "50,-0.0001,0.0001" "70,0.4,1.1" "70,0.4,1.1")

for i in ${!varNames[@]}; do
  python makeSig.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python plotSig.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]} --mass "30"
  python plotSig.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]} --mass "50"
  python plotSig.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]} --mass "70"
  python makeSigAll.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python plotSigAll.py --name "${graphNames[$i]}" --binning ${binRanges[$i]} --label ${lblNames[$i]}
  echo "$i ${varNames[$i]} is done"
done
