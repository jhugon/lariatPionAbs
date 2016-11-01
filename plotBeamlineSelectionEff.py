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
      #'fn': "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
      #'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
      'fn': "anaTree_data_runI_pos_v0.1.root",
      'addFriend': ["friend","friendTree_data_runI_pos_v0.1.root"],
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
    {
      'name': "wctrk_XFaceCoor",
      'xtitle': "x Coordinate of WC Track Extrapolated to TPC [cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,-1000,1000],
      'var': "wctrk_XFaceCoor",
      'cuts': "",
    },
    {
      'name': "wctrk_YFaceCoor",
      'xtitle': "y Coordinate of WC Track Extrapolated to TPC [cm]",
      'ytitle': "Tracks / bin",
      'binning': [100,-100,100],
      'var': "wctrk_YFaceCoor",
      'cuts': "",
    },
    {
      'name': "wctrk_theta",
      'xtitle': "WC Track #theta [deg]",
      'ytitle': "Tracks / bin",
      'binning': [80,-20,20],
      'var': "wctrk_theta*180/pi",
      'cuts': "",
    },
    {
      'name': "wctrk_phi",
      'xtitle': "WC Track #phi [deg]",
      'ytitle': "Tracks / bin",
      'binning': [180,-180,180],
      'var': "wctrk_phi*180/pi",
      'cuts': "",
    },
    {
      'name': "wctrk_momentum",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "Tracks / bin",
      'binning': [200,0,2000],
      'var': "wctrk_momentum",
      'cuts': "",
    },
    {
      'name': "tofObject",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "TOF / bin",
      'binning': [200,-100,100],
      'var': "tofObject",
      'cuts': "",
    },
    {
      'name': "tof_timestamp",
      'xtitle': "Time of Flight Timestamp [ns]",
      'ytitle': "TOF / bin",
      'binning': [2000,-5e5,5e5],
      'var': "tof_timestamp",
      'cuts': "",
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX)

