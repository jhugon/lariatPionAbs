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
  nData = 224281.0
  fileConfigData = [
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorData/Pos_RunII_100A_v02_all.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorData/friendTrees/friend_Pos_RunII_100A_v02_all.root"],
      'name': "RunII_Pos_100",
      'title': "Run II +100A",
      'caption': "Run II +100A",
      'color': root.kBlack,
      'isData': True,
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorData/Pos_RunII_60A_v02_all.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorData/friendTrees/friend_Pos_RunII_60A_v02_all.root"],
      'name': "RunII_Pos_60",
      'title': "Run II +60A",
      'caption': "Run II +60A",
      'color': root.kGray+2,
      'isData': True,
    },
  ]
  fileConfigsMC = [
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_211.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_211.root"],
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      'scaleFactor': 1./25000*nData,
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_2212.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_2212.root"],
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-11.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-11.root"],
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-13.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-13.root"],
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      'scaleFactor': 1./10000*nData,
    },
    {
      'fn': "/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_321.root",
      'addFriend': ["friend", "/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_321.root"],
      'name': "kp",
      'title': "K^{+} MC",
      'caption': "K^{+} MC",
      'color': root.kOrange-3,
      'scaleFactor': 1./10000*nData,
    },
  ]


  NMinusOnePlot(fileConfigData,fileConfigsMC,cutConfigs,c,"PiAbsSelectorTC/tree",outPrefix="NM1_",nMax=NMAX,weight="pzWeight")

