#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *
from fitCosmicHalo import *

if __name__ == "__main__":

  c = root.TCanvas("c")
  f = root.TFile("unifiso_hists.root")
  f.ls()

  #for logy,xmax,outext,ytitle in [(False,4,"","Normalized--Hits")]:#,(True,10,"_logy","Hits/bin")]:
  #  c.SetLogy(logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartTheta_UniformIsoMuon"),"Slices_trueStartTheta_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#theta",rebinX=5,rebinY=10,xunits="deg",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartThetaY_UniformIsoMuon"),"Slices_trueStartThetaY_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#theta_{y}",rebinX=5,rebinY=10,xunits="deg",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartThetaX_UniformIsoMuon"),"Slices_trueStartThetaX_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#theta_{x}",rebinX=5,rebinY=10,xunits="deg",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartPhi_UniformIsoMuon"),"Slices_trueStartPhi_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#phi",rebinX=5,rebinY=5,xunits="deg",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartPhiZX_UniformIsoMuon"),"Slices_trueStartPhiZX_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#phi_{zx}",rebinX=5,rebinY=10,xunits="deg",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVtrueStartPhiZY_UniformIsoMuon"),"Slices_trueStartPhiZY_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"#phi_{xy}",rebinX=5,rebinY=10,xunits="deg",normalize=not logy)

  #  plotSlices(c,f.Get("primTrkdEdxsVx_UniformIsoMuon"),"Slices_x_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,rebinY=10,xunits="cm",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVy_UniformIsoMuon"),"Slices_y_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=5,rebinY=10,xunits="cm",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsVz_UniformIsoMuon"),"Slices_z_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=5,rebinY=10,xunits="cm",normalize=not logy)

  #  plotSlices(c,f.Get("primTrkdEdxsVprimTrkPitches_UniformIsoMuon"),"Slices_primTrkPitches_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"pitch",rebinY=20,xunits="cm",normalize=not logy)
  #  plotSlices(c,f.Get("primTrkdEdxsV1OprimTrkPitches_UniformIsoMuon"),"Slices_1OprimTrkPitches_UniformIsoMuon"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"pitch^{-1}",rebinX=10,rebinY=20,xunits="cm^{-1}",normalize=not logy)


  ##############################################

  c.SetLogy(False)
#  graphConfigs = [
#    (f.Get("primTrkdEdxsVtrueStartPhiZY_UniformIsoMuon"),"Slices_trueStartPhiZY_fit","#phi_{zy}","Fit of dE/dx [MeV/cm]"),
#    (f.Get("primTrkdEdxsVtrueStartPhiZX_UniformIsoMuon"),"Slices_trueStartPhiZX_fit","#phi_{zx}","Fit of dE/dx [MeV/cm]"),
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

  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartPhiZY_UniformIsoMuon").Rebin2D(5,20,"newPhiZy"),"Fits_trueStartPhiZY_UniformIsoMuon_")
  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartPhiZX_UniformIsoMuon").Rebin2D(5,1,"newPhiZx"),"Fits_trueStartPhiZX_UniformIsoMuon_")
  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartPhi_UniformIsoMuon").Rebin2D(5,1,"newPhiXY"),"Fits_trueStartPhi_UniformIsoMuon_")
  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartCosThetaX_UniformIsoMuon").Rebin2D(5,2,"newCosThX"),"Fits_trueStartCosThetaX_UniformIsoMuon_")
  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartCosThetaY_UniformIsoMuon").Rebin2D(5,2,"newCosThY"),"Fits_trueStartCosThetaY_UniformIsoMuon_")
  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVtrueStartCosTheta_UniformIsoMuon").Rebin2D(5,2,"newCosTh"),"Fits_trueStartCosTheta_UniformIsoMuon_")

#  c.SetLogx(True)
#  fitSlicesLandauCore(c,f.Get("primTrkdEdxsVprimTrkPitches_UniformIsoMuon").Rebin2D(1,10,"newPitches"),"Fits_primTrkPitches_UniformIsoMuon_")
