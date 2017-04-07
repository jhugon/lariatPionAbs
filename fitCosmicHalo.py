#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

def plotSlices(c,hist,savename,xlimits,xtitle,ytitle,xvarname,rebinX=1,rebinY=1,xunits=None,normalize=False):
  hist = hist.Clone(uuid.uuid1().hex)

  hist.RebinX(rebinX)
  hist.RebinY(rebinY)
  histAll = hist.ProjectionY("_pyAll",1,hist.GetNbinsX())
  if normalize:
    integral = histAll.Integral()
    if integral != 0.:
        histAll.Scale(1./integral)
  ymax = histAll.GetMaximum()
  histAll.SetLineColor(root.kBlack)
  histAll.SetMarkerColor(root.kBlack)
  labels = ["All"]

  nBinsX = hist.GetNbinsX()
  sliceHists = []
  for iBin in range(1,nBinsX+1):
    sliceHist = getXBinHist(hist,iBin)
    if normalize:
      integral = sliceHist.Integral()
      if integral != 0.:
          sliceHist.Scale(1./integral)
    ymax = max(sliceHist.GetMaximum(),ymax)
    sliceHist.SetLineColor(COLORLIST[iBin-1])
    sliceHist.SetMarkerColor(COLORLIST[iBin-1])
    sliceHists.append(sliceHist)
    xlow = hist.GetXaxis().GetBinLowEdge(iBin)
    xhigh = hist.GetXaxis().GetBinUpEdge(iBin)
    if xunits:
      labels.append("{0} {3} < {1} < {2} {3}".format(xlow,xvarname,xhigh,xunits))
    else:
      labels.append("{0} < {1} < {2}".format(xlow,xvarname,xhigh))
  if c.GetLogy() == 1:
    ybound = ymax * 10**((log10(ymax)+1)*0.5)
    axisHist = Hist2D(1,xlimits[0],xlimits[1],1,0.1,ybound)
  else:
    axisHist = Hist2D(1,xlimits[0],xlimits[1],1,0,ymax*1.1)
  setHistTitles(axisHist,xtitle,ytitle)
  axisHist.Draw()
  for sliceHist in sliceHists:
    sliceHist.Draw("histsame")
  histAll.Draw("histsame")
  leg = drawNormalLegend([histAll]+sliceHists,labels)
  c.SaveAs(savename+".png")
  c.SaveAs(savename+".pdf")

def getMaxAndFWHM(hist,xBin):
  sliceHist = getXBinHist(hist,xBin)
  nBins = sliceHist.GetNbinsX()
  contentMax = sliceHist.GetMaximum()
  halfContentMax = 0.5*contentMax
  iMax = sliceHist.GetMaximumBin()
  xMax = sliceHist.GetXaxis().GetBinCenter(iMax)
  xHalfMaxAbove = float('nan')
  xHalfMaxBelow = float('nan')
  for iBin in range(iMax,nBins+2):
    if sliceHist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxAbove = sliceHist.GetXaxis().GetBinLowEdge(iBin)
        break
  for iBin in range(iMax,-1,-1):
    if sliceHist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxBelow = sliceHist.GetXaxis().GetBinUpEdge(iBin)
        break
  fwhm = xHalfMaxAbove-xHalfMaxBelow
  return xMax, fwhm

def makeGraphsModeAndFWHM(hist):
  hist = hist.Clone(uuid.uuid1().hex)
  graph = root.TGraph()
  graphFWHM = root.TGraph()
  for iBin in range(1,hist.GetNbinsX()+1):
    yMax, fwhm = getMaxAndFWHM(hist,iBin)
    x = hist.GetXaxis().GetBinCenter(iBin)
    graph.SetPoint(iBin-1,x,yMax)
    graphFWHM.SetPoint(iBin-1,x,fwhm)
  return graph, graphFWHM

if __name__ == "__main__":

  c = root.TCanvas("c")
  fHalo = root.TFile("halo_hists.root")
  #fHalo.ls()
  fCosmics = root.TFile("cosmics_hists.root")
  fCosmics.ls()

  for logy,xmax,outext,ytitle in [(False,4,"","Normalized--Hits"),(True,50,"_logy","Hits/bin")]:
    c.SetLogy(logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVx_RunIIPos"),"SlicesXRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVx_HaloMC"),"SlicesXHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"SlicesXRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_CosmicMC"),"SlicesXCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVy_RunIIPos"),"SlicesYRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVy_HaloMC"),"SlicesYHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"SlicesYRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"),"SlicesYCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=2,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVz_RunIIPos"),"SlicesZRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVz_HaloMC"),"SlicesZHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"SlicesZRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=2,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVz_CosmicMC"),"SlicesZ_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=2,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVrun_RunIIPos"),"SlicesRunRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"SlicesRunRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)

  ##############################################

  c.SetLogy(False)
  graphConfigs = [
    (fHalo.Get("primTrkdEdxsVrun_RunIIPos"),"Slices_modefwhm_run_halo","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
    (fHalo.Get("primTrkdEdxsVx_RunIIPos"),"Slices_modefwhm_x_halo","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
    (fHalo.Get("primTrkdEdxsVy_RunIIPos"),"Slices_modefwhm_y_halo","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
    (fHalo.Get("primTrkdEdxsVz_RunIIPos"),"Slices_modefwhm_z_halo","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
    (fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"Slices_modefwhm_run_cosmics","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
    (fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"Slices_modefwhm_x_cosmics","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
    (fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"Slices_modefwhm_y_cosmics","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
    (fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"Slices_modefwhm_z_cosmics","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
  ]

  for hist, savename, xtitle, ytitle, in graphConfigs:
    graphMode,graphFWHM = makeGraphsModeAndFWHM(hist)
    axisHist = makeStdAxisHist([graphMode,graphFWHM],ylim=[0,4])
    axisHist.Draw()
    graphMode.Draw("P")
    graphFWHM.Draw("P")
    graphFWHM.SetMarkerColor(COLORLIST[0])
    graphFWHM.SetLineColor(COLORLIST[0])
    setHistTitles(axisHist,xtitle,ytitle)
    c.SaveAs(savename+".png")
    c.SaveAs(savename+".pdf")
