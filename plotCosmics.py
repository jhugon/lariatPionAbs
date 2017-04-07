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
  #cuts += "*( iBestMatch >= 0)" # primary Track found

  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100
  fileConfigs = [
    {
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/CosmicAna_Pos_RunII.root",
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_data_Lovely1_Pos_RunII_elanag_v02_v05/anahist.root",
      'name': "RunIIPos",
      'title': "Run II Pos. Polarity",
      'caption': "Run II Pos. Polarity",
      'color': root.kBlack,
      'isData': True,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_cosmics_v1/anahist.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'color': root.kRed-4,
      'isData': False,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_halo_v1/anahist.root",
      'name': "HaloMC",
      'title': "Halo MC",
      'caption': "Halo MC",
      'color': root.kBlue+7,
      'isData': False,
    },
  ]

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
    {
      'name': "trackLength",
      'xtitle': "TPC Track Length [cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,-10,100],
      'var': "trackLength",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
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
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [200,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
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

#  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
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
#    {
#      'name': "primTrkdEdxVRange",
#      'xtitle': "Primary Track Hit Residual Range [cm]",
#      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
#      'binning': [100,0,100,100,0,50],
#      'var': "primTrkdEdxs:primTrkResRanges",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
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
      'name': "primTrkStartThetaVPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Primary TPC Track #theta [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "primTrkStartTheta*180/pi:primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkdEdxsVx",
      'xtitle': "Hit x [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,0,50,1000,0,50],
      'var': "primTrkdEdxs:primTrkXs",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVy",
      'xtitle': "Hit y [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,1000,0,50],
      'var': "primTrkdEdxs:primTrkYs",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVz",
      'xtitle': "Hit z [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,-5,95,1000,0,50],
      'var': "primTrkdEdxs:primTrkZs",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVrun",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [200,8000,10000,500,0,50],
      'var': "primTrkdEdxs:runNumber",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
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
  outfile = root.TFile("cosmics_hists.root","recreate")
  outfile.cd()
  for var in hists:
    for ds in hists[var]:
        newname = var+"_"+ds
        hist = hists[var][ds]
        hist.SetName(newname)
        hist.Print()
        hist.Write()
  outfile.Close()
