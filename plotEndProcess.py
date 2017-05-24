#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*(pWC < 500.)"
  cuts += "*(primTrkEndInFid)"
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
  fileConfigs = [
    {
      #'fn': "piAbs_pip_v5.2.root",
      #'addFriend': ["friend", "friendTree_pip_v5.root"],
      'fn': "test_pip_piAbsSelector.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      #'fn': "piAbs_p_v5.2.root",
      #'addFriend': ["friend", "friendTree_p_v5.root"],
      'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.162/(1.-0.086)*0.7216, #proton, tpc, matching
    },
    {
      #'fn': "piAbs_ep_v5.2.root",
      #'addFriend': ["friend", "friendTree_ep_v5.root"],
      'fn': "test_ep_piAbsSelector.root",
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      'scaleFactor': 1./35700*nData*0.301/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35700*nData*0.301/(1.-0.086)*0.35, # pion, tpc, match cuts
    },
    {
      #'fn': "piAbs_mup_v5.2.root",
      #'addFriend': ["friend", "friendTree_mup_v5.root"],
      'fn': "test_mup_piAbsSelector.root",
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      'scaleFactor': 1./35200*nData*0.021/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.021/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      #'fn': "piAbs_kp_v5.2.root",
      #'addFriend': ["friend", "friendTree_kp_v5.root"],
      'fn': "test_kp_piAbsSelector.root",
      'name': "kp",
      'title': "K^{+} MC",
      'caption': "K^{+} MC",
      'color': root.kOrange-3,
      'scaleFactor': 1./35700*nData*0.00057/(1.-0.086), #No Cuts
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

  histConfigs = [
    {
      'name': "pWC",
      'xtitle': "Momentum from WC [MeV/c]",
      'ytitle': "Events / bin",
      'binning': [100,0,2000],
      'var': "pWC",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      #'printIntegral': True,
    },
#    {
#      'name': "trackPIDA",
#      'xtitle': "TPC Track PIDA",
#      'ytitle': "Tracks / bin",
#      'binning': [100,0,50],
#      'var': "trackPIDA",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkKins",
#      'xtitle': "Hit Kinetic Energy [MeV]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,1000],
#      'var': "primTrkKins",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#      #'printIntegral': True,
#    },
    #{
    #  'name': "primTrkdEdxLast3Hits",
    #  'xtitle': "Hit dE/dx [MeV/cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,50],
    #  'var': "(primTrkIBackwards < 3)*primTrkdEdxs-(primTrkIBackwards >= 3)",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #  #'printIntegral': True,
    #},
    #{
    #  'name': "primTrkdEdxLast1cm",
    #  'xtitle': "Hit dE/dx [MeV/cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,50],
    #  'var': "(primTrkResRanges < 1.)*primTrkdEdxs-(primTrkResRanges >= 1.)",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #  #'printIntegral': True,
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
      'binning': [40,0,20],
      'var': "trackStartDistToPrimTrkEnd",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "trackEndDistToPrimTrkEnd",
      'xtitle': "TPC Track End Distance to Primary End [cm]",
      'ytitle': "Tracks / bin",
      'binning': [40,0,20],
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
    {
      'name': "secTrkCaloKin",
      'xtitle': "Secondary Track Calo Estimate of KE [MeV]",
      'ytitle': "Tracks / bin",
      'binning': [50,0,2500],
      'var': "trackCaloKin",
      'cuts': weightStr+secTrkCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianLast3Hits",
      'xtitle': "Median dE/dx of last 3 hits [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianLast3Hits",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianLast5Hits",
      'xtitle': "Median dE/dx of last 5 hits [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianLast5Hits",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianLast7Hits",
      'xtitle': "Median dE/dx of last 7 hits [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianLast7Hits",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL1",
      'xtitle': "Median dE/dx of hits RR < 1 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL1",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL3",
      'xtitle': "Median dE/dx of hits RR < 3 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL3",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL5",
      'xtitle': "Median dE/dx of hits RR < 5 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL5",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL7",
      'xtitle': "Median dE/dx of hits RR < 7 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL3",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL3G1",
      'xtitle': "Median dE/dx of hits 1 cm < RR < 3 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL3G1",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL5G1",
      'xtitle': "Median dE/dx of hits 1 cm < RR < 5 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL5G1",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxMedianRRL7G1",
      'xtitle': "Median dE/dx of hits RR < 7 cm [MeV/cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxMedianRRL7G1",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
  ]

  cutList = [
    "",
    "*(trueEndProcess == 6)",
    "*(trueEndProcess == 14)",
    "*(trueEndProcess == 15)",
    "*(trueEndProcess == 10 || trueEndProcess == 11 || trueEndProcess == 13 || trueEndProcess == 1)",
  ]
  titles = [
    "All",
    "Decay",
    "Stop",
    "Leave World",
    "Inelastic",
  ]
  colors = [root.kBlue-7, root.kRed-4, root.kGreen, root.kMagenta-4, root.kOrange-3,root.kGray+1]

  for histConfig in histConfigs:
    name = histConfig["name"]
    hcs = []
    for cut,title,color in zip(cutList,titles,colors[:len(cutList)]): 
      hc = copy.deepcopy(histConfig)
      hc["cuts"] = histConfig["cuts"]+cut
      hc["title"] = title
      hc["color"] = color
      hcs.append(hc)
    plotManyHistsOnePlot(fileConfigs,hcs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix=name+"_")
