#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks
  cuts += "*( iBestMatch >= 0 && nMatchedTracks == 1)" # matching in analyzer

  cuts += "*(trueEndProcess == 10 || trueEndProcess == 11 || trueEndProcess == 13 || trueEndProcess == 1)"

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
      'fn': "piAbs_pip_v5.2.root",
      #'addFriend': ["friend", "friendTree_pip_v5.root"],
      #'fn': "test_pip_piAbsSelector.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      'fn': "piAbs_p_v5.2.root",
      #'addFriend': ["friend", "friendTree_p_v5.root"],
      #'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.162/(1.-0.086)*0.7216, #proton, tpc, matching
    },
    {
      'fn': "piAbs_ep_v5.2.root",
      #'addFriend': ["friend", "friendTree_ep_v5.root"],
      #'fn': "test_ep_piAbsSelector.root",
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      'scaleFactor': 1./35700*nData*0.301/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35700*nData*0.301/(1.-0.086)*0.35, # pion, tpc, match cuts
    },
    {
      'fn': "piAbs_mup_v5.2.root",
      #'addFriend': ["friend", "friendTree_mup_v5.root"],
      #'fn': "test_mup_piAbsSelector.root",
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      'scaleFactor': 1./35200*nData*0.021/(1.-0.086), #No Cuts
      #'scaleFactor': 1./35200*nData*0.021/(1.-0.086)*0.51, # pion, tpc, match cuts
    },
    {
      'fn': "piAbs_kp_v5.2.root",
      #'addFriend': ["friend", "friendTree_kp_v5.root"],
      #'fn': "test_kp_piAbsSelector.root",
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
      'title': "#pi^{#pm}",
      'xtitle': "Number of daughter particles",
      'ytitle': "Daughters / bin",
      'binning': [10,0,10],
      'var': "trueNSecondaryChPions",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      "color": root.kBlue-7,
    },
    {
      'title': "#pi^{0}",
      'xtitle': "Number of daughter particles",
      'ytitle': "Daughters / bin",
      'binning': [10,0,10],
      'var': "trueNSecondaryPiZeros",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'color': root.kOrange-3,
    },
    {
      'title': "p",
      'xtitle': "Number of daughter particles",
      'ytitle': "Daughters / bin",
      'binning': [10,0,10],
      'var': "trueNSecondaryProtons",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      "color": root.kRed-4,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix="Inelastic_nDaughters_")
