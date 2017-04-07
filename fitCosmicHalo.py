#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

if __name__ == "__main__":

  c = root.TCanvas("c")
  f = root.TFile("halo_hists.root")
  #f.ls()
  hist = f.Get("primTrkdEdxsVx_RunIIPos")
  hist.RebinY(1)

  histAll = hist.ProjectionY("_pyAll",1,hist.GetNbinsX())
  integral = histAll.Integral()
  if integral != 0.:
      histAll.Scale(1./integral)
  ymax = histAll.GetMaximum()
  histAll.SetLineColor(root.kBlack)
  histAll.SetMarkerColor(root.kBlack)
  labels = ["All"]

  hist.RebinX(5)
  nBinsX = hist.GetNbinsX()
  sliceHists = []
  for iBin in range(1,nBinsX+1):
    sliceHist = getXBinHist(hist,iBin)
    integral = sliceHist.Integral()
    if integral != 0.:
        sliceHist.Scale(1./integral)
    ymax = max(sliceHist.GetMaximum(),ymax)
    sliceHist.SetLineColor(COLORLIST[iBin-1])
    sliceHist.SetMarkerColor(COLORLIST[iBin-1])
    sliceHists.append(sliceHist)
    xlow = hist.GetXaxis().GetBinLowEdge(iBin)
    xhigh = hist.GetXaxis().GetBinUpEdge(iBin)
    labels.append("{} cm < x < {} cm".format(xlow,xhigh))
  axisHist = Hist2D(1,0,4,1,0,ymax*1.1)
  setHistTitles(axisHist,"dE/dx [MeV/cm]","Normalized Events")
  axisHist.Draw()
  for sliceHist in sliceHists:
    sliceHist.Draw("histsame")
  histAll.Draw("histsame")
  leg = drawNormalLegend([histAll]+sliceHists,labels)
  c.SaveAs("FitTest.png")
  
  
  
  
