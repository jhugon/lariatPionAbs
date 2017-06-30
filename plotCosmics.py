#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*(isMC || ((triggerBits >> 4) & 1))" # BEAMON trigger
  cuts += "*(isMC || ((triggerBits >> 10) & 1))" # COSMICON trigger
  #cuts += "*(isMC || !((triggerBits >> 10) & 1))" # Not COSMICON trigger
  #cuts += "*(isMC || ((triggerBits >> 11) & 1))" # COSMIC trigger
  cuts += "*(isMC || (nWCTracks ==0 && nTOFs ==0))"
  cuts += "*( iBestMatch >= 0)" # primary Track found
  cuts += "*(acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi < 5. || acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi > 175.)" # theta vertical
  #cuts += "*((!isMC) || (trueStartMom>3000. && trueStartMom < 8000.))"
  #cuts += "*( iBestMatch >= 0)" # primary Track found
  #cuts += "*(primTrkPitches > 0.5 && primTrkPitches < 0.6)"
  #cuts += "*(primTrkXs > 10. && primTrkXs < 11.)"

  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100
  fileConfigs = [
    {
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/CosmicAna_Pos_RunII.root",
      #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna2/lariat_data_Lovely1_RunII_run8300to8500_jhugon_v01_v01/anahist.root",
      'fn': "cosmicsv2/lariat_data_Lovely1_RunII_run8300to8500_jhugon_v01_v01.root",
      'name': "RunII8300to8500",
      'title': "Run II 8300-8500",
      'caption': "Run II 8300-8500",
      'color': root.kBlack,
      'isData': True,
    },
    {
      #'fn': "cosmicsv2/lariat_PiAbsAndChEx_cosmics_v3.root",
      'fn': "cosmics_vert/coscmis_vert_v1.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'isData': False,
      'scaleFactor': 1367./99535.
    },
    #{
    #  'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_presmear20perc_v1/anahist.root",
    #  'name': "CosmicMC_presmear20perc",
    #  'title': "Cosmic MC Pre-smear 20% ",
    #  'caption': "Cosmic MC Pre-smear 20%",
    #  'isData': False,
    #  'scaleFactor': 1367./99692.
    #},
    {
      #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_presmear30perc_v1/anahist.root",
      'fn': "cosmics_vert/coscmis_vert_presmear30perc_v1.root",
      'name': "CosmicMC_presmear30perc",
      'title': "Cosmic MC Pre-smear 30% ",
      'caption': "Cosmic MC Pre-smear 30%",
      'isData': False,
      'scaleFactor': 1367./19365.
    },
    {
      #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_presmear35perc_v1/anahist.root",
      'fn': "cosmics_vert/coscmis_vert_presmear35perc_v1.root",
      'name': "CosmicMC_presmear35perc",
      'title': "Cosmic MC Pre-smear 35% ",
      'caption': "Cosmic MC Pre-smear 35%",
      'isData': False,
      'scaleFactor': 1367./19379.
    },
    {
      #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_presmear40perc_v1/anahist.root",
      'fn': "cosmics_vert/coscmis_vert_presmear40perc_v1.root",
      'name': "CosmicMC_presmear40perc",
      'title': "Cosmic MC Pre-smear 40% ",
      'caption': "Cosmic MC Pre-smear 40%",
      'isData': False,
      'scaleFactor': 1367./110166.
    },
    #{
    #  'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_postsmear10perc_v1/anahist.root",
    #  'name': "CosmicMC_postsmear10perc",
    #  'title': "Cosmic MC Post-smear 10% ",
    #  'caption': "Cosmic MC Post-smear 10%",
    #  'isData': False,
    #  'scaleFactor': 1367./109553.
    #},
    #{
    #  'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_postsmear20perc_v1/anahist.root",
    #  'name': "CosmicMC_postsmear20perc",
    #  'title': "Cosmic MC Post-smear 20% ",
    #  'caption': "Cosmic MC Post-smear 20%",
    #  'isData': False,
    #  'scaleFactor': 1367./112612.
    #},
    #{
    #  'fn': "cosmics_vert/coscmis_vert_postsmear40perc_v1.root",
    #  'name': "CosmicMC_postsmear40perc",
    #  'title': "Cosmic MC Post-smear 40% ",
    #  'caption': "Cosmic MC Post-smear 40%",
    #  'isData': False,
    #  'scaleFactor': 1367./110166.
    #},
    #{
    #  'fn': "cosmics_vert/coscmis_vert_postsmear60perc_v1.root",
    #  'name': "CosmicMC_postsmear60perc",
    #  'title': "Cosmic MC Post-smear 60% ",
    #  'caption': "Cosmic MC Post-smear 60%",
    #  'isData': False,
    #  'scaleFactor': 1367./25596.
    #},
    #{
    #  'fn': "cosmics_vert/coscmis_vert_postsmear80perc_v1.root",
    #  'name': "CosmicMC_postsmear80perc",
    #  'title': "Cosmic MC Post-smear 80% ",
    #  'caption': "Cosmic MC Post-smear 80%",
    #  'isData': False,
    #  'scaleFactor': 1367./25042.
    #},
    #{
    #  'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_postsmear120perc_v1/anahist.root",
    #  'name': "CosmicMC_postsmear120perc",
    #  'title': "Cosmic MC Post-smear 120% ",
    #  'caption': "Cosmic MC Post-smear 120%",
    #  'isData': False,
    #  'scaleFactor': 1367./21010.
    #},
    #{
    #  'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_vert_postnoise10perc_v1/anahist.root",
    #  'name': "CosmicMC_2xNoise",
    #  'title': "Cosmic MC 2x Noise",
    #  'caption': "Cosmic MC 2x Noise",
    #  'isData': False,
    #  'scaleFactor': 1367./110413.
    #},
  ]

  for i in range(len(fileConfigs)):
    if not ('isData' in fileConfigs[i]) or not fileConfigs[i]['isData']:
        fileConfigs[i]['color'] = COLORLIST[i-1]

  histConfigs = [
#    {
#      'name': "trackXFront",
#      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [50,0,50],
#      'var': "trackXFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackYFront",
#      'xtitle': "Y of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [50,-50,50],
#      'var': "trackYFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackMatchLowestZ",
#      'xtitle': "TPC Track Start Z [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [40,0,20],
#      'var': "trackMatchLowestZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "nTOFs",
#      'xtitle': "Number of TOF Objects",
#      'ytitle': "Events / bin",
#      'binning': [11,0,10],
#      'var': "nTOFs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartX",
#      'xtitle': "TPC Track Start X [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,60],
#      'var': "trackStartX",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartY",
#      'xtitle': "TPC Track Start Y [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-50,50],
#      'var': "trackStartY",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartZ",
#      'xtitle': "TPC Track Start Z [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,110],
#      'var': "trackStartZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndX",
#      'xtitle': "TPC Track End X [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,60],
#      'var': "trackEndX",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndY",
#      'xtitle': "TPC Track End Y [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-50,50],
#      'var': "trackEndY",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndZ",
#      'xtitle': "TPC Track End Z [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,110],
#      'var': "trackEndZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackLength",
#      'xtitle': "TPC Track Length [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-10,100],
#      'var': "trackLength",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
    #{
    #  'name': "trackCaloKin",
    #  'xtitle': "TPC Calo Estimate of KE [MeV]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [50,0,2500],
    #  'var': "trackCaloKin",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "primTrkLength",
      'xtitle': "Primary TPC Track Length [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "primTrkLength",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "primTrkStartTheta",
      'xtitle': "Primary TPC Track #theta [deg]",
      'ytitle': "Events / bin",
      'binning': [180,0,180],
      'var': "primTrkStartTheta*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Events / bin",
      'binning': [180,-180,180],
      'var': "primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartThetaVertical",
      'xtitle': "Primary TPC Track #theta w.r.t. Vertical [deg]",
      'ytitle': "Events / bin",
      'binning': [180,0,180],
      'var': "acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi",
      'cuts': weightStr+"*(primTrkStartTheta > -360.)",
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      'normalize': not logy,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxs_zoom3",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      'normalize': logy,
      'logy': not logy,
    },
#    {
#      'name': "primTrkTruedEdxs",
#      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,50],
#      'var': "primTrkTruedEdxs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedEdxs_zoom",
#      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkTruedEdxs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkdQdxs",
#      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
#      'ytitle': "Events / bin",
#      'binning': [300,0,3e4],
#      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkdQdxs_zoom",
#      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,8e3],
#      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#      'printIntegral' : True,
#    },
#    {
#      'name': "primTrkdQdxs_zoom2",
#      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,8e3],
#      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': not logy,
#      'printIntegral' : True,
#    },
#    {
#      'name': "primTrkdQs",
#      'xtitle': "Primary TPC Track dQ [ADC]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,8e3],
#      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': not logy,
#      'printIntegral' : True,
#    },
#    {
#      'name': "primTrkTruedQdxs",
#      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,5e6],
#      'var': "primTrkTruedQdxs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedQdxs_zoom",
#      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,1e5],
#      'var': "primTrkTruedQdxs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedQs",
#      'xtitle': "Primary TPC Track Q [e^{-}]",
#      'ytitle': "Events / bin",
#      #'binning': [200,0,1e5],
#      'binning': getLogBins(100,1e3,1e7),
#      'var': "primTrkTruedQs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#      'logx': True,
#    },
#    {
#      'name': "primTrkTruedQs2",
#      'xtitle': "Primary TPC Track Q [e^{-}]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,2e5],
#      'var': "primTrkTruedQs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': not logy,
#      'logx': False,
#    },
#    {
#      'name': "primTrkdEdxs_Q1000to1500_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 1500.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "1000 ADC < Q < 1500 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q1500to2000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1500. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 2000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "1500 ADC < Q < 2000 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q2000to3000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 2000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 3000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "2000 ADC < Q < 3000 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q3000to4000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 3000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 4000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "3000 ADC < Q < 4000 ADC",
#    },
    #{
    #  'name': "primTrkdEdxsFidCut",
    #  'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [200,0,50],
    #  'var': "primTrkdEdxs",
    #  'cuts': weightStr+"*primTrkInFids",
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "primTrkResRanges",
      'xtitle': "Primary TPC Track Residual Range [cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,100],
      'var': "primTrkResRanges",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitches",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10],
      'var': "primTrkPitches",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    #{
    #  'name': "primTrkEndKin",
    #  'xtitle': "Primary TPC Track End Kinetic Energy [MeV]",
    #  'ytitle': "Events / bin",
    #  'binning': [50,0,1000],
    #  'var': "primTrkEndKin",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkEndKinFid",
    #  'xtitle': "Primary TPC Track End Kinetic Energy [MeV]",
    #  'ytitle': "Events / bin",
    #  'binning': [50,0,1000],
    #  'var': "primTrkEndKinFid",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueEndProcess",
    #  'xtitle': "trueEndProcess",
    #  'ytitle': "Events / bin",
    #  'binning': [17,0,17],
    #  'var': "trueEndProcess",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
#  fileConfigMCs = copy.deepcopy(fileConfigs)
#  fileConfigData = None
#  for i in reversed(range(len(fileConfigMCs))):
#    if 'isData' in fileConfigMCs[i] and fileConfigMCs[i]['isData']:
#      fileConfigData = fileConfigMCs.pop(i)
#  DataMCStack(fileConfigData,fileConfigMCs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)

########################################################
########################################################
########################################################

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'title': "All",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      'color': root.kBlack,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "x < 10 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs < 10.)",
      'color': root.kBlue-7,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "10 cm < x < 20 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 10. && primTrkXs < 20.)",
      'color': root.kRed-4,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "20 cm < x < 30 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 20. && primTrkXs < 30.)",
      'color': root.kGreen,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "30 cm < x < 40 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 30. && primTrkXs < 40.)",
      'color': root.kMagenta-4,
      #'normalize': True,
      'logy': logy,
    },
  ]

#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_dEdxForX")

########################################################
########################################################
########################################################

  histConfigs = [
    {
      'name': "primTrkdEdxVRange",
      'xtitle': "Primary Track Hit Residual Range [cm]",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [100,0,100,100,0,50],
      'var': "primTrkdEdxs:primTrkResRanges",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
#    {
#      'name': "primTrkdEdxVRangeFidCut",
#      'xtitle': "Primary Track Hit Residual Range [cm]",
#      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
#      'binning': [100,0,100,100,0,50],
#      'var': "primTrkdEdxs:primTrkResRanges",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "trackYFrontVtrackXFront",
#      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "Y of TPC Track Projection to TPC Front [cm]",
#      'binning': [40,0,40,40,-20,20],
#      'var': "trackYFront:trackXFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
    {
      'name': "primTrkdEdxVwire",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxs:primTrkTrueWires",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkStartThetaVPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Primary TPC Track #theta [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "primTrkStartTheta*180/pi:primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
#    {
#      'name': "primTrkdEdxsVx",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [20,0,50,10000,0,50],
#      'var': "primTrkdEdxs:primTrkXs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVy",
#      'xtitle': "Hit y [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [20,-25,25,10000,0,50],
#      'var': "primTrkdEdxs:primTrkYs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVz",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,-5,95,10000,0,50],
#      'var': "primTrkdEdxs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVrun",
#      'xtitle': "Run Number",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [200,8000,1000,500,0,50],
#      'var': "primTrkdEdxs:runNumber",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVyFromCenter",
#      'xtitle': "Hit |y| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,25,10000,0,50],
#      'var': "primTrkdEdxs:fabs(primTrkYs)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVzFromCenter",
#      'xtitle': "Hit |z-45| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,50,10000,0,50],
#      'var': "primTrkdEdxs:fabs(primTrkZs-45.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "hitYVhitX",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [60,-5,55,60,-30,30],
#      'var': "primTrkYs:primTrkXs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitX_cosmicon",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [60,-5,55,60,-30,30],
#      'var': "primTrkYs:primTrkXs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_cosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ_cosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ_NotCosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': "1"+"*(isMC || !((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_cosmic",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 11) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_beamon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 4) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_pickytrack",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || nWCTracks > 0)",
#      #'normalize': True,
#      #'logz': True,
#    },
  ]

  hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
#  outfile = root.TFile("cosmics_hists.root","recreate")
#  outfile.cd()
#  for var in hists:
#    for ds in hists[var]:
#        newname = var+"_"+ds
#        hist = hists[var][ds]
#        hist.SetName(newname)
#        hist.Print()
#        hist.Write()
#  outfile.Close()

######################################################################################
######################################################################################
######################################################################################
######################################################################################

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      "title": "Reco",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedEdxs",
      "title": "MC Truth",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primMCdEdxs",
      "title": "MC Trajectory",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primMCdEdxs",
      'cuts': weightStr+"*(primMCXs>2. && primMCXs < 47. && primMCYs > -23. && primMCYs < 23. && primMCZs > 0. && primMCZs < 90 && primMClastXs>2. && primMClastXs < 47. && primMClastYs > -23. && primMClastYs < 23. && primMClastZs > 0. && primMClastZs < 90 )",
      #'normalize': True,
      'logy': logy,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="CosmicsTrue_dEdx")

  histConfigs = [
    {
      'name': "primTrkdEdxs_zoom",
      "title": "Reco",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedEdxs_zoom",
      "title": "MC Truth",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primMCdEdxs_zoom",
      "title": "MC Trajectory",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primMCdEdxs",
      'cuts': weightStr+"*(primMCXs>2. && primMCXs < 47. && primMCYs > -23. && primMCYs < 23. && primMCZs > 0. && primMCZs < 90 && primMClastXs>2. && primMClastXs < 47. && primMClastYs > -23. && primMClastYs < 23. && primMClastZs > 0. && primMClastZs < 90 )",
      #'normalize': True,
      'logy': logy,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="CosmicsTrue_dEdxZoom")

  histConfigs = [
    {
      'name': "primTrkdQdxs_zoom",
      'title': "Reco [10.8*ADC/cm]",
      'xtitle': "Primary TPC Track dQ/dx",# [10*ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,1e5],
      'var': "10.8*primTrkdQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedQdxs_zoom",
      'title': "MC Truth [e^{-}/cm]",
      'xtitle': "Primary TPC Track True dQ/dx",# [e^{-}/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,1e5],
      'var': "primTrkTruedQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
#  fileConfigMCs = copy.deepcopy(fileConfigs)
#  fileConfigData = None
#  for i in reversed(range(len(fileConfigMCs))):
#    if 'isData' in fileConfigMCs[i] and fileConfigMCs[i]['isData']:
#      fileConfigData = fileConfigMCs.pop(i)
#  DataMCStack(fileConfigData,fileConfigMCs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)

########################################################
########################################################
########################################################

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'title': "All",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      'color': root.kBlack,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "x < 10 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs < 10.)",
      'color': root.kBlue-7,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "10 cm < x < 20 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 10. && primTrkXs < 20.)",
      'color': root.kRed-4,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "20 cm < x < 30 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 20. && primTrkXs < 30.)",
      'color': root.kGreen,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'title': "30 cm < x < 40 cm",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr + "*(primTrkXs > 30. && primTrkXs < 40.)",
      'color': root.kMagenta-4,
      #'normalize': True,
      'logy': logy,
    },
  ]

#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_dEdxForX")

########################################################
########################################################
########################################################

  histConfigs = [
    {
      'name': "primTrkdEdxVRange",
      'xtitle': "Primary Track Hit Residual Range [cm]",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [100,0,100,100,0,50],
      'var': "primTrkdEdxs:primTrkResRanges",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
#    {
#      'name': "primTrkdEdxVRangeFidCut",
#      'xtitle': "Primary Track Hit Residual Range [cm]",
#      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
#      'binning': [100,0,100,100,0,50],
#      'var': "primTrkdEdxs:primTrkResRanges",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "trackYFrontVtrackXFront",
#      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "Y of TPC Track Projection to TPC Front [cm]",
#      'binning': [40,0,40,40,-20,20],
#      'var': "trackYFront:trackXFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
    {
      'name': "primTrkdEdxVwire",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxs:primTrkTrueWires",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkStartThetaVPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Primary TPC Track #theta [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "primTrkStartTheta*180/pi:primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
#    {
#      'name': "primTrkdEdxsVx",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [20,0,50,10000,0,50],
#      'var': "primTrkdEdxs:primTrkXs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVy",
#      'xtitle': "Hit y [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [20,-25,25,10000,0,50],
#      'var': "primTrkdEdxs:primTrkYs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVz",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,-5,95,10000,0,50],
#      'var': "primTrkdEdxs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVrun",
#      'xtitle': "Run Number",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [200,8000,1000,500,0,50],
#      'var': "primTrkdEdxs:runNumber",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVyFromCenter",
#      'xtitle': "Hit |y| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,25,10000,0,50],
#      'var': "primTrkdEdxs:fabs(primTrkYs)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVzFromCenter",
#      'xtitle': "Hit |z-45| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,50,10000,0,50],
#      'var': "primTrkdEdxs:fabs(primTrkZs-45.)",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "hitYVhitX",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [60,-5,55,60,-30,30],
#      'var': "primTrkYs:primTrkXs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitX_cosmicon",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [60,-5,55,60,-30,30],
#      'var': "primTrkYs:primTrkXs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_cosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ_cosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ_NotCosmicon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': "1"+"*(isMC || !((triggerBits >> 10) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_cosmic",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 11) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_beamon",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || ((triggerBits >> 4) & 1))",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ_pickytrack",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': "1"+"*(isMC || nWCTracks > 0)",
#      #'normalize': True,
#      #'logz': True,
#    },
  ]

  hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
#  outfile = root.TFile("cosmics_hists.root","recreate")
#  outfile.cd()
#  for var in hists:
#    for ds in hists[var]:
#        newname = var+"_"+ds
#        hist = hists[var][ds]
#        hist.SetName(newname)
#        hist.Print()
#        hist.Write()
#  outfile.Close()

######################################################################################
######################################################################################
######################################################################################
######################################################################################

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      "title": "Reco",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedEdxs",
      "title": "MC Truth",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primMCdEdxs",
      "title": "MC Trajectory",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [400,0,50],
      'var': "primMCdEdxs",
      'cuts': weightStr+"*(primMCXs>2. && primMCXs < 47. && primMCYs > -23. && primMCYs < 23. && primMCZs > 0. && primMCZs < 90 && primMClastXs>2. && primMClastXs < 47. && primMClastYs > -23. && primMClastYs < 23. && primMClastZs > 0. && primMClastZs < 90 )",
      #'normalize': True,
      'logy': logy,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="CosmicsTrue_dEdx")

  histConfigs = [
    {
      'name': "primTrkdEdxs_zoom",
      "title": "Reco",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedEdxs_zoom",
      "title": "MC Truth",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primMCdEdxs_zoom",
      "title": "MC Trajectory",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primMCdEdxs",
      'cuts': weightStr+"*(primMCXs>2. && primMCXs < 47. && primMCYs > -23. && primMCYs < 23. && primMCZs > 0. && primMCZs < 90 && primMClastXs>2. && primMClastXs < 47. && primMClastYs > -23. && primMClastYs < 23. && primMClastZs > 0. && primMClastZs < 90 )",
      #'normalize': True,
      'logy': logy,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="CosmicsTrue_dEdxZoom")

  histConfigs = [
    {
      'name': "primTrkdQdxs_zoom",
      'title': "Reco [10.8*ADC/cm]",
      'xtitle': "Primary TPC Track dQ/dx",# [10*ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,1e5],
      'var': "10.8*primTrkdQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedQdxs_zoom",
      'title': "MC Truth [e^{-}/cm]",
      'xtitle': "Primary TPC Track True dQ/dx",# [e^{-}/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,1e5],
      'var': "primTrkTruedQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="CosmicsTrue_dQdxZoom")

  histConfigs = [
    {
      'name': "primTrkdEdxsVprimTrkQs",
      'xtitle': "Primary TPC Track Hit Q [ADC]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [200,0,8e3,200,0,10],
      'var': "primTrkdEdxs:primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdEdxsVprimTrkdQdxs",
      'xtitle': "Primary TPC Track Hit dQ/dx [ADC/cm]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [200,0,1e4,200,0,10],
      'var': "primTrkdEdxs:primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdEdxsVprimTrkTruedEdx",
      'xtitle': "Primary TPC Track Hit True dE/dx [MeV/cm]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [200,0,10,200,0,10],
      'var': "primTrkdEdxs:primTrkTruedEdxs",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdEdxsVprimTrkXs",
      'xtitle': "Primary TPC Track Hit X [cm]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [50,0,50,50,0,10],
      'var': "primTrkdEdxs:primTrkXs",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdEdxsVprimTrkXs_zoom",
      'xtitle': "Primary TPC Track Hit X [cm]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [50,0,50,100,1,3],
      'var': "primTrkdEdxs:primTrkXs",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdEdxsVprimTrkPitches",
      'xtitle': "Primary TPC Track Hit Pitch [cm]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [50,0,10,50,0,10],
      'var': "primTrkdEdxs:primTrkPitches",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdQsVprimTrkXs",
      'xtitle': "Primary TPC Track Hit X [cm]",
      'ytitle': "Primary TPC Track Hit Q [ADC]",
      'binning': [50,0,50,50,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.):primTrkXs",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdQsVprimTrkXs_zoom",
      'xtitle': "Primary TPC Track Hit X [cm]",
      'ytitle': "Primary TPC Track Hit Q [ADC]",
      'binning': [50,0,50,100,500,2500],
      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.):primTrkXs",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdQsVprimTrkPitches",
      'xtitle': "Primary TPC Track Hit Pitch [cm]",
      'ytitle': "Primary TPC Track Hit Q [ADC]",
      'binning': [50,0,10,50,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.):primTrkPitches",
      'cuts': weightStr,
    },
    {
      'name': "primTrkdQdxsVprimTrkTruedQdx",
      'xtitle': "Primary TPC Track Hit True dQ/dx [e-/cm]",
      'ytitle': "Primary TPC Track Hit dQ/dx [ADC/cm]",
      'binning': [200,0,1e5,200,0,8e3],
      'var': "primTrkdQdxs:primTrkTruedQdxs",
      'cuts': weightStr,
    },
  ]
  #plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
