#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import copy

if __name__ == "__main__":

  cuts = ""
  #cuts += "*(isMC || ((triggerBits >> 4) & 1))" # BEAMON trigger
  cuts += "*(isMC || ((triggerBits >> 10) & 1))" # COSMICON trigger
  #cuts += "*(isMC || !((triggerBits >> 10) & 1))" # Not COSMICON trigger
  #cuts += "*(isMC || ((triggerBits >> 11) & 1))" # COSMIC trigger
  cuts += "*(isMC || (nWCTracks ==0 && nTOFs ==0))"
  #cuts += "*( iBestMatch >= 0)" # primary Track found

  #wirelist = [59]
  wirelist = [59,124,179]
  #wirelist = [59,100,124,150,179]

  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100
  fileConfigs = [
    {
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/CosmicAna_Pos_RunII.root",
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna2/lariat_data_Lovely1_RunII_run8300to8500_jhugon_v01_v01/anahist.root",
      'name': "RunII8300to8500",
      'title': "Run II 8300-8500",
      'caption': "Run II 8300-8500",
      'color': root.kBlack,
      'isData': True,
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna2/lariat_PiAbsAndChEx_cosmics_v3/anahist.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'color': root.kRed-4,
      'isData': False,
      'scaleFactor': 10888./19032.
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna2/lariat_PiAbsAndChEx_cosmics_smear10perc_v1/anahist.root",
      'name': "CosmicMC_smear10perc",
      'title': "Cosmic MC Smear 10% ",
      'caption': "Cosmic MC Smear 10%",
      'color': root.kCyan,
      'isData': False,
      'scaleFactor': 10888./6434.
    },
    {
      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna2/lariat_PiAbsAndChEx_cosmics_smear50perc_v1/anahist.root",
      'name': "CosmicMC_smear50perc",
      'title': "Cosmic MC Smear 50% ",
      'caption': "Cosmic MC Smear 50%",
      'color': root.kMagenta,
      'isData': False,
      'scaleFactor': 10888./6316.
    },
#    {
#      'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/cosmicAna/lariat_PiAbsAndChEx_halo_v1/anahist.root",
#      'name': "HaloMC",
#      'title': "Halo MC",
#      'caption': "Halo MC",
#      'color': root.kBlue+7,
#      'isData': False,
#    },
  ]

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,30],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxs_Q1000to1500_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 1500.)",
      #'normalize': True,
      'logy': not logy,
      'caption': "1000 ADC < Q < 1500 ADC",
    },
    {
      'name': "primTrkdEdxs_Q1500to2000_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1500. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 2000.)",
      #'normalize': True,
      'logy': not logy,
      'caption': "1500 ADC < Q < 2000 ADC",
    },
    {
      'name': "primTrkdEdxs_Q2000to3000_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 2000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 3000.)",
      #'normalize': True,
      'logy': not logy,
      'caption': "2000 ADC < Q < 3000 ADC",
    },
    {
      'name': "primTrkdEdxs_Q3000to4000_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [60,0,6],
      'var': "primTrkdEdxs",
      'cuts': weightStr+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 3000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 4000.)",
      #'normalize': True,
      'logy': not logy,
      'caption': "3000 ADC < Q < 4000 ADC",
    },
    {
      'name': "primTrkTruedEdxs",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,50],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedEdxs_zoom",
      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10],
      'var': "primTrkTruedEdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdQdxs",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,3e4],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdQdxs_zoom",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,8e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkdQdxs_zoom2",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,8e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': not logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkdQs",
      'xtitle': "Primary TPC Track dQ [ADC]",
      'ytitle': "Events / bin",
      'binning': [100,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': not logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkTruedQdxs",
      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,5e6],
      'var': "primTrkTruedQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedQdxs_zoom",
      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,1e5],
      'var': "primTrkTruedQdxs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkTruedQs",
      'xtitle': "Primary TPC Track Q/Wire [e^{-}]",
      'ytitle': "Events / bin",
      #'binning': [200,0,1e5],
      'binning': getLogBins(100,1e3,1e7),
      'var': "primTrkTruedQs",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'logx': True,
    },
    {
      'name': "primTrkResRanges",
      'xtitle': "Primary TPC Track Residual Range [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "primTrkResRanges",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitches",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10],
      'var': "primTrkPitches",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
  ]

  for wire in wirelist:
      thisHistConfigs = copy.deepcopy(histConfigs)
      for i in range(len(thisHistConfigs)):
        thisHistConfigs[i]['cuts'] = thisHistConfigs[i]['cuts'] + "*(primTrkTrueWires == {})".format(wire)
        oldCaption = None
        try:
            oldCaption = thisHistConfigs[i]['caption']
        except KeyError:
            oldCaption = ""
        else:
            oldCaption = " " + oldCaption
        thisHistConfigs[i]['caption'] = "Wire {}".format(wire) + oldCaption
      plotManyFilesOnePlot(fileConfigs,thisHistConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Wires{}_".format(wire))

  histConfigs = [
    {
      'name': "primTrkdEdxsVQ",
      'xtitle': "Primary TPC Track Hit Q [ADC]",
      'ytitle': "Primary TPC Track Hit dE/dx [MeV/cm]",
      'binning': [50,0,10000,50,0,10],
      'var': "primTrkdEdxs:primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
  ]

  for wire in wirelist:
      for i in range(len(histConfigs)):
        histConfigs[i]['cuts'] = weightStr + "*(primTrkTrueWires == {})".format(wire)
        histConfigs[i]['caption'] = "Wire {}".format(wire)
      hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Wires{}_".format(wire))
