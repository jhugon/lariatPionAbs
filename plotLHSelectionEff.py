#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  NMAX=1000
  tpcBaseCuts = "nTracksLengthLt5cm <= 2 && nTracksFirst14cm <= 3 && nTracksFirst2cm >= 1"
  fileConfigs = [
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
      'fn': "anaTree_p_v2.root",
      'addFriend': ["friend","friendTree_p_v2.root"],
      'pdg': 2212,
      'name': "p",
      'title': "p MC Sample",
      'caption': "p MC Sample",
      'color': root.kRed,
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
#    {
#      'fn': "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
#      'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
#      'name': "RunI",
#      'title': "Run I Pos. Polarity",
#      'caption': "Run I Pos. Polarity",
#      'color': root.kBlack,
#    },
  ]

  histConfigs = [
    {
      'name': "trkpidlhr_pi_p",
      'xtitle': "#pi^{+}/p Likelihood Ratio of Primary Particle",
      'ytitle': "Events / bin",
      'binning': [100,-500,500],
      'var': "trkpidlhr_pi_p[primarytrkkey][1]",
      'cuts': tpcBaseCuts+"",
    },
    {
      'name': "trkpidlh_pi",
      'xtitle': "log(L_{#pi^{+}}) of Primary Particle",
      'ytitle': "Events / bin",
      'binning': [150,-1500,0],
      'var': "trkpidlh_pi[primarytrkkey][1]",
      'cuts': tpcBaseCuts+"",
    },
    {
      'name': "trkpidlhr_p",
      'xtitle': "log(L_{p}) of Primary Particle",
      'ytitle': "Events / bin",
      'binning': [150,-1500,0],
      'var': "trkpidlh_p[primarytrkkey][1]",
      'cuts': tpcBaseCuts+"",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="LH_")

  histConfigs = [
    {
      'name': "dEdxVrr_primary",
      'xtitle': "Residual Range for Primary Particle [cm]",
      'ytitle': "dE/dx for Primary Particle [MeV/cm]",
      'binning': [130,0,26,100,0,100],
      'var': "trkdedx[primarytrkkey][1][]:trkrr[primarytrkkey][1][]",
      'cuts': "",
    },
    {
      'name': "lhPiVP_primary",
      'xtitle': "Residual Range for Primary Particle [cm]",
      'ytitle': "dE/dx for Primary Particle [MeV/cm]",
      'binning': [130,0,26,100,0,100],
      'var': "trkpidlh_pi[primarytrkkey][1]:P[0]",
      'cuts': "",
    },
    {
      'name': "lhPiVP_primary",
      'xtitle': "Primary Particle Initial Momentum [MeV/c]",
      'ytitle': "log(L_{#pi^{+}}) of Primary Particle",
      'binning': [75,0,1500,75,-1500,0],
      'var': "trkpidlh_pi[primarytrkkey][1]:P[0]*1000.",
      'cuts': "",
    },
    {
      'name': "lhPVP_primary",
      'xtitle': "Primary Particle Initial Momentum [MeV/c]",
      'ytitle': "log(L_{p}) of Primary Particle",
      'binning': [75,0,1500,75,-1500,0],
      'var': "trkpidlh_p[primarytrkkey][1]:P[0]*1000.",
      'cuts': "",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="LH_")
