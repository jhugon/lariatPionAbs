#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF < 25)))" # pions
  cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # protons
  cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks
#  cuts += "*(trackMatchDeltaAngle*180/pi > 15.)"
#  cuts += "*(sqrt(pow(xWC-23.75,2)+pow(yWC-0.2,2)) < 11.93)" # wc track in flange
#  cuts += "*(sqrt(pow(trackXFront-23.75,2)+pow(trackYFront-0.2,2)) < 11.93)" # TPC track in flange
#  cuts += "*(trackMatchLowestZ < 2.)" # matching
  #cuts = "*(iBestMatch >= 0 && fabs(trackMatchDeltaY[iBestMatch]) < 5. && fabs(trackMatchDeltaX[iBestMatch]) < 5. && trackMatchDeltaAngle[iBestMatch]*180/pi < 10.)" # matching
  ###
  ###
  secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2. || trackEndDistToPrimTrkEnd < 2.)"
  #weightStr = "pzWeight"+cuts
  weightStr = "1"+cuts
  nData = 30860.0
  logy = False

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      'fn': "piAbs_data_Pos_RunI_v03.root",
      'addFriend': ["friend", "friendTree_Pos_RunI_v03.root"],
      #'fn': "test_data_Pos_RunI_piAbsSelector.root",
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
      'isData': True,
    },
    #{
    #  'fn': "piAbs_data_Pos_RunII_v03.root",
    #  #'addFriend': ["friend", "friendTree_Pos_RunII_v03.root"],
    #  #'fn': "test_data_Pos_RunII_piAbsSelector.root",
    #  'name': "RunII_Pos",
    #  'title': "Run II Pos. Polarity",
    #  'caption': "Run II Pos. Polarity",
    #  'color': root.kGray+1,
    #  'isData': True,
    #},
    #{
    #  'fn': "piAbs_pip_v5.root",
    #  'addFriend': ["friend", "friendTree_pip_v5.root"],
    #  #'fn': "test_pip_piAbsSelector.root",
    #  'name': "pip",
    #  'title': "#pi^{+} MC",
    #  'caption': "#pi^{+} MC",
    #  'color': root.kBlue-7,
    #  #'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
    #  'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.70, # pion/tpc tracks cuts
    #},
    {
      'fn': "piAbs_p_v5.root",
      'addFriend': ["friend", "friendTree_p_v5.root"],
      #'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
    },
    #{
    #  'fn': "piAbs_ep_v5.root",
    #  'addFriend': ["friend", "friendTree_ep_v5.root"],
    #  #'fn': "test_ep_piAbsSelector.root",
    #  'name': "ep",
    #  'title': "e^{+} MC",
    #  'caption': "e^{+} MC",
    #  'color': root.kGreen,
    #  #'scaleFactor': 1./35700*nData*0.301/(1.-0.086), #No Cuts
    #  'scaleFactor': 1./35700*nData*0.301/(1.-0.086)*0.70, # pion/tpc tracks cuts
    #},
    #{
    #  'fn': "piAbs_mup_v5.root",
    #  'addFriend': ["friend", "friendTree_mup_v5.root"],
    #  #'fn': "test_mup_piAbsSelector.root",
    #  'name': "mup",
    #  'title': "#mu^{+} MC",
    #  'caption': "#mu^{+} MC",
    #  'color': root.kMagenta-4,
    #  #'scaleFactor': 1./35200*nData*0.021/(1.-0.086), #No Cuts
    #  'scaleFactor': 1./35200*nData*0.021/(1.-0.086)*0.70, # pion/tpc tracks cuts
    #},
    #{
    #  'fn': "piAbs_kp_v5.root",
    #  'addFriend': ["friend", "friendTree_kp_v5.root"],
    #  #'fn': "test_kp_piAbsSelector.root",
    #  'name': "kp",
    #  'title': "K^{+} MC",
    #  'caption': "K^{+} MC",
    #  'color': root.kOrange-3,
    #  'scaleFactor': 1./35700*nData*0.00057/(1.-0.086), #No Cuts
    #},
    #{
    #  #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_gam_v4/anahist.root",
    #  #'addFriend': ["friend", "friendTree_gam_v4.root"],
    #  'fn': "test_gam_piAbsSelector.root",
    #  'name': "gam",
    #  'title': "#gamma MC",
    #  'caption': "#gamma MC",
    #  'color': root.kOrange-3,
    #  'scaleFactor': 2953., #AllWeightsCuts Proton
    #},
  ]

  histConfigs = [
    {
      'name': "xWC4Hit",
      'xtitle': "X Position at WC4 [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,50],
      'var': "xWC4Hit",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "yWC4Hit",
      'xtitle': "Y Position at WC4 [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-25,25],
      'var': "yWC4Hit",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "zWC4Hit",
      'xtitle': "Z Position at WC4 [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-97,-95],
      'var': "zWC4Hit",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "xWC",
      'xtitle': "X Position of WC track projection to TPC [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,75],
      'var': "xWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "yWC",
      'xtitle': "Y Position of WC track projection to TPC [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-50,50],
      'var': "yWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "pzWC",
      'xtitle': "Z Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "pzWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "pWC",
      'xtitle': "Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "pzWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    #{
    #  'name': "kinWC",
    #  'xtitle': "Kinetic Energy at WC [MeV/c] (m=m_{#pi^{#pm}})",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,2000],
    #  'var': "kinWC",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "kinWCInTPC",
    #  'xtitle': "Kinetic Energy at TPC [MeV/c] (m=m_{#pi^{#pm}})",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,2000],
    #  'var': "kinWCInTPC",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "phiWC",
      'xtitle': "WC track #phi [deg]",
      'ytitle': "Events / bin",
      'binning': [360,-180,180],
      'var': "phiWC*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "thetaWC",
      'xtitle': "WC track #theta [deg]",
      'ytitle': "Events / bin",
      'binning': [40,0,10],
      'var': "thetaWC*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "thetaxzWC",
      'xtitle': "WC track #theta_{xz} [deg]",
      'ytitle': "Events / bin",
      'binning': [100,-10,10],
      'var': "(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "thetayzWC",
      'xtitle': "WC track #theta_{yz} [deg]",
      'ytitle': "Events / bin",
      'binning': [100,-5,5],
      'var': "(asin(sin(thetaWC)*sin(phiWC)))*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "sinthetayz",
      'xtitle': "WC Track sin(#theta_{yz})",
      'ytitle': "Tracks / bin",
      'binning': [80,-0.1,0.1],
      'var': "sin(thetaWC)*sin(phiWC)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
#    {
#      'name': "nTracks",
#      'xtitle': "Number of TPC Tracks / Event",
#      'ytitle': "Events / bin",
#      'binning': [31,0,30],
#      'var': "nTracks",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "nTracksInFirstZ2",
#      'xtitle': "Number of TPC Tracks in first 2 cm / Event",
#      'ytitle': "Events / bin",
#      'binning': [16,0,15],
#      'var': "nTracksInFirstZ[2]",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "nTracksInFirstZ14",
#      'xtitle': "Number of TPC Tracks in first 14 cm / Event",
#      'ytitle': "Events / bin",
#      'binning': [16,0,15],
#      'var': "nTracksInFirstZ[14]",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "nTracksLengthLt5",
#      'xtitle': "Number of TPC Tracks with length < 5 cm / Event",
#      'ytitle': "Events / bin",
#      'binning': [16,0,15],
#      'var': "nTracksLengthLt[5]",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
    {
      'name': "trackMatchDeltaX",
      'xtitle': "TPC / WC Track #Delta x at TPC Front [cm]",
      'ytitle': "TPC Tracks / bin",
      'binning': [40,-20,20],
      'var': "trackMatchDeltaX[iBestMatch]",
      'cuts': "(iBestMatch >= 0)*"+weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackMatchDeltaY",
      'xtitle': "TPC / WC Track #Delta y at TPC Front [cm]",
      'ytitle': "TPC Tracks / bin",
      'binning': [40,-20,20],
      'var': "trackMatchDeltaY[iBestMatch]",
      'cuts': "(iBestMatch >= 0)*"+weightStr,
      #'normalize': True,
      'logy': logy,
    },
#    {
#      'name': "trackMatchDeltaR",
#      'xtitle': "TPC / WC Track #Delta r at TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [40,0,20],
#      'var': "trackMatchDeltaR",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
    {
      'name': "trackMatchDeltaAngle",
      'xtitle': "TPC / WC Track #Delta #alpha [deg]",
      'ytitle': "TPC Tracks / bin",
      #'binning': [90,0,180],
      'binning': [20,0,20],
      'var': "trackMatchDeltaAngle[iBestMatch]*180/pi",
      'cuts': "(iBestMatch >= 0)*"+weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackXFront",
      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
      'ytitle': "TPC Tracks / bin",
      'binning': [50,0,50],
      'var': "trackXFront",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackYFront",
      'xtitle': "Y of TPC Track Projection to TPC Front [cm]",
      'ytitle': "TPC Tracks / bin",
      'binning': [50,-50,50],
      'var': "trackYFront",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackMatchLowestZ",
      'xtitle': "TPC Track Start Z [cm]",
      'ytitle': "TPC Tracks / bin",
      'binning': [40,0,20],
      'var': "trackMatchLowestZ",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
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
#      'name': "TOFs",
#      'xtitle': "TOF [ns]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,100],
#      'var': "TOFs[0]",
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
#    #{
#    #  'name': "trackEndX",
#    #  'xtitle': "TPC Track End X [cm]",
#    #  'ytitle': "Tracks / bin",
#    #  'binning': [100,-20,60],
#    #  'var': "trackEndX",
#    #  'cuts': weightStr,
#    #  #'normalize': True,
#    #  'logy': logy,
#    #},
#    #{
#    #  'name': "trackEndY",
#    #  'xtitle': "TPC Track End Y [cm]",
#    #  'ytitle': "Tracks / bin",
#    #  'binning': [100,-50,50],
#    #  'var': "trackEndY",
#    #  'cuts': weightStr,
#    #  #'normalize': True,
#    #  'logy': logy,
#    #},
#    #{
#    #  'name': "trackEndZ",
#    #  'xtitle': "TPC Track End Z [cm]",
#    #  'ytitle': "Tracks / bin",
#    #  'binning': [100,-20,110],
#    #  'var': "trackEndZ",
#    #  'cuts': weightStr,
#    #  #'normalize': True,
#    #  'logy': logy,
#    #},
    #{
    #  'name': "trackLength",
    #  'xtitle': "TPC Track Length [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-10,100],
    #  'var': "trackLength",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
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
    #{
    #  'name': "trackLLHPion",
    #  'xtitle': "TPC Track Pion -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHPion",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackLLHProton",
    #  'xtitle': "TPC Track Proton -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHProton",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackLLHMuon",
    #  'xtitle': "TPC Track Muon -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHMuon",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackLLHKaon",
    #  'xtitle': "TPC Track Kaon -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHKaon",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackPIDA",
    #  'xtitle': "TPC Track PIDA",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,50],
    #  'var': "trackPIDA",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackLLR",
    #  'xtitle': "TPC Track Pion/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "trackLLHPion-trackLLHProton",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackLLRInt",
    #  'xtitle': "TPC Track Pion/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHPion-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'logy': logy,
    #  'normalize': True,
    #  'integral': True
    #},
    #{
    #  'name': "primTrkLLHPion",
    #  'xtitle': "Primary TPC Track Pion -logLH",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,5000],
    #  'var': "-primTrkLLHPion",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLHProton",
    #  'xtitle': "Primary TPC Track Proton -logLH",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,5000],
    #  'var': "-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLHMuon",
    #  'xtitle': "Primary TPC Track Muon -logLH",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,5000],
    #  'var': "-primTrkLLHMuon",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLHKaon",
    #  'xtitle': "Primary TPC Track Kaon -logLH",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,5000],
    #  'var': "-primTrkLLHKaon",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLR",
    #  'xtitle': "Primary TPC Track Pion/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHPion-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLRInt",
    #  'xtitle': "Primary TPC Track Pion/Proton LLHR",
    #  'ytitle': "Efficiency for Cut >= X",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHPion-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'logy': logy,
    #  'normalize': True,
    #  'integral': True
    #},
    #{
    #  'name': "primTrkLLRKP",
    #  'xtitle': "Primary TPC Track Kaon/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHKaon-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkLLRKPInt",
    #  'xtitle': "Primary TPC Track Kaon/Proton LLHR",
    #  'ytitle': "Efficiency for Cut >= X",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHKaon-primTrkLLHProton",
    #  'cuts': weightStr,
    #  #'logy': logy,
    #  'normalize': True,
    #  'integral': True
    #},
    #{
    #  'name': "primTrkPIDA",
    #  'xtitle': "Primary TPC Track PIDA",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,50],
    #  'var': "primTrkPIDA",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackStartDistToPrimTrkEnd",
    #  'xtitle': "TPC Track Start Distance to Primary End [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [40,0,20],
    #  'var': "trackStartDistToPrimTrkEnd",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trackEndDistToPrimTrkEnd",
    #  'xtitle': "TPC Track End Distance to Primary End [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [40,0,20],
    #  'var': "trackEndDistToPrimTrkEnd",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLength",
    #  'xtitle': "Secondary TPC Track Length [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-10,100],
    #  'var': "trackLength",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkCaloKin",
    #  'xtitle': "Secondary Track Calo Estimate of KE [MeV]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [50,0,2500],
    #  'var': "trackCaloKin",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLHPion",
    #  'xtitle': "Secondary TPC Track Pion -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHPion",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLHProton",
    #  'xtitle': "Secondary TPC Track Proton -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHProton",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLHMuon",
    #  'xtitle': "Secondary TPC Track Muon -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHMuon",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLHKaon",
    #  'xtitle': "Secondary TPC Track Kaon -logLH",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,5000],
    #  'var': "-trackLLHKaon",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLR",
    #  'xtitle': "Secondary TPC Track Pion/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "trackLLHPion-trackLLHProton",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "secTrkLLRInt",
    #  'xtitle': "Secondary TPC Track Pion/Proton LLHR",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,-300,1000],
    #  'var': "primTrkLLHPion-primTrkLLHProton",
    #  'cuts': weightStr+secTrkCuts,
    #  #'logy': logy,
    #  'normalize': True,
    #  'integral': True
    #},
    #{
    #  'name': "secTrkPIDA",
    #  'xtitle': "Secondary TPC Track PIDA",
    #  'ytitle': "Tracks / bin",
    #  'binning': [100,0,50],
    #  'var': "trackPIDA",
    #  'cuts': weightStr+secTrkCuts,
    #  #'normalize': True,
    #  'logy': logy,
    #},
  ]

  #for i in reversed(range(len(histConfigs))):
  #  if histConfigs[i]['name'] != "pzWC":
  #  #if histConfigs[i]['name'] != "zWC4Hit":
  #    histConfigs.pop(i)

#  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)
  fileConfigMCs = copy.deepcopy(fileConfigs)
  fileConfigData = None
  for i in reversed(range(len(fileConfigMCs))):
    if 'isData' in fileConfigMCs[i] and fileConfigMCs[i]['isData']:
      fileConfigData = fileConfigMCs.pop(i)
  DataMCStack(fileConfigData,fileConfigMCs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)

  #for i in range(len(histConfigs)):
  #  histConfigs[i]['cuts'] = weightStr + "*(pzWC > 450 && pzWC < 1100 && nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3) && (isMC || (firstTOF > 28 && firstTOF < 55))"
  #  #histConfigs[i]['cuts'] = weightStr + "*(pzWC > 450 && pzWC < 1100 && nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3) && (isMC || (firstTOF < 25))"
  #  #histConfigs[i]['cuts'] = weightStr + "*(pzWC > 450 && pzWC < 1100 && nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3 && fabs(trackMatchDeltaY) < 5. && fabs(trackMatchDeltaX) < 5. && trackMatchDeltaAngle*180/pi < 10.)"
  #plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outSuffix="HistCuts")

  #for i in range(len(histConfigs)):
  #  histConfigs[i]['cuts'] = " allWeight *( pzWC > 450 && pzWC < 1100 && nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3 && (isMC || (firstTOF > 28 && firstTOF < 55)))"
  #  #histConfigs[i]['cuts'] = " allWeight *( pzWC > 450 && pzWC < 1100 && nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3 && (isMC || (firstTOF < 25)))"
  #plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outSuffix="HistAllWeightsCuts")

  histConfigs = [
    #{
    #  'name': "thetayzWCVthetaxzWC",
    #  'xtitle': "WC track #theta_{xz} [deg]",
    #  'ytitle': "WC track #theta_{yz} [deg]",
    #  'binning': [40,-10,10,40,-10,10],
    #  'var': "(asin(sin(thetaWC)*sin(phiWC)))*180/pi:(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
    #  'cuts': "",
    #  #'normalize': True,
    #  #'logy': logy,
    #},
    #{
    #  'name': "xWCVthetaxzWC",
    #  'xtitle': "WC track #theta_{xz} [deg]",
    #  'ytitle': "X of WC track projected to front of TPC [cm]",
    #  'binning': [40,-10,10,40,0,75],
    #  'var': "xWC:(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
    #  'cuts': "",
    #  #'normalize': True,
    #  #'logy': logy,
    #},
    #{
    #  'name': "xWCVxWC4Hit",
    #  'xtitle': "X of WC4 Hit [cm]",
    #  'ytitle': "X of WC track projected to front of TPC [cm]",
    #  'binning': [50,0,50,40,0,75],
    #  'var': "xWC:xWC4Hit",
    #  'cuts': "",
    #  #'normalize': True,
    #  #'logy': logy,
    #},
    {
      'name': "primTrkLLRVPIDA",
      'xtitle': "Primary TPC Track PIDA",
      'ytitle': "Primary TPC Track Pion/Proton LLHR",
      'binning': [100,0,50,100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton:primTrkPIDA",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': logz,
    },
    {
      'name': "primTrkLLRVpWC",
      'xtitle': "WC Momentum [MeV/c]",
      'ytitle': "Primary TPC Track Pion/Proton LLHR",
      'binning': [100,0,1500,100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton:pWC",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': logz,
    },
    {
      'name': "primTrkLLRKPVpWC",
      'xtitle': "WC Momentum [MeV/c]",
      'ytitle': "Primary TPC Track Kaon/Proton LLHR",
      'binning': [100,0,1500,100,-300,1000],
      'var': "primTrkLLHKaon-primTrkLLHProton:pWC",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': logz,
    },
    {
      'name': "primTrkPIDAPVpWC",
      'xtitle': "WC Momentum [MeV/c]",
      'ytitle': "Primary TPC Track PIDA",
      'binning': [100,0,1500,100,0,50],
      'var': "primTrkPIDA:pWC",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': logz,
    },
  ]

  #plotOneHistOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)
