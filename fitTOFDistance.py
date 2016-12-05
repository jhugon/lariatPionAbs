#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def fitTOFDistanceProfile(fn,tofMax,c,nmax):
  fileConfigs = [
    {
      'fn': fn,
      'name': "",
      'title': "",
      'caption': "",
      'color': root.kBlack,
    },
  ]
  histConfigs = [  
    {
      'name': "FitTOF_dumbFit",
      'ytitle': "TOF^{2}p^{2} [(ns)^{2} (MeV/c)^{2}]",
      'xtitle': "p^{2} [(MeV/c)^{2}]",
      'binning': [1000,0,2e6,1000,0,1e9],
      'var': "tofObject[0]*tofObject[0]*wctrk_momentum[0]*wctrk_momentum[0]:wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<={0:f}".format(tofMax),
      'profileXtoo':True,
    },
  ]
  hists,profiles=plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=nmax)
  assert(len(hists)==1)
  assert(len(profiles)==1)
  hist = hists[0]
  profile = profiles[0]
  xAxis = profile.GetXaxis()

  func = root.TF1(uuid.uuid1().hex,"pol1",3e5,8e5)
  fitResult = profile.Fit(func,"NS","",3e5,8e5)

  fakeFunc = root.TF1(uuid.uuid1().hex,"pol1",xAxis.GetBinLowEdge(1),xAxis.GetBinUpEdge(xAxis.GetNbins()))
  fakeFunc.SetLineStyle(2)

  d = None
  dErr = None
  if fitResult.IsValid():
    # slope has units of time^2 in ns^2 
    # intercept has units of momentum^2 time^2 in ns^2 MeV^2 c^-2
    slope = fitResult.Parameter(1)
    intercept = fitResult.Parameter(0)
    slopeErr = fitResult.ParError(1)
    interceptErr = fitResult.ParError(0)
    print("Slope: {} +/- {}, Intercept: {} /- {}".format(slope,slopeErr,intercept,interceptErr))
    d2 = slope * 0.2998**2 # now in meters^2
    d = d2**(0.5) # now in meters
    d2Err = slopeErr * 0.2998**2
    dErr = d2Err**(0.5)
    print("Distance: {} +/- {}".format(d,dErr))
    fakeFunc.SetParameter(0,fitResult.Parameter(0))
    fakeFunc.SetParameter(1,fitResult.Parameter(1))
  else:
    print("Fit Failed")
    return None, None


  histConfigs[0]["funcs"] = [func,fakeFunc]
  histConfigs[0]["name"] = "fit"
  hists,profiles=plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=nmax)

  histConfigs2 = [  
    {
      'name': "FitTOF_mass2_narrow",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [100,-1e5,1e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/{0:f}/{0:f} - 1.)".format(d),
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(d),
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "FitTOF_mass2_narrowK",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [30,1.0e5,3.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/{0:f}/{0:f} - 1.)".format(d),
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(d),
      'caption': "Around Kaon Peak",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "FitTOF_mass2_narrowP",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [100,6e5,12e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/{0:f}/{0:f} - 1.)".format(d),
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(d),
      'caption': "Around Proton Peak",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "FitTOF_mass2",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [150,-1.5e6,1.5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/{0:f}/{0:f} - 1.)".format(d),
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(d),
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'logy': True,
    },
    {
      'name': "FitTOF_mass2_wide",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [200,-2e6,5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/{0:f}/{0:f} - 1.)".format(d),
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(d),
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2,1875.6**2],
      'logy': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs2,c,"anatree/anatree",nMax=nmax)
  return d, dErr

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=10000
  fns = ["BeamLineAnaTree_run6264_v06_15_00_v1.root"]
  fitTOFDistanceProfile(fns,27,c,NMAX)
