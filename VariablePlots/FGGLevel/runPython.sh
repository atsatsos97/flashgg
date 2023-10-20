varNames=("dipho_mass" "leadPt" "subleadPt" "leadEta" "subleadEta" "dipho_pt" "dipho_sumpt" "diphoMVA" "dipho_leadIDMVA" "dipho_subleadIDMVA" "dipho_lead_ptoM" "dipho_sublead_ptoM" "dipho_leadEta" "dipho_subleadEta" "vtxprob" "cosphi" "dipho_lead_phoiso" "dipho_sublead_phoiso" "dipho_lead_sieie" "dipho_sublead_sieie" "sigmaMrvoM" "sigmaMwvoM")
lblNames=("Mass" "LeadPt" "SubleadPt" "LeadEta" "SubleadEta" "DiphotonPt" "DiphotonSumPt" "DiphoMVA" "LeadIDMVA" "SubleadIDMVA" "LeadScaledPt" "SubleadScaledPt" "DiphoLeadEta" "DiphoSubleadEta" "VtxProb" "CosPhi" "LeadPhotonIso" "SubleadPhotonIso" "LeadSieie" "SubleadSieie" "SigmaRV" "SigmaWV")
binRanges=("60,0.,120." "100,0.,600." "100,0.,600." "60,-3.,3." "60,-3.,3." "100,0.,800." "100,0.,1000." "100,-1.,1." "100,-1.,1." "100,-1.,1." "100,0.,4." "100,0.,4." "60,-3.,3." "60,-3.,3." "101,0.,1.01" "50,-1.,1." "100,0.,4." "100,0.,4." "40,0.,0.04" "40,0.,0.04" "50,0.,0.05" "50,0.,0.05")

for i in ${!varNames[@]}; do
  python makeBkg040.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeBkg4080.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeBkg80Inf.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeData.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python makeSig.py --name ${varNames[$i]} --binning ${binRanges[$i]}
  python plotDataSigBkg.py --name ${varNames[$i]} --binning ${binRanges[$i]} --label ${lblNames[$i]}
  python plotDataSigBkg_log.py --name ${varNames[$i]} --binning ${binRanges[$i]} --label ${lblNames[$i]}
  echo "$i ${varNames[$i]} is done"
done
