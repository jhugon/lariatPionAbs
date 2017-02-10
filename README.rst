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
  *Entries :     1000 : Total =         1915101 bytes  File  Size =    1161341 *
  *        :          : Tree compression factor =   1.62                       *
  ******************************************************************************
  *Br    0 :isMC      : isMC/O                                                 *
  *Entries :     1000 : Total  Size=       1535 bytes  File Size  =         99 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  10.82     *
  *............................................................................*
  *Br    1 :runNumber : runNumber/i                                            *
  *Entries :     1000 : Total  Size=       4566 bytes  File Size  =        131 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  31.11     *
  *............................................................................*
  *Br    2 :subRunNumber : subRunNumber/i                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =        141 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  28.93     *
  *............................................................................*
  *Br    3 :eventNumber : eventNumber/i                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       1523 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   2.68     *
  *............................................................................*
  *Br    4 :nWCTracks : nWCTracks/i                                            *
  *Entries :     1000 : Total  Size=       4566 bytes  File Size  =        126 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  32.35     *
  *............................................................................*
  *Br    5 :xWC       : xWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3571 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br    6 :yWC       : yWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3817 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.07     *
  *............................................................................*
  *Br    7 :thetaWC   : thetaWC/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3651 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br    8 :phiWC     : phiWC/F                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =       3624 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br    9 :pzWC      : pzWC/F                                                 *
  *Entries :     1000 : Total  Size=       4541 bytes  File Size  =       3687 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.10     *
  *............................................................................*
  *Br   10 :pWC       : pWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3678 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br   11 :eWC       : eWC/F                                                  *
  *Entries :     1000 : Total  Size=       4536 bytes  File Size  =       3649 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   12 :kinWC     : kinWC/F                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =       3719 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   13 :kinWCInTPC : kinWCInTPC/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3728 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   14 :yKinkWC   : yKinkWC/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        134 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.40     *
  *............................................................................*
  *Br   15 :nHitsWC   : nHitsWC/i                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        124 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  32.85     *
  *............................................................................*
  *Br   16 :xWC4Hit   : xWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3614 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   17 :yWC4Hit   : yWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =       3727 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   18 :zWC4Hit   : zWC4Hit/F                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        132 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.86     *
  *............................................................................*
  *Br   19 :nTOFs     : nTOFs/i                                                *
  *Entries :     1000 : Total  Size=       4546 bytes  File Size  =        122 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  33.38     *
  *............................................................................*
  *Br   20 :TOFs      : TOFs[nTOFs]/F                                          *
  *Entries :     1000 : Total  Size=       4640 bytes  File Size  =        132 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.90     *
  *............................................................................*
  *Br   21 :TOFTimeStamps : TOFTimeStamps[nTOFs]/i                             *
  *Entries :     1000 : Total  Size=       4678 bytes  File Size  =        141 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  28.99     *
  *............................................................................*
  *Br   22 :trueStartX : trueStartX/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3617 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   23 :trueStartY : trueStartY/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3730 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   24 :trueStartZ : trueStartZ/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =        135 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=  30.20     *
  *............................................................................*
  *Br   25 :trueEndX  : trueEndX/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3670 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br   26 :trueEndY  : trueEndY/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3851 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.06     *
  *............................................................................*
  *Br   27 :trueEndZ  : trueEndZ/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       3755 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   28 :trueStartTheta : trueStartTheta/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3658 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   29 :trueStartPhi : trueStartPhi/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3631 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   30 :trueStartMom : trueStartMom/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3687 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.11     *
  *............................................................................*
  *Br   31 :trueStartE : trueStartE/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       3653 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   32 :trueStartKin : trueStartKin/F                                      *
  *Entries :     1000 : Total  Size=       4581 bytes  File Size  =       3724 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.10     *
  *............................................................................*
  *Br   33 :trueEndMom : trueEndMom/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       1046 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.90     *
  *............................................................................*
  *Br   34 :trueEndE  : trueEndE/F                                             *
  *Entries :     1000 : Total  Size=       4561 bytes  File Size  =       1043 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.91     *
  *............................................................................*
  *Br   35 :trueEndKin : trueEndKin/F                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =       1032 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   3.95     *
  *............................................................................*
  *Br   36 :trueSecondToEndMom : trueSecondToEndMom/F                          *
  *Entries :     1000 : Total  Size=       4611 bytes  File Size  =       3745 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.09     *
  *............................................................................*
  *Br   37 :trueSecondToEndE : trueSecondToEndE/F                              *
  *Entries :     1000 : Total  Size=       4601 bytes  File Size  =       3619 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.13     *
  *............................................................................*
  *Br   38 :trueSecondToEndKin : trueSecondToEndKin/F                          *
  *Entries :     1000 : Total  Size=       4611 bytes  File Size  =       3773 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.08     *
  *............................................................................*
  *Br   39 :trueXFrontTPC : trueXFrontTPC/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3581 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br   40 :trueYFrontTPC : trueYFrontTPC/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3827 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.07     *
  *............................................................................*
  *Br   41 :nTracks   : nTracks/i                                              *
  *Entries :     1000 : Total  Size=       4556 bytes  File Size  =        852 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   4.78     *
  *............................................................................*
  *Br   42 :nTracksInFirstZ : nTracksInFirstZ[95]/i                            *
  *Entries :     1000 : Total  Size=     381668 bytes  File Size  =       9573 *
  *Baskets :       13 : Basket Size=      32000 bytes  Compression=  39.81     *
  *............................................................................*
  *Br   43 :nTracksLengthLt : nTracksLengthLt[20]/i                            *
  *Entries :     1000 : Total  Size=      80768 bytes  File Size  =       3955 *
  *Baskets :        3 : Basket Size=      32000 bytes  Compression=  20.29     *
  *............................................................................*
  *Br   44 :trackStartX : trackStartX[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       7863 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.38     *
  *............................................................................*
  *Br   45 :trackStartY : trackStartY[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8192 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   46 :trackStartZ : trackStartZ[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8158 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   47 :trackStartTheta : trackStartTheta[nTracks]/F                       *
  *Entries :     1000 : Total  Size=      11463 bytes  File Size  =       8075 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   48 :trackStartPhi : trackStartPhi[nTracks]/F                           *
  *Entries :     1000 : Total  Size=      11453 bytes  File Size  =       8129 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   49 :trackEndX : trackEndX[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       7945 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   50 :trackEndY : trackEndY[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       8157 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   51 :trackEndZ : trackEndZ[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       7918 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.37     *
  *............................................................................*
  *Br   52 :trackLength : trackLength[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8036 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   53 :trackXFront : trackXFront[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8027 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   54 :trackYFront : trackYFront[nTracks]/F                               *
  *Entries :     1000 : Total  Size=      11443 bytes  File Size  =       8280 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   55 :trackCaloKin : trackCaloKin[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       8089 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   56 :trackLLHPion : trackLLHPion[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       8052 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.35     *
  *............................................................................*
  *Br   57 :trackLLHProton : trackLLHProton[nTracks]/F                         *
  *Entries :     1000 : Total  Size=      11458 bytes  File Size  =       7988 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   58 :trackLLHMuon : trackLLHMuon[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       7930 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.37     *
  *............................................................................*
  *Br   59 :trackLLHKaon : trackLLHKaon[nTracks]/F                             *
  *Entries :     1000 : Total  Size=      11448 bytes  File Size  =       7978 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   60 :trackPIDA : trackPIDA[nTracks]/F                                   *
  *Entries :     1000 : Total  Size=      11433 bytes  File Size  =       7954 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.36     *
  *............................................................................*
  *Br   61 :trackStartDistToPrimTrkEnd : trackStartDistToPrimTrkEnd[nTracks]/F *
  *Entries :     1000 : Total  Size=      11518 bytes  File Size  =       5733 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.89     *
  *............................................................................*
  *Br   62 :trackEndDistToPrimTrkEnd : trackEndDistToPrimTrkEnd[nTracks]/F     *
  *Entries :     1000 : Total  Size=      11508 bytes  File Size  =       5651 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.92     *
  *............................................................................*
  *Br   63 :iBestMatch : iBestMatch/I                                          *
  *Entries :     1000 : Total  Size=       4571 bytes  File Size  =        733 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   5.56     *
  *............................................................................*
  *Br   64 :trackMatchDeltaX : trackMatchDeltaX[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8191 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   65 :trackMatchDeltaY : trackMatchDeltaY[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8324 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   66 :trackMatchDeltaR : trackMatchDeltaR[nTracks]/F                     *
  *Entries :     1000 : Total  Size=      11468 bytes  File Size  =       8196 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   67 :trackMatchDeltaAngle : trackMatchDeltaAngle[nTracks]/F             *
  *Entries :     1000 : Total  Size=      11488 bytes  File Size  =       8121 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   68 :trackMatchLowestZ : trackMatchLowestZ[nTracks]/F                   *
  *Entries :     1000 : Total  Size=      11473 bytes  File Size  =       8178 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   69 :primTrkStartMomTrking : primTrkStartMomTrking/F                    *
  *Entries :     1000 : Total  Size=       4626 bytes  File Size  =        524 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   7.80     *
  *............................................................................*
  *Br   70 :primTrkStartTheta : primTrkStartTheta/F                            *
  *Entries :     1000 : Total  Size=       4606 bytes  File Size  =       3107 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   71 :primTrkStartPhi : primTrkStartPhi/F                                *
  *Entries :     1000 : Total  Size=       4596 bytes  File Size  =       3110 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   72 :primTrkLength : primTrkLength/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3043 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   73 :primTrkStartX : primTrkStartX/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       2982 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.37     *
  *............................................................................*
  *Br   74 :primTrkStartY : primTrkStartY/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3165 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.29     *
  *............................................................................*
  *Br   75 :primTrkStartZ : primTrkStartZ/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       3134 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   76 :primTrkEndX : primTrkEndX/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3042 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.34     *
  *............................................................................*
  *Br   77 :primTrkEndY : primTrkEndY/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3180 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.28     *
  *............................................................................*
  *Br   78 :primTrkEndZ : primTrkEndZ/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3056 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   79 :primTrkCaloKin : primTrkCaloKin/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3101 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.32     *
  *............................................................................*
  *Br   80 :primTrkEndKin : primTrkEndKin/F                                    *
  *Entries :     1000 : Total  Size=       4586 bytes  File Size  =       2945 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.39     *
  *............................................................................*
  *Br   81 :primTrkLLHPion : primTrkLLHPion/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3109 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   82 :primTrkLLHProton : primTrkLLHProton/F                              *
  *Entries :     1000 : Total  Size=       4601 bytes  File Size  =       3112 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   83 :primTrkLLHMuon : primTrkLLHMuon/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3108 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   84 :primTrkLLHKaon : primTrkLLHKaon/F                                  *
  *Entries :     1000 : Total  Size=       4591 bytes  File Size  =       3116 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.31     *
  *............................................................................*
  *Br   85 :primTrkPIDA : primTrkPIDA/F                                        *
  *Entries :     1000 : Total  Size=       4576 bytes  File Size  =       3061 *
  *Baskets :        1 : Basket Size=      32000 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   86 :primTrkdEdxs : vector<float>                                       *
  *Entries :     1000 : Total  Size=     302432 bytes  File Size  =     264059 *
  *Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
  *Br   87 :primTrkResRanges : vector<float>                                   *
  *Entries :     1000 : Total  Size=     302488 bytes  File Size  =     269594 *
  *Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   88 :primTrkKins : vector<float>                                        *
  *Entries :     1000 : Total  Size=     302418 bytes  File Size  =     264879 *
  *Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.14     *
  *............................................................................*
