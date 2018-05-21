#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import sys

if __name__ == "__main__":

  cuts = ""
  cuts += "*(nTracks == 1)"
  cuts += "*( iBestMatch >= 0)" # primary Track found

  cosmicCuts = cuts
  cosmicCuts += "*((!isMC) || (trueHitCosmic1 && trueHitCosmic2) || (trueHitCosmic3 && trueHitCosmic4))"
  cosmicCuts += "*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)" # only angles that match MC
  cosmicPhiGeq0Cuts = cosmicCuts + "*(primTrkStartPhi >= 0.)"
  cosmicPhiLt0Cuts = cosmicCuts + "*(primTrkStartPhi < 0.)"

  beamCuts = "*pzWeight"+cuts
  beamPionCuts = beamCuts + "*((((!isMC) && pWC > 100 && pWC < 1100) || (isMC && trueStartMom > 100 && trueStartMom < 1100)) && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) < 5e4))" + "*(primTrkLength > 85.)"
  beamProtonCuts = beamCuts + "*((((!isMC) && pWC > 1000 && pWC < 1100) || (isMC && trueStartMom > 1000 && trueStartMom < 1100)) && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) > 7e5))" + "*(primTrkLength < 60.)"

  hitCuts = "*(primTrkXs > 3. && primTrkXs < 46. && primTrkYs < 18. && primTrkYs > -18. && primTrkZs > 3. && primTrkZs < 87.)"
  cosmicHitCuts = hitCuts
  beamHitCuts = hitCuts+"*(primTrkZs > 5. && primTrkZs < 10.)"
  beamProtonHitCuts = hitCuts+"*(primTrkZs > 2. && primTrkZs < 6.)"

  logy = True
  scaleFactor = 0.066

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100

  baseDir="/scratch/jhugon/"
  baseDir=""

  ########################################################
  ## Beam Pions Definitions ##############################
  ########################################################

  fileConfigs = [
    {
      'fn': baseDir+"cosmicBeamData_v2/new/cosmicAna_beam_Pos_RunII_current100_v02_a.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/new/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_a.root"],
      'name': "BeamRunIIP100A_PiMuE",
      'title': "Run II Beam +100 A a #pi/#mu/e",
      'caption': "Run II Beam +100 A a #pi/#mu/e",
      'isData': True,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_pip_v6.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_pip_v6.root"],
      'name': "BeamMC_pip",
      'title': "Beam #pi MC",
      'caption': "Beam #pi MC",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_pip_presmear10_v6.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_pip_presmear10_v6.root"],
      'name': "BeamMC_pip_presmear10",
      'title': "Beam #pi MC 10% Smearing",
      'caption': "Beam #pi MC 10% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"caloAmpFiles/CosmicAna_data_Pos_RunII_current100_a_caloAmp.root",
      'addFriend': ["friend", baseDir+"caloAmpFiles/friendTrees/CosmicAna_data_Pos_RunII_current100_a_caloAmp.root"],
      'name': "BeamRunIIP100A_PiMuE_CaloAmp",
      'title': "Run II Beam +100 A a #pi/#mu/e Amp",
      'caption': "Run II Beam +100 A a #pi/#mu/e Amp",
      'isData': True,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"caloAmpFiles/CosmicAna_pip_flat_caloAmp.root",
      'addFriend': ["friend", baseDir+"caloAmpFiles/friendTrees/CosmicAna_pip_flat_caloAmp.root"],
      'name': "BeamMC_pip_CaloAmp",
      'title': "Beam #pi MC Amp",
      'caption': "Beam #pi MC Amp",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  m2SF = 1.
  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [50,1.,2.5],
      'var': "primTrkdEdxs*((1.02-1.)*isMC + 1.)",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "pWC",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [40,100,1100],
      'var': "(!isMC)*pWC+isMC*trueStartMom",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "primTrkLength",
      'xtitle': "Primary Track Length [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "primTrkLength",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "primTrkKinInteract",
      'xtitle': "Interaction Kinetic Energy [MeV]",
      'ytitle': "Events / bin",
      'binning': [50,0,800],
      'var': "primTrkKinInteract",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "beamlineMass",
      'xtitle': "Beamline Mass Squared [1000#times (MeV^{2})]",
      'ytitle': "Events / bin",
      'binning': [100,-5e5*m2SF,2e6*m2SF],
      'var': "pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.)",
      'cuts': "1",
      #'normalize': True,
      'logy': True,
      'drawvlines':[105.65**2*m2SF,139.6**2*m2SF,493.677**2*m2SF,938.272046**2*m2SF],
    },
  ]
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_PiMuE_",nMax=NMAX)
  histConfigs = [
    {
      'name': "primTrkdEdxsVbeamlineMom",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,300,1100,50,1.,2.5],
      'var': "primTrkdEdxs*((1.02-1.)*isMC + 1.):(!isMC)*pWC+isMC*trueStartMom",
      'cuts': "1",
    },
    {
      'name': "primTrkdEdxsVResRange",
      'xtitle': "Residual Range [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,0,100,50,1.,2.5],
      'var': "primTrkdEdxs*((1.02-1.)*isMC + 1.):primTrkResRanges",
      'cuts': "1",
    },
    {
      'name': "primTrkdEdxsVRangeSoFar",
      'xtitle': "Track Distance from Start [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,0,100,50,1.,2.5],
      'var': "primTrkdEdxs*((1.02-1.)*isMC + 1.):primTrkRangeSoFars",
      'cuts': "1",
    },
    {
      'name': "primTrkLengthVkinWCInTPC",
      'xtitle': "Kinetic Energy at TPC Start [MeV]",
      'ytitle': "Primary TPC Track Length [cm]",
      'binning': [50,0,600,50,0,100],
      'var': "primTrkLength:kinWCInTPC",
      'cuts': "1",
    },
    #{
    #  'name': "beamline_TOFVMom",
    #  'xtitle': "Beamline Momentum [MeV/c]",
    #  'ytitle': "Time Of Flight [ns]",
    #  'binning': [100,0,2000,100,0,100],
    #  'var': "firstTOF:pWC",
    #  'cuts': "1",
    #  'normalize': True,
    #},
    #{
    #  'name': "beamline_TOFVMom",
    #  'xtitle': "Beamline Momentum [MeV/c]",
    #  'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
    #  'binning': [100,100,1100,50,1,3.5],
    #  'var': "primTrkdEdxs:pWC",
    #  'cuts': "1",
    #},
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_PiMuE_",nMax=NMAX)

  ########################################################
  ## Beam Protons Definitions ##############################
  ########################################################

  fileConfigs = [
    {
      'fn': baseDir+"cosmicBeamData_v2/new/cosmicAna_beam_Pos_RunII_current100_v02_a.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/new/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_a.root"],
      'name': "BeamRunIIP100A_Proton",
      'title': "Run II Beam +100 A a p",
      'caption': "Run II Beam +100 A a p",
      'isData': True,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_v5.root"],
      'name': "BeamMC_pip",
      'title': "Beam p MC",
      'caption': "Beam p MC",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/newv5/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/newv5/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root"],
      'name': "BeamMC_p_presmear30",
      'title': "Beam p MC 30% Smearing",
      'caption': "Beam p MC 30% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"caloAmpFiles/CosmicAna_data_Pos_RunII_current100_a_caloAmp.root",
      'addFriend': ["friend", baseDir+"caloAmpFiles/friendTrees/CosmicAna_data_Pos_RunII_current100_a_caloAmp.root"],
      'name': "BeamRunIIP100Aa_Proton_CaloAmp",
      'title': "Run II Beam +100 A a p Amp",
      'caption': "Run II Beam +100 A a p Amp",
      'isData': True,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"caloAmpFiles/CosmicAna_p_flat_caloAmp.root",
      'addFriend': ["friend", baseDir+"caloAmpFiles/friendTrees/CosmicAna_p_flat_caloAmp.root"],
      'name': "BeamMC_pip",
      'title': "Beam p MC",
      'caption': "Beam p MC",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [50,0,10.],
      'var': "primTrkdEdxs",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "primTrkdEdxs_zoom4",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [50,3,8.],
      'var': "primTrkdEdxs",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "pWC",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [40,0,2000],
      'var': "(!isMC)*pWC+isMC*trueStartMom",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "primTrkKinInteract",
      'xtitle': "Interaction Kinetic Energy [MeV]",
      'ytitle': "Events / bin",
      'binning': [50,0,800],
      'var': "primTrkKinInteractProton",
      'cuts': "1",
      'normalize': True,
    },
    #{
    #  'name': "beamlineMass",
    #  'xtitle': "Beamline Mass Squared [1000#times (MeV^{2})]",
    #  'ytitle': "Events / bin",
    #  'binning': [100,-5e5*m2SF,2e6*m2SF],
    #  'var': "pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.)",
    #  'cuts': "1",
    #  #'normalize': True,
    #  'logy': True,
    #  'drawvlines':[105.65**2*m2SF,139.6**2*m2SF,493.677**2*m2SF,938.272046**2*m2SF],
    #},
  ]
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_P_",nMax=NMAX)

  histConfigs = [
    {
      'name': "primTrkdEdxsVbeamlineMom",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,300,1100,100,0.,10.],
      'var': "primTrkdEdxs:(!isMC)*pWC+isMC*trueStartMom",
      'cuts': "1",
    },
    {
      'name': "beamline_TOFVMom",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Time of Flight [ns]",
      'binning': [100,100,1100,100,0,100],
      'var': "firstTOF:pWC",
      'cuts': "1",
    },
    {
      'name': "primTrkdEdxsVResRange",
      'xtitle': "Residual Range [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,0,100,50,1.,2.5],
      'var': "primTrkdEdxs*((1.02-1.)*isMC + 1.):primTrkResRanges",
      'cuts': "1",
    },
    {
      'name': "primTrkLengthVkinWCInTPCProton",
      'xtitle': "Kinetic Energy at TPC Start [MeV]",
      'ytitle': "Primary TPC Track Length [cm]",
      'binning': [50,0,600,50,0,100],
      'var': "primTrkLength:kinWCInTPCProton",
      'cuts': "1",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_P_",nMax=NMAX)


  ########################################################
  ## Cosmics Definitions #################################
  ########################################################

  fileConfigs = [
    {
      'fn': [baseDir+"cosmicData/CosmicAna_RIIP100_64a_v01.root"],
      'name': "CosmicsRunIIPos100a",
      'title': "Run II +100 A Cosmics a",
      'caption': "Run II +100 A Cosmics a",
      'isData': True,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_v04.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'isData': False,
    },
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing20_v01.root",
    #  'name': "CosmicMC_presmear20perc",
    #  'title': "Cosmic MC Pre-smear 20% ",
    #  'caption': "Cosmic MC Pre-smear 20%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing70_v01.root",
    #  'name': "CosmicMC_presmear70perc",
    #  'title': "Cosmic MC Pre-smear 70% ",
    #  'caption': "Cosmic MC Pre-smear 70%",
    #  'isData': False,
    #},
    {
      'fn': [baseDir+"caloAmpFiles/CosmicAna_cosmic_data_Pos_RunII_current100_a_caloAmp.root"],
      'name': "CosmicsRunIIPos100aAmp",
      'title': "Run II +100 A Cosmics a Amp",
      'caption': "Run II +100 A Cosmics a Amp",
      'isData': True,
    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,1.,3.5],
      #'var': "primTrkdEdxs*((1.05-1.)*isMC + 1.)",
      'var': "primTrkdEdxs",
      'cuts': "1"+cosmicPhiGeq0Cuts,
      'normalize': True,
      'caption':"Cosmics #phi #geq 0",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareReco_Cosmic_phiGeq0_",nMax=NMAX)

  fileConfigs = [
    {
      'fn': [baseDir+"cosmicData/CosmicAna_RIIP100_64a_v01.root"],
      'name': "CosmicsRunIIPos100a",
      'title': "Run II +100 A Cosmics a",
      'caption': "Run II +100 A Cosmics a",
      'isData': True,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_v04.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'isData': False,
    },
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing20_v01.root",
    #  'name': "CosmicMC_presmear20perc",
    #  'title': "Cosmic MC Pre-smear 20% ",
    #  'caption': "Cosmic MC Pre-smear 20%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing70_v01.root",
    #  'name': "CosmicMC_presmear70perc",
    #  'title': "Cosmic MC Pre-smear 70% ",
    #  'caption': "Cosmic MC Pre-smear 70%",
    #  'isData': False,
    #},
    {
      'fn': [baseDir+"caloAmpFiles/CosmicAna_cosmic_data_Pos_RunII_current100_a_caloAmp.root"],
      'name': "CosmicsRunIIPos100aAmp",
      'title': "Run II +100 A Cosmics a Amp",
      'caption': "Run II +100 A Cosmics a Amp",
      'isData': True,
    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,1.,3.5],
      #'var': "primTrkdEdxs*((0.91-1.)*isMC + 1.)",
      'var': "primTrkdEdxs",
      'cuts': "1"+cosmicPhiLt0Cuts,
      'normalize': True,
      'caption':"Cosmics #phi < 0",
    },
    {
      'name': "primTrkPitches",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0.3,1.5],
      'var': "primTrkPitches",
      'cuts': "1"+cosmicPhiLt0Cuts,
      'caption':"Cosmics #phi < 0",
      #'normalize': True,
      'logy': True,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareReco_Cosmic_phiLt0_",nMax=NMAX)

