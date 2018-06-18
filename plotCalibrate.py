#!/usr/bin/env python

import ROOT as root
from helpers import *
import fitCosmicHalo
import bethe
root.gROOT.SetBatch(True)
import sys
import numpy

SLABTHICKNESS = 0.4/math.sin(60.*math.pi/180.)
SLABTHICKNESS = 1.

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # old pions
  piMassCuts = "*( pWC > 100 && pWC < 1100 && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) < 5e4))" # pions
  #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # old protons
  protonMassCuts = "*( pWC > 450 && pWC < 1100 && (isMC || pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.) > 7e5))" # protons
  #cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks
  cuts += "*(primTrkStartZ < 2.)" # tpc tracks

  cuts += "*( iBestMatch >= 0 && nMatchedTracks == 1)" # matching in analyzer

  #cuts += "*(primTrkEndInFid == 1)"
  cuts += "*(primTrkEndX > 5.4 && primTrkEndX < 42.7)"
  cuts += "*(primTrkEndY > -15. && primTrkEndY < 15.)"
  cuts += "*(primTrkEndZ > 5. && primTrkEndZ < 85.)"

  # From dE/dx calibration tech note
  cuts += "*(primTrkLength > 10.)"
  cuts += "*(nTracksLengthLt[5] < 3.)"

  hitcuts = "*(Iteration$ < 12)"



  logy = True
  nData = 224281.0

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100

  baseDir="/scratch/jhugon/"
  baseDir=""


  ########################################################
  ## Beam Pions Definitions ##############################
  ########################################################

  fileConfigs = [
    #{
    #  'fn': "piAbs_v2/piAbsSelector_Pos_RunII_current100_v02_all.root",
    #  'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current100_v02_all.root"],
    #  'name': "RunII_Pos_100",
    #  'title': "Run II +100A",
    #  'caption': "Run II +100A",
    #  'isData': True,
    #},
    #{
    #  'fn': "piAbs_v2/piAbsSelector_Pos_RunII_current60_v02_all.root",
    #  'addFriend': ["friend", "piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current60_v02_all.root"],
    #  'name': "RunII_Pos_60",
    #  'title': "Run II +60A",
    #  'caption': "Run II +60A",
    #  'isData': True,
    #},
    #{
    #  'fn': "billMC1/MC1_PDG_211.root",
    #  'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_211.root"],
    #  'name': "pip_weighted",
    #  'title': "#pi^{+} MC Weighted",
    #  'caption': "#pi^{+} MC Weighted",
    #  'scaleFactor': 1./25000*nData,
    #  'cuts': "*pzWeight",
    #},
    {
      'fn': "billMC1/MC1_PDG_211.root",
      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_211.root"],
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'scaleFactor': 1./25000*nData,
    },
    {
      'fn': "mcSmearedForCalibration/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear10_v6.root",
      'addFriend': ["friend", "mcSmearedForCalibration/friendTrees/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear10_v6.root"],
      'name': "pip_presmear10",
      'title': "#pi^{+} MC Smear 10%",
      'caption': "#pi^{+} MC Smear 10%",
      'scaleFactor': 1./25000*nData,
    },
    #{
    #  'fn': "mcSmearedForCalibration/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear10_v6.root",
    #  'addFriend': ["friend", "mcSmearedForCalibration/friendTrees/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear10_v6.root"],
    #  'name': "pip_presmear10_weighted",
    #  'title': "#pi^{+} MC Smear 10%",
    #  'caption': "#pi^{+} MC Smear 10%",
    #  'scaleFactor': 1./25000*nData,
    #  'cuts': "*pzWeight",
    #},
    {
      'fn': "mcSmearedForCalibration/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear30_v6.root",
      'addFriend': ["friend", "mcSmearedForCalibration/friendTrees/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear30_v6.root"],
      'name': "pip_presmear30",
      'title': "#pi^{+} MC Smear 30%",
      'caption': "#pi^{+} MC Smear 30%",
      'scaleFactor': 1./25000*nData,
    },
    #{
    #  'fn': "mcSmearedForCalibration/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear30_v6.root",
    #  'addFriend': ["friend", "mcSmearedForCalibration/friendTrees/PiAbsSelector_lariat_PiAbsAndChEx_flat_pip_presmear30_v6.root"],
    #  'name': "pip_presmear30_weighted",
    #  'title': "#pi^{+} MC Smear 30%",
    #  'caption': "#pi^{+} MC Smear 30%",
    #  'scaleFactor': 1./25000*nData,
    #  'cuts': "*pzWeight",
    #},
#    {
#      'fn': "billMC1/MC1_PDG_2212.root",
#      'addFriend': ["friend", "billMC1/friendTrees/friend_MC1_PDG_2212.root"],
#      'name': "p",
#      'title': "proton MC",
#      'caption': "proton MC",
#      'color': root.kRed-4,
#      'scaleFactor': 1./10000*nData,
#    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]
    try:
      fileConfigs[i]['cuts'] += cuts+piMassCuts
    except KeyError:
      fileConfigs[i]['cuts'] = cuts+piMassCuts

  histConfigs = [
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,1.,5.0],
      'var': "primTrkdEdxs",
      'cuts': "1"+hitcuts,
      'normalize': True,
    },
    {
      'name': "primTrkPitches",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0.,2.0],
      'var': "primTrkPitches",
      'cuts': "1"+hitcuts,
      'normalize': True,
    },
    {
      'name': "nTracksLengthLt3",
      'xtitle': "N Tracks with Length < 5 cm",
      'ytitle': "Events / bin",
      'binning': [20,0,20],
      'var': "nTracksLengthLt[5]",
      'cuts': "1",
      'normalize': True,
    },
    #{
    #  'name': "pWC",
    #  'xtitle': "Beamline Momentum [MeV/c]",
    #  'ytitle': "Events / bin",
    #  'binning': [40,100,1100],
    #  'var': "(!isMC)*pWC+isMC*trueStartMom",
    #  'cuts': "1",
    #  'normalize': True,
    #},
    #{
    #  'name': "primTrkLength",
    #  'xtitle': "Primary Track Length [cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,100],
    #  'var': "primTrkLength",
    #  'cuts': "1",
    #  'normalize': True,
    #},
    #{
    #  'name': "beamlineMass",
    #  'xtitle': "Beamline Mass Squared [MeV^{2}]",
    #  'ytitle': "Events / bin",
    #  'binning': [100,-5e5,2e6],
    #  'var': "pWC*pWC*(firstTOF*firstTOF*0.00201052122-1.)",
    #  'cuts': "1",
    #  #'normalize': True,
    #  'logy': True,
    #  'drawvlines':[105.65**2,139.6**2,493.677**2,938.272046**2],
    #},
    #{
    #  'name': "primTrkRangeSoFars",
    #  'ytitle': "Hits / bin",
    #  'xtitle': "Primary Track Range so Far [cm]",
    #  'binning': [100,0,50],
    #  'var': "primTrkLength-primTrkResRanges",
    #  'cuts': "1"+hitcuts,
    #  'normalize': True,
    #},
    #{
    #  'name': "primTrkZs",
    #  'ytitle': "Hits / bin",
    #  'xtitle': "Primary Track Hit z [cm]",
    #  'binning': [120,-10,110],
    #  'var': "primTrkZs",
    #  'cuts': "1"+hitcuts,
    #  'normalize': True,
    #},
  ]
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",outPrefix="Calibrate_PiMuE_",nMax=NMAX)
  histConfigs = [
    {
      'name': "primTrkdEdxsVbeamlineMom",
      'xtitle': "Beamline Momentum [MeV/c]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,100,1100,100,0,10.0],
      'var': "primTrkdEdxs:(!isMC)*pWC+isMC*trueStartMom",
      'cuts': "1"+hitcuts,
    },
    #{
    #  'name': "primTrkdEdxsVResRange",
    #  'xtitle': "Residual Range [cm]",
    #  'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
    #  'binning': [50,0,100,50,1.,2.5],
    #  'var': "primTrkdEdxs:primTrkResRanges",
    #  'cuts': "1"+hitcuts,
    #},
    #{
    #  'name': "primTrkLengthVkinWCInTPC",
    #  'xtitle': "Kinetic Energy at TPC Start [MeV]",
    #  'ytitle': "Primary TPC Track Length [cm]",
    #  'binning': [50,0,600,50,0,100],
    #  'var': "primTrkLength:kinWCInTPC",
    #  'cuts': "1",
    #},
    #{
    #  'name': "beamline_TOFVMom",
    #  'xtitle': "Beamline Momentum [MeV/c]",
    #  'ytitle': "Time Of Flight [ns]",
    #  'binning': [100,0,2000,100,0,100],
    #  'var': "firstTOF:pWC",
    #  'cuts': "1",
    #  'logz': True,
    #},
    #{
    #  'name': "primTrkRangeSoFarsVIteration",
    #  'xtitle': "Primary Track Hit Iteration",
    #  'ytitle': "Primary Track Range so Far [cm]",
    #  'binning': [20,0,20,40,0,20],
    #  'var': "primTrkLength-primTrkResRanges:Iteration$",
    #  'cuts': "1"+hitcuts,
    #  'logz': True,
    #},
  ]
  hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",outPrefix="Calibrate_PiMuE_",nMax=NMAX)
  for histname in hists:
    mpvGraphs = []
    wGraphs = []
    labels = []
    names = []
    for samplename in sorted(hists[histname]):
      hist = hists[histname][samplename]
      mpvGraph, wGraph = fitCosmicHalo.fitSlicesLandaus(c,hist,samplename,fracMax=0.4)
      mpvGraphs.append(mpvGraph)
      wGraphs.append(wGraph)
      label = samplename
      for fileConfig in fileConfigs:
        if fileConfig['name'] == samplename:
          label = fileConfig['title']
      labels.append(label)
      names.append(samplename)
      #fitCosmicHalo.fitSlicesLandauCore(c,hist,samplename)
    c.Clear()
    for i in range(len(mpvGraphs)):
        mpvGraphs[i].SetLineColor(COLORLIST[i])
        mpvGraphs[i].SetMarkerColor(COLORLIST[i])
    predictor = bethe.Bethe()
    pionPredGraph = root.TGraph()
    muonPredGraph = root.TGraph()
    muonPredGraph.SetLineColor(root.kGray+2)
    for iPoint, mom in enumerate(numpy.linspace(100,1500)):
      mpvPred = predictor.mpv(SLABTHICKNESS,mom,bethe.PIONMASS)/SLABTHICKNESS
      pionPredGraph.SetPoint(iPoint,mom,mpvPred)
      mpvPred = predictor.mpv(SLABTHICKNESS,mom,bethe.MUONMASS)/SLABTHICKNESS
      muonPredGraph.SetPoint(iPoint,mom,mpvPred)
    ax = drawGraphs(c,mpvGraphs+[pionPredGraph,muonPredGraph],"Beamline Momentum [MeV/c]","Landau MPV [MeV/cm]",xlims=[0,1200],ylims=[0,5],freeTopSpace=0.5,drawOptions=["pez"]*len(mpvGraphs)+["c"]*2,reverseDrawOrder=True)
    #ax = drawGraphs(c,mpvGraphs,"Beamline Momentum [MeV/c]","Landau MPV [MeV/cm]",xlims=[400,1200],ylims=[0,10],freeTopSpace=0.5)
    leg = drawNormalLegend(mpvGraphs+[pionPredGraph,muonPredGraph],labels+["Bethe #pi^{+}","Bethe #mu^{+}"],["lep"]*len(mpvGraphs)+["l"]*2)
    drawStandardCaptions(c,"Assuming Slab Thickness {:.3f} cm".format(SLABTHICKNESS))

    c.SaveAs("Calibrate_mpvs.png")
    c.SaveAs("Calibrate_mpvs.pdf")

    ########################################
    ## Ratio Plot

    mpvGraphsRatioToPred = []
    for mpvGraph in mpvGraphs:
      N = mpvGraph.GetN()
      xs  = mpvGraph.GetX()
      ys  = mpvGraph.GetY()
      exs = mpvGraph.GetEX()
      eys = mpvGraph.GetEY()
      graph = root.TGraphErrors()
      graph.SetLineColor(mpvGraph.GetLineColor())
      graph.SetMarkerColor(mpvGraph.GetMarkerColor())
      for iPoint in range(N):
        mom = xs[iPoint]
        mpvPred = predictor.mpv(SLABTHICKNESS,mom,bethe.PIONMASS)/SLABTHICKNESS
        graph.SetPoint(iPoint,xs[iPoint],ys[iPoint]/mpvPred)
        graph.SetPointError(iPoint,exs[iPoint],eys[iPoint]/mpvPred)
      mpvGraphsRatioToPred.append(graph)

    xlims = [0,1200]
    oneGraph = root.TGraph()
    oneGraph.SetLineStyle(7)
    oneGraph.SetPoint(0,xlims[0],1)
    oneGraph.SetPoint(1,xlims[1],1)
    ax = drawGraphs(c,mpvGraphsRatioToPred+[oneGraph],"Beamline Momentum [MeV/c]","Landau MPV: Measured / Bethe Prediction",xlims=xlims,ylims=[0,2.5],drawOptions=["pez"]*len(mpvGraphsRatioToPred)+["l"],reverseDrawOrder=True)
    leg = drawNormalLegend(mpvGraphsRatioToPred,labels,"lep")
    drawStandardCaptions(c,"Assuming Slab Thickness {:.3f} cm".format(SLABTHICKNESS))
    c.SaveAs("Calibrate_mpvs_pi_ratio.png")
    c.SaveAs("Calibrate_mpvs_pi_ratio.pdf")

    mpvGraphsRatioToUnsmearMC = []
    labelsRatioToUnsmearMC = []
    unsmearMCGraph = None
    for name, mpvGraph in zip(names,mpvGraphs):
        if name == "pip":
            unsmearMCGraph = mpvGraph
            break
    if unsmearMCGraph is None:
        raise Exception("Couldn't find pip graph for unsmeared MC")
    for name, label, mpvGraph in zip(names,labels,mpvGraphs):
      if name == "pip":
        continue
      labelsRatioToUnsmearMC.append(label)
      N = mpvGraph.GetN()
      xs  = mpvGraph.GetX()
      ys  = mpvGraph.GetY()
      exs = mpvGraph.GetEX()
      eys = mpvGraph.GetEY()
      if N != unsmearMCGraph.GetN():
        raise Exception("Unsmeared mpv graph N points doesn't match this graph N points")
      ys_unsmear = unsmearMCGraph.GetY()
      graph = root.TGraphErrors()
      graph.SetLineColor(mpvGraph.GetLineColor())
      graph.SetMarkerColor(mpvGraph.GetMarkerColor())
      for iPoint in range(N):
        mom = xs[iPoint]
        mpvUnsmear = ys_unsmear[iPoint]
        graph.SetPoint(iPoint,xs[iPoint],ys[iPoint]/mpvUnsmear)
        graph.SetPointError(iPoint,exs[iPoint],eys[iPoint]/mpvUnsmear)
      mpvGraphsRatioToUnsmearMC.append(graph)

    ax = drawGraphs(c,mpvGraphsRatioToUnsmearMC+[oneGraph],"Beamline Momentum [MeV/c]","Landau MPV: Ratio to Unsmeared MC",xlims=xlims,ylims=[0.8,1.2],freeTopSpace=0.5,drawOptions=["pez"]*len(mpvGraphsRatioToUnsmearMC)+["l"],reverseDrawOrder=True)
    leg = drawNormalLegend(mpvGraphsRatioToUnsmearMC,labelsRatioToUnsmearMC,"lep")
    c.SaveAs("Calibrate_mpvs_nosmear_ratio.png")
    c.SaveAs("Calibrate_mpvs_nosmear_ratio.pdf")
