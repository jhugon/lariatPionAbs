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
    #{
    #  'fn': [baseDir+"cosmicBeamData_v2/cosmicAna_beam_Neg_RunII_current100_v02_all.root",
    #         baseDir+"cosmicBeamData_v2/cosmicAna_beam_Neg_RunII_current60_v02_all.root",
    #         baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
    #         baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current60_v02_all.root"],
    #  'name': "BeamRunIIPiMuE",
    #  'title': "Run II Beam #pi/#mu/e",
    #  'caption': "Run II Beam #pi/#mu/e",
    #  'color': root.kGray+2,
    #  'isData': True,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    #{
    #  'fn': [baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
    #         baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current60_v02_all.root"],
    #  'name': "BeamRunIIPlusPiMuE",
    #  'title': "Run II+ Beam #pi/#mu/e",
    #  'caption': "Run II+ Beam #pi/#mu/e",
    #  'color': root.kGray+2,
    #  'isData': True,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    #{
    #  'fn': baseDir+"cosmicBeamData_v2/cosmicAna_beam_Neg_RunII_current60_v02_all.root",
    #  'name': "BeamRunIIM60A_PiMuE",
    #  'title': "Run II Beam -60 A #pi/#mu/e",
    #  'caption': "Run II Beam -60 A #pi/#mu/e",
    #  'isData': True,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    #{
    #  'fn': baseDir+"cosmicBeamData_v2/cosmicAna_beam_Neg_RunII_current100_v02_all.root",
    #  'name': "BeamRunIIM100A_PiMuE",
    #  'title': "Run II Beam -100 A #pi/#mu/e",
    #  'caption': "Run II Beam -99 A #pi/#mu/e",
    #  'isData': True,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    #{
    #  'fn': baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current60_v02_all.root",
    #  'addFriend': ["friend", baseDir+"cosmicBeamData_v2/friendTrees/cosmicAna_beam_Pos_RunII_current60_v02_all.root"],
    #  'name': "BeamRunIIP60A_PiMuE",
    #  'title': "Run II Beam +60 A #pi/#mu/e",
    #  'caption': "Run II Beam +60 A #pi/#mu/e",
    #  'isData': True,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    {
      'fn': baseDir+"cosmicBeamData_v2/new/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/new/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_all.root"],
      'name': "BeamRunIIP100A_PiMuE",
      'title': "Run II Beam +100 A #pi/#mu/e",
      'caption': "Run II Beam +100 A #pi/#mu/e",
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
    #{
    #  'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root",
    #  'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root"],
    #  'name': "BeamMC_pip_presmear15",
    #  'title': "Beam #pi MC 15% Smearing",
    #  'caption': "Beam #pi MC 15% Smearing",
    #  'isData': False,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_pip_presmear20_v6.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_pip_presmear20_v6.root"],
      'name': "BeamMC_pip_presmear20",
      'title': "Beam #pi MC 20% Smearing",
      'caption': "Beam #pi MC 20% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    #{
    #  'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root",
    #  'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root"],
    #  'name': "BeamMC_pip_presmear25",
    #  'title': "Beam #pi MC 25% Smearing",
    #  'caption': "Beam #pi MC 25% Smearing",
    #  'isData': False,
    #  'isBeam': True,
    #  'cuts': beamPionCuts + beamHitCuts,
    #},
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_pip_presmear30_v6.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_pip_presmear30_v6.root"],
      'name': "BeamMC_pip_presmear30",
      'title': "Beam #pi MC 30% Smearing",
      'caption': "Beam #pi MC 30% Smearing",
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
      'fn': baseDir+"cosmicBeamData_v2/new/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/new/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_all.root"],
      'name': "BeamRunIIP100A_Proton",
      'title': "Run II Beam +100 A p",
      'caption': "Run II Beam +100 A p",
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
      'fn': baseDir+"cosmicBeamMC/newv5/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/newv5/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root"],
      'name': "BeamMC_p_presmear10",
      'title': "Beam p MC 10% Smearing",
      'caption': "Beam p MC 10% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    #{
    #  'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root",
    #  'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root"],
    #  'name': "BeamMC_p_presmear15",
    #  'title': "Beam p MC 15% Smearing",
    #  'caption': "Beam p MC 15% Smearing",
    #  'isData': False,
    #  'isBeam': True,
    #  'cuts': beamProtonCuts + beamHitCuts,
    #},
    {
      'fn': baseDir+"cosmicBeamMC/newv5/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/newv5/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root"],
      'name': "BeamMC_p_presmear20",
      'title': "Beam p MC 20% Smearing",
      'caption': "Beam p MC 20% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    #{
    #  'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root",
    #  'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root"],
    #  'name': "BeamMC_p_presmear25",
    #  'title': "Beam p MC 25% Smearing",
    #  'caption': "Beam p MC 25% Smearing",
    #  'isData': False,
    #  'isBeam': True,
    #  'cuts': beamProtonCuts + beamHitCuts,
    #},
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
      'fn': [baseDir+"cosmicsManyRecos/Cosmics_RIIN100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIN60.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP60.root"],
      'name': "CosmicsRunII",
      'title': "Run II Cosmics",
      'caption': "Run II Cosmics",
      'isData': True,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_v04.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'isData': False,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing10_v01.root",
      'name': "CosmicMC_presmear10perc",
      'title': "Cosmic MC Pre-smear 10% ",
      'caption': "Cosmic MC Pre-smear 10%",
      'isData': False,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing20_v01.root",
      'name': "CosmicMC_presmear20perc",
      'title': "Cosmic MC Pre-smear 20% ",
      'caption': "Cosmic MC Pre-smear 20%",
      'isData': False,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing30_v01.root",
      'name': "CosmicMC_presmear30perc",
      'title': "Cosmic MC Pre-smear 30% ",
      'caption': "Cosmic MC Pre-smear 30%",
      'isData': False,
    },
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing40_v01.root",
    #  'name': "CosmicMC_presmear40perc",
    #  'title': "Cosmic MC Pre-smear 40% ",
    #  'caption': "Cosmic MC Pre-smear 40%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing45_v01.root",
    #  'name': "CosmicMC_presmear45perc",
    #  'title': "Cosmic MC Pre-smear 45% ",
    #  'caption': "Cosmic MC Pre-smear 45%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing50_v01.root",
    #  'name': "CosmicMC_presmear50perc",
    #  'title': "Cosmic MC Pre-smear 50% ",
    #  'caption': "Cosmic MC Pre-smear 50%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing55_v01.root",
    #  'name': "CosmicMC_presmear55perc",
    #  'title': "Cosmic MC Pre-smear 55% ",
    #  'caption': "Cosmic MC Pre-smear 55%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing60_v01.root",
    #  'name': "CosmicMC_presmear60perc",
    #  'title': "Cosmic MC Pre-smear 60% ",
    #  'caption': "Cosmic MC Pre-smear 60%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing70_v01.root",
    #  'name': "CosmicMC_presmear70perc",
    #  'title': "Cosmic MC Pre-smear 70% ",
    #  'caption': "Cosmic MC Pre-smear 70%",
    #  'isData': False,
    #},
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,1.,3.5],
      'var': "primTrkdEdxs*((1.05-1.)*isMC + 1.)",
      'cuts': "1"+cosmicPhiGeq0Cuts,
      'normalize': True,
      'caption':"Cosmics #phi #geq 0",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_Cosmic_phiGeq0_",nMax=NMAX)

  fileConfigs = [
    {
      'fn': [baseDir+"cosmicsManyRecos/Cosmics_RIIN100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIN60.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP60.root"],
      'name': "CosmicsRunII",
      'title': "Run II Cosmics",
      'caption': "Run II Cosmics",
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
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing10_v01.root",
    #  'name': "CosmicMC_presmear10perc",
    #  'title': "Cosmic MC Pre-smear 10% ",
    #  'caption': "Cosmic MC Pre-smear 10%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing20_v01.root",
    #  'name': "CosmicMC_presmear20perc",
    #  'title': "Cosmic MC Pre-smear 20% ",
    #  'caption': "Cosmic MC Pre-smear 20%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing30_v01.root",
    #  'name': "CosmicMC_presmear30perc",
    #  'title': "Cosmic MC Pre-smear 30% ",
    #  'caption': "Cosmic MC Pre-smear 30%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing40_v01.root",
    #  'name': "CosmicMC_presmear40perc",
    #  'title': "Cosmic MC Pre-smear 40% ",
    #  'caption': "Cosmic MC Pre-smear 40%",
    #  'isData': False,
    #},
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing45_v01.root",
    #  'name': "CosmicMC_presmear45perc",
    #  'title': "Cosmic MC Pre-smear 45% ",
    #  'caption': "Cosmic MC Pre-smear 45%",
    #  'isData': False,
    #},
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing50_v01.root",
      'name': "CosmicMC_presmear50perc",
      'title': "Cosmic MC Pre-smear 50% ",
      'caption': "Cosmic MC Pre-smear 50%",
      'isData': False,
    },
    #{
    #  'fn': baseDir+"cosmicMC/cosmicAna_smearing55_v01.root",
    #  'name': "CosmicMC_presmear55perc",
    #  'title': "Cosmic MC Pre-smear 55% ",
    #  'caption': "Cosmic MC Pre-smear 55%",
    #  'isData': False,
    #},
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing60_v01.root",
      'name': "CosmicMC_presmear60perc",
      'title': "Cosmic MC Pre-smear 60% ",
      'caption': "Cosmic MC Pre-smear 60%",
      'isData': False,
    },
    {
      'fn': baseDir+"cosmicMC/cosmicAna_smearing70_v01.root",
      'name': "CosmicMC_presmear70perc",
      'title': "Cosmic MC Pre-smear 70% ",
      'caption': "Cosmic MC Pre-smear 70%",
      'isData': False,
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
      'var': "primTrkdEdxs*((0.91-1.)*isMC + 1.)",
      'cuts': "1"+cosmicPhiLt0Cuts,
      'normalize': True,
      'caption':"Cosmics #phi < 0",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",outPrefix="CompareSmearing_Cosmic_phiLt0_",nMax=NMAX)


"""
Attaching file cosmicBeamMC/CosmicAna_pip_v6.root as _file0...
root [1] new TBrowser
(class TBrowser*)0x25a8520
root [2] ******************************************************************************
*Tree    :tree      : tree                                                   *
*Entries :    75516 : Total =      1475308613 bytes  File  Size = 1004441546 *
*        :          : Tree compression factor =   1.47                       *
******************************************************************************
*Br    0 :isMC      : isMC/O                                                 *
*Entries :    75516 : Total  Size=     121846 bytes  File Size  =      46552 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.39     *
*............................................................................*
*Br    1 :runNumber : runNumber/i                                            *
*Entries :    75516 : Total  Size=     350950 bytes  File Size  =      53130 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.41     *
*............................................................................*
*Br    2 :subRunNumber : subRunNumber/i                                      *
*Entries :    75516 : Total  Size=     352480 bytes  File Size  =      54648 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.26     *
*............................................................................*
*Br    3 :eventNumber : eventNumber/i                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =     169510 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.01     *
*............................................................................*
*Br    4 :nWCTracks : nWCTracks/i                                            *
*Entries :    75516 : Total  Size=     350950 bytes  File Size  =      51612 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.60     *
*............................................................................*
*Br    5 :xWC       : xWC/F                                                  *
*Entries :    75516 : Total  Size=     347890 bytes  File Size  =      50094 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.74     *
*............................................................................*
*Br    6 :yWC       : yWC/F                                                  *
*Entries :    75516 : Total  Size=     347890 bytes  File Size  =      50094 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.74     *
*............................................................................*
*Br    7 :thetaWC   : thetaWC/F                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.51     *
*............................................................................*
*Br    8 :phiWC     : phiWC/F                                                *
*Entries :    75516 : Total  Size=     348910 bytes  File Size  =      51106 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.62     *
*............................................................................*
*Br    9 :pzWC      : pzWC/F                                                 *
*Entries :    75516 : Total  Size=     348400 bytes  File Size  =     337921 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   10 :pWC       : pWC/F                                                  *
*Entries :    75516 : Total  Size=     347890 bytes  File Size  =     337421 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   11 :eWC       : eWC/F                                                  *
*Entries :    75516 : Total  Size=     347890 bytes  File Size  =     335760 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.01     *
*............................................................................*
*Br   12 :kinWC     : kinWC/F                                                *
*Entries :    75516 : Total  Size=     348910 bytes  File Size  =     338495 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   13 :kinWCInTPC : kinWCInTPC/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =     341025 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   14 :eWCProton : eWCProton/F                                            *
*Entries :    75516 : Total  Size=     350950 bytes  File Size  =     327853 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.04     *
*............................................................................*
*Br   15 :kinWCProton : kinWCProton/F                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =     341532 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   16 :kinWCInTPCProton : kinWCInTPCProton/F                              *
*Entries :    75516 : Total  Size=     354520 bytes  File Size  =     344062 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   17 :yKinkWC   : yKinkWC/F                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.51     *
*............................................................................*
*Br   18 :nHitsWC   : nHitsWC/i                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      50600 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.71     *
*............................................................................*
*Br   19 :xWC4Hit   : xWC4Hit/F                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.51     *
*............................................................................*
*Br   20 :yWC4Hit   : yWC4Hit/F                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.51     *
*............................................................................*
*Br   21 :zWC4Hit   : zWC4Hit/F                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.51     *
*............................................................................*
*Br   22 :nTOFs     : nTOFs/i                                                *
*Entries :    75516 : Total  Size=     348910 bytes  File Size  =      49588 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.83     *
*............................................................................*
*Br   23 :TOFs      : TOFs[nTOFs]/F                                          *
*Entries :    75516 : Total  Size=     352539 bytes  File Size  =      52624 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.50     *
*............................................................................*
*Br   24 :TOFTimeStamps : TOFTimeStamps[nTOFs]/i                             *
*Entries :    75516 : Total  Size=     357122 bytes  File Size  =      57178 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.06     *
*............................................................................*
*Br   25 :firstTOF  : firstTOF/F                                             *
*Entries :    75516 : Total  Size=     350440 bytes  File Size  =      52624 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.46     *
*............................................................................*
*Br   26 :triggerBits : triggerBits/i                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =      52624 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.49     *
*............................................................................*
*Br   27 :triggerBEAMON : triggerBEAMON/O                                    *
*Entries :    75516 : Total  Size=     126436 bytes  File Size  =      51106 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.27     *
*............................................................................*
*Br   28 :triggerCOSMICON : triggerCOSMICON/O                                *
*Entries :    75516 : Total  Size=     127456 bytes  File Size  =      52118 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.25     *
*............................................................................*
*Br   29 :triggerCOSMIC : triggerCOSMIC/O                                    *
*Entries :    75516 : Total  Size=     126436 bytes  File Size  =      51106 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.27     *
*............................................................................*
*Br   30 :triggerUSTOF : triggerUSTOF/O                                      *
*Entries :    75516 : Total  Size=     125926 bytes  File Size  =      50600 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.28     *
*............................................................................*
*Br   31 :triggerDSTOF : triggerDSTOF/O                                      *
*Entries :    75516 : Total  Size=     125926 bytes  File Size  =      50600 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.28     *
*............................................................................*
*Br   32 :triggerWCCOINC3OF4 : triggerWCCOINC3OF4/O                          *
*Entries :    75516 : Total  Size=     128986 bytes  File Size  =      53636 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.21     *
*............................................................................*
*Br   33 :triggerMICHEL : triggerMICHEL/O                                    *
*Entries :    75516 : Total  Size=     126436 bytes  File Size  =      51106 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.27     *
*............................................................................*
*Br   34 :trueEndProcess : trueEndProcess/I                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =     102367 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   3.35     *
*............................................................................*
*Br   35 :trueNDaughters : trueNDaughters/i                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =     144757 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.37     *
*............................................................................*
*Br   36 :trueNSecondaryChPions : trueNSecondaryChPions/i                    *
*Entries :    75516 : Total  Size=     357070 bytes  File Size  =     100318 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   3.45     *
*............................................................................*
*Br   37 :trueNSecondaryPiZeros : trueNSecondaryPiZeros/i                    *
*Entries :    75516 : Total  Size=     357070 bytes  File Size  =      87432 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   3.96     *
*............................................................................*
*Br   38 :trueNSecondaryProtons : trueNSecondaryProtons/i                    *
*Entries :    75516 : Total  Size=     357070 bytes  File Size  =     125093 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.77     *
*............................................................................*
*Br   39 :trueStartX : trueStartX/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =     337471 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.01     *
*............................................................................*
*Br   40 :trueStartY : trueStartY/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =     341015 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   41 :trueStartZ : trueStartZ/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =      53636 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.36     *
*............................................................................*
*Br   42 :trueEndX  : trueEndX/F                                             *
*Entries :    75516 : Total  Size=     350440 bytes  File Size  =     339206 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   43 :trueEndY  : trueEndY/F                                             *
*Entries :    75516 : Total  Size=     350440 bytes  File Size  =     340014 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   44 :trueEndZ  : trueEndZ/F                                             *
*Entries :    75516 : Total  Size=     350440 bytes  File Size  =     339956 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   45 :trueStartTheta : trueStartTheta/F                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =     341427 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   46 :trueStartPhi : trueStartPhi/F                                      *
*Entries :    75516 : Total  Size=     352480 bytes  File Size  =     339564 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.01     *
*............................................................................*
*Br   47 :trueStartMom : trueStartMom/F                                      *
*Entries :    75516 : Total  Size=     352480 bytes  File Size  =     341975 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   48 :trueStartE : trueStartE/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =     339301 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.01     *
*............................................................................*
*Br   49 :trueEndMom : trueEndMom/F                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =     135192 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.52     *
*............................................................................*
*Br   50 :trueEndE  : trueEndE/F                                             *
*Entries :    75516 : Total  Size=     350440 bytes  File Size  =     132777 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.56     *
*............................................................................*
*Br   51 :trueSecondToEndMom : trueSecondToEndMom/F                          *
*Entries :    75516 : Total  Size=     355540 bytes  File Size  =     345074 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.00     *
*............................................................................*
*Br   52 :trueSecondToEndE : trueSecondToEndE/F                              *
*Entries :    75516 : Total  Size=     354520 bytes  File Size  =     340549 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.01     *
*............................................................................*
*Br   53 :trueHitCosmic1 : trueHitCosmic1/O                                  *
*Entries :    75516 : Total  Size=     126946 bytes  File Size  =      51618 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.26     *
*............................................................................*
*Br   54 :trueHitCosmic2 : trueHitCosmic2/O                                  *
*Entries :    75516 : Total  Size=     126946 bytes  File Size  =      51710 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.25     *
*............................................................................*
*Br   55 :trueHitCosmic3 : trueHitCosmic3/O                                  *
*Entries :    75516 : Total  Size=     126946 bytes  File Size  =      51625 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.26     *
*............................................................................*
*Br   56 :trueHitCosmic4 : trueHitCosmic4/O                                  *
*Entries :    75516 : Total  Size=     126946 bytes  File Size  =      51809 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.25     *
*............................................................................*
*Br   57 :nTracks   : nTracks/i                                              *
*Entries :    75516 : Total  Size=     349930 bytes  File Size  =     117066 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.90     *
*............................................................................*
*Br   58 :nTracksInFirstZ : nTracksInFirstZ[95]/i                            *
*Entries :    75516 : Total  Size=   28799646 bytes  File Size  =     750046 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=  38.37     *
*............................................................................*
*Br   59 :nTracksLengthLt : nTracksLengthLt[20]/i                            *
*Entries :    75516 : Total  Size=    6093234 bytes  File Size  =     344164 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=  17.67     *
*............................................................................*
*Br   60 :trackStartX : trackStartX[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     679830 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.29     *
*............................................................................*
*Br   61 :trackStartY : trackStartY[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     705548 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.24     *
*............................................................................*
*Br   62 :trackStartZ : trackStartZ[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     704228 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.24     *
*............................................................................*
*Br   63 :trackStartTheta : trackStartTheta[nTracks]/F                       *
*Entries :    75516 : Total  Size=     887217 bytes  File Size  =     698109 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.26     *
*............................................................................*
*Br   64 :trackStartPhi : trackStartPhi[nTracks]/F                           *
*Entries :    75516 : Total  Size=     886197 bytes  File Size  =     701348 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.25     *
*............................................................................*
*Br   65 :trackEndX : trackEndX[nTracks]/F                                   *
*Entries :    75516 : Total  Size=     884157 bytes  File Size  =     684812 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.28     *
*............................................................................*
*Br   66 :trackEndY : trackEndY[nTracks]/F                                   *
*Entries :    75516 : Total  Size=     884157 bytes  File Size  =     702761 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.24     *
*............................................................................*
*Br   67 :trackEndZ : trackEndZ[nTracks]/F                                   *
*Entries :    75516 : Total  Size=     884157 bytes  File Size  =     681102 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.28     *
*............................................................................*
*Br   68 :trackLength : trackLength[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     694236 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.26     *
*............................................................................*
*Br   69 :trackXFront : trackXFront[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     191958 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.56     *
*............................................................................*
*Br   70 :trackYFront : trackYFront[nTracks]/F                               *
*Entries :    75516 : Total  Size=     885177 bytes  File Size  =     191958 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.56     *
*............................................................................*
*Br   71 :trackLLHPion : trackLLHPion[nTracks]/F                             *
*Entries :    75516 : Total  Size=     885687 bytes  File Size  =     191999 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.56     *
*............................................................................*
*Br   72 :trackLLHProton : trackLLHProton[nTracks]/F                         *
*Entries :    75516 : Total  Size=     886707 bytes  File Size  =     193014 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.54     *
*............................................................................*
*Br   73 :trackLLHMuon : trackLLHMuon[nTracks]/F                             *
*Entries :    75516 : Total  Size=     885687 bytes  File Size  =     191999 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.56     *
*............................................................................*
*Br   74 :trackLLHKaon : trackLLHKaon[nTracks]/F                             *
*Entries :    75516 : Total  Size=     885687 bytes  File Size  =     191999 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.56     *
*............................................................................*
*Br   75 :trackPIDA : trackPIDA[nTracks]/F                                   *
*Entries :    75516 : Total  Size=     884157 bytes  File Size  =     189183 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.62     *
*............................................................................*
*Br   76 :trackStartDistToPrimTrkEnd : trackStartDistToPrimTrkEnd[nTracks]/F *
*Entries :    75516 : Total  Size=     892827 bytes  File Size  =     199191 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.43     *
*............................................................................*
*Br   77 :trackEndDistToPrimTrkEnd : trackEndDistToPrimTrkEnd[nTracks]/F     *
*Entries :    75516 : Total  Size=     891807 bytes  File Size  =     198039 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.45     *
*............................................................................*
*Br   78 :iBestMatch : iBestMatch/I                                          *
*Entries :    75516 : Total  Size=     351460 bytes  File Size  =      97404 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   3.50     *
*............................................................................*
*Br   79 :trackMatchDeltaX : trackMatchDeltaX[nTracks]/F                     *
*Entries :    75516 : Total  Size=     887727 bytes  File Size  =     193952 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.52     *
*............................................................................*
*Br   80 :trackMatchDeltaY : trackMatchDeltaY[nTracks]/F                     *
*Entries :    75516 : Total  Size=     887727 bytes  File Size  =     193952 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.52     *
*............................................................................*
*Br   81 :trackMatchDeltaR : trackMatchDeltaR[nTracks]/F                     *
*Entries :    75516 : Total  Size=     887727 bytes  File Size  =     193952 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.52     *
*............................................................................*
*Br   82 :trackMatchDeltaAngle : trackMatchDeltaAngle[nTracks]/F             *
*Entries :    75516 : Total  Size=     889767 bytes  File Size  =     195961 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.49     *
*............................................................................*
*Br   83 :trackMatchLowestZ : trackMatchLowestZ[nTracks]/F                   *
*Entries :    75516 : Total  Size=     888237 bytes  File Size  =     193213 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   4.54     *
*............................................................................*
*Br   84 :nMatchedTracks : nMatchedTracks/i                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =      54142 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.34     *
*............................................................................*
*Br   85 :primTrkStartMomTrking : primTrkStartMomTrking/F                    *
*Entries :    75516 : Total  Size=     357070 bytes  File Size  =      96848 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   3.58     *
*............................................................................*
*Br   86 :primTrkStartTheta : primTrkStartTheta/F                            *
*Entries :    75516 : Total  Size=     355030 bytes  File Size  =     315810 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br   87 :primTrkStartPhi : primTrkStartPhi/F                                *
*Entries :    75516 : Total  Size=     354010 bytes  File Size  =     317050 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.08     *
*............................................................................*
*Br   88 :primTrkLength : primTrkLength/F                                    *
*Entries :    75516 : Total  Size=     352990 bytes  File Size  =     307805 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.11     *
*............................................................................*
*Br   89 :primTrkStartX : primTrkStartX/F                                    *
*Entries :    75516 : Total  Size=     352990 bytes  File Size  =     304554 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br   90 :primTrkStartY : primTrkStartY/F                                    *
*Entries :    75516 : Total  Size=     352990 bytes  File Size  =     318981 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.07     *
*............................................................................*
*Br   91 :primTrkStartZ : primTrkStartZ/F                                    *
*Entries :    75516 : Total  Size=     352990 bytes  File Size  =     316337 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.08     *
*............................................................................*
*Br   92 :primTrkEndX : primTrkEndX/F                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =     310059 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.10     *
*............................................................................*
*Br   93 :primTrkEndY : primTrkEndY/F                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =     318259 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.07     *
*............................................................................*
*Br   94 :primTrkEndZ : primTrkEndZ/F                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =     305591 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br   95 :primTrkPitchC : primTrkPitchC/F                                    *
*Entries :    75516 : Total  Size=     352990 bytes  File Size  =     304407 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.13     *
*............................................................................*
*Br   96 :primTrkPitchCInduct : primTrkPitchCInduct/F                        *
*Entries :    75516 : Total  Size=     356050 bytes  File Size  =     307208 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br   97 :primTrkCaloRange : primTrkCaloRange/F                              *
*Entries :    75516 : Total  Size=     354520 bytes  File Size  =     309890 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.11     *
*............................................................................*
*Br   98 :primTrkEndInFid : primTrkEndInFid/O                                *
*Entries :    75516 : Total  Size=     127456 bytes  File Size  =      75498 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.55     *
*............................................................................*
*Br   99 :primTrkLLHPion : primTrkLLHPion/F                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =      55660 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.16     *
*............................................................................*
*Br  100 :primTrkLLHProton : primTrkLLHProton/F                              *
*Entries :    75516 : Total  Size=     354520 bytes  File Size  =      56672 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.07     *
*............................................................................*
*Br  101 :primTrkLLHMuon : primTrkLLHMuon/F                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =      55660 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.16     *
*............................................................................*
*Br  102 :primTrkLLHKaon : primTrkLLHKaon/F                                  *
*Entries :    75516 : Total  Size=     353500 bytes  File Size  =      55660 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.16     *
*............................................................................*
*Br  103 :primTrkPIDA : primTrkPIDA/F                                        *
*Entries :    75516 : Total  Size=     351970 bytes  File Size  =      54142 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   6.31     *
*............................................................................*
*Br  104 :primTrkKinInteract : primTrkKinInteract/F                          *
*Entries :    75516 : Total  Size=     355540 bytes  File Size  =     230930 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.49     *
*............................................................................*
*Br  105 :primTrkKinInteractProton : primTrkKinInteractProton/F              *
*Entries :    75516 : Total  Size=     358600 bytes  File Size  =     237470 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.47     *
*............................................................................*
*Br  106 :primTrkdEdxs : vector<float>                                       *
*Entries :    75516 : Total  Size=   25324686 bytes  File Size  =   22228923 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  107 :primTrkdQdxs : vector<float>                                       *
*Entries :    75516 : Total  Size=   25324686 bytes  File Size  =   21886083 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.16     *
*............................................................................*
*Br  108 :primTrkResRanges : vector<float>                                   *
*Entries :    75516 : Total  Size=   25328750 bytes  File Size  =   22640955 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  109 :primTrkRangeSoFars : vector<float>                                 *
*Entries :    75516 : Total  Size=   25330782 bytes  File Size  =   22665083 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  110 :primTrkPitches : vector<float>                                     *
*Entries :    75516 : Total  Size=   25326718 bytes  File Size  =    4272761 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   5.92     *
*............................................................................*
*Br  111 :primTrkIBackwards : vector<float>                                  *
*Entries :    75516 : Total  Size=   25329766 bytes  File Size  =    2356970 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=  10.74     *
*............................................................................*
*Br  112 :primTrkXs : vector<float>                                          *
*Entries :    75516 : Total  Size=   25321638 bytes  File Size  =   21917104 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  113 :primTrkYs : vector<float>                                          *
*Entries :    75516 : Total  Size=   25321638 bytes  File Size  =   23157199 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br  114 :primTrkZs : vector<float>                                          *
*Entries :    75516 : Total  Size=   25321638 bytes  File Size  =   22598130 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  115 :primTrkKins : vector<float>                                        *
*Entries :    75516 : Total  Size=   25323670 bytes  File Size  =   22204960 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  116 :primTrkKinsProton : vector<float>                                  *
*Entries :    75516 : Total  Size=   25329766 bytes  File Size  =   22811761 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.11     *
*............................................................................*
*Br  117 :primTrkdEdxsInduct : vector<float>                                 *
*Entries :    75516 : Total  Size=   25677210 bytes  File Size  =   21953213 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.17     *
*............................................................................*
*Br  118 :primTrkdQdxsInduct : vector<float>                                 *
*Entries :    75516 : Total  Size=   25677210 bytes  File Size  =   22477870 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  119 :primTrkResRangesInduct : vector<float>                             *
*Entries :    75516 : Total  Size=   25681274 bytes  File Size  =   22967663 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  120 :primTrkPitchesInduct : vector<float>                               *
*Entries :    75516 : Total  Size=   25679242 bytes  File Size  =    4311214 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   5.95     *
*............................................................................*
*Br  121 :primTrkIBackwardsInduct : vector<float>                            *
*Entries :    75516 : Total  Size=   25682290 bytes  File Size  =    2384807 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=  10.76     *
*............................................................................*
*Br  122 :primTrkXsInduct : vector<float>                                    *
*Entries :    75516 : Total  Size=   25674162 bytes  File Size  =   22228755 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  123 :primTrkYsInduct : vector<float>                                    *
*Entries :    75516 : Total  Size=   25674162 bytes  File Size  =   23484670 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br  124 :primTrkZsInduct : vector<float>                                    *
*Entries :    75516 : Total  Size=   25674162 bytes  File Size  =   22919452 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  125 :primTrkTrueWiresInduct : vector<unsigned int>                      *
*Entries :    75516 : Total  Size=   25681274 bytes  File Size  =    3044396 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   8.43     *
*............................................................................*
*Br  126 :primTrkTruedEdxs : vector<float>                                   *
*Entries :    75516 : Total  Size=   25328750 bytes  File Size  =   22230340 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  127 :primTrkTruedQdxs : vector<float>                                   *
*Entries :    75516 : Total  Size=   25328750 bytes  File Size  =   21664935 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.17     *
*............................................................................*
*Br  128 :primTrkTruedEs : vector<float>                                     *
*Entries :    75516 : Total  Size=   25326718 bytes  File Size  =   21849756 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.16     *
*............................................................................*
*Br  129 :primTrkTruedQs : vector<float>                                     *
*Entries :    75516 : Total  Size=   25326718 bytes  File Size  =   22065466 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  130 :primTrkTrueResRanges : vector<float>                               *
*Entries :    75516 : Total  Size=   25332814 bytes  File Size  =   22644988 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   1.12     *
*............................................................................*
*Br  131 :primTrkTrueWires : vector<unsigned int>                            *
*Entries :    75516 : Total  Size=   25328750 bytes  File Size  =    3056834 *
*Baskets :     1012 : Basket Size=      32000 bytes  Compression=   8.28     *
*............................................................................*
*Br  132 :primTrkHitIsCollections : vector<bool>                             *
*Entries :    75516 : Total  Size=   13283571 bytes  File Size  =    1894281 *
*Baskets :      508 : Basket Size=      32000 bytes  Compression=   7.01     *
*............................................................................*
*Br  133 :primTrkHitWires : vector<unsigned int>                             *
*Entries :    75516 : Total  Size=   49930584 bytes  File Size  =   18713428 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   2.67     *
*............................................................................*
*Br  134 :primTrkHitStartTimes : vector<int>                                 *
*Entries :    75516 : Total  Size=   49940099 bytes  File Size  =   20183361 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   2.47     *
*............................................................................*
*Br  135 :primTrkHitEndTimes : vector<int>                                   *
*Entries :    75516 : Total  Size=   49936293 bytes  File Size  =   21067973 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   2.37     *
*............................................................................*
*Br  136 :primTrkHitPeakTimes : vector<float>                                *
*Entries :    75516 : Total  Size=   49938196 bytes  File Size  =   42888417 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.16     *
*............................................................................*
*Br  137 :primTrkHitSigPeakTimes : vector<float>                             *
*Entries :    75516 : Total  Size=   49944022 bytes  File Size  =   43439631 *
*Baskets :     1900 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  138 :primTrkHitRMSs : vector<float>                                     *
*Entries :    75516 : Total  Size=   49928681 bytes  File Size  =   41532996 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.20     *
*............................................................................*
*Br  139 :primTrkHitAmps : vector<float>                                     *
*Entries :    75516 : Total  Size=   49928681 bytes  File Size  =   43268220 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  140 :primTrkHitSigAmps : vector<float>                                  *
*Entries :    75516 : Total  Size=   49934390 bytes  File Size  =   38971113 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.28     *
*............................................................................*
*Br  141 :primTrkHitIntegrals : vector<float>                                *
*Entries :    75516 : Total  Size=   49938196 bytes  File Size  =   44176360 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.13     *
*............................................................................*
*Br  142 :primTrkHitSigIntegrals : vector<float>                             *
*Entries :    75516 : Total  Size=   49944022 bytes  File Size  =   43441505 *
*Baskets :     1900 : Basket Size=      32000 bytes  Compression=   1.15     *
*............................................................................*
*Br  143 :primTrkHitMultiplicities : vector<int>                             *
*Entries :    75516 : Total  Size=   49947830 bytes  File Size  =    1991848 *
*Baskets :     1900 : Basket Size=      32000 bytes  Compression=  25.06     *
*............................................................................*
*Br  144 :primTrkHitChi2NDFs : vector<float>                                 *
*Entries :    75516 : Total  Size=   49936293 bytes  File Size  =   45677509 *
*Baskets :     1899 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br  145 :primMCdEdxs : vector<float>                                        *
*Entries :    75516 : Total  Size=   17070144 bytes  File Size  =   14754075 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.16     *
*............................................................................*
*Br  146 :primMCXs  : vector<float>                                          *
*Entries :    75516 : Total  Size=   17067375 bytes  File Size  =   14984173 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  147 :primMCYs  : vector<float>                                          *
*Entries :    75516 : Total  Size=   17067375 bytes  File Size  =   15621166 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br  148 :primMCZs  : vector<float>                                          *
*Entries :    75516 : Total  Size=   17067375 bytes  File Size  =   14062296 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.21     *
*............................................................................*
*Br  149 :primMClastXs : vector<float>                                       *
*Entries :    75516 : Total  Size=   17071067 bytes  File Size  =   14997880 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.14     *
*............................................................................*
*Br  150 :primMClastYs : vector<float>                                       *
*Entries :    75516 : Total  Size=   17071067 bytes  File Size  =   15632479 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.09     *
*............................................................................*
*Br  151 :primMClastZs : vector<float>                                       *
*Entries :    75516 : Total  Size=   17071067 bytes  File Size  =   13886720 *
*Baskets :      919 : Basket Size=      32000 bytes  Compression=   1.23     *
*............................................................................*
*Br  152 :enterExitXp : enterExitXp/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      57788 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.99     *
*............................................................................*
*Br  153 :enterExitXm : enterExitXm/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      63501 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.81     *
*............................................................................*
*Br  154 :enterExitYp : enterExitYp/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      54513 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.11     *
*............................................................................*
*Br  155 :enterExitYm : enterExitYm/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      55012 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   2.09     *
*............................................................................*
*Br  156 :enterExitZp : enterExitZp/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      70948 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.62     *
*............................................................................*
*Br  157 :enterExitZm : enterExitZm/O                                        *
*Entries :    75516 : Total  Size=     125416 bytes  File Size  =      73162 *
*Baskets :      506 : Basket Size=      32000 bytes  Compression=   1.57     *
*............................................................................*

root [2] 

"""
