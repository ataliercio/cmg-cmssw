import FWCore.ParameterSet.Config as cms

from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

ebMax = 1.4442
eeMin = 1.566
ebCutOff=1.479
heepElectronID_HEEPV50 = cms.PSet(
    idName = cms.string("heepElectronID-HEEPV50"),
    cutFlow = cms.VPSet(
        cms.PSet( cutName = cms.string("MinPtCut"),
                  minPt = cms.double(35.0),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)                ),
        cms.PSet( cutName = cms.string("GsfEleSCEtaMultiRangeCut"),
                  useAbsEta = cms.bool(True),
                  allowedEtaRanges = cms.VPSet( 
                                  cms.PSet( minEta = cms.double(0.0), 
                                            maxEta = cms.double(ebMax) ),
                                  cms.PSet( minEta = cms.double(eeMin), 
                                            maxEta = cms.double(2.5) )
                                  ),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleDEtaInLinearCut'),
                  constTermEB = cms.double(0.016),
                  constTermEE = cms.double(0),
                  slopeTermEB = cms.double(-1E-4),
                  slopeTermEE = cms.double(0),
                  minValueEB = cms.double(0.004),
                  minValueEE = cms.double(0.02),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleDPhiInCut'),
                  dPhiInCutValueEB = cms.double(0.06),
                  dPhiInCutValueEE = cms.double(0.15),
                  barrelCutOff = cms.double(ebCutOff),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                  full5x5SigmaIEtaIEtaCutValueEB = cms.double(9999),
                  full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.03),
                  barrelCutOff = cms.double(ebCutOff),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleFull5x5E2x5OverE5x5Cut'),
                  minE1x5OverE5x5EB = cms.double(0.83),
                  minE1x5OverE5x5EE = cms.double(-1),
                  minE2x5OverE5x5EB = cms.double(0.94),
                  minE2x5OverE5x5EE = cms.double(-1),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                  slopeTermEB = cms.double(0.05),
                  slopeTermEE = cms.double(0.05),
                  slopeStartEB = cms.double(0),
                  slopeStartEE = cms.double(0),
                  constTermEB = cms.double(2),
                  constTermEE = cms.double(12.5),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleTrkPtIsoCut'),
                  slopeTermEB = cms.double(0),
                  slopeTermEE = cms.double(0),
                  slopeStartEB = cms.double(0),
                  slopeStartEE = cms.double(0),
                  constTermEB = cms.double(5),
                  constTermEE = cms.double(5),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                  slopeTermEB = cms.double(0.03),
                  slopeTermEE = cms.double(0.03),
                  slopeStartEB = cms.double(0),
                  slopeStartEE = cms.double(50),
                  constTermEB = cms.double(2),
                  constTermEE = cms.double(2.5),
                  rhoConstant = cms.double(0.28),
                  rho = cms.InputTag("fixedGridRhoFastjetAll"),
                  needsAdditionalProducts = cms.bool(True),
                  isIgnored = cms.bool(False)),
    
        cms.PSet( cutName = cms.string('GsfEleDxyCut'),
                  dxyCutValueEB = cms.double(0.02),
                  dxyCutValueEE = cms.double(0.05),
                  vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                  barrelCutOff = cms.double(ebCutOff),
                  needsAdditionalProducts = cms.bool(True),
                  isIgnored = cms.bool(False)),
        cms.PSet( cutName = cms.string('GsfEleMissingHitsCut'),
                  maxMissingHitsEB = cms.uint32(1),
                  maxMissingHitsEE = cms.uint32(1),
                  barrelCutOff = cms.double(ebCutOff),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False))
                     
    )
)


from RecoEgamma.ElectronIdentification.Identification.idTools import convertIDToRunOnMiniAOD

heepElectronID_HEEPV50_miniAOD = heepElectronID_HEEPV50.clone()
convertIDToRunOnMiniAOD(heepElectronID_HEEPV50_miniAOD)

central_id_registry.register(heepElectronID_HEEPV50.idName,"83b8b53c30a66bd682faa00367cc568f")
central_id_registry.register(heepElectronID_HEEPV50_miniAOD.idName,"3a617fe6cbb52b63a18dc13cf9e4f39c")
