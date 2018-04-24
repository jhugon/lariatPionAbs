#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cutConfigs = [
    {
      'name': "pWC",
      'xtitle': "Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "pWC",
      'cut': "pWC > 100 && pWC < 1100",
    },
    {
      'name': "firstTOF",
      'xtitle': "TOF [ns]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "firstTOF",
      'cut': "isMC || (firstTOF > 0 && firstTOF < 25)",
    },
    {
      'name': "iBestMatch",
      'xtitle': "iBestMatch",
      'ytitle': "Events / bin",
      'binning': [21,-1,20],
      'var': "iBestMatch",
      'cut': "iBestMatch >= 0",
    },
    {
      'name': "nMatchedTracks",
      'xtitle': "nMatchedTracks",
      'ytitle': "Events / bin",
      'binning': [21,-1,20],
      'var': "nMatchedTracks",
      'cut': "nMatchedTracks == 1",
    },
    {
      'name': "nTracksInFirstZ2",
      'xtitle': "Number of TPC Tracks in first 2 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksInFirstZ[2]",
      'cut': "nTracksInFirstZ[2] >= 1",
    },
    {
      'name': "nTracksInFirstZ14",
      'xtitle': "Number of TPC Tracks in first 14 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksInFirstZ[14]",
      'cut': "nTracksInFirstZ[14] < 4",
    },
    {
      'name': "nTracksLengthLt5",
      'xtitle': "Number of TPC Tracks with length < 5 cm / Event",
      'ytitle': "Events / bin",
      'binning': [16,0,15],
      'var': "nTracksLengthLt[5]",
      'cut': "nTracksLengthLt[5] < 3",
    },
    {
      'name': "primTrkStartZ",
      'xtitle': "Primary Track Start Z Postion [cm]",
      'ytitle': "Events / bin",
      'binning': [40,-5,5],
      'var': "primTrkStartZ",
      'cut': "primTrkStartZ >= -1 && primTrkStartZ < 2.",
    },
    {
      'name': "primTrkEndInFid",
      'xtitle': "Primary Track End in Fiducial Region",
      'ytitle': "Events / bin",
      'binning': [2,0,2],
      'var': "primTrkEndInFid",
      'cut': "primTrkEndInFid == 1",
    },
    {
      'name': "primTrkEndX",
      'xtitle': "Primary Track End X Postion [cm]",
      'ytitle': "Events / bin",
      'binning': [55,-5,50],
      'var': "primTrkEndX",
      'cut': "primTrkEndX > 5.4 && primTrkEndX < 42.7",
    },
    {
      'name': "primTrkEndY",
      'xtitle': "Primary Track End Y Postion [cm]",
      'ytitle': "Events / bin",
      'binning': [50,-25,25],
      'var': "primTrkEndY",
      'cut': "primTrkEndY > -15. && primTrkEndY < 15",
    },
    {
      'name': "primTrkEndZ",
      'xtitle': "Primary Track End Z Postion [cm]",
      'ytitle': "Events / bin",
      'binning': [120,-10,110],
      'var': "primTrkEndZ",
      'cut': "primTrkEndZ > 5 && primTrkEndZ < 85",
    },
  ]

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigData = \
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorData/Pos_RunII_60A_b_v02_triggerFilter.root",
      #'addFriend': ["friend", "friendTree_Pos_RunII_v03.root"],
      #'fn': "test_data_Pos_RunII_piAbsSelector.root",
      'name': "RunII_Pos_60b_Trig",
      'title': "Run II +60A Trigger Cut",
      'caption': "Run II +60A Trigger Cut",
      'color': root.kBlack,
      'isData': True,
    }
  fileConfigsMC = [
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_211.root",
      #'addFriend': ["friend", "friendTree_pip_v5.root"],
      #'fn': "test_pip_piAbsSelector.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_2212.root",
      #'addFriend': ["friend", "friendTree_p_v5.root"],
      #'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      #'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.162/(1.-0.086)*0.7216, #proton, tpc, matching
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-11.root",
      #'addFriend': ["friend", "friendTree_ep_v5.root"],
      #'fn': "test_ep_piAbsSelector.root",
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      #'scaleFactor': 1./35700*nData*0.301/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35700*nData*0.301/(1.-0.086)*0.35, # pion, tpc, match cuts
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-13.root",
      #'addFriend': ["friend", "friendTree_mup_v5.root"],
      #'fn': "test_mup_piAbsSelector.root",
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      #'scaleFactor': 1./35200*nData*0.021/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.021/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_321.root",
      #'addFriend': ["friend", "friendTree_kp_v5.root"],
      #'fn': "test_kp_piAbsSelector.root",
      'name': "kp",
      'title': "K^{+} MC",
      'caption': "K^{+} MC",
      'color': root.kOrange-3,
      #'scaleFactor': 1./35700*nData*0.00057/(1.-0.086), #No Cuts
    },
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


  NMinusOnePlot(fileConfigData,fileConfigsMC,cutConfigs,c,"PiAbsSelectorTC/tree",outPrefix="NM1_",nMax=NMAX)

