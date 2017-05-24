#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # pions
# # #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # protons
  #cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks

  #cuts += "*( iBestMatch >= 0 && nMatchedTracks == 1)" # matching in analyzer

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
  #weightStr = "pzWeight"+cuts
  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/CosmicAnalyzer.root",
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
      'isData': True,
    },
  ]

  histConfigs = [
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
      'name': "nWCTracks",
      'xtitle': "Number of WC Tracks",
      'ytitle': "Events / bin",
      'binning': [11,0,10],
      'var': "nWCTracks",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "nTOFs",
      'xtitle': "Number of TOF Objects",
      'ytitle': "Events / bin",
      'binning': [11,0,10],
      'var': "nTOFs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
  ]

  cutList = [
    "",
    #"*(triggerCOSMICON)",
    #"*(triggerCOSMIC)",
    #"*(triggerBEAMON)",
    #"*(triggerUSTOF || triggerDSTOF)",
    #"*(triggerUSTOF && triggerDSTOF)",
    #"*(triggerWCCOINC3OF4)",
    #"*(triggerMICHEL)",
    "*((triggerBits >> 10) & 1)",
    "*((triggerBits >> 11) & 1)",
    "*((triggerBits >> 4) & 1)",
    "*(((triggerBits >> 5) & 1) || ((triggerBits >> 6) & 1))",
    "*(((triggerBits >> 5) & 1) && ((triggerBits >> 6) & 1))",
    "*((triggerBits >> 0) & 1)*((triggerBits >> 1) & 1)*((triggerBits >> 2) & 1)*((triggerBits >> 3) & 1)",
    "*((triggerBits >> 13) & 1)",
    "*((triggerBits >> 14) & 1)",
  ]
  titles = [
    "All",
    "COSMICON",
    "COSMIC",
    "BEAMON",
    "USTOF || DSTOF",
    "USTOF && DSTOF",
    "All WC",
    "MICHEL",
    "LARSCINT",
  ]
  colors = [root.kBlack,root.kBlue-7, root.kRed-4, root.kGreen, root.kMagenta-4, root.kOrange-3,root.kGray+1,root.kYellow]

  for histConfig in histConfigs:
    name = histConfig["name"]
    hcs = []
    for cut,title,color in zip(cutList,titles,colors[:len(cutList)]): 
      hc = copy.deepcopy(histConfig)
      hc["cuts"] = histConfig["cuts"]+cut
      hc["title"] = title
      hc["color"] = color
      hcs.append(hc)
    plotManyHistsOnePlot(fileConfigs,hcs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Triggers_"+name+"_")
