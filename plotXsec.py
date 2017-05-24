#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # pions
  #cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # protons
  #cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks

  cuts = "*(iBestMatch >= 0  && nMatchedTracks == 1)" # matching in analyzer

  ###
  ###
  #secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2. || trackEndDistToPrimTrkEnd < 2.)"
  #weightStr = "pzWeight"+cuts
  weightStr = "1"
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
    },
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi2GeV.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip2GeV",
      'title': "#pi^{+} 2 GeV MC",
      'caption': "#pi^{+} 2 GeV MC",
    },
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi3GeV.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip3GeV",
      'title': "#pi^{+} 3 GeV MC",
      'caption': "#pi^{+} 3 GeV MC",
    },
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi6GeV.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip6GeV",
      'title': "#pi^{+} 6 GeV MC",
      'caption': "#pi^{+} 6 GeV MC",
    },
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi7GeV.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip7GeV",
      'title': "#pi^{+} 7 GeV MC",
      'caption': "#pi^{+} 7 GeV MC",
    },
    {
      'fn': "/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_33_01_01/srcs/dunetpc/dune/PionAna/pionana_pi.root",
      #'addFriend': ["friend", "friendTree_pip_v3.root"],
      #'fn': "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root",
      'name': "pip147GeV",
      'title': "#pi^{+} 1,4,7 GeV MC",
      'caption': "#pi^{+} 1,4,7 GeV MC",
    },
  ]

  histConfigs = [
    {
      'name': "Incident",
      'title': "Incident",
      'xtitle': "Reco Kinetic Energy [MeV]",
      'ytitle': "Track Hits / MeV",
      'binning': [50,0,1000],
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
      'binning': [50,0,1000],
      'var': "primTrkKinInteract",
      'cuts': weightStr+cuts,
      'normToBinWidth': True,
      'logy': logy,
      'color': root.kBlue,
      'printIntegral': True,
    },
  ]

  kinHists_low = plotOneHistOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="XsecPlot_low_",writeImages=False)

  histConfigs[0]["cuts"] += "*(1./100)"
  histConfigs[0]["title"] += "/100"
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="RecoKin_low_")

  histConfigs = [
    {
      'name': "Incident",
      'title': "Incident",
      'xtitle': "Reco Kinetic Energy [MeV]",
      'ytitle': "Track Hits / MeV",
      'binning': [280,0,7000],
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
      'binning': [280,0,7000],
      'var': "primTrkKinInteract",
      'cuts': weightStr+cuts,
      'normToBinWidth': True,
      'logy': logy,
      'color': root.kBlue,
      'printIntegral': True,
    },
  ]

  kinHists_high = plotOneHistOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="XsecPlot_",writeImages=False)

  histConfigs[0]["cuts"] += "*(1./100)"
  histConfigs[0]["title"] += "/100"
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"pionabs/tree",nMax=NMAX,outPrefix="RecoKin_")

  for kinHists, caption in [(kinHists_low,"low"),(kinHists_high,"high")]:
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
      sliceThickness = 0.479/math.cos(0.282441) # cm (beam angle w.r.t. z-axis i.e. theta beam)
      scaleFactorcm = 1./(numberdensity*sliceThickness) # cm2 / particles
      scaleFactorBarn = 1e24 * scaleFactorcm # barn / particles
      #
      xsec.Scale(scaleFactorBarn)
      xsec.GetXaxis().SetTitle("Reco Kinetic Energy [MeV]")
      xsec.GetYaxis().SetTitle("Total Cross Section [barn]")
      #xsec.GetXaxis().SetRangeUser(50,1000)
      #xsec.GetYaxis().SetRangeUser(0,3.5)
      xsec.GetYaxis().SetRangeUser(0,6.)
      xsec.Draw()
      #c.SetLogy(True)
      drawStandardCaptions(c,"Super-preliminary",captionright1="#pi^{+} MC")
      c.SaveAs("xsec_MC_{}_{}.png".format(caption,fileName))
      c.SaveAs("xsec_MC_{}_{}.pdf".format(caption,fileName))

    
