#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def printAllPDGs(tree):
  pdgSecondariesSet = set()
  pdgTertiariesSet = set()
  for iEntry in range(min(tree.GetEntries(),100)):
    tree.GetEntry()
    #print "tree.pdg[iGeant], tree.TrackId[iGeant], tree.Mother[iGeant], tree.NumberDaughters[iGeant]"
    for iGeant in range(tree.geant_list_size):
      #print tree.pdg[iGeant], tree.TrackId[iGeant], tree.Mother[iGeant], tree.NumberDaughters[iGeant]
      if not tree.process_primary[iGeant]:
        pdg = tree.pdg[iGeant]
        motherNum = tree.Mother[iGeant]
        if motherNum == 1 and not pdg in pdgSecondariesSet:
          pdgSecondariesSet.add(pdg)
        elif motherNum != 1 and not pdg in pdgTertiariesSet:
          pdgTertiariesSet.add(pdg)
  
  pdgSecondariesList = sorted(list(pdgSecondariesSet))
  print "PDG IDs of Secondary Particles:"
  for pdg in pdgSecondariesList:
    print pdg
  pdgTertiariesList = sorted(list(pdgTertiariesSet))
  print "PDG IDs of Tertiary Particles:"
  for pdg in pdgTertiariesList:
    print pdg

if __name__ == "__main__":

  NMAX=500000
  fileConfigs = [
    #{
    #  'fn': "anaTree_p_v1.root",
    #  'addFriend': ["friend","friendTree_p_v1.root"],
    #  'pdg': 2212,
    #  'name': "p",
    #  'title': "p MC Sample",
    #  'caption': "p MC Sample",
    #  'color': root.kGreen+1,
    #},
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "0p5GeV",
      'title': "0.5 GeV #pi^{+} MC Sample",
      'caption': "0.5 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "1GeV",
      'title': "1 GeV #pi^{+} MC Sample",
      'caption': "1 GeV #pi^{+} MC Sample",
      'color': root.kBlack,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_1p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_1p5GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "1p5GeV",
      'title': "1.5 GeV #pi^{+} MC Sample",
      'caption': "1.5 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_3p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_3p0GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "3p5GeV",
      'title': "3.5 GeV #pi^{+} MC Sample",
      'caption': "3.5 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_4p0GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_4p0GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "4p0GeV",
      'title': "4.0 GeV #pi^{+} MC Sample",
      'caption': "4.0 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_4p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_4p5GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "4p5GeV",
      'title': "4.5 GeV #pi^{+} MC Sample",
      'caption': "4.5 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_5p0GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_5p0GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "5p0GeV",
      'title': "5.0 GeV #pi^{+} MC Sample",
      'caption': "5.0 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_5p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_5p5GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "5p5GeV",
      'title': "5.5 GeV #pi^{+} MC Sample",
      'caption': "5.5 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_6p0GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_6p0GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "6p0GeV",
      'title': "6.0 GeV #pi^{+} MC Sample",
      'caption': "6.0 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    #{
    #  'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_6p5GeV_mono_3ms_mcc8.0_v2/anahist.root",
    #  'addFriend': ["friend","friendTree_ProtoDUNE_pion_6p5GeV_mono_3ms_mcc8.0_v2.root"],
    #  'name': "6p5GeV",
    #  'title': "6.5 GeV #pi^{+} MC Sample",
    #  'caption': "6.5 GeV #pi^{+} MC Sample",
    #  'color': root.kBlue,
    #  #'scaleFactor' : 0.5,
    #},
    {
      'fn': "/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_7p0GeV_mono_3ms_mcc8.0_v2/anahist.root",
      'addFriend': ["friend","friendTree_ProtoDUNE_pion_7p0GeV_mono_3ms_mcc8.0_v2.root"],
      'name': "7p0GeV",
      'title': "7.0 GeV #pi^{+} MC Sample",
      'caption': "7.0 GeV #pi^{+} MC Sample",
      'color': root.kBlue,
      #'scaleFactor' : 0.5,
    },
    #{
    #  'fn': "anaTree_mup_v10.root",
    #  'addFriend': ["friend","friendTree_mup_v10.root"],
    #  'pdg': -13,
    #  'name': "mup",
    #  'title': "#mu^{+} MC Sample",
    #  'caption': "#mu^{+} MC Sample",
    #  'color': root.kRed,
    #},
    #{
    #  'fn': "anaTree_kp_v10.root",
    #  'addFriend': ["friend","friendTree_kp_v10.root"],
    #  'pdg': 321,
    #  'name': "kp",
    #  'title': "K^{+} MC Sample",
    #  'caption': "K^{+} MC Sample",
    #  'color': root.kBlue,
    #},
  ]

  for iFile in range(len(fileConfigs)):
      fileConfigs[iFile]['color'] = COLORLIST[iFile]

  histConfigs = [
    {
      'name': "pPrimary",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,7500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary",
    },
    {
      'name': "pSecondary",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "!process_primary && Mother == 1 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && abs(pdg) < 1000000",
      #'cuts': "!process_primary && pdg != 2112",
    },
    {
      'name': "pTertiary",
      'xtitle': "Tertiary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [100,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "!process_primary && Mother != 1 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && abs(pdg) < 1000000",
      #'cuts': "!process_primary && pdg != 2112",
    },
    #{
    #  'name': "motherPecondary",
    #  'xtitle': "Mother TrackID",
    #  'ytitle': "Entries/bin",
    #  'binning': [21,-0.5,20.5],
    #  'var': "Mother",
    #  'cuts': "process_primary && abs(pdg) < 1000000",
    #},
    #{
    #  'name': "motherSecondary",
    #  'xtitle': "Mother TrackID",
    #  'ytitle': "Entries/bin",
    #  'binning': [21,-0.5,20.5],
    #  'var': "Mother",
    #  'cuts': "!process_primary && abs(pdg) < 1000000",
    #},
    {
      'name': "thetaz",
      'xtitle': "Primary particle #theta w.r.t. z-axis [deg]",
      'ytitle': "Events / bin",
      'binning': [30,0,90],
      'var': "acos(Pz/sqrt(Px*Px+Py*Py+Pz*Pz))*180/pi",
      'cuts': "process_primary",
    },
    {
      'name': "costhetaz",
      'xtitle': "Primary particle cos(#theta) w.r.t. z-axis",
      'ytitle': "Events / bin",
      'binning': [100,0,1],
      'var': "Pz/sqrt(Px*Px+Py*Py+Pz*Pz)",
      'cuts': "process_primary",
    },
    {
      'name': "thetaxz",
      'xtitle': "Primary particle #theta in x-z plane",
      'ytitle': "Events / bin",
      'binning': [90,-90,90],
      'var': "TMath::ATan2(Px,Pz)*180/pi",
      'cuts': "process_primary",
    },
    {
      'name': "thetayz",
      'xtitle': "Primary particle #theta in y-z plane",
      'ytitle': "Events / bin",
      'binning': [90,-90,90],
      'var': "TMath::ATan2(Py,Pz)*180/pi",
      'cuts': "process_primary",
    },
  ]

#  TDirectoryFile*               analysistree    analysistree (dune/AnaTree/AnalysisTree) folder
#   KEY: TTree   anatree;1       analysis tree

  c = root.TCanvas()
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX)

  histConfigs = [
    {
      'name': "pip",
      'title': "#pi^{+}",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Arbitrary units",
      'normalize': True,
      'binning': [50,0,1500],
      'var': "P*1000",
      'cuts': "Mother == 1 && pdg==211 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
      'color': root.kBlack,
    },
    {
      'name': "pi0",
      'title': "#pi^{0}",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Arbitrary units",
      'normalize': True,
      'binning': [50,0,1500],
      'var': "P*1000",
      'cuts': "Mother == 1 && pdg==111 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
      'color': root.kRed,
    },
    {
      'name': "p",
      'title': "p",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Arbitrary units",
      'normalize': True,
      'binning': [50,0,1500],
      'var': "P*1000",
      'cuts': "Mother == 1 && pdg==2212 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
      'color': root.kGreen+1,
    },
    #{
    #  'name': "gam",
    #  'title': "#gamma",
    #  'xtitle': "Secondary particle |p| [MeV/c]",
    #  'ytitle': "Arbitrary units",
    #  'normalize': True,
    #  'binning': [150,0,1500],
    #  'var': "P*1000",
    #  'cuts': "Mother == 1 && pdg==22 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
    #  'color': root.kMagenta,
    #},
    #{
    #  'name': "mup",
    #  'title': "#mu^{+}",
    #  'xtitle': "Secondary particle |p| [MeV/c]",
    #  'ytitle': "Arbitrary units",
    #  'normalize': True,
    #  'binning': [150,0,1500],
    #  'var': "P*1000",
    #  'cuts': "Mother == 1 && pdg==-13 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
    #  'color': root.kCyan,
    #},
    {
      'name': "n",
      'title': "n",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Arbitrary units",
      'normalize': True,
      'binning': [50,0,1500],
      'var': "P*1000",
      'cuts': "Mother == 1 && pdg==2112 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && endsInTPC[0] && endsInTPC",
      'color': root.kBlue,
    },
  ]
  for iHist in range(len(histConfigs)):
      histConfigs[iHist]['color'] = COLORLIST[iHist]

  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="pSecondary_")

  histConfigs = [
    {
      'name': "stopped",
      'title': "Stopped in TPC",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary && endsInTPC",
      'color': root.kGreen,
    },
    {
      'name': "stoppedBefore",
      'title': "Stopped before TPC",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary && EndPointz < -5.",
      'color': root.kRed,
    },
    {
      'name': "all",
      'title': "All",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary",
      'color': root.kBlue,
    },
  ]
  for iHist in range(len(histConfigs)):
      histConfigs[iHist]['color'] = COLORLIST[iHist]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="pPrimaryStopped_")

  histConfigs = [
    {
      'name': "stopped",
      'title': "Stopped in TPC",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary && endsInTPC",
      'color': root.kGreen,
      #'logy': True,
    },
    #{
    #  'name': "allSecondariesTop",
    #  'title': "All Secondaries Stop in TPC",
    #  'xtitle': "Primary particle |p| [MeV/c]",
    #  'ytitle': "Particles per MeV/c",
    #  'normToBinWidth': True,
    #  'binning': [75,0,1500],
    #  'var': "P*1000",
    #  'cuts': "process_primary && endsInTPC && allSecondariesEndInTPC",
    #  'color': root.kCyan,
    #},
    {
      'name': "allSecondaryPiPSTop",
      'title': "All Secondary p/#pi^{#pm} Stop in TPC",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary && endsInTPC && allSecondaryPionsEndInTPC && allSecondaryProtonsEndInTPC",
      'color': root.kMagenta,
    },
    {
      'name': "stoppedBefore",
      'title': "Stopped before TPC",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary && EndPointz < -5.",
      'color': root.kRed,
    },
    {
      'name': "all",
      'title': "All",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "P*1000",
      'cuts': "process_primary",
      'color': root.kBlue,
    },
  ]
  for iHist in range(len(histConfigs)):
      histConfigs[iHist]['color'] = COLORLIST[iHist]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="pAllStopped_")

  histConfigs = [
    #{
    #  'name': "yVxPrimary",
    #  'xtitle': "Primary start x [cm]",
    #  'ytitle': "Primary start y [cm]",
    #  'ztitle': "Events/bin",
    #  'binning': [100,-500,500,100,0,600],
    #  'var': "StartPointy:StartPointx",
    #  'cuts': "process_primary",
    #},
    #{
    #  'name': "yVzPrimary",
    #  'xtitle': "Primary start z [cm]",
    #  'ytitle': "Primary start y [cm]",
    #  'ztitle': "Events/bin",
    #  'binning': [100,-300,500,100,0,600],
    #  'var': "StartPointy:StartPointz",
    #  'cuts': "process_primary",
    #},
    {
      'name': "yVxEndPrimary",
      'xtitle': "Primary end x [cm]",
      'ytitle': "Primary end y [cm]",
      'ztitle': "Events/bin",
      'binning': [100,-500,500,100,0,600],
      'var': "EndPointy:EndPointx",
      'cuts': "process_primary",
    },
    {
      'name': "yVzEndPrimary",
      'xtitle': "Primary end z [cm]",
      'ytitle': "Primary end y [cm]",
      'ztitle': "Events/bin",
      'binning': [100,-300,800,100,0,600],
      'var': "EndPointy:EndPointz",
      'cuts': "process_primary",
    },
    {
      'name': "xVzEndPrimary",
      'xtitle': "Primary end z [cm]",
      'ytitle': "Primary end x [cm]",
      'ztitle': "Events/bin",
      'binning': [100,-300,800,100,-500,500],
      'var': "EndPointx:EndPointz",
      'cuts': "process_primary",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="")

  histConfigs = [
    {
      'name': "pip",
      'title': "#pi^{+}",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryPiPlus",
      'cuts': "endsInTPC[0]",
      'color': root.kBlack,
      'logy': True,
    },
    {
      'name': "pim",
      'title': "#pi^{-}",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryPiMinus",
      'cuts': "endsInTPC[0]",
      'color': root.kCyan,
    },
    {
      'name': "pi0",
      'title': "#pi^{0}",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryPi0",
      'cuts': "endsInTPC[0]",
      'color': root.kRed,
    },
    {
      'name': "p",
      'title': "p",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryProton",
      'cuts': "endsInTPC[0]",
      'color': root.kBlue,
    },
    {
      'name': "gamma",
      'title': "#gamma",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryPhoton",
      'cuts': "endsInTPC[0]",
      'color': root.kGreen,
    },
    {
      'name': "n",
      'title': "n",
      'xtitle': "N Secondaries",
      'ytitle': "Particles / bin",
      'binning': [11,-0.5,10.5],
      'var': "nSecondaryNeutron",
      'cuts': "endsInTPC[0]",
      'color': root.kMagenta,
    },
  ]
  for iHist in range(len(histConfigs)):
      histConfigs[iHist]['color'] = COLORLIST[iHist]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="nPrimaryStopped_")

  histConfigs = [
    {
      'name': "pSecondaryPipVPrimary",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Secondary #pi^{+} |p| [MeV/c]",
      'ztitle': "Events/bin",
      'binning': [75,0,1500,50,0,1000],
      'var': "P*1000:P[0]*1000",
      'cuts': "endsInTPC[0] && Mother == 1 && pdg == 211 && endsInTPC",
    },
    {
      'name': "pSecondaryProtonVPrimary",
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Secondary proton |p| [MeV/c]",
      'ztitle': "Events/bin",
      'binning': [75,0,1500,50,0,1000],
      'var': "P*1000:P[0]*1000",
      'cuts': "endsInTPC[0] && Mother == 1 && pdg == 2212 && endsInTPC",
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"analysistree/anatree",nMax=NMAX,outPrefix="")
