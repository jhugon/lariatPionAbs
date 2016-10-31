#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  NMAX=1000
  fileConfigs = [
    {
      'fn': "anaTree_p_v2.root",
      'addFriend': ["friend","friendTree_p_v2.root"],
      'pdg': 2212,
      'name': "p",
      'title': "p MC Sample",
      'caption': "p MC Sample",
      'color': root.kRed,
    },
    {
      'fn': "anaTree_pip_v2.root",
      'addFriend': ["friend","friendTree_pip_v2.root"],
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+} MC Sample",
      'caption': "#pi^{+} MC Sample",
      'color': root.kBlue,
    },
    {
      'fn': "anaTree_mup_v2.root",
      'addFriend': ["friend","friendTree_mup_v2.root"],
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+} MC Sample",
      'caption': "#mu^{+} MC Sample",
      'color': root.kMagenta,
    },
    {
      'fn': "anaTree_kp_v2.root",
      'addFriend': ["friend","friendTree_kp_v2.root"],
      'pdg': 321,
      'name': "kp",
      'title': "K^{+} MC Sample",
      'caption': "K^{+} MC Sample",
      'color': root.kOrange-3,
    },
    {
      'fn': "anaTree_ep_v2.root",
      'addFriend': ["friend","friendTree_ep_v2.root"],
      'pdg': -11,
      'name': "ep",
      'title': "e^{+} MC Sample",
      'caption': "e^{+} MC Sample",
      'color': root.kGreen+1,
    },
    {
      'fn': "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
      'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
      'name': "RunI",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
    },
  ]

  histConfigs = [
    {
      'name': "pPrimary",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary",
    },
    {
      'name': "nTracksFirst2cm",
      'xtitle': "Number of tracks in first 2 cm of TPC",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nTracksFirst2cm",
      'cuts': "process_primary",
    },
    {
      'name': "nTracksFirst14cm",
      'xtitle': "Number of tracks in first 14 cm of TPC",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nTracksFirst14cm",
      'cuts': "process_primary",
    },
    {
      'name': "nTracksLengthLt5cm",
      'xtitle': "Number of tracks with length < 5 cm",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nTracksLengthLt5cm",
      'cuts': "process_primary",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX)

  histConfigs = [
    {
      'name': "All",
      'title': "All",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary",
      'color': root.kBlack,
    },
    {
      'name': "n2cm",
      'title': "#geq 1 trk in first 2 cm",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary && nTracksFirst2cm >= 1",
      'color': root.kBlue,
    },
    {
      'name': "n2cm",
      'title': "#leq 3 trk in first 14 cm",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary && nTracksFirst14cm <= 3",
      'color': root.kGreen +1,
    },
    {
      'name': "n2cm",
      'title': "#leq 2 short trks",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary && nTracksLengthLt5cm <= 2",
      'color': root.kRed,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="pPrimary_")

  #plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="")
