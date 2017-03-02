#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  cuts = ""
  #cuts += "*( pWC > 100 && pWC < 1100 && (isMC || (firstTOF > 0 && firstTOF < 25)))" # pions
  cuts += "*( pWC > 450 && pWC < 1100 && (isMC || (firstTOF > 28 && firstTOF < 55)))" # protons
  cuts += "*(nTracksInFirstZ[2] >= 1 && nTracksInFirstZ[14] < 4 && nTracksLengthLt[5] < 3)" # tpc tracks

  cuts = "*(iBestMatch >= 0  && nMatchedTracks == 1)" # matching in analyzer

  ###
  ###
  secTrkCuts = "*(trackStartDistToPrimTrkEnd < 2. || trackEndDistToPrimTrkEnd < 2.)"
  #weightStr = "pzWeight"+cuts
  weightStr = "1"+cuts
  nData = 30860.0
  logy = True

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=100
  fileConfigs = [
    {
      #'fn': "piAbs_data_Pos_RunI_v03.root",
      #'addFriend': ["friend", "friendTree_Pos_RunI_v03.root"],
      'fn': "test_data_Pos_RunI_piAbsSelector.root",
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
      'isData': True,
    },
    {
      #'fn': "piAbs_data_Pos_RunII_v03.root",
      #'addFriend': ["friend", "friendTree_Pos_RunII_v03.root"],
      'fn': "test_data_Pos_RunII_piAbsSelector.root",
      'name': "RunII_Pos",
      'title': "Run II Pos. Polarity",
      'caption': "Run II Pos. Polarity",
      'color': root.kGray+1,
      'isData': True,
    },
    {
      #'fn': "piAbs_pip_v5.root",
      #'addFriend': ["friend", "friendTree_pip_v5.root"],
      'fn': "test_pip_piAbsSelector.root",
      'name': "pip",
      'title': "#pi^{+} MC",
      'caption': "#pi^{+} MC",
      'color': root.kBlue-7,
      #'scaleFactor': 1./35250*nData*0.428/(1.-0.086), #No Cuts
      'scaleFactor': 1./35250*nData*0.428/(1.-0.086)*0.70, # pion/tpc tracks cuts
    },
    {
      #'fn': "piAbs_p_v5.root",
      #'addFriend': ["friend", "friendTree_p_v5.root"],
      'fn': "test_p_piAbsSelector.root",
      'name': "p",
      'title': "proton MC",
      'caption': "proton MC",
      'color': root.kRed-4,
      'scaleFactor': 1./35200*nData*0.162/(1.-0.086), #No Cuts
    },
    {
      #'fn': "piAbs_ep_v5.root",
      #'addFriend': ["friend", "friendTree_ep_v5.root"],
      'fn': "test_ep_piAbsSelector.root",
      'name': "ep",
      'title': "e^{+} MC",
      'caption': "e^{+} MC",
      'color': root.kGreen,
      #'scaleFactor': 1./35700*nData*0.301/(1.-0.086), #No Cuts
      'scaleFactor': 1./35700*nData*0.301/(1.-0.086)*0.70, # pion/tpc tracks cuts
    },
    {
      #'fn': "piAbs_mup_v5.root",
      #'addFriend': ["friend", "friendTree_mup_v5.root"],
      'fn': "test_mup_piAbsSelector.root",
      'name': "mup",
      'title': "#mu^{+} MC",
      'caption': "#mu^{+} MC",
      'color': root.kMagenta-4,
      #'scaleFactor': 1./35200*nData*0.021/(1.-0.086), #No Cuts
      'scaleFactor': 1./35200*nData*0.021/(1.-0.086)*0.70, # pion/tpc tracks cuts
    },
    #{
    #  'fn': "piAbs_kp_v5.root",
    #  'addFriend': ["friend", "friendTree_kp_v5.root"],
    #  #'fn': "test_kp_piAbsSelector.root",
    #  'name': "kp",
    #  'title': "K^{+} MC",
    #  'caption': "K^{+} MC",
    #  'color': root.kOrange-3,
    #  'scaleFactor': 1./35700*nData*0.00057/(1.-0.086), #No Cuts
    #},
    #{
    #  #'fn': "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_gam_v4/anahist.root",
    #  #'addFriend': ["friend", "friendTree_gam_v4.root"],
    #  'fn': "test_gam_piAbsSelector.root",
    #  'name': "gam",
    #  'title': "#gamma MC",
    #  'caption': "#gamma MC",
    #  'color': root.kOrange-3,
    #  'scaleFactor': 2953., #AllWeightsCuts Proton
    #},
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

  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix="RecoKin_")
  kinHists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"PiAbsSelector/tree",nMax=NMAX,outPrefix="XsecPlot_",writeImages=False)
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

    
