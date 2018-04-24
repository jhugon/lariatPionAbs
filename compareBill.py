#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def plotHists(canvas,filenames,labels,histNames):
  for iHistName, histName in enumerate(histNames):
    hists = []
    mylabels = []
    mycolors = []
    for iFile, f in enumerate(files):
      hist = f.Get(histName)
      if hist:
        hist.UseCurrentStyle()
        hist.SetLineColor(COLORLIST[iFile])
        hist.SetMarkerColor(COLORLIST[iFile])
        hists.append(hist)
        mycolors.append(COLORLIST[iFile])
        mylabels.append(labels[iFile])
    axisHist = makeStdAxisHist(hists)
    setHistTitles(axisHist,histName,"Counts / bin")
    axisHist.Draw()
    for hist in hists:
      if "PDG" in histName:
        hist.Draw("Phistsame")
      else:
        hist.Draw("histsame")
    leg = drawNormalLegend(hists,mylabels,wide=True)
    canvas.SaveAs(histName+".png")
    canvas.Clear()
    for hist in hists:
      integral = hist.Integral()
      if integral != 0.:
        hist.Scale(1./integral)
    axisHist = makeStdAxisHist(hists)
    setHistTitles(axisHist,histName,"Normalized Counts / bin")
    axisHist.Draw()
    for hist in hists:
      if "PDG" in histName:
        hist.Draw("Phistsame")
      else:
        hist.Draw("histsame")
    leg = drawNormalLegend(hists,mylabels,wide=True)
    canvas.SaveAs(histName+"_norm.png")
    canvas.Clear()


if __name__ == "__main__":

  canvas = root.TCanvas("canvas")
  filenames = [
        "/scratch/metcalf/lariat/pip_LC5_histos.root",
        "/scratch/metcalf/lariat/pip_TC5_histos.root",
        "/scratch/metcalf/lariat/pip_TCEl5_histos.root",
    ]
  labels = ["Default linecluster","Default trajcluster","Elena's trajcluster"]
  files = [root.TFile(fn) for fn in filenames]
  histNames = set()
  for f in files:
    #f.ls()
    for key in f.GetListOfKeys():
        name = key.GetName()
        histNames.add(name)
  histNames = list(histNames)
  histNames.sort()
  histNames_nt = [h for h in histNames if ("_NT" == h[-3:])]
  histNames_not_nt = [h for h in histNames if not ("_NT" == h[-3:] or "_T" == h[-2:])]
  plotHists(canvas,filenames,labels,histNames)
