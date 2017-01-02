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
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_data_Lovely1_Pos_RunI_elanag_v02_v02/anahist.root",
      #'fn': "PiAbs_data.root",
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_pip_v2/anahist.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue,
      #'scaleFactor': 1e-2,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_p_v2/anahist.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed,
      #'scaleFactor': 1e-2,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_ep_v2/anahist.root",
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen+1,
      #'scaleFactor': 1e-2,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_mup_v2/anahist.root",
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kCyan,
      #'scaleFactor': 1e-2,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_kp_v2/anahist.root",
      'name': "kp",
      'title': "K^{+} MC",
      'caption': "K^{+} MC",
      'color': root.kMagenta,
      #'scaleFactor': 1e-2,
    },
  ]

  histConfigs = [
    {
      'name': "xWC4Hit",
      'xtitle': "X Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-100,100],
      'var': "xWC4Hit",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "yWC4Hit",
      'xtitle': "Y Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-100,100],
      'var': "yWC4Hit",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "zWC4Hit",
      'xtitle': "Z Position at WC4 [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-200,0],
      'var': "zWC4Hit",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "xWC",
      'xtitle': "X Position of WC track projection to TPC [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-100,100],
      'var': "xWC",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "yWC",
      'xtitle': "Y Position of WC track projection to TPC [cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-100,100],
      'var': "yWC",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "pzWC",
      'xtitle': "Z Momentum from WC [MeV/c]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0,2000],
      'var': "pzWC",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "phiWC",
      'xtitle': "WC track #phi [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [360,-180,180],
      'var': "phiWC*180/pi",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "thetaWC",
      'xtitle': "WC track #theta [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [40,0,10],
      'var': "thetaWC*180/pi",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "thetaxzWC",
      'xtitle': "WC track #theta_{xz} [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-10,10],
      'var': "(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "thetayzWC",
      'xtitle': "WC track #theta_{yz} [deg]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,-5,5],
      'var': "(asin(sin(thetaWC)*sin(phiWC)))*180/pi",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
    {
      'name': "sinthetayz",
      'xtitle': "WC Track sin(#theta_{yz})",
      'ytitle': "Tracks / bin",
      'binning': [80,-0.1,0.1],
      'var': "sin(thetaWC)*sin(phiWC)",
      'cuts': "",
      #'normalize': True,
      'logy': True,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)

  histConfigs = [
    {
      'name': "thetayzWCVthetaxzWC",
      'xtitle': "WC track #theta_{xz} [deg]",
      'ytitle': "WC track #theta_{yz} [deg]",
      'binning': [40,-10,10,40,-10,10],
      'var': "(asin(sin(thetaWC)*sin(phiWC)))*180/pi:(atan(tan(thetaWC)*cos(phiWC)))*180/pi",
      'cuts': "",
      #'normalize': True,
      #'logy': True,
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX)
