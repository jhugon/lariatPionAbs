LArIAT Pion Absorption Analysis
===============================

This repository holds code for the LArIAT pion absorption analysis. The code
here processes the anaTree files produced by LArIATSoft.

The .C parts of the code are meant to create tree friends for the main anaTrees
with higher-level variables. the .py parts of the code use tree.Draw() to
create histograms and paint them to image files

Tree Info
---------

in the file it is usually "anatree/anatree" and the branches are:

  ::

  ******************************************************************************
  *Tree    :tree      : tree                                                   *
  *Entries :     1000 : Total =         1569736 bytes  File  Size =     863570 *
  *        :          : Tree compression factor =   1.78                       *
  ******************************************************************************
  *Br    0 :isMC      : isMC/O                                                 *
  *Entries :     1000 : Total  Size=       1535 bytes  File Size  =         99 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  10.82     *
  *............................................................................*
  *Br    1 :nWCTracks : nWCTracks/i                                            *
  *Entries :     1000 : Total  Size=       4566 bytes  File Size  =        126 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  32.35     *
  *............................................................................*
  *Br    2 :xWC       : xWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3571 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br    3 :yWC       : yWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3817 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.07     *
  *............................................................................*
  *Br    4 :thetaWC   : thetaWC/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3651 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br    5 :phiWC     : phiWC/F                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =       3624 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br    6 :pzWC      : pzWC/F                                                 *
  *Entries :     1000 : Total  Size=       4541 bytes  File Size  =       3687 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.10     *
  *............................................................................*
  *Br    7 :pWC       : pWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3678 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br    8 :eWC       : eWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3649 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br    9 :kinWC     : kinWC/F                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =       3719 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   10 :kinWCInTPC : kinWCInTPC/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3728 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   11 :yKinkWC   : yKinkWC/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        134 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.40     *
  *............................................................................*
  *Br   12 :nHitsWC   : nHitsWC/i                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        124 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  32.85     *
  *............................................................................*
  *Br   13 :xWC4Hit   : xWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3614 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   14 :yWC4Hit   : yWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3727 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   15 :zWC4Hit   : zWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        132 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.86     *
  *............................................................................*
  *Br   16 :nTOFs     : nTOFs/i                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =        122 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  33.38     *
  *............................................................................*
  *Br   17 :TOFs      : TOFs[nTOFs]/F                                          *
  *Entries :     1000 : Total  Size=       4640 bytes  File Size  =        132 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.90     *
  *............................................................................*
  *Br   18 :TOFTimeStamps : TOFTimeStamps[nTOFs]/i                             *
  *Entries :     1000 : Total  Size=       4678 bytes  File Size  =        141 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  28.99     *
  *............................................................................*
  *Br   19 :trueStartX : trueStartX/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3617 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   20 :trueStartY : trueStartY/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3730 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   21 :trueStartZ : trueStartZ/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =        135 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.20     *
  *............................................................................*
  *Br   22 :trueEndX  : trueEndX/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3670 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br   23 :trueEndY  : trueEndY/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3851 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.06     *
  *............................................................................*
  *Br   24 :trueEndZ  : trueEndZ/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3755 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   25 :trueStartTheta : trueStartTheta/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3658 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   26 :trueStartPhi : trueStartPhi/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3631 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   27 :trueStartMom : trueStartMom/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3687 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br   28 :trueStartE : trueStartE/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3653 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   29 :trueStartKin : trueStartKin/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3724 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.10     *
  *............................................................................*
  *Br   30 :trueEndMom : trueEndMom/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       1046 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.90     *
  *............................................................................*
  *Br   31 :trueEndE  : trueEndE/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       1043 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.91     *
  *............................................................................*
  *Br   32 :trueEndKin : trueEndKin/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       1032 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.95     *
  *............................................................................*
  *Br   33 :trueSecondToEndMom : trueSecondToEndMom/F                          *
  *Entries :     1000 : Total  Size=       4611 bytes  File Size  =       3745 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   34 :trueSecondToEndE : trueSecondToEndE/F                              *
  *Entries :     1000 : Total  Size=       4601 bytes  File Size  =       3619 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   35 :trueSecondToEndKin : trueSecondToEndKin/F                          *
  *Entries :     1000 : Total  Size=       4611 bytes  File Size  =       3773 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.08     *
  *............................................................................*
  *Br   36 :trueXFrontTPC : trueXFrontTPC/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3581 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br   37 :trueYFrontTPC : trueYFrontTPC/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3827 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.07     *
  *............................................................................*
  *Br   38 :nTracks   : nTracks/i                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        852 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   4.78     *
  *............................................................................*
  *Br   39 :nTracksInFirstZ : nTracksInFirstZ[95]/i                            *
  *Entries :     1000 : Total  Size=     381668 bytes  File Size  =       9573 *
  *Baskets :       13 : Basket Size=      32000 bytes  Compression=  39.81     *
  *............................................................................*
  *Br   40 :nTracksLengthLt : nTracksLengthLt[20]/i                            *
  *Entries :     1000 : Total  Size=      80768 bytes  File Size  =       3955 *
  *Baskets :        3 : Basket Size=      32000 bytes  Compression=  20.29     *
  *............................................................................*
  *Br   41 :trackStartX : trackStartX[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       7863 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.38     *
  *............................................................................*
  *Br   42 :trackStartY : trackStartY[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8192 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   43 :trackStartZ : trackStartZ[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8158 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   44 :trackStartTheta : trackStartTheta[nTracks]/F                       *
  *Entries :     1000 : Total  Size=      11463 bytes  File Size  =       8075 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   45 :trackStartPhi : trackStartPhi[nTracks]/F                           *
  *Entries :     1000 : Total  Size=      11453 bytes  File Size  =       8129 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   46 :trackEndX : trackEndX[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       7945 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   47 :trackEndY : trackEndY[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       8157 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   48 :trackEndZ : trackEndZ[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       7918 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.37     *
  *............................................................................*
  *Br   49 :trackLength : trackLength[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8036 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   50 :trackCaloKin : trackCaloKin[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       8089 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   51 :trackLLHPion : trackLLHPion[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       8052 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   52 :trackLLHProton : trackLLHProton[nTracks]/F                         *
  *Entries :     1000 : Total  Size=      11458 bytes  File Size  =       7988 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   53 :trackLLHMuon : trackLLHMuon[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       1574 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   6.89     *
  *............................................................................*
  *Br   54 :trackLLHKaon : trackLLHKaon[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       1574 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   6.89     *
  *............................................................................*
  *Br   55 :iBestMatch : iBestMatch/I                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =        710 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   5.74     *
  *............................................................................*
  *Br   56 :trackMatchDeltaX : trackMatchDeltaX[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8191 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   57 :trackMatchDeltaY : trackMatchDeltaY[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8324 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   58 :trackMatchDeltaR : trackMatchDeltaR[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8196 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   59 :trackMatchDeltaAngle : trackMatchDeltaAngle[nTracks]/F             *
  *Entries :     1000 : Total  Size=      11488 bytes  File Size  =       8121 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   60 :trackMatchLowestZ : trackMatchLowestZ[nTracks]/F                   *
  *Entries :     1000 : Total  Size=      11473 bytes  File Size  =       8178 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   61 :trackMatchLowestZX : trackMatchLowestZX[nTracks]/F                 *
  *Entries :     1000 : Total  Size=      11478 bytes  File Size  =       7876 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.38     *
  *............................................................................*
  *Br   62 :trackMatchLowestZY : trackMatchLowestZY[nTracks]/F                 *
  *Entries :     1000 : Total  Size=      11478 bytes  File Size  =       8196 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   63 :primTrkStartMomTrking : primTrkStartMomTrking/F                    *
  *Entries :     1000 : Total  Size=       4626 bytes  File Size  =        506 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   8.08     *
  *............................................................................*
  *Br   64 :primTrkStartTheta : primTrkStartTheta/F                            *
  *Entries :     1000 : Total  Size=       4606 bytes  File Size  =       3204 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.27     *
  *............................................................................*
  *Br   65 :primTrkStartPhi : primTrkStartPhi/F                                *
  *Entries :     1000 : Total  Size=       4596 bytes  File Size  =       3205 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.27     *
  *............................................................................*
  *Br   66 :primTrkLength : primTrkLength/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3135 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   67 :primTrkStartX : primTrkStartX/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3063 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   68 :primTrkStartY : primTrkStartY/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3256 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.25     *
  *............................................................................*
  *Br   69 :primTrkStartZ : primTrkStartZ/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3238 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.26     *
  *............................................................................*
  *Br   70 :primTrkEndX : primTrkEndX/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3124 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   71 :primTrkEndY : primTrkEndY/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3272 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.25     *
  *............................................................................*
  *Br   72 :primTrkEndZ : primTrkEndZ/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3149 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   73 :primTrkCaloKin : primTrkCaloKin/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3193 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.28     *
  *............................................................................*
  *Br   74 :primTrkEndKin : primTrkEndKin/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3020 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   75 :primTrkLLHPion : primTrkLLHPion/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3192 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.28     *
  *............................................................................*
  *Br   76 :primTrkLLHProton : primTrkLLHProton/F                              *
  *Entries :     1000 : Total  Size=       4601 bytes  File Size  =       3201 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.28     *
  *............................................................................*
  *Br   77 :primTrkLLHMuon : primTrkLLHMuon/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =        495 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   8.24     *
  *............................................................................*
  *Br   78 :primTrkLLHKaon : primTrkLLHKaon/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =        495 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   8.24     *
  *............................................................................*
  *Br   79 :primTrkdEdxs : vector<float>                                       *
  *Entries :     1000 : Total  Size=     307224 bytes  File Size  =     268566 *
  *Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br   80 :primTrkResRanges : vector<float>                                   *
  *Entries :     1000 : Total  Size=     307280 bytes  File Size  =     274107 *
  *Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*

