#!/usr/bin/env python

import re
import ROOT

def getLifetimeGraphs(scaleFactor=1.):
  graph = ROOT.TGraphAsymmErrors()
  iPoint = 0
  with open("ZoomLifetime_Run2_v05_01_01.txt") as f:
    for line in f:
      reString = r"([-+.0-9]+)\s+"*13
      match = re.match(reString,line)
      if match:
        firstRun = int(match.group(1))
        lastRun = int(match.group(2))
        value = float(match.group(3))*scaleFactor
        errLow = float(match.group(4))*scaleFactor
        errHigh = float(match.group(5))*scaleFactor
        middleRun = 0.5*(firstRun+lastRun)
        graph.SetPoint(iPoint,middleRun,value)
        graph.SetPointEYhigh(iPoint,errHigh)
        graph.SetPointEYlow(iPoint,errLow)
        graph.SetPointEXhigh(iPoint,0.5*(lastRun-firstRun))
        graph.SetPointEXlow(iPoint,0.5*(lastRun-firstRun))
        iPoint+=1
  return graph

if __name__ == "__main__":
  from helpers import *
  graph = getLifetimeGraphs()
  c = ROOT.TCanvas()
  axisHist = drawGraphs(c,[graph],"Run Number","Electron Lifetime",ylims=[0,2000])
  c.SaveAs("MonicaElectonLifetime.png")
  c.SaveAs("MonicaElectonLifetime.pdf")
