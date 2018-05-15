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
  beamPionCuts = beamCuts + "*((((!isMC) && pWC > 100 && pWC < 1100) || (isMC && trueStartMom > 100 && trueStartMom < 1100)) && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) < 5e4))"
  beamProtonCuts = beamCuts + "*((((!isMC) && pWC > 450 && pWC < 1100) || (isMC && trueStartMom > 450 && trueStartMom < 1100)) && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) > 7e5))"

  hitCuts = "*(primTrkXs > 3. && primTrkXs < 46. && primTrkYs < 18. && primTrkYs > -18. && primTrkZs > 3. && primTrkZs < 87.)"
  cosmicHitCuts = hitCuts
  beamHitCuts = hitCuts+"*(primTrkZs < 10.)"

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
      'fn': baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_all.root"],
      'name': "BeamRunIIP100A_PiMuE",
      'title': "Run II Beam +100 A #pi/#mu/e",
      'caption': "Run II Beam +100 A #pi/#mu/e",
      'isData': True,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root"],
      'name': "BeamMC_pip",
      'title': "Beam #pi MC",
      'caption': "Beam #pi MC",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear10_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear10_v5.root"],
      'name': "BeamMC_pip_presmear10",
      'title': "Beam #pi MC 10% Smearing",
      'caption': "Beam #pi MC 10% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root"],
      'name': "BeamMC_pip_presmear15",
      'title': "Beam #pi MC 15% Smearing",
      'caption': "Beam #pi MC 15% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear20_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear20_v5.root"],
      'name': "BeamMC_pip_presmear20",
      'title': "Beam #pi MC 20% Smearing",
      'caption': "Beam #pi MC 20% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root"],
      'name': "BeamMC_pip_presmear25",
      'title': "Beam #pi MC 25% Smearing",
      'caption': "Beam #pi MC 25% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear30_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear30_v5.root"],
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

  ########################################################
  ## Single Hists -- All Samples #########################
  ########################################################

  binning = [60,0.5,3.5]
  binning = [50,1.0,3.5]

  m2SF = 1.
  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': binning,
      'var': "primTrkdEdxs",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "pWC",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "(!isMC)*pWC+isMC*trueStartMom",
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
  ## Beam Pions Definitions ##############################
  ########################################################

  fileConfigs = [
    {
      'fn': baseDir+"cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current100_v02_all.root",
      'addFriend': ["friend", baseDir+"cosmicBeamData_v2/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_all.root"],
      'name': "BeamRunIIP100A_Proton",
      'title': "Run II Beam +100 A p",
      'caption': "Run II Beam +100 A p",
      'isData': True,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root"],
      'name': "BeamMC_pip",
      'title': "Beam #pi MC",
      'caption': "Beam #pi MC",
      'isData': False,
      'isBeam': True,
      'cuts': beamPionCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root"],
      'name': "BeamMC_p_presmear10",
      'title': "Beam p MC 10% Smearing",
      'caption': "Beam p MC 10% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root"],
      'name': "BeamMC_p_presmear15",
      'title': "Beam p MC 15% Smearing",
      'caption': "Beam p MC 15% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root"],
      'name': "BeamMC_p_presmear20",
      'title': "Beam p MC 20% Smearing",
      'caption': "Beam p MC 20% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root"],
      'name': "BeamMC_p_presmear25",
      'title': "Beam p MC 25% Smearing",
      'caption': "Beam p MC 25% Smearing",
      'isData': False,
      'isBeam': True,
      'cuts': beamProtonCuts + beamHitCuts,
    },
    {
      'fn': baseDir+"cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root",
      'addFriend': ["friend", baseDir+"cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root"],
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
      'binning': binning,
      'var': "primTrkdEdxs",
      'cuts': "1",
      'normalize': True,
    },
    {
      'name': "pWC",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "(!isMC)*pWC+isMC*trueStartMom",
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

  fileConfigs = [
    {
      'fn': [baseDir+"cosmicsManyRecos/Cosmics_RIIN100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIN60.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP60.root"],
      'name': "CosmicsRunII_PhiGeq0",
      'title': "Run II Cosmics #phi #geq 0",
      'caption': "Run II Cosmics #phi #geq 0",
      'isData': True,
    },
    {
      'fn': [baseDir+"cosmicsManyRecos/Cosmics_RIIN100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIN60.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP60.root"],
      'name': "CosmicsRunII_PhiLt0",
      'title': "Run II Cosmics #phi < 0",
      'caption': "Run II Cosmics #phi < 0",
      'isData': True,
    },
  ]
