#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import sys

from lookAtMonicaLifetime import getLifetimeGraphs

if __name__ == "__main__":

  cuts = ""
  #cuts += "*(isMC || ((triggerBits >> 4) & 1))" # BEAMON trigger
  cuts += "*(isMC || ((triggerBits >> 10) & 1))" # COSMICON trigger
  #cuts += "*(isMC || !((triggerBits >> 10) & 1))" # Not COSMICON trigger
  #cuts += "*(isMC || ((triggerBits >> 11) & 1))" # COSMIC trigger
  #cuts += "*(isMC || (nWCTracks ==0 && nTOFs ==0))"
  cuts += "*( iBestMatch >= 0)" # primary Track found
  #cuts += "*(acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi < 5. || acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi > 175.)" # theta vertical
  #cuts += "*((!isMC) || (trueStartMom>3000. && trueStartMom < 8000.))"

  #cuts += "*enterExitYm*enterExitYp"
  #cuts += "*(primTrkXs > 10. && primTrkXs < 38. &&  primTrkYs > 15. && primTrkZs > 10. && primTrkZs > 80.)"
  #cuts += "*(primTrkYs > 15.)"
  cuts += "*((!isMC) || (trueHitCosmic1 && trueHitCosmic2) || (trueHitCosmic3 && trueHitCosmic4))"
  cuts += "*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)" # only angles that match MC
  #cuts += "*(primTrkLength > 10.)" # didn't seem to make a difference
  cuts += "*(nTracks == 1)"
  #cuts += "*(primTrkLength > 80. && primTrkLength < 85.)"

  hitExtraCuts = "*(primTrkXs > 3. && primTrkXs < 46. && primTrkYs < 18. && primTrkYs > -18. && primTrkZs > 3. && primTrkZs < 87.)"
  hitExtraCutsInduct = "*(primTrkXsInduct > 3. && primTrkXsInduct < 46. && primTrkYsInduct < 18. && primTrkYsInduct > -18. && primTrkZsInduct > 3. && primTrkZsInduct < 87.)"
  #hitExtraCuts += "*((primTrkStartPhi >= 0 && primTrkPitches >= 0.45 && primTrkPitches < 0.47) || (primTrkStartPhi < 0 && primTrkPitches >= 0.68 && primTrkPitches < 0.70))" #small pitch region

  weightStr = "1"+cuts
  logy = True
  scaleFactor = 0.066

  c = root.TCanvas()
  NMAX=1000000000
  #NMAX=100

  lifetimeGraph = getLifetimeGraphs()
  lifetimeGraph.SetMarkerSize(0.7)
  lifetimeGraph.SetLineWidth(1)
  lifetimeGraphs = [lifetimeGraph]

  ########################################################
  ## File Definitions ####################################
  ########################################################

  baseDir="/scratch/jhugon/"
  baseDir=""

  fileConfigs = [
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_RIIP60_64a_v02.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP60_64b_v02.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP60_64c_v02.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64a_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64b_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64c_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64d_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64e_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64f_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64g_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM20_64abc.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64a.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64b.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64c.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64d.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64e.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64f.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64g.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64a.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64b.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64c.root"],
    #  'name': "RunII",
    #  'title': "Run II",
    #  'caption': "Run II",
    #  'color': root.kBlack,
    #  'isData': True,
    #},
    {
      'fn': [
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_a_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_b_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_c_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_d_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_e_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_f_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_g_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_a_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_b_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_c_cosmics_nocorrections.root",
             baseDir+"cosmicData/CosmicAna_RIIM20_64abc_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64a_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64b_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64c_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64d_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64e_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64f_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM60_64g_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM100_64a_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM100_64b_nocrct.root",
             baseDir+"cosmicData/CosmicAna_RIIM100_64c_nocrct.root"],
      'name': "RunIINocrct",
      'title': "Uncorrected Run II",
      'caption': "Uncorrected Run II",
      'color': root.kGray+2,
      'isData': True,
    },
    {
      'fn': [baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_a_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_b_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_c_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_a_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_b_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_c_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_d_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_e_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_f_cosmics.root",
             baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current100_secondary64_g_cosmics.root"],
      'name': "RunIIPos",
      'title': "Run II Positive Polarity",
      'caption': "Run II Positive Polarity",
      'color': root.kBlack,
      'isData': True,
    },
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_RIIM20_64abc.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64a.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64b.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64c.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64d.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64e.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64f.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64g.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64a.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64b.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64c.root"],
    #  'name': "RunIINeg",
    #  'title': "Run II Negative Polarity",
    #  'caption': "Run II Negative Polarity",
    #  'color': root.kGreen+3,
    #  'isData': True,
    #},
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_RIIM20_64abc_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64a_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64b_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64c_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64d_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64e_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64f_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM60_64g_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64a_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64b_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIM100_64c_nocrct.root"],
    #  'name': "RunIINegNocrct",
    #  'title': "Uncorrected Run II Negative Polarity",
    #  'caption': "Uncorrected Run II Negative Polarity",
    #  'color': root.kRed-4,
    #  'isData': True,
    #},
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_RIIP60_64a_v02_v2_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP60_64b_v02_v2_nocrct.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP60_64c_v02_v2_nocrct.root"],
    #  'name': "RunIIP60Uncorr",
    #  'title': "Run II+ 60 A Uncorrected",
    #  'caption': "Run II+ 60 A Uncorrected",
    #  'color': root.kGray+2,
    #  'isData': True,
    #},
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_a_cosmics.root",
    #         baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_b_cosmics.root",
    #         baseDir+"cosmicData/CosmicAna_data_Pos_RunII_current60_secondary64_c_cosmics.root"],
    #  'name': "RunIIP60",
    #  'title': "Run II+ 60 A",
    #  'caption': "Run II+ 60 A",
    #  'color': root.kGray+2,
    #  'isData': True,
    #},
    #{
    #  'fn': [baseDir+"cosmicData/CosmicAna_RIIP100_64a_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64b_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64c_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64d_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64e_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64f_v01.root",
    #         baseDir+"cosmicData/CosmicAna_RIIP100_64g_v01.root"],
    #  'name': "RunIIP100",
    #  'title': "Run II+ 100 A",
    #  'caption': "Run II+ 100 A",
    #  'color': root.kGray+2,
    #  'isData': True,
    #},
    {
      'fn': baseDir+"cosmicMC/cosmicAna_v04.root",
      'name': "CosmicMC",
      'title': "Cosmic MC",
      'caption': "Cosmic MC",
      'isData': False,
      'scaleFactor': scaleFactor,
    },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing10_v01.root",
 #     'name': "CosmicMC_presmear10perc",
 #     'title': "Cosmic MC Pre-smear 10% ",
 #     'caption': "Cosmic MC Pre-smear 10%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing20_v01.root",
 #     'name': "CosmicMC_presmear20perc",
 #     'title': "Cosmic MC Pre-smear 20% ",
 #     'caption': "Cosmic MC Pre-smear 20%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing30_v01.root",
 #     'name': "CosmicMC_presmear30perc",
 #     'title': "Cosmic MC Pre-smear 30% ",
 #     'caption': "Cosmic MC Pre-smear 30%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing40_v01.root",
 #     'name': "CosmicMC_presmear40perc",
 #     'title': "Cosmic MC Pre-smear 40% ",
 #     'caption': "Cosmic MC Pre-smear 40%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing45_v01.root",
 #     'name': "CosmicMC_presmear45perc",
 #     'title': "Cosmic MC Pre-smear 45% ",
 #     'caption': "Cosmic MC Pre-smear 45%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing50_v01.root",
 #     'name': "CosmicMC_presmear50perc",
 #     'title': "Cosmic MC Pre-smear 50% ",
 #     'caption': "Cosmic MC Pre-smear 50%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing55_v01.root",
 #     'name': "CosmicMC_presmear55perc",
 #     'title': "Cosmic MC Pre-smear 55% ",
 #     'caption': "Cosmic MC Pre-smear 55%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing60_v01.root",
 #     'name': "CosmicMC_presmear60perc",
 #     'title': "Cosmic MC Pre-smear 60% ",
 #     'caption': "Cosmic MC Pre-smear 60%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
 #   {
 #     'fn': baseDir+"cosmicMC/cosmicAna_smearing70_v01.root",
 #     'name': "CosmicMC_presmear70perc",
 #     'title': "Cosmic MC Pre-smear 70% ",
 #     'caption': "Cosmic MC Pre-smear 70%",
 #     'isData': False,
 #     'scaleFactor': scaleFactor,
 #   },
  ]

  for i in range(len(fileConfigs)):
    if not ('isData' in fileConfigs[i]) or not fileConfigs[i]['isData']:
        fileConfigs[i]['color'] = COLORLIST[i-1]

  ########################################################
  ## Compare Files #######################################
  ########################################################

  histConfigs = [
    {
      'name': "primTrkHitAmpsCollection",
      'xtitle': "Collection Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitAmpsInduction",
      'xtitle': "Induction Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsCollection",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsInduction",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitAmpsCollection_phiLt0",
      'xtitle': "Collection Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitAmpsInduction_phiLt0",
      'xtitle': "Induction Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsCollection_phiLt0",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsInduction_phiLt0",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitAmpsCollection_phiGeq0",
      'xtitle': "Collection Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitAmpsInduction_phiGeq0",
      'xtitle': "Induction Plane Hit Amplitudes [ADC]",
      'ytitle': "Hits / bin",
      'binning': [150,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsCollection_phiGeq0",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkHitIntsInduction_phiGeq0",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
#    {
#      'name': "trackXFront",
#      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [50,0,50],
#      'var': "trackXFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackYFront",
#      'xtitle': "Y of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [50,-50,50],
#      'var': "trackYFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackMatchLowestZ",
#      'xtitle': "TPC Track Start Z [cm]",
#      'ytitle': "TPC Tracks / bin",
#      'binning': [40,0,20],
#      'var': "trackMatchLowestZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "nTOFs",
#      'xtitle': "Number of TOF Objects",
#      'ytitle': "Events / bin",
#      'binning': [11,0,10],
#      'var': "nTOFs",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartX",
#      'xtitle': "TPC Track Start X [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,60],
#      'var': "trackStartX",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartY",
#      'xtitle': "TPC Track Start Y [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-50,50],
#      'var': "trackStartY",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackStartZ",
#      'xtitle': "TPC Track Start Z [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,110],
#      'var': "trackStartZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndX",
#      'xtitle': "TPC Track End X [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,60],
#      'var': "trackEndX",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndY",
#      'xtitle': "TPC Track End Y [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-50,50],
#      'var': "trackEndY",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackEndZ",
#      'xtitle': "TPC Track End Z [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-20,110],
#      'var': "trackEndZ",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "trackLength",
#      'xtitle': "TPC Track Length [cm]",
#      'ytitle': "Tracks / bin",
#      'binning': [100,-10,100],
#      'var': "trackLength",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logy': logy,
#    },
    #{
    #  'name': "trackCaloKin",
    #  'xtitle': "TPC Calo Estimate of KE [MeV]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [50,0,2500],
    #  'var': "trackCaloKin",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "primTrkLength",
      'xtitle': "Primary TPC Track Length [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,100],
      'var': "primTrkLength",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "primTrkStartTheta",
      'xtitle': "Primary TPC Track #theta [deg]",
      'ytitle': "Events / bin",
      'binning': [180,0,180],
      'var': "primTrkStartTheta*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartTheta_phiGeq0",
      'xtitle': "Primary TPC Track #theta [deg]",
      'ytitle': "Events / bin",
      'binning': [120,0,60],
      'var': "primTrkStartTheta*180/pi",
      'cuts': weightStr+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkStartTheta_phiLt0",
      'xtitle': "Primary TPC Track #theta [deg]",
      'ytitle': "Events / bin",
      'binning': [120,0,60],
      'var': "primTrkStartTheta*180/pi",
      'cuts': weightStr+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkStartCosTheta",
      'xtitle': "Primary TPC Track cos(#theta)",
      'ytitle': "Events / bin",
      'binning': [100,0,1],
      'var': "cos(primTrkStartTheta)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Events / bin",
      'binning': [180,-180,180],
      'var': "primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartThetaY",
      'xtitle': "Primary TPC Track #theta_{y} [deg]",
      'ytitle': "Events / bin",
      'binning': [180,0,180],
      'var': "acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartCosThetaY",
      'xtitle': "Primary TPC Track cos(#theta_{y})",
      'ytitle': "Events / bin",
      'binning': [100,0,1],
      'var': "sin(primTrkStartTheta)*sin(primTrkStartPhi)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartPhiZX",
      'xtitle': "Primary TPC Track #phi_{zx} [deg]",
      'ytitle': "Events / bin",
      'binning': [180,-180,180],
      'var': "atan2(sin(primTrkStartTheta)*cos(primTrkStartPhi),cos(primTrkStartTheta))*180./pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartThetaX",
      'xtitle': "Primary TPC Track #theta_{x} [deg]",
      'ytitle': "Events / bin",
      'binning': [180,0,180],
      'var': "acos(sin(primTrkStartTheta)*cos(primTrkStartPhi))*180./pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartCosThetaX",
      'xtitle': "Primary TPC Track cos(#theta_{x})",
      'ytitle': "Events / bin",
      'binning': [100,0,1],
      'var': "sin(primTrkStartTheta)*cos(primTrkStartPhi)",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkStartPhiZY",
      'xtitle': "Primary TPC Track #phi_{zy} [deg]",
      'ytitle': "Events / bin",
      'binning': [180,-180,180],
      'var': "atan2(sin(primTrkStartTheta)*sin(primTrkStartPhi),cos(primTrkStartTheta))*180./pi",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,50],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "primTrkdEdxsInduct",
      'xtitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,20],
      'var': "primTrkdEdxsInduct*((2.65-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct,
      #'normalize': True,
      'logy': logy,
      'printIntegral': True,
    },
    {
      'name': "primTrkdEdxs_zoom",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'normalize': not logy,
      'logy': logy,
    },
    {
      'name': "primTrkdEdxs_zoom2",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,10],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxs_zoom3",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxsInduct_zoom3",
      'xtitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [50,0,4],
      'var': "primTrkdEdxsInduct*((2.65-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct,
      #'normalize': True,
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiGeq0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiLt0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxsInduct_zoom3_phiGeq0",
      'xtitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxsInduct*((2.65-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdEdxsInduct_zoom3_phiLt0",
      'xtitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxsInduct*((2.65-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
#    {
#      'name': "primTrkTruedEdxs",
#      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,50],
#      'var': "primTrkTruedEdxs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedEdxs_zoom",
#      'xtitle': "Primary TPC Track True dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkTruedEdxs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': logy,
#    },
    {
      'name': "primTrkdQdxs",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [300,0,3e4],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts,
      'normalize': not logy,
      'logy': logy,
    },
    {
      'name': "primTrkdQdxsInduct",
      'xtitle': "Induction Plane -- Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [300,0,1e4],
      'var': "primTrkdQdxsInduct*((0.70-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct,
      'normalize': not logy,
      'logy': logy,
    },
    {
      'name': "primTrkdQdxs_zoom",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,8e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts,
      'normalize': not logy,
      'logy': logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkdQdxs_zoom2",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,8e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts,
      'normalize': logy,
      'logy': not logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkdQdxs_zoom3",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,5e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts,
      'normalize': logy,
      'logy': not logy,
      'printIntegral' : True,
    },
    {
      'name': "primTrkdQdxs_zoom3_phiGeq0",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdQdxs_zoom3_phiLt0",
      'xtitle': "Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdQdxsInduct_zoom3_phiGeq0",
      'xtitle': "Induct: Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [100,0,2e3],
      'var': "primTrkdQdxsInduct*((0.70-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi >= 0)",
      'caption': "Track #phi #geq 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdQdxsInduct_zoom3_phiLt0",
      'xtitle': "Induct: Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [100,0,2e3],
      'var': "primTrkdQdxsInduct*((0.70-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      'caption': "Track #phi < 0",
      'normalize': logy,
      'logy': not logy,
    },
    {
      'name': "primTrkdQs",
      'xtitle': "Primary TPC Track dQ [ADC]",
      'ytitle': "Normalized Hits / bin",
      'binning': [100,0,5e3],
      'var': "primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.)",
      'cuts': weightStr+hitExtraCuts,
      'normalize': logy,
      'logy': not logy,
      'printIntegral' : True,
    },
#    {
#      'name': "primTrkTruedQdxs",
#      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,5e6],
#      'var': "primTrkTruedQdxs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedQdxs_zoom",
#      'xtitle': "Primary TPC Track True dQ/dx [e^{-}/cm]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,1e5],
#      'var': "primTrkTruedQdxs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': logy,
#    },
#    {
#      'name': "primTrkTruedQs",
#      'xtitle': "Primary TPC Track Q [e^{-}]",
#      'ytitle': "Events / bin",
#      #'binning': [200,0,1e5],
#      'binning': getLogBins(100,1e3,1e7),
#      'var': "primTrkTruedQs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': logy,
#      'logx': True,
#    },
#    {
#      'name': "primTrkTruedQs2",
#      'xtitle': "Primary TPC Track Q [e^{-}]",
#      'ytitle': "Events / bin",
#      'binning': [200,0,2e5],
#      'var': "primTrkTruedQs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logy': not logy,
#      'logx': False,
#    },
#    {
#      'name': "primTrkdEdxs_Q1000to1500_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+hitExtraCuts+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 1500.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "1000 ADC < Q < 1500 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q1500to2000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+hitExtraCuts+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 1500. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 2000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "1500 ADC < Q < 2000 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q2000to3000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+hitExtraCuts+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 2000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 3000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "2000 ADC < Q < 3000 ADC",
#    },
#    {
#      'name': "primTrkdEdxs_Q3000to4000_zoom2",
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'cuts': weightStr+hitExtraCuts+"*(primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) > 3000. && primTrkdQdxs*primTrkPitches*((0.5-1.)*isMC + 1.) < 4000.)",
#      #'normalize': True,
#      'logy': not logy,
#      'caption': "3000 ADC < Q < 4000 ADC",
#    },
    #{
    #  'name': "primTrkdEdxsFidCut",
    #  'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
    #  'ytitle': "Events / bin",
    #  'binning': [200,0,50],
    #  'var': "primTrkdEdxs",
    #  'cuts': weightStr+hitExtraCuts+"*primTrkInFids",
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "primTrkResRanges",
      'xtitle': "Primary TPC Track Residual Range [cm]",
      'ytitle': "Hits / bin",
      'binning': [200,0,100],
      'var': "primTrkResRanges",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkResRangesInduct",
      'xtitle': "Induction Plane -- Primary TPC Track Residual Range [cm]",
      'ytitle': "Hits / bin",
      'binning': [200,0,100],
      'var': "primTrkResRangesInduct",
      'cuts': weightStr+hitExtraCutsInduct,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitches",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'var': "primTrkPitches",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitches_phiGeq0",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,2],
      'var': "primTrkPitches",
      'captionright1': "Track #phi #geq 0",
      'cuts': weightStr+hitExtraCuts +" * (primTrkStartPhi >= 0)",
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitches_phiLt0",
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,2],
      'var': "primTrkPitches",
      'captionright1': "Track #phi < 0",
      'cuts': weightStr+hitExtraCuts +" * (primTrkStartPhi < 0)",
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitchesInduct_phiGeq0",
      'xtitle': "Induction Plane -- Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,2],
      'var': "primTrkPitchesInduct",
      'captionright1': "Track #phi #geq 0",
      'cuts': weightStr+hitExtraCutsInduct +" * (primTrkStartPhi >= 0)",
      #'normalize': True,
      'logy': logy,
    },
    {
      'name': "primTrkPitchesInduct_phiLt0",
      'xtitle': "Induction Plane -- Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,2],
      'var': "primTrkPitchesInduct",
      'captionright1': "Track #phi < 0",
      'cuts': weightStr+hitExtraCutsInduct +" * (primTrkStartPhi < 0)",
      #'normalize': True,
      'logy': logy,
    },
    #{
    #  'name': "primTrkEndKin",
    #  'xtitle': "Primary TPC Track End Kinetic Energy [MeV]",
    #  'ytitle': "Events / bin",
    #  'binning': [50,0,1000],
    #  'var': "primTrkEndKin",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "primTrkEndKinFid",
    #  'xtitle': "Primary TPC Track End Kinetic Energy [MeV]",
    #  'ytitle': "Events / bin",
    #  'binning': [50,0,1000],
    #  'var': "primTrkEndKinFid",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueEndProcess",
    #  'xtitle': "trueEndProcess",
    #  'ytitle': "Events / bin",
    #  'binning': [17,0,17],
    #  'var': "trueEndProcess",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueStartTheta",
    #  'xtitle': "True Start #theta [deg]",
    #  'binning': [90,0,180],
    #  'var': "trueStartTheta*180/pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #},
    #{
    #  'name': "trueStartPhi",
    #  'xtitle': "True Start #phi",
    #  'binning': [90,-180,180],
    #  'var': "trueStartPhi*180/pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #},
    #{
    #  'name': "trueStartThetaY",
    #  'xtitle': "True Start #theta_{y} [deg]",
    #  'ytitle': "Events / bin",
    #  'binning': [180,0,180],
    #  'var': "acos(sin(trueStartTheta)*sin(trueStartPhi))*180./pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueStartPhiZX",
    #  'xtitle': "True Start #theta_{zx} [deg]",
    #  'ytitle': "Events / bin",
    #  'binning': [180,-180,180],
    #  'var': "atan2(sin(trueStartTheta)*cos(trueStartPhi),cos(trueStartTheta))*180./pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueStartThetaX",
    #  'xtitle': "True Start #theta_{x} [deg]",
    #  'ytitle': "Events / bin",
    #  'binning': [180,0,180],
    #  'var': "acos(sin(trueStartTheta)*cos(trueStartPhi))*180./pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    #{
    #  'name': "trueStartPhiZY",
    #  'xtitle': "True Start #theta_{zy} [deg]",
    #  'ytitle': "Events / bin",
    #  'binning': [180,-180,180],
    #  'var': "atan2(sin(trueStartTheta)*sin(trueStartPhi),cos(trueStartTheta))*180./pi",
    #  'cuts': weightStr,
    #  #'normalize': True,
    #  'logy': logy,
    #},
    {
      'name': "trueStartE",
      'xtitle': "Muon True Initial Momentum [GeV]",
      'ytitle': "Events / bin",
      'binning': [100,0,300],
      'var': "1e-3*trueStartE",
      'cuts': weightStr,
      #'normalize': True,
      'logy': logy,
      #'printIntegral': True,
    },
    {
      'name': "trueStartE_zoom",
      'xtitle': "Muon True Initial Momentum [GeV]",
      'ytitle': "Events / bin",
      'binning': [40,0,10],
      'var': "1e-3*trueStartE",
      'cuts': weightStr,
      #'normalize': True,
      'logy': False,
      #'printIntegral': True,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
#  fileConfigMCs = copy.deepcopy(fileConfigs)
#  fileConfigData = None
#  for i in reversed(range(len(fileConfigMCs))):
#    if 'isData' in fileConfigMCs[i] and fileConfigMCs[i]['isData']:
#      fileConfigData = fileConfigMCs.pop(i)
#  DataMCStack(fileConfigData,fileConfigMCs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX)

  ########################################################
  ## Single Hists -- All Samples #########################
  ########################################################

  histConfigs = [
    {
      'name': "primTrkHitAmpsVIntsCollection",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Collection Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.):primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)",
      'logz': True,
    },
    {
      'name': "primTrkHitAmpsVIntsInduction",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Induction Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.):primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)",
      'logz': True,
    },
    {
      'name': "primTrkHitAmpsVIntsCollection_phiLt0",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Collection Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.):primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'captionleft1': "Track #phi < 0",
      'logz': True,
    },
    {
      'name': "primTrkHitAmpsVIntsInduction_phiLt0",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Induction Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.):primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi < 0)",
      'captionleft1': "Track #phi < 0",
      'logz': True,
    },
    {
      'name': "primTrkHitAmpsVIntsCollection_phiGeq0",
      'xtitle': "Collection Plane Hit Integrals [ADC us]",
      'ytitle': "Collection Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.62-1.)*isMC + 1.):primTrkHitIntegrals*((0.67-1.)*isMC + 1.)",
      'cuts': weightStr+"*(primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'captionleft1': "Track #phi #geq 0",
      'logz': True,
    },
    {
      'name': "primTrkHitAmpsVIntsInduction_phiGeq0",
      'xtitle': "Induction Plane Hit Integrals [ADC us]",
      'ytitle': "Induction Plane Hit Amplitudes [ADC]",
      'binning': [50,0,5e3,50,0,150],
      'var': "primTrkHitAmps*((0.47-1.)*isMC + 1.):primTrkHitIntegrals*((0.52-1.)*isMC + 1.)",
      'cuts': weightStr+"*(!primTrkHitIsCollections)"+"*(primTrkStartPhi >= 0)",
      'captionleft1': "Track #phi #geq 0",
      'logz': True,
    },
    {
      'name': "primTrkdEdxs_zoom3",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiGeq0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxs_zoom3_phiLt0",
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,5],
      'var': "primTrkdEdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
#    {
#      'name': "primTrkdEdxVRange",
#      'xtitle': "Primary Track Hit Residual Range [cm]",
#      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
#      'binning': [100,0,100,100,0,50],
#      'var': "primTrkdEdxs:primTrkResRanges",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkdEdxVRangeFidCut",
#      'xtitle': "Primary Track Hit Residual Range [cm]",
#      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
#      'binning': [100,0,100,100,0,50],
#      'var': "primTrkdEdxs:primTrkResRanges",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "trackYFrontVtrackXFront",
#      'xtitle': "X of TPC Track Projection to TPC Front [cm]",
#      'ytitle': "Y of TPC Track Projection to TPC Front [cm]",
#      'binning': [40,0,40,40,-20,20],
#      'var': "trackYFront:trackXFront",
#      'cuts': weightStr,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVyFromCenter",
#      'xtitle': "Hit |y| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,25,200,0,20],
#      'var': "primTrkdEdxs:fabs(primTrkYs)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVzFromCenter",
#      'xtitle': "Hit |z-45| [cm]",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [40,0,50,200,0,20],
#      'var': "primTrkdEdxs:fabs(primTrkZs-45.)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "hitYVhitX",
#      'xtitle': "Hit x [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [60,-5,55,60,-30,30],
#      'var': "primTrkYs:primTrkXs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitYVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit y [cm]",
#      'binning': [120,-10,110,60,-30,30],
#      'var': "primTrkYs:primTrkZs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "hitXVhitZ",
#      'xtitle': "Hit z [cm]",
#      'ytitle': "Hit x [cm]",
#      'binning': [120,-10,110,60,-5,55],
#      'var': "primTrkXs:primTrkZs",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      #'logz': True,
#    },
#    {
#      'name': "trueStartThetaVtrueStartPhi",
#      'xtitle': "True Start #phi [deg]",
#      'ytitle': "True Start #theta [deg]",
#      'binning': [90,-180,180,90,0,180],
#      'var': "trueStartTheta*180/pi:trueStartPhi*180/pi",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "trueStartThetaYVtrueStartPhiZX",
#      'xtitle': "True Start #phi_{zx} [deg]",
#      'ytitle': "True Start #theta_{y} [deg]",
#      'binning': [90,-180,180,90,0,180],
#      'var': "acos(sin(trueStartTheta)*sin(trueStartPhi))*180/pi:atan2(sin(trueStartTheta)*cos(trueStartPhi),cos(trueStartTheta))*180./pi",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "trueStartThetaXVtrueStartPhiZY",
#      'xtitle': "True Start #phi_{zy} [deg]",
#      'ytitle': "True Start #theta_{x} [deg]",
#      'binning': [90,-180,180,90,0,180],
#      'var': "acos(sin(trueStartTheta)*cos(trueStartPhi))*180/pi:atan2(sin(trueStartTheta)*sin(trueStartPhi),cos(trueStartTheta))*180./pi",
#      'cuts': weightStr,
#      #'normalize': True,
#      'logz': False,
#    },
  ]

  hists = plotOneHistOnePlot(fileConfigs,histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
  outfile = root.TFile("cosmics_hists.root","recreate")
  outfile.cd()
  for var in hists:
    for ds in hists[var]:
        newname = var+"_"+ds
        hist = hists[var][ds]
        hist.SetName(newname)
        hist.Print()
        hist.Write()

  ########################################################
  ## Single Hists -- Not Smear Samples ###################
  ########################################################

  histConfigs = [
    {
      'name': "primTrkStartThetaVPhi",
      'xtitle': "Primary TPC Track #phi [deg]",
      'ytitle': "Primary TPC Track #theta [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "primTrkStartTheta*180/pi:primTrkStartPhi*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkStartThetaYVprimTrkStartPhiZX",
      'xtitle': "Primary TPC Track #phi_{zx} [deg]",
      'ytitle': "Primary TPC Track #theta_{y} [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180/pi:atan2(sin(primTrkStartTheta)*cos(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logz': False,
    },
    {
      'name': "primTrkStartThetaYVprimTrkStartPhiZX_Zoom",
      'xtitle': "Primary TPC Track #phi_{zx} [deg]",
      'ytitle': "Primary TPC Track #theta_{y} [deg]",
      'binning': [45,0,45,80,50,130],
      'var': "acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180/pi:atan2(sin(primTrkStartTheta)*cos(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logz': False,
    },
    {
      'name': "primTrkStartThetaXVprimTrkStartPhiZY",
      'xtitle': "Primary TPC Track #phi_{zy} [deg]",
      'ytitle': "Primary TPC Track #theta_{x} [deg]",
      'binning': [90,-180,180,90,0,180],
      'var': "acos(sin(primTrkStartTheta)*cos(primTrkStartPhi))*180/pi:atan2(sin(primTrkStartTheta)*sin(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
      'cuts': weightStr,
      #'normalize': True,
      'logz': False,
    },
    {
      'name': "primTrkdEdxsVx",
      'xtitle': "Hit x [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,0,50,200,0,20],
      'var': "primTrkdEdxs:primTrkXs",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVy",
      'xtitle': "Hit y [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,200,0,20],
      'var': "primTrkdEdxs:primTrkYs",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVz",
      'xtitle': "Hit z [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,-5,95,200,0,20],
      'var': "primTrkdEdxs:primTrkZs",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVx_phiGeq0",
      'xtitle': "Hit x [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,0,50,200,0,20],
      'var': "primTrkdEdxs:primTrkXs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVy_phiGeq0",
      'xtitle': "Hit y [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,200,0,20],
      'var': "primTrkdEdxs:primTrkYs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsInductVy_phiGeq0",
      'xtitle': "Hit y [cm]",
      'ytitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,100,0,10],
      'var': "primTrkdEdxsInduct:primTrkYsInduct",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVz_phiGeq0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,-5,95,200,0,20],
      'var': "primTrkdEdxs:primTrkZs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVx_phiLt0",
      'xtitle': "Hit x [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,0,50,200,0,20],
      'var': "primTrkdEdxs:primTrkXs",
      'captionright1': "Track #phi < 0",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsInductVx_phiLt0",
      'xtitle': "Hit x [cm]",
      'ytitle': "Induct: Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,0,50,100,0,10],
      'var': "primTrkdEdxsInduct:primTrkXsInduct",
      'captionright1': "Track #phi < 0",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVy_phiLt0",
      'xtitle': "Hit y [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,200,0,20],
      'var': "primTrkdEdxs:primTrkYs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'captionright1': "Track #phi < 0",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsInductVy_phiLt0",
      'xtitle': "Hit y [cm]",
      'ytitle': "Induct: Primary TPC Track dE/dx [MeV/cm]",
      'binning': [20,-25,25,100,0,10],
      'var': "primTrkdEdxsInduct:primTrkYsInduct",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      'captionright1': "Track #phi < 0",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVz_phiLt0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [50,-5,95,200,0,20],
      'var': "primTrkdEdxs:primTrkZs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'captionright1': "Track #phi < 0",
      #'normalize': True,
      'logz': True,
    },
  ]

  hists = plotOneHistOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],
                histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
  outfile.cd()
  for var in hists:
    for ds in hists[var]:
        newname = var+"_"+ds
        hist = hists[var][ds]
        hist.SetName(newname)
        hist.Print()
        hist.Write()

  ########################################################
  ## Single Hists -- Data Only ###########################
  ########################################################

  histConfigs = [
    {
      'name': "primTrkdQdxs",
      'xtitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,1e4],
      'var': "primTrkdQdxs",
      'cuts': weightStr+hitExtraCuts,
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxs_phiGeq0",
      'xtitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,1e4],
      'var': "primTrkdQdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxs_phiLt0",
      'xtitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'ytitle': "Hits / bin",
      'binning': [100,0,1e4],
      'var': "primTrkdQdxs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQs",
      'xtitle': "Primary TPC Track dQ [ADC ns]",
      'ytitle': "Hits / bin",
      'binning': [200,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches",
      'cuts': weightStr+hitExtraCuts,
      'writeImage': False,
    },
    {
      'name': "primTrkdQs_phiGeq0",
      'xtitle': "Primary TPC Track dQ [ADC ns]",
      'ytitle': "Hits / bin",
      'binning': [200,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQs_phiLt0",
      'xtitle': "Primary TPC Track dQ [ADC ns]",
      'ytitle': "Hits / bin",
      'binning': [200,0,8e3],
      'var': "primTrkdQdxs*primTrkPitches",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkStartPhiVrun",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track #phi [deg]",
      'binning': [1400,8200,9600,45,-180,180],
      'var': "primTrkStartPhi*180/pi:runNumber",
      'cuts': weightStr,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVrun",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [1400,8200,9600,200,0,20],
      'var': "primTrkdEdxs:runNumber",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsVrun_phiGeq0",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [1400,8200,9600,200,0,20],
      'var': "primTrkdEdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxsVrun_phiLt0",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
      'binning': [1400,8200,9600,200,0,20],
      'var': "primTrkdEdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxsInductVrun_phiGeq0",
      'xtitle': "Run Number",
      'ytitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'binning': [1400,8200,9600,100,0,10],
      'var': "primTrkdEdxsInduct:runNumber",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxsInductVrun_phiLt0",
      'xtitle': "Run Number",
      'ytitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'binning': [1400,8200,9600,100,0,10],
      'var': "primTrkdEdxsInduct:runNumber",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxVwire",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkdEdxVwire_phiGeq0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      #'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxVwire_phiLt0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      #'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxInductVwire_phiGeq0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Induction: Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxsInduct:primTrkTrueWiresInduct",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdEdxInductVwire_phiLt0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Induction: Primary Track Hit dE/dx [MeV/cm]",
      'binning': [240,0,240,100,0,10],
      'var': "primTrkdEdxsInduct:primTrkTrueWiresInduct",
      'cuts': weightStr+hitExtraCutsInduct+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdQdxsVrun",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'binning': [1400,8200,9600,100,0,1e4],
      'var': "primTrkdQdxs:runNumber",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      'logz': True,
      'graphs': lifetimeGraphs,
    },
    {
      'name': "primTrkdQdxsVrun_phiGeq0",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'binning': [1400,8200,9600,100,0,1e4],
      'var': "primTrkdQdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxsVrun_phiLt0",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'binning': [1400,8200,9600,100,0,1e4],
      'var': "primTrkdQdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxsVrun_phiLt0_xLt10",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'binning': [1400,8200,9600,100,0,1e4],
      'var': "primTrkdQdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)*(primTrkXs < 10)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdQdxsVrun_phiLt0_xGeq30",
      'xtitle': "Run Number",
      'ytitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'binning': [1400,8200,9600,100,0,1e4],
      'var': "primTrkdQdxs:runNumber",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)*(primTrkXs >= 30)",
      #'normalize': True,
      'logz': True,
    },
    {
      'name': "primTrkdQdxVwire",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dQ/dx [ADC ns / cm]",
      'binning': [240,0,240,100,0,1e4],
      'var': "primTrkdQdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts,
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "primTrkdQdxVwire_phiGeq0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dQ/dx [ADC ns / cm]",
      'binning': [240,0,240,100,0,1e4],
      'var': "primTrkdQdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      #'normalize': True,
      #'logz': True,
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxVwire_phiLt0",
      'xtitle': "Primary Track Hit Wire Number",
      'ytitle': "Primary Track Hit dQ/dx [ADC ns / cm]",
      'binning': [240,0,240,100,0,1e4],
      'var': "primTrkdQdxs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      #'normalize': True,
      #'logz': True,
      'writeImage': False,
    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartCosTheta",
#      'xtitle': "Primary TPC Track cos(#theta)",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,0,1,10000,0,50],
#      'var': "primTrkdEdxs:cos(primTrkStartTheta)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartPhi",
#      'xtitle': "Primary TPC Track #phi",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [30,-180,180,10000,0,50],
#      'var': "primTrkdEdxs:primTrkStartPhi*180/pi",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartCosThetaX",
#      'xtitle': "Primary TPC Track cos(#theta_{x})",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,0,1,10000,0,50],
#      'var': "primTrkdEdxs:sin(primTrkStartTheta)*cos(primTrkStartPhi)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartCosThetaX_zoom",
#      'xtitle': "Primary TPC Track cos(#theta_{x})",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,0,1,100,0,5],
#      'var': "primTrkdEdxs:sin(primTrkStartTheta)*cos(primTrkStartPhi)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartPhiZY",
#      'xtitle': "Primary TPC Track #phi_{zy}",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [60,-180,180,10000,0,50],
#      'var': "primTrkdEdxs:atan2(sin(primTrkStartTheta)*sin(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartPhiZY_zoom",
#      'xtitle': "Primary TPC Track #phi_{zy}",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [60,-180,180,100,0,5],
#      'var': "primTrkdEdxs:atan2(sin(primTrkStartTheta)*sin(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': False,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartPhiZY_zoom_logy",
#      'xtitle': "Primary TPC Track #phi_{zy}",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [60,-180,180,100,0,5],
#      'var': "primTrkdEdxs:atan2(sin(primTrkStartTheta)*sin(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartCosThetaY",
#      'xtitle': "Primary TPC Track cos(#theta_{y})",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [50,0,1,10000,0,50],
#      'var': "primTrkdEdxs:sin(primTrkStartTheta)*sin(primTrkStartPhi)",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
#    {
#      'name': "primTrkdEdxsVprimTrkStartPhiZX",
#      'xtitle': "Primary TPC Track #phi_{zx}",
#      'ytitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'binning': [30,-180,180,10000,0,50],
#      'var': "primTrkdEdxs:atan2(sin(primTrkStartTheta)*cos(primTrkStartPhi),cos(primTrkStartTheta))*180/pi",
#      'cuts': weightStr+hitExtraCuts,
#      #'normalize': True,
#      'logz': True,
#    },
    {
      'name': "primTrkdEdxsVHitWireAndHitY_phiLt0",
      'xtitle': "Hit Wire Number",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx [MeV/cm]",
      'binning': [240,0,240,10,-25,25,50,0,5],
      'var': "primTrkdEdxs:primTrkYs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxsVHitWireAndHitY_phiGeq0",
      'xtitle': "Hit Wire Number",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx [MeV/cm]",
      'binning': [240,0,240,10,-25,25,50,0,5],
      'var': "primTrkdEdxs:primTrkYs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxsVHitWireAndHitY_phiLt0",
      'xtitle': "Hit Wire Number",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx dQ/dx [ADC ns / cm]",
      'binning': [240,0,240,10,-25,25,50,0,1e4],
      'var': "primTrkdQdxs:primTrkYs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxsVHitWireAndHitY_phiGeq0",
      'xtitle': "Hit Wire Number",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx dQ/dx [ADC ns / cm]",
      'binning': [240,0,240,10,-25,25,50,0,1e4],
      'var': "primTrkdQdxs:primTrkYs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdQdxsVrunAndHitX_phiLt0",
      'xtitle': "Run Number",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx dQ/dx [ADC ns / cm]",
      'binning': [20,8200,9600,20,-5,55,50,0,1e4],
      'var': "primTrkdQdxs:primTrkXs:primTrkTrueWires",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxsVHitZAndHitY_phiLt0",
      'xtitle': "Hit z position [cm]",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx [MeV/cm]",
      'binning': [60,3,87,60,-18,18,50,0,5],
      'var': "primTrkdEdxs:primTrkYs:primTrkZs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi < 0)",
      'writeImage': False,
    },
    {
      'name': "primTrkdEdxsVHitZAndHitY_phiGeq0",
      'xtitle': "Hit z position [cm]",
      'ytitle': "Hit y position [cm]",
      'ztitle': "dE/dx [MeV/cm]",
      'binning': [60,3,87,60,-18,18,50,0,5],
      'var': "primTrkdEdxs:primTrkYs:primTrkZs",
      'cuts': weightStr+hitExtraCuts+"*(primTrkStartPhi >= 0)",
      'writeImage': False,
    },
  ]

  hists = plotOneHistOnePlot([x for x in fileConfigs if x["isData"]],
                histConfigs,c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_")
  outfile.cd()
  for var in hists:
    for ds in hists[var]:
        newname = var+"_"+ds
        hist = hists[var][ds]
        hist.SetName(newname)
        hist.Print()
        hist.Write()
  outfile.Close()

  ######################################################################################
  ## Compare Cuts -- True Paddle Hits ##################################################
  ######################################################################################

#  histConfigs = [
#    {
#      'title': "All",
#      'cuts': "( iBestMatch >= 0)",
#    },
#    {
#      'title': "Hit Cosmic 1",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic1",
#    },
#    {
#      'title': "Hit Cosmic 2",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic2",
#    },
#    {
#      'title': "Hit Cosmic 3",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic3",
#    },
#    {
#      'title': "Hit Cosmic 4",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic4",
#    },
#    {
#      'title': "Hit Cosmic 1 & 2",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic1*trueHitCosmic2",
#    },
#    {
#      'title': "Hit Cosmic 3 & 4",
#      'cuts': "( iBestMatch >= 0)*trueHitCosmic3*trueHitCosmic4",
#    },
#  ]
#  for i in range(len(histConfigs)):
#    histConfigs[i]["color"] = COLORLIST[i]
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Muon True Initial Energy [GeV]",
#        'ytitle': "Events / bin",
#        'binning': [100,0,300],
#        'var': "1e-3*trueStartE",
#        #'normalize': True,
#        'logy': logy,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_trueStartE")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Muon True Initial Energy [MeV]",
#        'ytitle': "Events / bin",
#        'binning': [10,0,2000],
#        'var': "trueStartE",
#        'normalize': False,
#        'logy': False,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs[1:],
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_trueStartE_zoom2")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Muon True Initial Energy [GeV]",
#        'ytitle': "Events / bin",
#        'binning': [40,0,10],
#        'var': "1e-3*trueStartE",
#        'normalize': False,
#        'logy': False,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs[1:],
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_trueStartE_zoom")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Muon True Initial Energy [MeV]",
#        'ytitle': "Events / bin",
#        'binning': [40,0,10],
#        'var': "1e-3*trueStartE",
#        'normalize': False,
#        'logy': True,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_trueStartE_zoom_logy")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Muon True Initial Energy [MeV]",
#        'ytitle': "Normalized events / bin",
#        'binning': [40,0,10],
#        'var': "1e-3*trueStartE",
#        'normalize': True,
#        'logy': False,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_trueStartE_zoom_norm")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Primary TPC Track #phi_{zx} [deg]",
#        'ytitle': "Events / bin",
#        'binning': [90,-180,180],
#        'var': "atan2(sin(primTrkStartTheta)*cos(primTrkStartPhi),cos(primTrkStartTheta))*180./pi",
#        #'normalize': True,
#        'logy': logy,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_primTrkStartPhiZX")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Primary TPC Track #theta_{y} [deg]",
#        'ytitle': "Events / bin",
#        'binning': [90,0,180],
#        'var': "acos(sin(primTrkStartTheta)*sin(primTrkStartPhi))*180./pi",
#        #'normalize': True,
#        'logy': logy,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_primTrkStartThetaY")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [100,0,10],
#      'var': "primTrkdEdxs",
#      'normalize': False,
#      'logy': True,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_primTrkdEdxs_zoom")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Events / bin",
#      'binning': [50,0,5],
#      'var': "primTrkdEdxs",
#      'normalize': True,
#      'logy': False,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_paddles_primTrkdEdxs_zoom3")


  ######################################################################################
  ## Compare Cuts -- Trigger Bits ######################################################
  ######################################################################################

#  histConfigs = [
#    {
#      'title': "All",
#      'cuts': "( iBestMatch >= 0)",
#    },
#    #{
#    #  'title': "!Trigger Bit 12",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 12) & 1))",
#    #},
#    #{
#    #  'title': "!Trigger Bit 13",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 13) & 1))",
#    #},
#    #{
#    #  'title': "!Trigger Bit 14",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 14) & 1))",
#    #},
#    #{
#    #  'title': "!Trigger Bit 4",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 4) & 1))",
#    #},
#    #{
#    #  'title': "!Trigger Bit 9",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 9) & 1))",
#    #},
#    #{
#    #  'title': "!Trigger Bit 10",
#    #  'cuts': "( iBestMatch >= 0) && (!((triggerBits >> 10) & 1))",
#    #},
#    {
#      'title': "Trigger Bit 10",
#      'cuts': "( iBestMatch >= 0) && ( ((triggerBits >> 10) & 1))",
#    },
#  ]
#  for i in range(len(histConfigs)):
#    histConfigs[i]["color"] = COLORLIST[i]
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#        'xtitle': "Primary TPC Track #phi [deg]",
#        'ytitle': "Events / bin",
#        'binning': [60,-180,180],
#        'var': "primTrkStartPhi*180./pi",
#        'logy': logy,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_triggers_primTrkStartPhi")


  ######################################################################################
  ## Compare Cuts -- Position ##########################################################
  ######################################################################################

  histConfigs = [
    {
      'title': "All",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1)",
    },
    {
      'title': " 40 cm < x < 45 cm",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) && (primTrkXs > 40 && primTrkXs < 45)",
    },
    {
      'title': "x > 45 cm",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) && (primTrkXs > 45)",
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'normalize': True,
      'logy': False,
      },
    )
#  plotManyHistsOnePlot([x for x in fileConfigs if x["isData"]],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_regions_primTrkdEdxs_zoom3")

  ######################################################################################
  ## Compare Cuts -- Phi >= or < 0 #####################################################
  ######################################################################################

  histConfigs = [
    {
      'title': "Track #phi #geq 0",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi >= 0)",
    },
    {
      'title': "Track #phi < 0",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi < 0)",
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]

  for i in range(len(histConfigs)):
    histConfigs[i].update(
    {
      'xtitle': "Primary TPC Track Length [cm]",
      'ytitle': "Events / bin",
      'binning': [40,0,120],
      'var': "primTrkLength",
      'normalize': True,
      'logy': False,
    },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkLength")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'normalize': True,
      'logy': False,
      },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkdEdxs_zoom3")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track dQ/dx [ADC ns / cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,10e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)",
      'normalize': True,
      'logy': False,
      },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkdQdxs_zoom")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track dQ [ADC ns]",
      'ytitle': "Events / bin",
      'binning': [200,0,8e3],
      'var': "primTrkdQdxs*((0.5-1.)*isMC + 1.)*primTrkPitches",
      'normalize': True,
      'logy': False,
      },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkdQs_zoom")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Hits / bin",
      'binning': [200,0,2],
      'var': "primTrkPitches",
      'normalize': False,
      'logy': True,
      },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkPitches_logy")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track Pitch [cm]",
      'ytitle': "Normalized hits / bin",
      'binning': [200,0,2],
      'var': "primTrkPitches",
      'normalize': True,
      'logy': False,
      },
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkPitches")

  histConfigs = [
    {
      'title': "Track #phi #geq 0",
      'cuts': weightStr+hitExtraCutsInduct+" * (primTrkStartPhi >= 0)",
    },
    {
      'title': "Track #phi < 0",
      'cuts': weightStr+hitExtraCutsInduct+" * (primTrkStartPhi < 0)",
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]

  for i in range(len(histConfigs)):
    histConfigs[i].update(
    {
      'xtitle': "Induction: Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Hits / bin",
      'binning': [50,0,4],
      'var': "primTrkdEdxsInduct*((2.65-1.)*isMC + 1.)",
      'normalize': True,
      'logy': False,
    }
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkdEdxsInduct_zoom3")

  for i in range(len(histConfigs)):
    histConfigs[i].update(
    {
      'xtitle': "Induction: Primary TPC Track dQ/dx [ADC/cm]",
      'ytitle': "Events / bin",
      'binning': [100,0,2e3],
      'var': "primTrkdQdxsInduct*((0.70-1.)*isMC + 1.)",
      'normalize': True,
      'logy': False,
    }
    )
  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhi_primTrkdQdxsInduct_zoom3")

  ######################################################################################
  ## Compare Cuts -- Phi >= or < 0 && other angle cuts #################################
  ######################################################################################

#  histConfigs = [
#    {
#      'title': "Track #phi #geq 0",
#      'cuts': "( iBestMatch >= 0) * (primTrkStartPhi >= 0)",
#    },
#    {
#      'title': "Track #phi <0",
#      'cuts': "( iBestMatch >= 0) * (primTrkStartPhi < 0)",
#    },
#    {
#      'title': "Track #phi #geq 0 & Angle Cuts",
#      'cuts': "( iBestMatch >= 0) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
#    },
#    {
#      'title': "Track #phi <0 & Angle Cuts",
#      'cuts': "( iBestMatch >= 0) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
#    },
#  ]
#  for i in range(len(histConfigs)):
#    histConfigs[i]["color"] = COLORLIST[i]
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
#      'ytitle': "Hits / bin",
#      'binning': [50,0,5],
#      'var': "primTrkdEdxs",
#      'normalize': True,
#      'logy': False,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhiCuts_primTrkdEdxs_zoom3")
#
#  for i in range(len(histConfigs)):
#    histConfigs[i].update(
#      {
#      'xtitle': "Primary TPC Track Pitch [cm]",
#      'ytitle': "Hits / bin",
#      'binning': [200,0,2],
#      'var': "primTrkPitches",
#      'normalize': False,
#      'logy': True,
#      },
#    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_trackPhiCuts_primTrkPitches")

  ######################################################################################
  ## Hit Locations -- Phi >= or < 0 && other angle cuts #################################
  ######################################################################################

  histConfigs = [
    {
      'name': "hitYVhitX_phiGeq0",
      'xtitle': "Hit x [cm]",
      'ytitle': "Hit y [cm]",
      'binning': [60,-5,55,60,-30,30],
      'var': "primTrkYs:primTrkXs",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitYVhitZ_phiGeq0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Hit y [cm]",
      'binning': [120,-10,110,60,-30,30],
      'var': "primTrkYs:primTrkZs",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitXVhitZ_phiGeq0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Hit x [cm]",
      'binning': [120,-10,110,60,-5,55],
      'var': "primTrkXs:primTrkZs",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitYVhitX_phiLt0",
      'xtitle': "Hit x [cm]",
      'ytitle': "Hit y [cm]",
      'binning': [60,-5,55,60,-30,30],
      'var': "primTrkYs:primTrkXs",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitYVhitZ_phiLt0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Hit y [cm]",
      'binning': [120,-10,110,60,-30,30],
      'var': "primTrkYs:primTrkZs",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitXVhitZ_phiLt0",
      'xtitle': "Hit z [cm]",
      'ytitle': "Hit x [cm]",
      'binning': [120,-10,110,60,-5,55],
      'var': "primTrkXs:primTrkZs",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitXVwire_phiLt0",
      'xtitle': "Wire Number",
      'ytitle': "Hit x [cm]",
      'binning': [240,0,240,60,-5,55],
      'var': "primTrkXs:primTrkTrueWires",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitXVwire_phiGeq0",
      'xtitle': "Wire Number",
      'ytitle': "Hit x [cm]",
      'binning': [240,0,240,60,-5,55],
      'var': "primTrkXs:primTrkTrueWires",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitYVwire_phiLt0",
      'xtitle': "Wire Number",
      'ytitle': "Hit y [cm]",
      'binning': [240,0,240,60,-30,30],
      'var': "primTrkYs:primTrkTrueWires",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitYVwire_phiGeq0",
      'xtitle': "Wire Number",
      'ytitle': "Hit y [cm]",
      'binning': [240,0,240,60,-30,30],
      'var': "primTrkYs:primTrkTrueWires",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitZVwire_phiLt0",
      'xtitle': "Wire Number",
      'ytitle': "Hit z [cm]",
      'binning': [240,0,240,120,-10,110],
      'var': "primTrkZs:primTrkTrueWires",
      'captionright1': "Track #phi < 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi < 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
    {
      'name': "hitZVwire_phiGeq0",
      'xtitle': "Wire Number",
      'ytitle': "Hit z [cm]",
      'binning': [240,0,240,120,-10,110],
      'var': "primTrkZs:primTrkTrueWires",
      'captionright1': "Track #phi #geq 0 & Angle Cuts",
      'cuts': "( iBestMatch >= 0) && (nTracks == 1) * (primTrkStartPhi >= 0)*((primTrkStartTheta > 27*pi/180.) && (primTrkStartTheta < 42*pi/180.))*(primTrkStartPhi > -57*pi/180. && primTrkStartPhi < 60*pi/180.)*(primTrkStartPhi < -15*pi/180. || primTrkStartPhi > 22*pi/180.)",
      #'normalize': True,
      #'logz': True,
    },
  ]
  #plotOneHistOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
  #      c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_HitPos_")

  ######################################################################################
  ## Compare Cuts -- Phi >= or < 0 and restrict pitch ##################################
  ######################################################################################

  histConfigs = [
    {
      'title': "Track #phi #geq 0",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi >= 0)",
    },
    {
      'title': "Track #phi < 0",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi < 0)",
    },
    {
      'title': "Track #phi #geq 0 & 0.45 #leq Pitch < 0.47",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi >= 0 && primTrkPitches >= 0.45 && primTrkPitches < 0.47)",
    },
    {
      'title': "Track #phi < 0 & 0.68 #leq Pitch < 0.70",
      'cuts': weightStr+hitExtraCuts+" * (primTrkStartPhi < 0 && primTrkPitches >= 0.68 && primTrkPitches < 0.70)",
    },
  ]
  #hitExtraCuts += "*((primTrkStartPhi >= 0) || (primTrkStartPhi < 0))" #small pitch region
  for i in range(len(histConfigs)):
    histConfigs[i]["color"] = COLORLIST[i]

  for i in range(len(histConfigs)):
    histConfigs[i].update(
      {
      'xtitle': "Primary TPC Track dE/dx [MeV/cm]",
      'ytitle': "Events / bin",
      'binning': [50,0,5],
      'var': "primTrkdEdxs",
      'normalize': True,
      'logy': False,
      },
    )
#  plotManyHistsOnePlot([x for x in fileConfigs if not ("smear" in x["name"])],histConfigs,
#        c,"cosmicanalyzer/tree",nMax=NMAX,outPrefix="Cosmics_pitchCuts_primTrkdEdxs_zoom3")

