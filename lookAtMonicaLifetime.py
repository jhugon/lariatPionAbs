#!/usr/bin/env python

import re
import ROOT

def getLifetimeGraphs(scaleFactor=1.):
  singleGraph = ROOT.TGraphErrors()
  multiGraph = ROOT.TGraphErrors()
  iPoint = 0
  with open("ZoomLifetime_Run2_v05_01_01.txt") as f:
    for line in f:
      reString = r"([-+.0-9]+)\s+"*13
      match = re.match(reString,line)
      if match:
        firstRun = int(match.group(1))
        lastRun = int(match.group(2))
        stuff = float(match.group(3))
        multi = float(match.group(4))*scaleFactor
        single = float(match.group(5))*scaleFactor
        middleRun = 0.5*(firstRun+lastRun)
        singleGraph.SetPoint(iPoint,middleRun,single)
        multiGraph.SetPoint(iPoint,middleRun,multi)
        singleGraph.SetPointError(iPoint,lastRun-firstRun,0.)
        multiGraph.SetPointError(iPoint,lastRun-firstRun,0.)
        iPoint+=1
  singleGraph.SetLineColor(ROOT.kRed-4)
  singleGraph.SetMarkerColor(ROOT.kRed-4)
  return singleGraph,multiGraph

if __name__ == "__main__":
  from helpers import *
  singleGraph, multiGraph = getLifetimeGraphs()
  c = ROOT.TCanvas()
  graphs = [singleGraph,multiGraph]
  labels = ["Single Track Method","Multi Track Method"]
  axisHist = drawGraphs(c,graphs,"Run Number","Electron Lifetime",freeTopSpace=0.35,ylims=[0,300])
  leg = drawNormalLegend(graphs,labels,option="lep",wide=True)
  c.SaveAs("MonicaElectonLifetimes.png")
  c.SaveAs("MonicaElectonLifetimes.pdf")
