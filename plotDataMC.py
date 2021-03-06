#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # old pions
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) < 5e4))" # pions
  #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # old protons
  #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) > 7e5))" # protons
  #cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks
  cuts += "*(primTrkStartZ < 2.)" # tpc tracks

  cuts += "*( iBestMatch >= 0 && nMatchedTracks == 1)" # matching in analyzer

  cuts += "*(primTrkEndInFid == 1)"
  cuts += "*(primTrkEndX > 5.4 && primTrkEndX < 42.7)"
  cuts += "*(primTrkEndY > -15. && primTrkEndY < 15.)"
  cuts += "*(primTrkEndZ > 5. && primTrkEndZ < 85.)"

  # matching debug
  #cuts += "*(sqrt(pow(xWC-23.75,2)+pow(yWC-0.2,2)) < 11.93)" # wc track in flange
  #cuts += "*(sqrt(pow(trackXFront-23.75,2)+pow(trackYFront-0.2,2)) < 11.93)" # TPC track in flange
  #cuts += "*(trackMatchLowestZ < 2.)" # matching
  #cuts += "*(fabs(trackMatchDeltaY) < 5.)" # matching
  #cuts += "*((!isMC && (trackMatchDeltaX < 6. && trackMatchDeltaX > -4.)) || (isMC && (fabs(trackMatchDeltaX) < 5.)))" # matching
  #cuts += "*(trackMatchDeltaAngle*180/pi < 10.)" # matching
  ###
  ###
  secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2.)"
  weightStr = "pzWeight"+cuts
  #weightStr = "1"+cuts

  #DataMC_pWC_NoCutsHist Run II +100A Integral: 224281.0
  #DataMC_pWC_NoCutsHist Run II +60A Integral: 50672.0

  nData = 224281.0
  logy = False

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      'fn': "piAbs_v2/piAbsSelector_Pos_RunII_current100_v02_all.root",
      'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current100_v02_all.root"],
      'name': "RunII_Pos_100",
      'title': "Run II +100A",
      'caption': "Run II +100A",
      'color': root.kBlack,
      'isData': True,
    },
    {
      'fn': "piAbs_v2/piAbsSelector_Pos_RunII_current60_v02_all.root",
      'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current60_v02_all.root"],
      'name': "RunII_Pos_60",
      'title': "Run II +60A",
      'caption': "Run II +60A",
      'color': root.kGray+2,
      'isData': True,
    },
    {
      'fn': "piAbs_v2/piAbsSelector_Neg_RunII_current100_v02_all.root",
      'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Neg_RunII_current100_v02_all.root"],
      'name': "RunII_Neg_100",
      'title': "Run II -100A",
      'caption': "Run II -100A",
      'color': root.kGreen,
      'isData': True,
    },
    {
      'fn': "piAbs_v2/piAbsSelector_Neg_RunII_current60_v02_all.root",
      'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Neg_RunII_current60_v02_all.root"],
      'name': "RunII_Neg_60",
      'title': "Run II -60A",
      'caption': "Run II -60A",
      'color': root.kYellow+1,
      'isData': True,
    },
    {
      'fn': "billMC1/MC1_PDG_211.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_211.root"],
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      'scaleFactor': 1./25000*nData,
    },
    {
      'fn': "billMC1/MC1_PDG_2212.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_2212.root"],
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "billMC1/MC1_PDG_-11.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_-11.root"],
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "billMC1/MC1_PDG_-13.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_-13.root"],
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "billMC1/MC1_PDG_321.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_321.root"],
      'name': "kp",
      'title': "K^{+} MC",
      'caption': "K^{+} MC",
      'color': root.kOrange-3,
      'scaleFactor': 1./10000*nData,
    },
  ]

  histConfigs = [
#    {
#      'name': "xWC4Hit",
#      'xtitle': "X Position at WC4 [cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,50],
#      'var': "xWC4Hit",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "yWC4Hit",
#      'xtitle': "Y Position at WC4 [cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,-25,25],
#      'var': "yWC4Hit",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "zWC4Hit",
#      'xtitle': "Z Position at WC4 [cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,-97,-95],
#      'var': "zWC4Hit",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "xWC",
#      'xtitle': "X Position of WC track projection to TPC [cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,75],
#      'var': "xWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "yWC",
#      'xtitle': "Y Position of WC track projection to TPC [cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,-50,50],
#      'var': "yWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "pzWC",
#      'xtitle': "Z Momentum from WC [MeV/c]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,2000],
#      'var': "pzWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#      #'printIntegral': True,
#    },
    {
      'name': "pWC",
      'xtitle': "Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [40,300,1100],
      'var': "pWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "pWC_NoCuts",
      'xtitle': "Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [60,300,1500],
      'var': "pWC",
      'cuts': "pzWeight*(isMC || (firstTOF > -100))",
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
#    {
#      'name': "kinWC",
#      'xtitle': "Kinetic Energy at WC [MeV/c] (m=m_{#pi^{#pm}})",
#      'ytitle': "Events / bin",
#      'binning': [100,0,2000],
#      'var': "kinWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "kinWCInTPC",
#      'xtitle': "Kinetic Energy at TPC [MeV/c] (m=m_{#pi^{#pm}})",
#      'ytitle': "Events / bin",
#      'binning': [100,0,2000],
#      'var': "kinWCInTPC",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
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
      'var': "(asin(tan(thetaWC)*sin(phiWC)))*180/pi",
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
    {
      'name': "primTrkStartZ",
      'xtitle': "Primary TPC Track Start Z [cm]",
      'ytitle': "Events / bin",
      'binning': [60,-3,3],
      'var': "primTrkStartZ",
      'cuts': weightStr,
      #'normalize': True,
      'logy': False,
    },
    {
      'name': "primTrkStartZ_Logy",
      'xtitle': "Primary TPC Track Start Z [cm]",
      'ytitle': "Events / bin",
      'binning': [60,-10,10],
      'var': "primTrkStartZ",
      'cuts': weightStr,
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "nTracks",
      'xtitle': "Number of TPC Tracks / Event",
      'ytitle': "Events / bin",
      'binning': [31,0,30],
      'var': "nTracks",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "nTracksInFirstZ2",
      'xtitle': "Number of TPC Tracks in first 2 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksInFirstZ[2]",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "nTracksInFirstZ14",
      'xtitle': "Number of TPC Tracks in first 14 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksInFirstZ[14]",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "nTracksLengthLt5",
      'xtitle': "Number of TPC Tracks with length < 5 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksLengthLt[5]",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
#    {
#      'name': "nMatchedTracks",
#      'xtitle': "Number of TPC/WC Track Matches / Event",
#      'ytitle': "Events / bin",
#      'binning': [11,0,10],
#      'var': "nMatchedTracks",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': True,
#    },
#    {
#      'name': "trackMatchDeltaX",
#      'xtitle': "TPC / WC Track #Delta x at TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [40,-10,10],
#      #'var': "trackMatchDeltaX[iBestMatch]",
#      #'cuts': "(iBestMatch >= 0)*"+weightStr,
#      'var': "trackMatchDeltaX",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackMatchDeltaY",
#      'xtitle': "TPC / WC Track #Delta y at TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [40,-10,10],
#      #'var': "trackMatchDeltaY[iBestMatch]",
#      #'cuts': "(iBestMatch >= 0)*"+weightStr,
#      'var': "trackMatchDeltaY",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackMatchDeltaAngle",
#      'xtitle': "TPC / WC Track #Delta #alpha [deg]",
#      'ytitle': "TPC Tracks / bin",
#      #'binning': [90,0,180],
#      'binning': [20,0,20],
#      #'var': "trackMatchDeltaAngle[iBestMatch]*180/pi",
#      #'cuts': "(iBestMatch >= 0)*"+weightStr,
#      'var': "trackMatchDeltaAngle*180/pi",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
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
#      'name': "TOFs",
#      'xtitle': "TOF [ns]",
#      'ytitle': "TOFs / bin",
#      'binning': [100,0,100],
#      'var': "TOFs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "firstTOF",
#      'xtitle': "TOF [ns]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,100],
#      'var': "firstTOF",
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
    {
      'name': "trackStartZ",
      'xtitle': "TPC Track Start Z [cm]",
      'ytitle': "Tracks / bin",
      'binning': [20,-5,5],
      'var': "trackStartZ",
      'cuts': weightStr,
      #'normalize': True,
      'logy': False,
    },
    {
      'name': "trackStartZ_Logy",
      'xtitle': "TPC Track Start Z [cm]",
      'ytitle': "Tracks / bin",
      'binning': [30,-10,20],
      'var': "trackStartZ",
      'cuts': weightStr,
      #'normalize': True,
      'logy': True,
    },
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
    {
      'name': "trackPIDA",
      'xtitle': "TPC Track PIDA",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "trackPIDA",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackLLR",
      'xtitle': "TPC Track Pion/Proton LLHR",
      'ytitle': "Tracks / bin",
      'binning': [100,-300,1000],
      'var': "trackLLHPion-trackLLHProton",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackLLRInt",
      'xtitle': "TPC Track Pion/Proton LLHR",
      'ytitle': "Tracks / bin",
      'binning': [100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton",
      'cuts': weightStr,
      #'logy': logy,
      'normalize': True,
      'integral': True
    },
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
    {
      'name': "primTrkLLR",
      'xtitle': "Primary TPC Track Pion/Proton LLHR",
      'ytitle': "Tracks / bin",
      'binning': [100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkLLRInt",
      'xtitle': "Primary TPC Track Pion/Proton LLHR",
      'ytitle': "Efficiency for Cut >= X",
      'binning': [100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton",
      'cuts': weightStr,
      #'logy': logy,
      'normalize': True,
      'integral': True
    },
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
    {
      'name': "primTrkPIDA",
      'xtitle': "Primary TPC Track PIDA",
      'ytitle': "Events / bin",
      'binning': [100,0,50],
      'var': "primTrkPIDA",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackStartDistToPrimTrkEnd",
      'xtitle': "TPC Track Start Distance to Primary End [cm]",
      'ytitle': "Tracks / bin",
      #'binning': [40,0,20],
      'binning': [160,0,80],
      'var': "trackStartDistToPrimTrkEnd",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackEndDistToPrimTrkEnd",
      'xtitle': "TPC Track End Distance to Primary End [cm]",
      'ytitle': "Tracks / bin",
      #'binning': [40,0,20],
      'binning': [160,0,80],
      'var': "trackEndDistToPrimTrkEnd",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "secTrkLength",
      'xtitle': "Secondary TPC Track Length [cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,-10,100],
      'var': "trackLength",
      'cuts': weightStr+secTrkCuts,
      #'normalize': True,
      'logy': logy,
    },
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
    {
      'name': "secTrkStartZ",
      'xtitle': "Secondary TPC Track Start z [cm]",
      'ytitle': "Tracks / bin",
      'binning': [120,-10,110],
      'var': "trackStartZ",
      'cuts': weightStr+secTrkCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "secTrkLLR",
      'xtitle': "Secondary TPC Track Pion/Proton LLHR",
      'ytitle': "Tracks / bin",
      'binning': [100,-300,1000],
      'var': "trackLLHPion-trackLLHProton",
      'cuts': weightStr+secTrkCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "secTrkLLRInt",
      'xtitle': "Secondary TPC Track Pion/Proton LLHR",
      'ytitle': "Tracks / bin",
      'binning': [100,-300,1000],
      'var': "primTrkLLHPion-primTrkLLHProton",
      'cuts': weightStr+secTrkCuts,
      #'logy': logy,
      'normalize': True,
      'integral': True
    },
    {
      'name': "secTrkPIDA",
      'xtitle': "Secondary TPC Track PIDA",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "trackPIDA",
      'cuts': weightStr+secTrkCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkLength",
      'xtitle': "Primary TPC Track Length [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "primTrkLength",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    #{
    #  'name': "primTrkdEdxs",
    #  'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [200,0,50],
    #  'var': "primTrkdEdxs",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
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
    #{
    #  'name': "primTrkResRanges",
    #  'xtitle': "Primary TPC Track Residual Range [cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [200,0,100],
    #  'var': "primTrkResRanges",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
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
    {
      'name': "primTrkKins",
      'xtitle': "Primary TPC Track Hit Kinetic Energy [MeV]",
      'ytitle': "Events / bin",
      'binning': [100,0,1000],
      'var': "primTrkKins",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkKinInteract",
      'xtitle': "Primary TPC Track Interaction Kinetic Energy [MeV]",
      'ytitle': "Events / bin",
      'binning': [100,0,1000],
      'var': "primTrkKinInteract",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkZs",
      'xtitle': "Primary TPC Track Hit Z coordinates [cm]",
      'ytitle': "Events / bin",
      'binning': [80,-10,10],
      'var': "primTrkZs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
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

  #for i in reversed(range(len(histConfigs))):
  #  if histConfigs[i]['name'] != "pzWC":
  #  #if histConfigs[i]['name'] != "zWC4Hit":
  #    histConfigs.pop(i)

#  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelectorTC/tree",outPrefix="DataMC_",nMax=NMAX)
  fileConfigMCs = copy.deepcopy(fileConfigs)
  fileConfigDatas = []
  for i in reversed(range(len(fileConfigMCs))):
    if 'isData' in fileConfigMCs[i] and fileConfigMCs[i]['isData']:
      fileConfigDatas.append(fileConfigMCs.pop(i))
  DataMCStack(fileConfigDatas,fileConfigMCs,histConfigs,c,"PiAbsSelectorTC/tree",outPrefix="DataMC_",nMax=NMAX)
  #DataMCCategoryStack(fileConfigDatas,fileConfigMCs,histConfigs,c,"PiAbsSelectorTC/tree",
  #              outPrefix="DataMC_",nMax=NMAX,
  #              catConfigs=TRUECATEGORYFEWERCONFIGS
  #           )

  m2SF = 1e-3
  histConfigs = [
    {
      'name': "beamlineMass_NoCuts",
      'xtitle': "Beamline Mass Squared [1000#times (MeV^{2})]",
      'ytitle': "Events / bin",
      'binning': [100,-2e5*m2SF,2e5*m2SF],
      'var': "pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.)*1e-3",
      'cuts': "(!isMC)",
      #'normalize': True,
      'logy': False,
      'drawvlines':[105.65**2*m2SF,139.6**2*m2SF,493.677**2*m2SF,938.272046**2*m2SF],
    },
    {
      'name': "beamlineMass_NoCuts_Logy",
      'xtitle': "Beamline Mass Squared [1000#times (MeV^{2})]",
      'ytitle': "Events / bin",
      'binning': [100,-5e5*m2SF,2e6*m2SF],
      'var': "pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.)*1e-3",
      'cuts': "(!isMC)",
      #'normalize': True,
      'logy': True,
      'drawvlines':[105.65**2*m2SF,139.6**2*m2SF,493.677**2*m2SF,938.272046**2*m2SF],
    },
  ]
  plotManyFilesOnePlot([f for f in fileConfigs if ('isData' in f and f['isData'])],histConfigs,c,"PiAbsSelectorTC/tree",outPrefix="DataMC_",nMax=NMAX)

  histConfigs = [
    {
      'name': "thetayzWCVthetaxzWC",
      'xtitle': "WC track #theta_{xz} [deg]",
      'ytitle': "WC track #theta_{yz} [deg]",
      'binning': [40,-10,10,40,-10,10],
      'var': "(asin(sin(thetaWC)*sin(phiWC)))*180/pi:(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
      'cuts': "",
      #'normalize': True,
      #'logy': logy,
    },
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
#    {
#      'name': "primTrkLLRVPIDA",
#      'xtitle': "Primary TPC Track PIDA",
#      'ytitle': "Primary TPC Track Pion/Proton LLHR",
#      'binning': [100,0,50,100,-300,1000],
#      'var': "primTrkLLHPion-primTrkLLHProton:primTrkPIDA",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkLLRVpWC",
#      'xtitle': "WC Momentum [MeV/c]",
#      'ytitle': "Primary TPC Track Pion/Proton LLHR",
#      'binning': [100,0,1500,100,-300,1000],
#      'var': "primTrkLLHPion-primTrkLLHProton:pWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkLLRKPVpWC",
#      'xtitle': "WC Momentum [MeV/c]",
#      'ytitle': "Primary TPC Track Kaon/Proton LLHR",
#      'binning': [100,0,1500,100,-300,1000],
#      'var': "primTrkLLHKaon-primTrkLLHProton:pWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkPIDAPVpWC",
#      'xtitle': "WC Momentum [MeV/c]",
#      'ytitle': "Primary TPC Track PIDA",
#      'binning': [100,0,1500,100,0,50],
#      'var': "primTrkPIDA:pWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkLengthPVpWC",
#      'xtitle': "WC Momentum [MeV/c]",
#      'ytitle': "Primary TPC Track Length [cm]",
#      'binning': [100,0,1500,100,0,100],
#      'var': "primTrkLength:pWC",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
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
#      'cuts': weightStr+"*primTrkInFids",
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "firstTOFVnTOFs",
#      'xtitle': "nTOFs",
#      'ytitle': "First TOF [ns]",
#      'binning': [11,0,10,100,0,50],
#      'var': "firstTOF:nTOFs",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "yWCVxWC",
#      'xtitle': "X Position of WC track projection to TPC [cm]",
#      'ytitle': "Y Position of WC track projection to TPC [cm]",
#      'binning': [40,0,40,40,-20,20],
#      'var': "yWC:xWC",
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
      'name': "trackLengthVtrackStartZ",
      'ytitle': "TPC Track Length [cm]",
      'xtitle': "TPC Track Start z [cm]",
      'binning': [25,0,100,30,-10,110],
      'var': "trackLength:trackStartZ",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "trackStartDistToPrimTrkEndVtrackStartZ",
      'xtitle': "TPC Track Start z [cm]",
      'ytitle': "TPC Track Start Distance to Primary End [cm]",
      'binning': [25,0,100,20,0,80],
      'var': "trackStartDistToPrimTrkEnd:trackStartZ",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "trackStartDistToPrimTrkEndVprimTrkEndZ",
      'xtitle': "Primary TPC Track End z [cm]",
      'ytitle': "TPC Track Start Distance to Primary End [cm]",
      'binning': [25,0,100,20,0,80],
      'var': "trackStartDistToPrimTrkEnd:primTrkEndZ",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",outPrefix="DataMC_",nMax=NMAX)

