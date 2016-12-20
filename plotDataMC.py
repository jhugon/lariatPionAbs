#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      'fn': "PiAbs_data.root",
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
    },
    {
      'fn': "PiAbs_pi.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue,
      'scaleFactor': 1e-2,
    },
  ]

  histConfigs = [
    {
      'name': "xWC4Hit",
      'xtitle': "X Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-1000,1000],
      'var': "xWC4Hit",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "yWC4Hit",
      'xtitle': "Y Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-1000,1000],
      'var': "yWC4Hit",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "zWC4Hit",
      'xtitle': "Z Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-1200,1000],
      'var': "zWC4Hit",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "xWC",
      'xtitle': "X Position of WC track projection to TPC [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-1000,1000],
      'var': "xWC",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "yWC",
      'xtitle': "Y Position of WC track projection to TPC [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-1000,1000],
      'var': "yWC",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "pzWC",
      'xtitle': "Z Momentum from WC [MeV/c]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0,2000],
      'var': "pzWC",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "phiWC",
      'xtitle': "WC track #phi [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [360,-180,180],
      'var': "phiWC*180/pi",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "thetaWC",
      'xtitle': "WC track #theta [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [60,0,30],
      'var': "thetaWC*180/pi",
      'cuts': "",
      'normalize': True,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)

