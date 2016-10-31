#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=1000
  fileConfigs = [
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
      'name': "nwctrks",
      'xtitle': "Number of Wire Chamber Tracks",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nwctrks",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "ntof",
      'xtitle': "Number of Time of Flight Objects",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "ntof",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "nAG",
      'xtitle': "Number of Aerogel Counter Objects",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nAG",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "ntracks_reco",
      'xtitle': "Number Reconstructed TPC Tracks",
      'ytitle': "Events / bin",
      'binning': [31,-0.5,30.5],
      'var': "ntracks_reco",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "nclus",
      'xtitle': "Number Reconstructed TPC Clusters",
      'ytitle': "Events / bin",
      'binning': [51,-0.5,51.5],
      'var': "nclus",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "nhits",
      'xtitle': "Number Reconstructed TPC Hits",
      'ytitle': "Events / bin",
      'binning': [100,0,10000],
      'var': "nhits",
      'cuts': "",
      'logy': True,
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX)

