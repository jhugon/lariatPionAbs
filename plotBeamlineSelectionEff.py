#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

if __name__ == "__main__":

  c = root.TCanvas()
  NMAX=10000000000
  #NMAX=10000
  fileConfigs = [
    {
      'fn': [
                "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
                "BeamLineAnaTree_data_Lovely1_Neg_Run1_elenag_v02_v01.root",
            ],
      'name': "RunI_All",
      'title': "Run I, + & -",
      'caption': "Run I, + & -",
      'color': root.kBlack,
    },
    {
      'fn': "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
      #'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
      #'fn': "anaTree_data_runI_pos_v0.1.root",
      #'addFriend': ["friend","friendTree_data_runI_pos_v0.1.root"],
      'name': "RunI_Pos",
      'title': "Run I Pos. Polarity",
      'caption': "Run I Pos. Polarity",
      'color': root.kBlack,
    },
#    {
#      'fn': "anaTree_data_Lovely1_Pos_RunII_elanag_v02_v01.root",
#      #'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
#      #'fn': "anaTree_data_runI_pos_v0.1.root",
#      #'addFriend': ["friend","friendTree_data_runI_pos_v0.1.root"],
#      'name': "RunII_Pos",
#      'title': "Run II Pos. Polarity",
#      'caption': "Run II Pos. Polarity",
#      'color': root.kBlue,
#    },
    {
      'fn': "BeamLineAnaTree_run4295_v1.root",
      'name': "Run4295_v60601",
      'title': "Run 4295 v6_06_01",
      'caption': "Run 4295 v6_06_01",
      'color': root.kBlue,
    },
    {
      'fn': "BeamLineAnaTree_run4295_v06_15_00_v1.root",
      'name': "Run4295_v61500",
      'title': "Run 4295 v6_15_00",
      'caption': "Run 4295 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run5605_v06_15_00_v1.root",
      'name': "Run5605_v61500",
      'title': "Run 5605 v6_15_00",
      'caption': "Run 5605 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run6111_v06_15_00_v1.root",
      'name': "Run6111_v61500",
      'title': "Run 6111 v6_15_00",
      'caption': "Run 6111 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run6264_v06_15_00_v1.root",
      'name': "Run6264_v61500",
      'title': "Run 6264 v6_15_00",
      'caption': "Run 6264 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run6336_v06_15_00_v1.root",
      'name': "Run6336_v61500",
      'title': "Run 6336 v6_15_00",
      'caption': "Run 6336 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run6373_v06_15_00_v1.root",
      'name': "Run6373_v61500",
      'title': "Run 6373 v6_15_00",
      'caption': "Run 6373 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_data_Lovely1_Neg_Run1_elenag_v02_v01.root",
      #'fn': "anaTree_runI_neg_1k.root",
      #'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
      'name': "RunI_Neg",
      'title': "Run I Neg. Polarity",
      'caption': "Run I Neg. Polarity",
      'color': root.kBlue,
    },
#    {
#      'fn': "anaTree_runII_neg_test.root",
#      #'fn': "anaTree_runII_neg_200.root",
#      #'addFriend': ["friend","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root"],
#      'name': "RunII_Neg",
#      'title': "Run II Neg. Polarity",
#      'caption': "Run II Neg. Polarity",
#      'color': root.kRed,
#    },
  ]

  histConfigs = [
    {
      'name': "runNumber",
      'xtitle': "Run Number",
      'ytitle': "Events / bin",
      'binning': [850,5550,6400],
      'var': "run",
      'cuts': "",
    },
    {
      'name': "nwctrks",
      'xtitle': "Number of Wire Chamber Tracks",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "nwctrks",
      'cuts': "",
      'logy': True,
    },
    {
      'name': "ntof",
      'xtitle': "Number of Time of Flight Objects",
      'ytitle': "Events / bin",
      'binning': [11,-0.5,10.5],
      'var': "ntof",
      'cuts': "",
      'logy': True,
    },
    #{
    #  'name': "nAG",
    #  'xtitle': "Number of Aerogel Counter Objects",
    #  'ytitle': "Events / bin",
    #  'binning': [11,-0.5,10.5],
    #  'var': "nAG",
    #  'cuts': "",
    #  'logy': True,
    #},
    #{
    #  'name': "ntracks_reco",
    #  'xtitle': "Number Reconstructed TPC Tracks",
    #  'ytitle': "Events / bin",
    #  'binning': [31,-0.5,30.5],
    #  'var': "ntracks_reco",
    #  'cuts': "",
    #  'logy': True,
    #},
    #{
    #  'name': "nclus",
    #  'xtitle': "Number Reconstructed TPC Clusters",
    #  'ytitle': "Events / bin",
    #  'binning': [51,-0.5,51.5],
    #  'var': "nclus",
    #  'cuts': "",
    #  'logy': True,
    #},
    #{
    #  'name': "nhits",
    #  'xtitle': "Number Reconstructed TPC Hits",
    #  'ytitle': "Events / bin",
    #  'binning': [100,0,10000],
    #  'var': "nhits",
    #  'cuts': "",
    #  'logy': True,
    #},
    #{
    #  'name': "wctrk_XFaceCoor",
    #  'xtitle': "x Coordinate of WC Track Extrapolated to TPC [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [600,-100,500],
    #  'var': "wctrk_XFaceCoor",
    #  'cuts': "",
    #},
    #{
    #  'name': "wctrk_YFaceCoor",
    #  'xtitle': "y Coordinate of WC Track Extrapolated to TPC [cm]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [200,-100,100],
    #  'var': "wctrk_YFaceCoor",
    #  'cuts': "",
    #},
    #{
    #  'name': "wctrk_XYFace",
    #  'xtitle': "WC Track X Position on Front of TPC [cm]",
    #  'ytitle': "WC Track Y Position on Front of TPC [cm]",
    #  'binning': [600,-100,500,200,-100,100],
    #  'var': "wctrk_YFaceCoor:wctrk_XFaceCoor",
    #  'cuts': "",
    #},
    #{
    #  'name': "wctrk_theta",
    #  'xtitle': "WC Track #theta [deg]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [80,-20,20],
    #  'var': "wctrk_theta*180/pi",
    #  'cuts': "",
    #},
    #{
    #  'name': "wctrk_phi",
    #  'xtitle': "WC Track #phi [deg]",
    #  'ytitle': "Tracks / bin",
    #  'binning': [180,-180,180],
    #  'var': "wctrk_phi*180/pi",
    #  'cuts': "",
    #},
    {
      'name': "wctrk_momentum",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "Tracks / bin",
      'binning': [200,0,2000],
      'var': "wctrk_momentum",
      'cuts': "",
    },
    {
      'name': "tofObject",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "TOF / ns",
      'binning': [360,10,55],
      'var': "tofObject",
      'cuts': "",
      'normToBinWidth': True,
    },
    {
      'name': "tofObject_wide",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "TOF / ns",
      'binning': [400,0,100],
      'var': "tofObject",
      'cuts': "",
      'normToBinWidth': True,
    },
    #{
    #  'name': "tof_timestamp",
    #  'xtitle': "Time of Flight Timestamp [ns]",
    #  'ytitle': "TOF / bin",
    #  'binning': [2000,-5e5,5e5],
    #  'var': "tof_timestamp",
    #  'cuts': "",
    #},
    {
      'name': "tofVP_wide",
      'ytitle': "Time of Flight [ns]",
      'xtitle': "WC Track Momentum [MeV/c]",
      'binning': [100,0,2000.,100,0,100],
      'var': "tofObject[0]:wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1",
      #'logz': True,
    },
    {
      'name': "tofVP",
      'ytitle': "Time of Flight [ns]",
      'xtitle': "WC Track Momentum [MeV/c]",
      'binning': [200,250,1250.,200,10,55],
      'var': "tofObject[0]:wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1",
      #'logz': True,
    },
    {
      'name': "tof2p2Vp2",
      'ytitle': "TOF^{2}p^{2} [(ns)^{2} (MeV/c)^{2}]",
      'xtitle': "p^{2} [(MeV/c)^{2}]",
      'binning': [200,0,2e6,200,0,1e9],
      'var': "tofObject[0]*tofObject[0]*wctrk_momentum[0]*wctrk_momentum[0]:wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1",
      #'logz': True,
    },
    {
      'name': "tof2p2Vp2_toflt27",
      'ytitle': "TOF^{2}p^{2} [(ns)^{2} (MeV/c)^{2}]",
      'xtitle': "p^{2} [(MeV/c)^{2}]",
      'binning': [200,0,2e6,200,0,1e9],
      'var': "tofObject[0]*tofObject[0]*wctrk_momentum[0]*wctrk_momentum[0]:wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
      #'logz': True,
    },
    {
      'name': "tof2p2Vp2_tofgeq27",
      'ytitle': "TOF^{2}p^{2} [(ns)^{2} (MeV/c)^{2}]",
      'xtitle': "p^{2} [(MeV/c)^{2}]",
      'binning': [200,0,2e6,200,0,1e9],
      'var': "tofObject[0]*tofObject[0]*wctrk_momentum[0]*wctrk_momentum[0]:wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]>=27.",
      #'logz': True,
    },
    {
      'name': "mass2_narrow",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [100,-1e5,1e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d=6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "mass2_narrowK",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [30,1.0e5,3.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(6.684),
      'captionleft2': "Around Proton Peak",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "mass2_narrowP",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [100,6e5,12e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d={:0.2f} m".format(6.684),
      'captionleft2': "Around Proton Peak",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "mass2",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [150,-1.5e6,1.5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "d=6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'logy': True,
    },
    {
      'name': "mass2_wide",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [200,-2e6,5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2,1875.6**2],
      'logy': True,
    },
    {
      'name': "mass2Vp",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "m^{2} [MeV^{2}/c^{4}]",
      'binning': [50,0,2000,50,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.):wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1",
      'drawhlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'profileXtoo': True,
      #'logz': True,
    },
    {
      'name': "mass2Vp_toflt26",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "m^{2} [MeV^{2}/c^{4}]",
      'binning': [50,0,2000,50,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.):wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0] < 26.",
      'captionleft1': "TOF < 26 ns",
      'drawhlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'profileXtoo': True,
      #'logz': True,
    },
    {
      'name': "mass2Vp2",
      'xtitle': "(WC Track Momentum)^{2} [(MeV/c)^{2}]",
      'ytitle': "m^{2} [MeV^{2}/c^{4}]",
      'binning': [50,0,2e6,50,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.):wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1",
      'drawhlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'profileXtoo': True,
      #'logz': True,
    },
    {
      'name': "mass2Vp2_toflt26",
      'xtitle': "(WC Track Momentum)^{2} [(MeV/c)^{2}]",
      'ytitle': "m^{2} [MeV^{2}/c^{4}]",
      'binning': [50,0,2e6,50,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.):wctrk_momentum[0]*wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0] < 26.",
      'captionleft1': "TOF < 26 ns",
      'drawhlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'profileXtoo': True,
      #'logz': True,
    },
    {
      'name': "mass",
      'xtitle': "m [MeV/c^{2}]",
      'ytitle': "Events / (MeV/c^{2})",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'captionright1': "d=6.684 m",
      'drawvlines': [105.658,139.570,493.667,938.272],
      'normToBinWidth': True,
    },
    {
      'name': "massVp",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "m [MeV/c^{2}]",
      'binning': [50,0,2000,50,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)):wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'captionright1': "d=6.684 m",
      'drawhlines': [105.658,139.570,493.667,938.272],
      #'logz': True,
    },
    {
      'name': "massVp_toflt26",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "m [MeV/c^{2}]",
      'binning': [50,0,2000,50,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)):wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0. && tofObject[0]<26.",
      'captionright1': "d=6.684 m",
      'drawhlines': [105.658,139.570,493.667,938.272],
      'profileXtoo': True,
      #'logz': True,
    },
    {
      'name': "massVp_toflt26",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "m [MeV/c^{2}]",
      'binning': [50,0,2000,50,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)):wctrk_momentum[0]",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0. && tofObject[0]<26.",
      'captionright1': "6.684 m",
      'captionleft1': "d=TOF < 26 ns",
      'drawhlines': [105.658,139.570,493.667,938.272],
      'profileXtoo': True,
      #'logz': True,
    },
  ]

  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX)

#  histConfigs = [
#    {
#      'name': "dmpi",
#      'title': "m_{#pi}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+19488.16,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileXtoo':True,
#    },
#    {
#      'name': "dmmu",
#      'title': "m_{#mu}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+11161.92,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileXtoo':True,
#    },
#    {
#      'name': "dm0",
#      'title': "m=0",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]:wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileXtoo':True,
#    },
#    {
#      'name': "dmp",
#      'title': "m_{p}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5.,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+880406.89,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]>=27.",
#      'profileXtoo':True,
#    },
#    {
#      'name': "dmk",
#      'title': "m_{K}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+243707.1,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1",
#      'profileXtoo':True,
#    },
#  ]
#  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="TOF_")
#
#  histConfigs = [
#    {
#      'name': "dmpi",
#      'title': "m_{#pi}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'ylim': [5.,9.],
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+19488.16,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kBlue,
#      'drawhlines': [6.684]
#    },
#    {
#      'name': "dmmu",
#      'title': "m_{#mu}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+11161.92,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kMagenta,
#    },
#    {
#      'name': "dm0",
#      'title': "m=0",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]:wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kGreen+1,
#    },
#    {
#      'name': "dmp",
#      'title': "m_{p}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5.,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+880406.89,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]>=27. && wctrk_momentum[0]>500. && wctrk_momentum[0]<1000.",
#      'profileX':True,
#      'color': root.kRed,
#    },
#    #{
#    #  'name': "dmk",
#    #  'title': "m_{K}",
#    #  'xtitle': "p [MeV/c]",
#    #  'ytitle': "d [m]",
#    #  'binning': [200,0,1200,200,5,10],
#    #  'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+243707.1,-0.5):wctrk_momentum[0]",
#    #  'cuts': "ntof == 1 && nwctrks == 1",
#    #  'profileX':True,
#    #  'color': root.kOrange-3,
#    #},
#  ]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="TOF_")
#
#  histConfigs = [
#    {
#      'name': "dmpi",
#      'title': "m_{#pi}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'ylim': [6.,8.],
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+19488.16,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kBlue,
#      'drawhlines': [6.684]
#    },
#    {
#      'name': "dmmu",
#      'title': "m_{#mu}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+11161.92,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kMagenta,
#    },
#    {
#      'name': "dm0",
#      'title': "m=0",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5,10],
#      'var': "0.299*tofObject[0]:wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]<27.",
#      'profileX':True,
#      'color': root.kGreen+1,
#    },
#    {
#      'name': "dmp",
#      'title': "m_{p}",
#      'xtitle': "p [MeV/c]",
#      'ytitle': "d [m]",
#      'binning': [200,0,1200,200,5.,10],
#      'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+880406.89,-0.5):wctrk_momentum[0]",
#      'cuts': "ntof == 1 && nwctrks == 1 && tofObject[0]>=27. && wctrk_momentum[0]>500. && wctrk_momentum[0]<1000.",
#      'profileX':True,
#      'color': root.kRed,
#    },
#    #{
#    #  'name': "dmk",
#    #  'title': "m_{K}",
#    #  'xtitle': "p [MeV/c]",
#    #  'ytitle': "d [m]",
#    #  'binning': [200,0,1200,200,5,10],
#    #  'var': "0.299*tofObject[0]*wctrk_momentum[0]*pow(wctrk_momentum[0]*wctrk_momentum[0]+243707.1,-0.5):wctrk_momentum[0]",
#    #  'cuts': "ntof == 1 && nwctrks == 1",
#    #  'profileX':True,
#    #  'color': root.kOrange-3,
#    #},
#  ]
#  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="TOF_fine_")

  histConfigs = [
    {
      'name': "mass",
      'title': "|m| = Re(m) + Im(m)",
      'xtitle': "m [MeV]",
      'ytitle': "Events / bin",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658,139.570,493.667,938.272]
    },
    {
      'name': "mass",
      'title': "Re(m)",
      'xtitle': "m [MeV]",
      'ytitle': "Events / bin",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'color': root.kGreen+1,
      'captionleft1': "6.684 m",
    },
    {
      'name': "mass",
      'title': "Im(m)",
      'xtitle': "m [MeV]",
      'ytitle': "Events / bin",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) < 0.",
      'color': root.kRed,
      'captionleft1': "6.684 m",
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="masses_")

###########################################3
###########################################3
###########################################3
###########################################3
###########################################3

  fileConfigs = [
    {
      'fn': [
                "anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",
                "BeamLineAnaTree_data_Lovely1_Neg_Run1_elenag_v02_v01.root",
            ],
      'name': "RunI_All",
      'title': "Run I, + & -",
      'caption': "Run I, + & -",
      'color': root.kBlack,
    },
  ]

  histConfigs = [
    {
      'name': "tofVrun",
      'ytitle': "Time of Flight [ns]",
      'xtitle': "Run Number",
      'binning': [170,5550,6400,100,0,100],
      'var': "tofObject[0]:run",
      'cuts': "ntof == 1 && nwctrks == 1",
      'logz': True,
    },
    {
      'name': "PVrun",
      'ytitle': "WC Track Momentum [MeV/c]",
      'xtitle': "Run Number",
      'binning': [170,5550,6400,75,0,1500],
      'var': "wctrk_momentum[0]:run",
      'cuts': "ntof == 1 && nwctrks == 1",
      'logz': True,
    },
    {
      'name': "massVrun",
      'ytitle': "m [MeV/c^{2}]",
      'xtitle': "Run Number",
      'binning': [170,5550,6400,75,0,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)):run",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'drawhlines': [105.658,139.570,493.667,938.272],
      'logz': True,
    },
    {
      'name': "mass2Vrun",
      'xtitle': "Run Number",
      'ytitle': "m^{2} [MeV^{2}/c^{4}]",
      'binning': [170,5550,6400,100,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.):run",
      'cuts': "ntof == 1 && nwctrks == 1",
      'drawhlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'logz': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX)

###########################################3
###########################################3
###########################################3
###########################################3
###########################################3


  fileConfigs = [
    {
      'fn': "BeamLineAnaTree_run4295_v1.root",
      'name': "Run4295_v60601",
      'title': "Run 4295 v6_06_01",
      'caption': "Run 4295 v6_06_01",
      'color': root.kBlue,
    },
    {
      'fn': "BeamLineAnaTree_run4295_v06_15_00_v1.root",
      'name': "Run4295_v61500",
      'title': "Run 4295 v6_15_00",
      'caption': "Run 4295 v6_15_00",
      'color': root.kGreen+1,
    },
  ]

  histConfigs = [
    {
      'name': "tofObject",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "TOF / ns",
      'binning': [360,10,55],
      'var': "tofObject",
      'cuts': "",
      'normToBinWidth': True,
    },
    {
      'name': "tofObject_wide",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "TOF / ns",
      'binning': [400,0,100],
      'var': "tofObject",
      'cuts': "",
      'normToBinWidth': True,
    },
    {
      'name': "mass2",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [2000,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "mass",
      'xtitle': "m [MeV/c^{2}]",
      'ytitle': "Events / (MeV/c^{2})",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'captionright1': "6.684 m",
      'drawvlines': [105.658,139.570,493.667,938.272],
      'normToBinWidth': True,
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="compare4295_")

###########################################3
###########################################3
###########################################3
###########################################3
###########################################3


  fileConfigs = [
    #{
    #  'fn': "BeamLineAnaTree_run4295_v06_15_00_v1.root",
    #  'name': "Run4295_v61500",
    #  'title': "Run 4295 v6_15_00",
    #  'caption': "Run 4295 v6_15_00",
    #  'color': root.kBlack,
    #},
    {
      'fn': "BeamLineAnaTree_run5605_v06_15_00_v1.root",
      'name': "Run5605_v61500",
      'title': "Run 5605 v6_15_00",
      'caption': "Run 5605 v6_15_00",
      'color': root.kBlue,
    },
    {
      'fn': "BeamLineAnaTree_run6111_v06_15_00_v1.root",
      'name': "Run6111_v61500",
      'title': "Run 6111 v6_15_00",
      'caption': "Run 6111 v6_15_00",
      'color': root.kRed+1,
    },
    {
      'fn': "BeamLineAnaTree_run6264_v06_15_00_v1.root",
      'name': "Run6264_v61500",
      'title': "Run 6264 v6_15_00",
      'caption': "Run 6264 v6_15_00",
      'color': root.kGreen+1,
    },
    {
      'fn': "BeamLineAnaTree_run6336_v06_15_00_v1.root",
      'name': "Run6336_v61500",
      'title': "Run 6336 v6_15_00",
      'caption': "Run 6336 v6_15_00",
      'color': root.kMagenta,
    },
    {
      'fn': "BeamLineAnaTree_run6373_v06_15_00_v1.root",
      'name': "Run6373_v61500",
      'title': "Run 6373 v6_15_00",
      'caption': "Run 6373 v6_15_00",
      'color': root.kCyan,
    },
  ]

  histConfigs = [
    {
      'name': "nwctrks",
      'xtitle': "Number of Wire Chamber Tracks",
      'ytitle': "Normalized Events",
      'binning': [11,-0.5,10.5],
      'var': "nwctrks",
      'cuts': "",
      'logy': True,
      'normalize': True,
    },
    {
      'name': "ntof",
      'xtitle': "Number of Time of Flight Objects",
      'ytitle': "Normalized Events",
      'binning': [11,-0.5,10.5],
      'var': "ntof",
      'cuts': "",
      'logy': True,
      'normalize': True,
    },
    {
      'name': "wctrk_momentum",
      'xtitle': "WC Track Momentum [MeV/c]",
      'ytitle': "Normalized Events",
      'binning': [200,0,2000],
      'var': "wctrk_momentum",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "tofObject",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "Normalized Events",
      'binning': [360,10,55],
      'var': "tofObject",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "tofObject_wide",
      'xtitle': "Time of Flight [ns]",
      'ytitle': "Normalized Events",
      'binning': [400,0,100],
      'var': "tofObject",
      'cuts': "",
      'normalize': True,
    },
    {
      'name': "mass",
      'xtitle': "m [MeV/c^{2}]",
      'ytitle': "Normalized Events",
      'binning': [150,0.,1500],
      'var': "sqrt(wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.))",
      'cuts': "ntof == 1 && nwctrks == 1 && (wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)) > 0.",
      'captionright1': "6.684 m",
      'drawvlines': [105.658,139.570,493.667,938.272],
      'normalize': True,
    },
    {
      'name': "mass2_narrow",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [2000,-2.5e5,2.5e5],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2]
    },
    {
      'name': "mass2",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [150,-1.5e6,1.5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2],
      'logy': True,
    },
    {
      'name': "mass2_wide",
      'xtitle': "m^{2} [MeV^{2}/c^{4}]",
      'ytitle': "Events / bin",
      'binning': [250,-5e6,5e6],
      'var': "wctrk_momentum[0]*wctrk_momentum[0] * (tofObject[0]*tofObject[0]*0.299*0.299/6.684/6.684 - 1.)",
      'cuts': "ntof == 1 && nwctrks == 1",
      'captionleft1': "6.684 m",
      'drawvlines': [105.658**2,139.570**2,493.667**2,938.272**2,1875.6**2],
      'logy': True,
    },
  ]
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"anatree/anatree",nMax=NMAX,outPrefix="compare_")
