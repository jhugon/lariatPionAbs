#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import sys

if __name__ == "__main__":

  cuts = ""
  #cuts += "*(isMC || ((triggerBits >> 4) & 1))" # BEAMON trigger
  cuts += "*(isMC || ((triggerBits >> 10) & 1))" # COSMICON trigger
  #cuts += "*(isMC || !((triggerBits >> 10) & 1))" # Not COSMICON trigger
  #cuts += "*(isMC || ((triggerBits >> 11) & 1))" # COSMIC trigger
  #cuts += "*(isMC || (nWCTracks ==0 && nTOFs ==0))"
  cuts += "*( iBestMatch >= 0)" # primary Track found
  #cuts += "*(acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi < 5. || acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi > 175.)" # theta vertical
  #cuts += "*((!isMC) || (trueStartMom>3000. && trueStartMom < 8000.))"

  #cuts += "*enterExitYm*enterExitYp"
  #cuts += "*(primTrkXs > 10. && primTrkXs < 38. &&  primTrkYs > 15. && primTrkZs > 10. && primTrkZs > 80.)"
  #cuts += "*(primTrkYs > 15.)"
  cuts += "*((!isMC) || (trueHitCosmic1 && trueHitCosmic2) || (trueHitCosmic3 && trueHitCosmic4))"
  cuts += "*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)" # only angles that match MC
  #cuts += "*(primTrkLength > 10.)" # didn't seem to make a difference
  cuts += "*(nTracks == 1)"
  #cuts += "*(primTrkLength > 80. && primTrkLength < 85.)"

  hitExtraCuts = "*(primTrkXs > 3. && primTrkXs < 46. && primTrkYs < 18. && primTrkYs > -18. && primTrkZs > 3. && primTrkZs < 87.)"
  hitExtraCutsInduct = "*(primTrkXsInduct > 3. && primTrkXsInduct < 46. && primTrkYsInduct < 18. && primTrkYsInduct > -18. && primTrkZsInduct > 3. && primTrkZsInduct < 87.)"
  #hitExtraCuts += "*((primTrkStartPhi >= 0 && primTrkPitches >= 0.45 && primTrkPitches < 0.47) || (primTrkStartPhi < 0 && primTrkPitches >= 0.68 && primTrkPitches < 0.70))" #small pitch region

  weightStr = "1"+cuts
  logy = True
  scaleFactor = 0.066

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100

  ########################################################
  ## File Definitions ####################################
  ########################################################

  baseDir="/scratch/jhugon/"
  baseDir=""

  fileConfigs = [
    {
      'fn': [baseDir+"cosmicsManyRecos/Cosmics_RIIN100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP100.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIN60.root",
             baseDir+"cosmicsManyRecos/Cosmics_RIIP60.root"],
      'name': "CosmicsRunII",
      'title': "Run II Cosmics",
      'caption': "Run II Cosmics",
      'color': root.kBlack,
      'isData': True,
    },
  ]

  ########################################################
  ## Single Hists -- All Samples #########################
  ########################################################

  histConfigs = [
    {
      'name': "primTrkdEdxs_zoom3",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'realVar': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_logy",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,20],
      'realVar': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'logy': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_zoom3_logy",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'realVar': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'logy': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiGeq0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'realVar': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiLt0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'realVar': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
  ]

  recos = [
    {
      'name': "standard",
      'title': "Standard",
      'tree': "cosmicanalyzer/tree",
      'scaleFactor': 1.,
    },
    {
      'name': "normarea",
      'title': "Norm Area",
      'tree': "cosmicanalyzerNormArea/tree",
      'scaleFactor': 7.1,
    },
    {
      'name': "amplitude",
      'title': "Amplitude",
      'tree': "cosmicanalyzerAmplitude/tree",
      'scaleFactor': 0.97,
    },
    {
      'name': "summedadc",
      'title': "Summed ADC",
      'tree': "cosmicanalyzerSummedADC/tree",
      'scaleFactor': 1.2,
    },
  ]
  for i, reco in enumerate(recos):
    if i > 0:
      reco['color'] = COLORLIST[i-1]
    else:
      reco['color'] = 1
  for reco in recos:
    for histConfig in histConfigs:
        histConfig['var'] = histConfig['realVar']+"*{}".format(reco['scaleFactor'])
    hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,reco['tree'],nMax=NMAX)
    reco["hists"] = {}
    for var in hists:
      reco["hists"][var] = {}
      for ds in hists[var]:
          newname = reco['name']+"_"+var+"_"+ds
          hist = hists[var][ds]
          hist.SetName(newname)
          hist.Print()
          reco["hists"][var][ds] =  hist
  print recos
  for fileConfig in fileConfigs:
    for histConfig in histConfigs:
      hists = []
      labels = []
      logy = False
      if "logy" in histConfig and histConfig["logy"]:
        logy = True
      for reco in recos:
        hist = reco['hists'][histConfig['name']][fileConfig["name"]]
        hist.SetLineColor(reco['color'])
        hists.append(hist)
        labels.append(reco['title'])
      axisHist = makeStdAxisHist(hists,logy=logy)
      setHistTitles(axisHist,histConfig['xtitle'],histConfig['ytitle'])
      c.cd()
      c.SetLogy(logy)
      axisHist.Draw()
      for h in hists:
        h.Draw('same')
      leg = drawNormalLegend(hists,labels,wide=True)
      c.RedrawAxis()
      c.SaveAs("CompareReco_{}_{}.png".format(fileConfig["name"],histConfig['name']))
