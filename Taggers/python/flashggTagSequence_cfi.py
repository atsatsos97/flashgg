import FWCore.ParameterSet.Config as cms
from flashgg.Taggers.flashggDiPhotonMVA_cfi import flashggDiPhotonMVA
from flashgg.Taggers.flashggVBFMVA_cff import flashggVBFMVA,flashggVBFDiPhoDiJetMVA
from flashgg.Taggers.flashggTags_cff import *
from flashgg.Taggers.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
from flashgg.Taggers.flashggTagSorter_cfi import flashggTagSorter
from flashgg.Taggers.flashggDifferentialPhoIdInputsCorrection_cfi import flashggDifferentialPhoIdInputsCorrection, setup_flashggDifferentialPhoIdInputsCorrection
flashggUntagged.Boundaries     = cms.vdouble(-0.364,0.334,0.753)
#flashggUntagged.Boundaries     = cms.vdouble(-1.0,0.334,0.792)

flashggTagSorter.TagPriorityRanges = cms.VPSet(
#  cms.PSet(TagName = cms.InputTag('flashggVBFTag')),
  cms.PSet(TagName = cms.InputTag('flashggUntagged'))
)
flashggTagSorter.MassCutUpper=cms.double(120.)
flashggTagSorter.MassCutLower=cms.double(60.)
def flashggPrepareTagSequence(process, options):


    setup_flashggDifferentialPhoIdInputsCorrection(process, options)
    flashggPreselectedDiPhotons.src = "flashggDifferentialPhoIdInputsCorrection"

    flashggTagSequence = cms.Sequence(flashggDifferentialPhoIdInputsCorrection
                                      * flashggPreselectedDiPhotons
                                      * flashggDiPhotonMVA
                                      * flashggUnpackedJets
#                                      * flashggVBFMVA
#                                      * flashggVBFDiPhoDiJetMVA
                                      * ( flashggUntagged
                                      #                                  *( flashggSigmaMoMpToMTag
#                                          + flashggVBFTag
#                                          + flashggTTHDiLeptonTag
#                                          + flashggTTHLeptonicTag
#					  + flashggTHQLeptonicTag
#                                     + flashggTTHHadronicTTag                                      
#                                     + flashggTTHHadronicLTag                                      
#                                          + flashggTTHHadronicTag
                                      #############old VH tags##############
                                      #                  + flashggVHEtTag
                                      #                  + flashggVHLooseTag
                                      #                  + flashggVHTightTag
 #                                     ###########updated VH tags############
 #                                         + flashggVHMetTag
 #                                         + flashggWHLeptonicTag
 #                                         + flashggZHLeptonicTag
  #                                        + flashggVHLeptonicLooseTag
 #                                         + flashggVHHadronicTag
                                      )
                                      * flashggTagSorter
                                  )

    return flashggTagSequence
