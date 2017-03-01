#!/usr/bin/env python2

import uuid
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)

class LandauMaker(object):
  def __init__(self,rooObservable,rooMpv,rooXi):
    self.mpv = rooMpv
    self.xi = rooXi
    self.observable = rooObservable
    self.name = "landau_"+uuid.uuid4().get_hex()
    self.p2 = root.RooFormulaVar(self.name+"p2","second landau param","4*@0",root.RooArgList(self.xi))
    self.p1 = root.RooFormulaVar(self.name+"p1","first landau param","@0+0.22278*@1",root.RooArgList(self.mpv,self.p2))
    self.landau = root.RooLandau(self.name,"landau",rooObservable,self.p1,self.p2)
  def getPdf(self):
    return self.landau

if __name__ == "__main__":

   t = root.RooRealVar("t","dE/dx [MeV/cm]",-10,50)
   observables = root.RooArgSet(t)

   # MIP Muon
   mpv = root.RooRealVar("mpv","mpv landau",1.7,-20,20)
   xi = root.RooRealVar("xi","xi landau",0.105,0,20)
   landauObj = LandauMaker(t,mpv,xi)
   landau = landauObj.getPdf()

   mg = root.RooRealVar("mg","mg",0)
   sg = root.RooRealVar("sg","sg",0.1)
   gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

   # 500 MeV proton
   mpv2 = root.RooRealVar("mpv2","mpv landau",6.5,-20,20)
   xi2 = root.RooRealVar("xi2","xi landau",0.375,0,20)
   wl2 = root.RooFormulaVar("wl2","second landau param","4*@0",root.RooArgList(xi2))
   ml2 = root.RooFormulaVar("ml2","first landau param","@0+0.22278*@1",root.RooArgList(mpv2,wl2))
   landau2 = root.RooLandau("lx2","lx",t,ml2,wl2)

   t.setBins(10000,"cache")
   langaus = root.RooFFTConvPdf("langaus","landau (X) gauss",t,landau,gauss)
   langaus2 = root.RooFFTConvPdf("langaus2","landau2 (X) gauss",t,landau2,gauss)

   ratio = root.RooRealVar("ratio","ratio",0.18,0,1)
   twolandaus = root.RooAddPdf("twolandaus","twolandaus",langaus,langaus2,ratio)

   model = twolandaus

   data = model.generate(observables,10000)

   #model.fitTo(data)

   frame = t.frame(root.RooFit.Title("landau (x) gauss convolution"))
   data.plotOn(frame)
   model.plotOn(frame)
   model.plotOn(frame,root.RooFit.Components("langaus"),root.RooFit.LineStyle(root.kDashed))
   model.plotOn(frame,root.RooFit.Components("langaus2"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))

   c = root.TCanvas("rf208_convolution","rf208_convolution",600,600)
   root.gPad.SetLeftMargin(0.15)
   frame.GetYaxis().SetTitleOffset(1.4)
   frame.Draw("same")
   axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
   #axisHist = root.TH2F("axisHist","",1,-5,5,1,0,1200)
   axisHist.Draw()
   frame.Draw("same")
   c.SaveAs("roofit.pdf")
