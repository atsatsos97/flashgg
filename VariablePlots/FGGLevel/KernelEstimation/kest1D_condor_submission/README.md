# Condor submission setup

### Preparation of the sideband tree based on a 2D fake pdf obtained using the Kernel estimation method.

   **Preliminary setup**:
   - Work in an lxplus8 area
   - Recommended CMSSW version: CMSSW_12_6_5

   **Available files in the repo**:
   - =submit_job.submit=: submission file containing the configuration for the condor job and calling the executable `chunk_reweight_with_multiKest.py`. It is configured to generate 10000 jobs with an automatic assignment of the job ID. Alternatively, =submission.sh= can be used to specify a loop with the desidered number of jobs to be produced and a manual assignment of the job ID.
   - =chunk_reweight_with_multiKest.py=: executable containing the code for the actual reweighting and generation of the new minimum photon ID.

   The input file is the 2018 data file, that is used to extract the sideband region defined as events with a minimum photon ID between [-0.9, -0.7]:
   `/eos/user/e/elfontan/DiPhotonAnalysis/diphotonBDT/NEW_BDT_TRAININGS/DefLM_MCBased/2018Data/2018EGamma.root`.
   All data are used (no blinding).

   The output file for each chunk is saved in:
   `/afs/cern.ch/work/e/elfontan/private/DiPhotonAnalysis/Sep2023_flashGG/CMSSW_12_6_5/src/kest1D_condor_submission/OUTPUT_FILES_MultiKest_MoreBw/output_sideband_kest1D_PF_chunk{process_number}.root`.
   Make sure to update this accordingly.

   The workspace including the pdf used for generating the new minimum is also copied in this directory: `w_hist_MirroLeft_noPF_lowerBw_all.root`.
   The file containing the generated 1D pdfs for each bin (0.1 steps) of maximum photon ID is also copied here: `file_histos_1DfakePdfs_from2D_10k.root`.

   **Submit the jobs**:
   ```
   condor_submit submit_job.submit
   ```
