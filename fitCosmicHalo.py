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

def fitLandaus(c,hist):

  t = root.RooRealVar("t","dE/dx [MeV/cm]",0.,10)
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  ##############
  mpvl = root.RooRealVar("mpvl","mpv landau",1.7,0,5)
  wl = root.RooRealVar("wl","width landau",0.42,0.01,10)
  ml = root.RooFormulaVar("ml","first landau param","@0+0.22278*@1",root.RooArgList(mpvl,wl))
  landau = root.RooLandau("lx","lx",t,ml,wl)

  mg = root.RooRealVar("mg","mg",0)
  sg = root.RooRealVar("sg","sg",0.1,0.01,2.)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  t.setBins(10000,"cache")
  langaus = root.RooFFTConvPdf("langaus","landau (X) gauss",t,landau,gauss)
  langaus.setBufferFraction(0.2)

  mpvl2 = root.RooRealVar("mpvl2","mpv landau",1.7,0,5)
  wl2 = root.RooRealVar("wl2","width landau",0.42,0.01,10)
  ml2 = root.RooFormulaVar("ml2","first landau param","@0+0.22278*@1",root.RooArgList(mpvl2,wl2))
  landau2 = root.RooLandau("lx2","lx2",t,ml2,wl2)
  langaus2 = root.RooFFTConvPdf("langaus2","landau (X) gauss",t,landau2,gauss)
  langaus2.setBufferFraction(0.2)
  
  mpvl3 = root.RooRealVar("mpvl3","mpv landau",1.7,0,5)
  wl3 = root.RooRealVar("wl3","width landau",0.42,0.01,10)
  ml3 = root.RooFormulaVar("ml3","first landau param","@0+0.22278*@1",root.RooArgList(mpvl3,wl3))
  landau3 = root.RooLandau("lx3","lx3",t,ml3,wl3)
  langaus3 = root.RooFFTConvPdf("langaus3","landau (X) gauss",t,landau3,gauss)
  langaus3.setBufferFraction(0.2)
  
  ratio = root.RooRealVar("ratio","ratio",0.18,0,1)
  ratio2 = root.RooRealVar("ratio2","ratio2",0.18,0,1)
  twolandaus = root.RooAddPdf("twolandaus","twolandaus",landau,landau2,ratio)
  threelandaus = root.RooAddPdf("threelandaus","threelandaus",root.RooArgList(landau,landau2,landau3),root.RooArgList(ratio,ratio2))
  twolangaus = root.RooAddPdf("twolangaus","twolandaus",langaus,langaus2,ratio)
  threelangaus = root.RooAddPdf("threelangaus","threelandaus",root.RooArgList(langaus,langaus2,langaus3),root.RooArgList(ratio,ratio2))


  model = threelandaus

  ##############

  model.fitTo(data)

  frame = t.frame(root.RooFit.Title("landau (x) gauss convolution"))
  data.plotOn(frame)
  model.plotOn(frame)

  model.plotOn(frame,root.RooFit.Components("lx"),root.RooFit.LineStyle(root.kDashed))
  model.plotOn(frame,root.RooFit.Components("lx2"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))
  model.plotOn(frame,root.RooFit.Components("lx3"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kGreen))

  #model.plotOn(frame,root.RooFit.Components("langaus"),root.RooFit.LineStyle(root.kDashed))
  #model.plotOn(frame,root.RooFit.Components("langaus2"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))
  #model.plotOn(frame,root.RooFit.Components("langaus3"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kGreen))

  #root.gPad.SetLeftMargin(0.15)
  #frame.GetYaxis().SetTitleOffset(1.4)
  #frame.Draw("same")
  #axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
  ##axisHist = root.TH2F("axisHist","",1,-1,1,1,1000,1300)
  #axisHist.Draw()
  #frame.Draw("same")
  frame.Draw()
  c.SaveAs("roofit.pdf")

def fitSlicesLandaus(c,hist):
  histAll = hist.ProjectionY("_pyAll",1,hist.GetNbinsX())
  fitLandaus(c,histAll)

if __name__ == "__main__":

  c = root.TCanvas("c")
  fHalo = root.TFile("halo_hists.root")
  #fHalo.ls()
  fCosmics = root.TFile("cosmics_hists.root")
  #fCosmics.ls()

  for logy,xmax,outext,ytitle in [(False,4,"","Normalized--Hits"),(True,50,"_logy","Hits/bin")]:
    c.SetLogy(logy)
#    plotSlices(c,fHalo.Get("primTrkdEdxsVx_RunIIPos"),"SlicesXRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
#    plotSlices(c,fHalo.Get("primTrkdEdxsVx_HaloMC"),"SlicesXHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"SlicesXRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_CosmicMC"),"SlicesXCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVy_RunIIPos"),"SlicesYRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVy_HaloMC"),"SlicesYHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"SlicesYRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"),"SlicesYCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVz_RunIIPos"),"SlicesZRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVz_HaloMC"),"SlicesZHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"SlicesZRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVz_CosmicMC"),"SlicesZ_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVyFromCenter_RunIIPos"),"SlicesYFromCenterRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVyFromCenter_HaloMC"),"SlicesYFromCenterHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_RunIIPos"),"SlicesYFromCenterRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_CosmicMC"),"SlicesYFromCenterCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)

    plotSlices(c,fHalo.Get("primTrkdEdxsVzFromCenter_RunIIPos"),"SlicesZFromCenterRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|z-45cm|",rebinX=8,xunits="cm",normalize=not logy)
    plotSlices(c,fHalo.Get("primTrkdEdxsVzFromCenter_HaloMC"),"SlicesZFromCenterHaloMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|z-45cm|",rebinX=8,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_RunIIPos"),"SlicesZFromCenterRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=4,xunits="cm",normalize=not logy)
    plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_CosmicMC"),"SlicesZFromCenter_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|z-45cm|",rebinX=8,xunits="cm",normalize=not logy)
#
#    plotSlices(c,fHalo.Get("primTrkdEdxsVrun_RunIIPos"),"SlicesRunRunIIPos_Halo"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"SlicesRunRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)

  ##############################################

#  c.SetLogy(False)
#  graphConfigs = [
#    (fHalo.Get("primTrkdEdxsVrun_RunIIPos"),"Slices_modefwhm_run_halo","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fHalo.Get("primTrkdEdxsVx_RunIIPos"),"Slices_modefwhm_x_halo","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fHalo.Get("primTrkdEdxsVy_RunIIPos"),"Slices_modefwhm_y_halo","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fHalo.Get("primTrkdEdxsVz_RunIIPos"),"Slices_modefwhm_z_halo","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"Slices_modefwhm_run_cosmics","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"Slices_modefwhm_x_cosmics","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"Slices_modefwhm_y_cosmics","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"Slices_modefwhm_z_cosmics","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#  ]
#
#  for hist, savename, xtitle, ytitle, in graphConfigs:
#    graphMode,graphFWHM = makeGraphsModeAndFWHM(hist)
#    axisHist = makeStdAxisHist([graphMode,graphFWHM],ylim=[0,4])
#    axisHist.Draw()
#    graphMode.Draw("P")
#    graphFWHM.Draw("P")
#    graphFWHM.SetMarkerColor(COLORLIST[0])
#    graphFWHM.SetLineColor(COLORLIST[0])
#    setHistTitles(axisHist,xtitle,ytitle)
#    c.SaveAs(savename+".png")
#    c.SaveAs(savename+".pdf")

  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_RunIIPos"))
  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"))
