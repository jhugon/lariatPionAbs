#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks
  cuts += "*( iBestMatch >= 0 && nMatchedTracks == 1)" # matching in analyzer

  ###
  secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2. || trackEndDistToPrimTrkEnd < 2.)"
  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  pionFileConfig = {
      #'fn': "piAbs_pip_v5.2.root",
      #'addFriend': ["friend", "friendTree_pip_v5.root"],
      'fn': "test_pip_piAbsSelector.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.51, # pion, tpc, match cuts
    }
  protonFileConfig = {
      #'fn': "piAbs_p_v5.2.root",
      #'addFriend': ["friend", "friendTree_p_v5.root"],
      'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.162/(1.-0.086)*0.7216, #proton, tpc, matching
    }

  histConfigs = [
    {
      'name': "primTrkKins",
      'xtitle': "Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKins",
      'cuts': weightStr,
      'logy': logy,
    },
    {
      'name': "primTrkKinsTrue",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKinsTrue",
      'cuts': weightStr,
      'logy': logy,
    },
    {
      'name': "primTrkKinsTrueCuts",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKinsTrue",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      'logy': logy,
    },
    {
      'name': "primTrkKinsVprimTrkKinsTrue",
      'ytitle': "Reco Hit Kinetic Energy [MeV]",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'binning': [50,0,1000,50,0,1000],
      'var': "primTrkKins:primTrkKinsTrue",
      'cuts': weightStr,
      'logz': True,
    },
    {
      'name': "primTrkKinsVprimTrkKinsTrueCuts",
      'ytitle': "Reco Hit Kinetic Energy [MeV]",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'binning': [50,0,1000,50,0,1000],
      'var': "primTrkKins:primTrkKinsTrue",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      'logz': True,
    },
    {
      'name': "primTrkKinErrVprimTrkDistToTrueTrajPoint",
      'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
      'xtitle': "Hit distance to true trajectory point [cm]",
      'binning': [40,0,10,50,-100,100],
      'var': "primTrkKins-primTrkKinsTrue:primTrkDistToTrueTrajPoint",
      'cuts': weightStr,
      'logz': True,
    },
    {
      'name': "primTrkKinErrVpWC",
      'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
      'xtitle': "True Initial Momentum [MeV/c]",
      'binning': [100,0,1500,100,20,60],
      #'binning': [50,0,1500,50,-1e3,1e3],
      'var': "primTrkKins-primTrkKinsTrue:pWC",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      #'logz': True,
      'profileXtoo': True,
    },
    {
      'name': "primTrkKinErrFirstHitVpWC",
      'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
      'xtitle': "True Initial Momentum [MeV/c]",
      'binning': [100,0,1500,100,20,60],
      #'binning': [50,0,1500,50,-1e3,1e3],
      'var': "primTrkKins[0]-primTrkKinsTrue[0]:pWC",
      'cuts': weightStr+"*(primTrkDistToTrueTraj[0] < 0.8 && primTrkKinsTrue[0] > 0.)",
      #'logz': True,
      'profileXtoo': True,
      'captionleft1': "First track hit",
    },
  ]

  plotOneHistOnePlot([pionFileConfig],histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix="TrueTraj_")

  histConfigs = [
    {
      'name': "primTrkKinsProton",
      'xtitle': "Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKinsProton",
      'cuts': weightStr,
      'logy': logy,
    },
    {
      'name': "primTrkKinsTrue",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKinsTrue",
      'cuts': weightStr,
      'logy': logy,
    },
    {
      'name': "primTrkKinsTrueCuts",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'ytitle': "Hits / bin",
      'binning': [50,0,1000],
      'var': "primTrkKinsTrue",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      'logy': logy,
    },
    {
      'name': "primTrkKinsProtonVprimTrkKinsTrueCuts",
      'ytitle': "Reco Hit Kinetic Energy [MeV]",
      'xtitle': "True Hit Kinetic Energy [MeV]",
      'binning': [100,0,500,100,0,500],
      'var': "primTrkKinsProton:primTrkKinsTrue",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      #'logz': True,
    },
    {
      'name': "primTrkKinProtonErrVpWC",
      'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
      'xtitle': "True Initial Momentum [MeV/c]",
      'binning': [100,0,1500,100,30,180],
      #'binning': [50,0,1500,50,0,250],
      'var': "primTrkKinsProton-primTrkKinsTrue:pWC",
      'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0.)",
      #'logz': True,
      'profileXtoo': True,
    },
    #{
    #  'name': "primTrkKinProtonErrVpWCTrueKinL100",
    #  'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
    #  'xtitle': "True Initial Momentum [MeV/c]",
    #  'binning': [50,0,1500,50,30,200],
    #  #'binning': [50,0,1500,50,0,250],
    #  'var': "primTrkKinsProton-primTrkKinsTrue:pWC",
    #  'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0. && primTrkKinsTrue < 100.)",
    #  #'logz': True,
    #  'profileXtoo': True,
    #},
    #{
    #  'name': "primTrkKinProtonErrVpWCTrueKinG100",
    #  'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
    #  'xtitle': "True Initial Momentum [MeV/c]",
    #  'binning': [50,0,1500,50,30,200],
    #  #'binning': [50,0,1500,50,0,250],
    #  'var': "primTrkKinsProton-primTrkKinsTrue:pWC",
    #  'cuts': weightStr+"*(primTrkDistToTrueTraj < 0.8 && primTrkKinsTrue > 0. && primTrkKinsTrue > 100.)",
    #  #'logz': True,
    #  'profileXtoo': True,
    #},
    {
      'name': "primTrkKinProtonErrFirstHitVpWC",
      'ytitle': "Reco - Truth Hit Kinetic Energy [MeV]",
      'xtitle': "True Initial Momentum [MeV/c]",
      'binning': [100,0,1500,100,30,180],
      #'binning': [50,0,1500,50,-1e3,1e3],
      'var': "primTrkKinsProton[0]-primTrkKinsTrue[0]:pWC",
      'cuts': weightStr+"*(primTrkDistToTrueTraj[0] < 0.8 && primTrkKinsTrue[0] > 0.)",
      #'logz': True,
      'profileXtoo': True,
      'captionleft1': "First track hit",
    },
  ]

  plotOneHistOnePlot([protonFileConfig],histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix="TrueTraj_")

  #tree = root.TChain("PiAbsSelector/tree")
  #tree.AddFile("test_pip_piAbsSelector.root")
  #tree.Scan("primTrkKins:primTrkKinsTrue:primTrkDistToTrueTraj:primTrkDistToTrueTrajPoint:primTrkdEdxs:primTrkResRanges:primTrkZs")
