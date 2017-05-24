#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # pions
  #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # protons
  #cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks

  #cuts = "*(iBestMatch >= 0  && nMatchedTracks == 1)" # matching in analyzer

  ###
  ###
  #secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2. || trackEndDistToPrimTrkEnd < 2.)"
  #weightStr = "pzWeight"+cuts
  weightStr = "1"+cuts
  logy = False

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi1GeV.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip1GeV",
      'title': "#pi^{+} 1 GeV MC",
      'caption': "#pi^{+} 1 GeV MC",
      'color': root.kBlue,
      #'scaleFactor': 0.28946*1.888,
      #'scaleFactor': 1275.21,
    },
  ]

  histConfigs = [
    {
      'name': "Incident",
      'title': "Incident",
      'xtitle': "Reco Kinetic Energy [MeV]",
      'ytitle': "Track Hits / MeV",
      'binning': [100,0,1000],
      'var': "primTrkKins",
      'cuts': weightStr+cuts+"*primTrkInFids",
      'normToBinWidth': True,
      'logy': logy,
    },
    {
      'name': "Interacting",
      'title': "Interacting",
      'xtitle': "Reco Kinetic Energy [MeV]",
      'ytitle': "Track Hits / MeV",
      'binning': [100,0,1000],
      'var': "primTrkKinInteract",
      'cuts': weightStr+cuts,
      'normToBinWidth': True,
      'logy': logy,
      'color': root.kBlue,
    },
  ]

  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="RecoKin_")
  kinHists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="XsecPlot_",writeImages=False)
  print(kinHists)

  for fileConfig in fileConfigs:
    fileName = fileConfig["name"]
    incident = kinHists['Incident'][fileName]
    interacting = kinHists['Interacting'][fileName]
    rebin = 5
    interacting.Rebin(rebin)
    incident.Rebin(rebin)
    interacting.Scale(1./rebin)
    incident.Scale(1./rebin)
    xsec = interacting.Clone(interacting.GetName()+"xsec")
    xsec.Divide(incident)
    #
    density = 1.3954 # g / cm3
    molardensity = 39.948 #g / mol
    avagadro = 6.022140857e23
    numberdensity = density * avagadro / molardensity # particles / cm3
    sliceThickness = 0.4/math.sin(60.*math.pi/180.) # cm
    scaleFactorcm = 1./(numberdensity*sliceThickness) # cm2 / particles
    scaleFactorBarn = 1e24 * scaleFactorcm # barn / particles
    #
    xsec.Scale(scaleFactorBarn)
    xsec.GetXaxis().SetTitle("Reco Kinetic Energy [MeV]")
    xsec.GetYaxis().SetTitle("Total Cross Section [barn]")
    xsec.GetXaxis().SetRangeUser(50,1000)
    xsec.GetYaxis().SetRangeUser(0,3.5)
    xsec.Draw()
    #c.SetLogy(True)
    drawStandardCaptions(c,"Super-preliminary",captionright1="#pi^{+} MC")
    c.SaveAs("xsec_MC_{}.png".format(fileName))
    c.SaveAs("xsec_MC_{}.pdf".format(fileName))

    
