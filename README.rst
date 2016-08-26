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
  *Tree    :anatree   : analysis tree                                          *
  *Entries :   100000 : Total =     59837345913 bytes  File  Size = 3925879965 *
  *        :          : Tree compression factor =  15.28                       *
  ******************************************************************************
  *Br    0 :run       : run/I                                                  *
  *Entries :   100000 : Total  Size=     418886 bytes  File Size  =      22853 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.14     *
  *............................................................................*
  *Br    1 :subrun    : subrun/I                                               *
  *Entries :   100000 : Total  Size=     419498 bytes  File Size  =      23552 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.63     *
  *............................................................................*
  *Br    2 :event     : event/I                                                *
  *Entries :   100000 : Total  Size=     419294 bytes  File Size  =     165228 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.51     *
  *............................................................................*
  *Br    3 :evttime   : evttime/D                                              *
  *Entries :   100000 : Total  Size=     819710 bytes  File Size  =      25027 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  32.58     *
  *............................................................................*
  *Br    4 :efield    : efield[3]/D                                            *
  *Entries :   100000 : Total  Size=    2419512 bytes  File Size  =      42369 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  57.00     *
  *............................................................................*
  *Br    5 :t0        : t0/I                                                   *
  *Entries :   100000 : Total  Size=     418682 bytes  File Size  =      22783 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.19     *
  *............................................................................*
  *Br    6 :nclus     : nclus/I                                                *
  *Entries :   100000 : Total  Size=     419294 bytes  File Size  =     123734 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   3.35     *
  *............................................................................*
  *Br    7 :clustertwire : clustertwire[nclus]/D                               *
  *Entries :   100000 : Total  Size=    4944061 bytes  File Size  =    1542960 *
  *Baskets :      300 : Basket Size=      47225 bytes  Compression=   3.20     *
  *............................................................................*
  *Br    8 :clusterttick : clusterttick[nclus]/D                               *
  *Entries :   100000 : Total  Size=    4944061 bytes  File Size  =    2755233 *
  *Baskets :      300 : Basket Size=      47225 bytes  Compression=   1.79     *
  *............................................................................*
  *Br    9 :cluendwire : cluendwire[nclus]/D                                   *
  *Entries :   100000 : Total  Size=    4943453 bytes  File Size  =    1490661 *
  *Baskets :      300 : Basket Size=      47225 bytes  Compression=   3.31     *
  *............................................................................*
  *Br   10 :cluendtick : cluendtick[nclus]/D                                   *
  *Entries :   100000 : Total  Size=    4943453 bytes  File Size  =    2737452 *
  *Baskets :      300 : Basket Size=      47225 bytes  Compression=   1.80     *
  *............................................................................*
  *Br   11 :cluplane  : cluplane[nclus]/I                                      *
  *Entries :   100000 : Total  Size=    2676910 bytes  File Size  =     466128 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   5.73     *
  *............................................................................*
  *Br   12 :ntracks_reco : ntracks_reco/I                                      *
  *Entries :   100000 : Total  Size=     420722 bytes  File Size  =      99810 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   4.17     *
  *............................................................................*
  *Br   13 :trkvtxx   : trkvtxx[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1598234 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.18     *
  *............................................................................*
  *Br   14 :trkvtxy   : trkvtxy[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1639147 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.15     *
  *............................................................................*
  *Br   15 :trkvtxz   : trkvtxz[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1631353 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.15     *
  *............................................................................*
  *Br   16 :trkendx   : trkendx[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1605652 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.17     *
  *............................................................................*
  *Br   17 :trkendy   : trkendy[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1638599 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.15     *
  *............................................................................*
  *Br   18 :trkendz   : trkendz[ntracks_reco]/D                                *
  *Entries :   100000 : Total  Size=    1887261 bytes  File Size  =    1606992 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.17     *
  *............................................................................*
  *Br   19 :trkstartdcosx : trkstartdcosx[ntracks_reco]/D                      *
  *Entries :   100000 : Total  Size=    1888485 bytes  File Size  =    1630829 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.16     *
  *............................................................................*
  *Br   20 :trkstartdcosy : trkstartdcosy[ntracks_reco]/D                      *
  *Entries :   100000 : Total  Size=    1888485 bytes  File Size  =    1630877 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.16     *
  *............................................................................*
  *Br   21 :trkstartdcosz : trkstartdcosz[ntracks_reco]/D                      *
  *Entries :   100000 : Total  Size=    1888485 bytes  File Size  =    1596933 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.18     *
  *............................................................................*
  *Br   22 :trkenddcosx : trkenddcosx[ntracks_reco]/D                          *
  *Entries :   100000 : Total  Size=    1888077 bytes  File Size  =    1630151 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.16     *
  *............................................................................*
  *Br   23 :trkenddcosy : trkenddcosy[ntracks_reco]/D                          *
  *Entries :   100000 : Total  Size=    1888077 bytes  File Size  =    1630219 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.16     *
  *............................................................................*
  *Br   24 :trkenddcosz : trkenddcosz[ntracks_reco]/D                          *
  *Entries :   100000 : Total  Size=    1888077 bytes  File Size  =    1606356 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.17     *
  *............................................................................*
  *Br   25 :trkWCtoTPCMath : trkWCtoTPCMath/I                                  *
  *Entries :   100000 : Total  Size=     421130 bytes  File Size  =      24160 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.25     *
  *............................................................................*
  *Br   26 :trklength : trklength[ntracks_reco]/D                              *
  *Entries :   100000 : Total  Size=    1887669 bytes  File Size  =    1614717 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.17     *
  *............................................................................*
  *Br   27 :trkmomrange : trkmomrange[ntracks_reco]/D                          *
  *Entries :   100000 : Total  Size=    1888077 bytes  File Size  =    1607397 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.17     *
  *............................................................................*
  *Br   28 :trkmommschi2 : trkmommschi2[ntracks_reco]/D                        *
  *Entries :   100000 : Total  Size=    1888281 bytes  File Size  =     498688 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   3.78     *
  *............................................................................*
  *Br   29 :trkmommsllhd : trkmommsllhd[ntracks_reco]/D                        *
  *Entries :   100000 : Total  Size=    1888281 bytes  File Size  =     595187 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   3.17     *
  *............................................................................*
  *Br   30 :ntrkhits  : ntrkhits[ntracks_reco]/I                               *
  *Entries :   100000 : Total  Size=    1154534 bytes  File Size  =     506325 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.27     *
  *............................................................................*
  *Br   31 :trkx      : trkx[ntracks_reco][1000]/D                             *
  *Entries :   100000 : Total  Size= 1470248067 bytes  File Size  =  169146151 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.69     *
  *............................................................................*
  *Br   32 :trky      : trky[ntracks_reco][1000]/D                             *
  *Entries :   100000 : Total  Size= 1470248067 bytes  File Size  =  174673806 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.41     *
  *............................................................................*
  *Br   33 :trkz      : trkz[ntracks_reco][1000]/D                             *
  *Entries :   100000 : Total  Size= 1470248067 bytes  File Size  =  173903487 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.45     *
  *............................................................................*
  *Br   34 :trkpitch  : trkpitch[ntracks_reco][2]/D                            *
  *Entries :   100000 : Total  Size=    3353303 bytes  File Size  =    2439706 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.37     *
  *............................................................................*
  *Br   35 :trkhits   : trkhits[ntracks_reco][2]/I                             *
  *Entries :   100000 : Total  Size=    1887252 bytes  File Size  =     724570 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.60     *
  *............................................................................*
  *Br   36 :trkdedx   : trkdedx[ntracks_reco][2][1000]/D                       *
  *Entries :100000 : Total  Size= 2938795157 bytes  File Size  = 184691895 *
  *Baskets :    64102 : Basket Size=   23612631 bytes  Compression=  15.90     *
  *............................................................................*
  *Br   37 :trkrr     : trkrr[ntracks_reco][2][1000]/D                         *
  *Entries :100000 : Total  Size= 2938666945 bytes  File Size  = 183747303 *
  *Baskets :    64102 : Basket Size=   23612631 bytes  Compression=  15.99     *
  *............................................................................*
  *Br   38 :trkpitchhit : trkpitchhit[ntracks_reco][2][1000]/D                 *
  *Entries :100000 : Total  Size= 2939051581 bytes  File Size  = 122017409 *
  *Baskets :    64102 : Basket Size=   23612631 bytes  Compression=  24.08     *
  *............................................................................*
  *Br   39 :trkke     : trkke[ntracks_reco][2]/D                               *
  *Entries :   100000 : Total  Size=    3352691 bytes  File Size  =    2999710 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   40 :trkpida   : trkpida[ntracks_reco][2]/D                             *
  *Entries :   100000 : Total  Size=    3353099 bytes  File Size  =    2996489 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.12     *
  *............................................................................*
  *Br   41 :nTrajPoint : nTrajPoint[ntracks_reco]/I                            *
  *Entries :   100000 : Total  Size=    1154942 bytes  File Size  =     506021 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.27     *
  *............................................................................*
  *Br   42 :pHat0_X   : pHat0_X[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =   84849919 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=  17.32     *
  *............................................................................*
  *Br   43 :pHat0_Y   : pHat0_Y[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =   79964662 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=  18.38     *
  *............................................................................*
  *Br   44 :pHat0_Z   : pHat0_Z[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =   71250292 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=  20.63     *
  *............................................................................*
  *Br   45 :trjPt_X   : trjPt_X[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =  169283430 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.68     *
  *............................................................................*
  *Br   46 :trjPt_Y   : trjPt_Y[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =  174812381 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.41     *
  *............................................................................*
  *Br   47 :trjPt_Z   : trjPt_Z[ntracks_reco][1000]/D                          *
  *Entries :   100000 : Total  Size= 1470366186 bytes  File Size  =  174042229 *
  *Baskets :    39369 : Basket Size=   23612631 bytes  Compression=   8.44     *
  *............................................................................*
  *Br   48 :trkg4id   : trkg4id[ntracks_reco]/I                                *
  *Entries :   100000 : Total  Size=    1154330 bytes  File Size  =     445740 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.58     *
  *............................................................................*
  *Br   49 :primarytrkkey : primarytrkkey/I                                    *
  *Entries :   100000 : Total  Size=     420926 bytes  File Size  =      23960 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.39     *
  *............................................................................*
  *Br   50 :nhits     : nhits/I                                                *
  *Entries :   100000 : Total  Size=     419294 bytes  File Size  =     212933 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   1.95     *
  *............................................................................*
  *Br   51 :hit_plane : hit_plane[nhits]/I                                     *
  *Entries :   100000 : Total  Size=  100157949 bytes  File Size  =    1888130 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  53.02     *
  *............................................................................*
  *Br   52 :hit_wire  : hit_wire[nhits]/I                                      *
  *Entries :   100000 : Total  Size=  100155344 bytes  File Size  =   20302821 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   4.93     *
  *............................................................................*
  *Br   53 :hit_channel : hit_channel[nhits]/I                                 *
  *Entries :   100000 : Total  Size=  100163159 bytes  File Size  =   21195272 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   4.72     *
  *............................................................................*
  *Br   54 :hit_peakT : hit_peakT[nhits]/D                                     *
  *Entries :   100000 : Total  Size=  199910383 bytes  File Size  =   97479164 *
  *Baskets :     5154 : Basket Size=    1814016 bytes  Compression=   2.05     *
  *............................................................................*
  *Br   55 :hit_charge : hit_charge[nhits]/D                                   *
  *Entries :   100000 : Total  Size=  199915865 bytes  File Size  =  112458379 *
  *Baskets :     5157 : Basket Size=    1814528 bytes  Compression=   1.78     *
  *............................................................................*
  *Br   56 :hit_ph    : hit_ph[nhits]/D                                        *
  *Entries :   100000 : Total  Size=  199894909 bytes  File Size  =  111852269 *
  *Baskets :     5154 : Basket Size=    1814016 bytes  Compression=   1.79     *
  *............................................................................*
  *Br   57 :hit_tstart : hit_tstart[nhits]/D                                   *
  *Entries :   100000 : Total  Size=  199915865 bytes  File Size  =   47973482 *
  *Baskets :     5157 : Basket Size=    1814528 bytes  Compression=   4.17     *
  *............................................................................*
  *Br   58 :hit_tend  : hit_tend[nhits]/D                                      *
  *Entries :   100000 : Total  Size=  199905225 bytes  File Size  =   48082522 *
  *Baskets :     5154 : Basket Size=    1814016 bytes  Compression=   4.16     *
  *............................................................................*
  *Br   59 :hit_trkid : hit_trkid[nhits]/I                                     *
  *Entries :   100000 : Total  Size=  100157949 bytes  File Size  =    6745828 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  14.84     *
  *............................................................................*
  *Br   60 :hit_trkkey : hit_trkkey[nhits]/I                                   *
  *Entries :   100000 : Total  Size=  100160554 bytes  File Size  =    6562335 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  15.25     *
  *............................................................................*
  *Br   61 :hit_clukey : hit_clukey[nhits]/I                                   *
  *Entries :   100000 : Total  Size=  100160554 bytes  File Size  =    7865054 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  12.73     *
  *............................................................................*
  *Br   62 :hit_pk    : hit_pk[nhits]/I                                        *
  *Entries :   100000 : Total  Size=  100150134 bytes  File Size  =    6778759 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  14.77     *
  *............................................................................*
  *Br   63 :hit_t     : hit_t[nhits]/I                                         *
  *Entries :   100000 : Total  Size=  100147529 bytes  File Size  =    6754370 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  14.82     *
  *............................................................................*
  *Br   64 :hit_ch    : hit_ch[nhits]/I                                        *
  *Entries :   100000 : Total  Size=  100150134 bytes  File Size  =    7084140 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  14.13     *
  *............................................................................*
  *Br   65 :hit_fwhh  : hit_fwhh[nhits]/I                                      *
  *Entries :   100000 : Total  Size=  100155344 bytes  File Size  =    5274611 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=  18.98     *
  *............................................................................*
  *Br   66 :hit_rms   : hit_rms[nhits]/D                                       *
  *Entries :   100000 : Total  Size=  199900067 bytes  File Size  =   15175200 *
  *Baskets :     5154 : Basket Size=    1814016 bytes  Compression=  13.17     *
  *............................................................................*
  *Br   67 :hit_nelec : hit_nelec[nhits]/D                                     *
  *Entries :   100000 : Total  Size=  199910383 bytes  File Size  =   64753898 *
  *Baskets :     5154 : Basket Size=    1814016 bytes  Compression=   3.09     *
  *............................................................................*
  *Br   68 :hit_energy : hit_energy[nhits]/D                                   *
  *Entries :   100000 : Total  Size=  199915865 bytes  File Size  =   65248672 *
  *Baskets :     5157 : Basket Size=    1814528 bytes  Compression=   3.06     *
  *............................................................................*
  *Br   69 :hit_dQds  : hit_dQds[nhits]/F                                      *
  *Entries :   100000 : Total  Size=  100155351 bytes  File Size  =   78852795 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.27     *
  *............................................................................*
  *Br   70 :hit_dEds  : hit_dEds[nhits]/F                                      *
  *Entries :   100000 : Total  Size=  100155351 bytes  File Size  =   80531607 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.24     *
  *............................................................................*
  *Br   71 :hit_ds    : hit_ds[nhits]/F                                        *
  *Entries :   100000 : Total  Size=  100150141 bytes  File Size  =   75126002 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.33     *
  *............................................................................*
  *Br   72 :hit_resrange : hit_resrange[nhits]/F                               *
  *Entries :   100000 : Total  Size=  100165771 bytes  File Size  =   79570241 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.26     *
  *............................................................................*
  *Br   73 :hit_x     : hit_x[nhits]/F                                         *
  *Entries :   100000 : Total  Size=  100147536 bytes  File Size  =   76862609 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.30     *
  *............................................................................*
  *Br   74 :hit_y     : hit_y[nhits]/F                                         *
  *Entries :   100000 : Total  Size=  100147536 bytes  File Size  =   80816000 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.24     *
  *............................................................................*
  *Br   75 :hit_z     : hit_z[nhits]/F                                         *
  *Entries :   100000 : Total  Size=  100147536 bytes  File Size  =   79392135 *
  *Baskets :     2601 : Basket Size=     908800 bytes  Compression=   1.26     *
  *............................................................................*
  *Br   76 :nwctrks   : nwctrks/I                                              *
  *Entries :   100000 : Total  Size=     419702 bytes  File Size  =      22760 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.25     *
  *............................................................................*
  *Br   77 :wctrk_XFaceCoor : wctrk_XFaceCoor[nwctrks]/D                       *
  *Entries :   100000 : Total  Size=     423041 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   78 :wctrk_YFaceCoor : wctrk_YFaceCoor[nwctrks]/D                       *
  *Entries :   100000 : Total  Size=     423041 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   79 :wctrk_momentum : wctrk_momentum[nwctrks]/D                         *
  *Entries :   100000 : Total  Size=     422837 bytes  File Size  =      25991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.10     *
  *............................................................................*
  *Br   80 :wctrk_theta : wctrk_theta[nwctrks]/D                               *
  *Entries :   100000 : Total  Size=     422225 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br   81 :wctrk_phi : wctrk_phi[nwctrks]/D                                   *
  *Entries :   100000 : Total  Size=     421817 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   82 :wctrk_XDist : wctrk_XDist[nwctrks]/D                               *
  *Entries :   100000 : Total  Size=     422225 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br   83 :wctrk_YDist : wctrk_YDist[nwctrks]/D                               *
  *Entries :   100000 : Total  Size=     422225 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br   84 :wctrk_ZDist : wctrk_ZDist[nwctrks]/D                               *
  *Entries :   100000 : Total  Size=     422225 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br   85 :XWireHist : XWireHist[nwctrks][1000]/D                             *
  *Entries :   100000 : Total  Size=     421829 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   86 :YWireHist : YWireHist[nwctrks][1000]/D                             *
  *Entries :   100000 : Total  Size=     421829 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   87 :XAxisHist : XAxisHist[nwctrks][1000]/D                             *
  *Entries :   100000 : Total  Size=     421829 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   88 :YAxisHist : YAxisHist[nwctrks][1000]/D                             *
  *Entries :   100000 : Total  Size=     421829 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   89 :Y_Kink    : Y_Kink[nwctrks]/D                                      *
  *Entries :   100000 : Total  Size=     421205 bytes  File Size  =      24394 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.09     *
  *............................................................................*
  *Br   90 :ntof      : ntof/I                                                 *
  *Entries :   100000 : Total  Size=     419090 bytes  File Size  =      22160 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.72     *
  *............................................................................*
  *Br   91 :tofObject : tofObject[ntof]/D                                      *
  *Entries :   100000 : Total  Size=     421805 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br   92 :tof_timestamp : tof_timestamp[ntof]/D                              *
  *Entries :   100000 : Total  Size=     422621 bytes  File Size  =      25791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.21     *
  *............................................................................*
  *Br   93 :nAG       : nAG/I                                                  *
  *Entries :   100000 : Total  Size=     418886 bytes  File Size  =      21960 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.88     *
  *............................................................................*
  *Br   94 :HitTimeStampUSE : HitTimeStampUSE[nAG]/D                           *
  *Entries :   100000 : Total  Size=     423025 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   95 :HitTimeStampUSW : HitTimeStampUSW[nAG]/D                           *
  *Entries :   100000 : Total  Size=     423025 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   96 :HitTimeStampDS1 : HitTimeStampDS1[nAG]/D                           *
  *Entries :   100000 : Total  Size=     423025 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   97 :HitTimeStampDS2 : HitTimeStampDS2[nAG]/D                           *
  *Entries :   100000 : Total  Size=     423025 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   98 :HitPulseAreaUSE : HitPulseAreaUSE[nAG]/F                           *
  *Entries :   100000 : Total  Size=     423017 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br   99 :HitPulseAreaUSW : HitPulseAreaUSW[nAG]/F                           *
  *Entries :   100000 : Total  Size=     423017 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  100 :HitPulseAreaDS1 : HitPulseAreaDS1[nAG]/F                           *
  *Entries :   100000 : Total  Size=     423017 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  101 :HitPulseAreaDS2 : HitPulseAreaDS2[nAG]/F                           *
  *Entries :   100000 : Total  Size=     423017 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  102 :HitExistUSE : HitExistUSE[nAG]/O                                   *
  *Entries :   100000 : Total  Size=     422195 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  103 :HitExistUSW : HitExistUSW[nAG]/O                                   *
  *Entries :   100000 : Total  Size=     422195 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  104 :HitExistDS1 : HitExistDS1[nAG]/O                                   *
  *Entries :   100000 : Total  Size=     422195 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  105 :HitExistDS2 : HitExistDS2[nAG]/O                                   *
  *Entries :   100000 : Total  Size=     422195 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  106 :no_primaries : no_primaries/I                                      *
  *Entries :   100000 : Total  Size=     420722 bytes  File Size  =      24653 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.89     *
  *............................................................................*
  *Br  107 :geant_list_size : geant_list_size/I                                *
  *Entries :   100000 : Total  Size=     421334 bytes  File Size  =     172150 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.42     *
  *............................................................................*
  *Br  108 :pdg       : pdg[geant_list_size]/I                                 *
  *Entries :   100000 : Total  Size=   16281957 bytes  File Size  =    4371645 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=   3.72     *
  *............................................................................*
  *Br  109 :Eng       : Eng[geant_list_size]/D                                 *
  *Entries :   100000 : Total  Size=   32143319 bytes  File Size  =   29038537 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.11     *
  *............................................................................*
  *Br  110 :Px        : Px[geant_list_size]/D                                  *
  *Entries :   100000 : Total  Size=   32142381 bytes  File Size  =   30776316 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.04     *
  *............................................................................*
  *Br  111 :Py        : Py[geant_list_size]/D                                  *
  *Entries :   100000 : Total  Size=   32142381 bytes  File Size  =   30775921 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.04     *
  *............................................................................*
  *Br  112 :Pz        : Pz[geant_list_size]/D                                  *
  *Entries :   100000 : Total  Size=   32142381 bytes  File Size  =   30779737 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.04     *
  *............................................................................*
  *Br  113 :EndEng    : EndEng[geant_list_size]/D                              *
  *Entries :   100000 : Total  Size=   32146133 bytes  File Size  =   14239202 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   2.26     *
  *............................................................................*
  *Br  114 :EndPx     : EndPx[geant_list_size]/D                               *
  *Entries :   100000 : Total  Size=   32145195 bytes  File Size  =   10640032 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   3.02     *
  *............................................................................*
  *Br  115 :EndPy     : EndPy[geant_list_size]/D                               *
  *Entries :   100000 : Total  Size=   32145195 bytes  File Size  =   10639757 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   3.02     *
  *............................................................................*
  *Br  116 :EndPz     : EndPz[geant_list_size]/D                               *
  *Entries :   100000 : Total  Size=   32145195 bytes  File Size  =   10625331 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   3.02     *
  *............................................................................*
  *Br  117 :StartPointx : StartPointx[geant_list_size]/D                       *
  *Entries :   100000 : Total  Size=   32150823 bytes  File Size  =   12403144 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   2.59     *
  *............................................................................*
  *Br  118 :StartPointy : StartPointy[geant_list_size]/D                       *
  *Entries :   100000 : Total  Size=   32150823 bytes  File Size  =   12529900 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   2.56     *
  *............................................................................*
  *Br  119 :StartPointz : StartPointz[geant_list_size]/D                       *
  *Entries :   100000 : Total  Size=   32150823 bytes  File Size  =   12054670 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   2.67     *
  *............................................................................*
  *Br  120 :EndPointx : EndPointx[geant_list_size]/D                           *
  *Entries :   100000 : Total  Size=   32148947 bytes  File Size  =   28795313 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.12     *
  *............................................................................*
  *Br  121 :EndPointy : EndPointy[geant_list_size]/D                           *
  *Entries :   100000 : Total  Size=   32148947 bytes  File Size  =   27779867 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.16     *
  *............................................................................*
  *Br  122 :EndPointz : EndPointz[geant_list_size]/D                           *
  *Entries :   100000 : Total  Size=   32148947 bytes  File Size  =   30202302 *
  *Baskets :      934 : Basket Size=     293888 bytes  Compression=   1.06     *
  *............................................................................*
  *Br  123 :Process   : Process[geant_list_size]/I                             *
  *Entries :   100000 : Total  Size=   16284241 bytes  File Size  =    1941012 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=   8.38     *
  *............................................................................*
  *Br  124 :NumberDaughters : NumberDaughters[geant_list_size]/I               *
  *Entries :   100000 : Total  Size=   16288809 bytes  File Size  =    2333734 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=   6.97     *
  *............................................................................*
  *Br  125 :Mother    : Mother[geant_list_size]/I                              *
  *Entries :   100000 : Total  Size=   16283670 bytes  File Size  =    2840041 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=   5.73     *
  *............................................................................*
  *Br  126 :TrackId   : TrackId[geant_list_size]/I                             *
  *Entries :   100000 : Total  Size=   16284241 bytes  File Size  =    3091913 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=   5.26     *
  *............................................................................*
  *Br  127 :process_primary : process_primary[geant_list_size]/I               *
  *Entries :   100000 : Total  Size=   16288809 bytes  File Size  =     745558 *
  *Baskets :      567 : Basket Size=     148992 bytes  Compression=  21.83     *
  *............................................................................*
  *Br  128 :G4Process : vector<string>                                         *
  *Entries :   100000 : Total  Size=   57026250 bytes  File Size  =    3364381 *
  *Baskets :     1557 : Basket Size=     523264 bytes  Compression=  16.94     *
  *............................................................................*
  *Br  129 :G4FinalProcess : vector<string>                                    *
  *Entries :   100000 : Total  Size=   83853637 bytes  File Size  =    6163013 *
  *Baskets :     2224 : Basket Size=     765440 bytes  Compression=  13.60     *
  *............................................................................*
  *Br  130 :NTrTrajPts : NTrTrajPts[no_primaries]/I                            *
  *Entries :   100000 : Total  Size=     822026 bytes  File Size  =     323304 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=   2.53     *
  *............................................................................*
  *Br  131 :MidPosX   : MidPosX[no_primaries][5000]/D                          *
  *Entries :100000 : Total  Size= 4008521036 bytes  File Size  = 67165898 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  59.66     *
  *............................................................................*
  *Br  132 :MidPosY   : MidPosY[no_primaries][5000]/D                          *
  *Entries :100000 : Total  Size= 4008521036 bytes  File Size  = 67868574 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  59.04     *
  *............................................................................*
  *Br  133 :MidPosZ   : MidPosZ[no_primaries][5000]/D                          *
  *Entries :100000 : Total  Size= 4008521036 bytes  File Size  = 67789503 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  59.11     *
  *............................................................................*
  *Br  134 :MidPx     : MidPx[no_primaries][5000]/D                            *
  *Entries :100000 : Total  Size= 4008366350 bytes  File Size  = 64356614 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  62.26     *
  *............................................................................*
  *Br  135 :MidPy     : MidPy[no_primaries][5000]/D                            *
  *Entries :100000 : Total  Size= 4008366350 bytes  File Size  = 64426387 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  62.19     *
  *............................................................................*
  *Br  136 :MidPz     : MidPz[no_primaries][5000]/D                            *
  *Entries :100000 : Total  Size= 4008366350 bytes  File Size  = 63031381 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  63.57     *
  *............................................................................*
  *Br  137 :no_mcshowers : no_mcshowers/I                                      *
  *Entries :   100000 : Total  Size=     420722 bytes  File Size  =      23760 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.53     *
  *............................................................................*
  *Br  138 :mcshwr_origin : mcshwr_origin[no_mcshowers]/D                      *
  *Entries :   100000 : Total  Size=     422653 bytes  File Size  =      25791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.21     *
  *............................................................................*
  *Br  139 :mcshwr_pdg : mcshwr_pdg[no_mcshowers]/D                            *
  *Entries :   100000 : Total  Size=     422041 bytes  File Size  =      25193 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.58     *
  *............................................................................*
  *Br  140 :mcshwr_TrackId : mcshwr_TrackId[no_mcshowers]/I                    *
  *Entries :   100000 : Total  Size=     422842 bytes  File Size  =      25991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.10     *
  *............................................................................*
  *Br  141 :mcshwr_startX : mcshwr_startX[no_mcshowers]/D                      *
  *Entries :   100000 : Total  Size=     422653 bytes  File Size  =      25791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.21     *
  *............................................................................*
  *Br  142 :mcshwr_startY : mcshwr_startY[no_mcshowers]/D                      *
  *Entries :   100000 : Total  Size=     422653 bytes  File Size  =      25791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.21     *
  *............................................................................*
  *Br  143 :mcshwr_startZ : mcshwr_startZ[no_mcshowers]/D                      *
  *Entries :   100000 : Total  Size=     422653 bytes  File Size  =      25791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.21     *
  *............................................................................*
  *Br  144 :mcshwr_endX : mcshwr_endX[no_mcshowers]/D                          *
  *Entries :   100000 : Total  Size=     422245 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  145 :mcshwr_endY : mcshwr_endY[no_mcshowers]/D                          *
  *Entries :   100000 : Total  Size=     422245 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  146 :mcshwr_endZ : mcshwr_endZ[no_mcshowers]/D                          *
  *Entries :   100000 : Total  Size=     422245 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  147 :mcshwr_CombEngX : mcshwr_CombEngX[no_mcshowers]/D                  *
  *Entries :   100000 : Total  Size=     423061 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  148 :mcshwr_CombEngY : mcshwr_CombEngY[no_mcshowers]/D                  *
  *Entries :   100000 : Total  Size=     423061 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  149 :mcshwr_CombEngZ : mcshwr_CombEngZ[no_mcshowers]/D                  *
  *Entries :   100000 : Total  Size=     423061 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  150 :mcshwr_CombEngPx : mcshwr_CombEngPx[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  151 :mcshwr_CombEngPy : mcshwr_CombEngPy[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  152 :mcshwr_CombEngPz : mcshwr_CombEngPz[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  153 :mcshwr_CombEngE : mcshwr_CombEngE[no_mcshowers]/D                  *
  *Entries :   100000 : Total  Size=     423061 bytes  File Size  =      26191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.98     *
  *............................................................................*
  *Br  154 :mcshwr_dEdx : mcshwr_dEdx[no_mcshowers]/D                          *
  *Entries :   100000 : Total  Size=     422245 bytes  File Size  =      25392 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.45     *
  *............................................................................*
  *Br  155 :mcshwr_StartDirX : mcshwr_StartDirX[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  156 :mcshwr_StartDirY : mcshwr_StartDirY[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  157 :mcshwr_StartDirZ : mcshwr_StartDirZ[no_mcshowers]/D                *
  *Entries :   100000 : Total  Size=     423265 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  158 :mcshwr_isEngDeposited : mcshwr_isEngDeposited[no_mcshowers]/I      *
  *Entries :   100000 : Total  Size=     424270 bytes  File Size  =      27391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.33     *
  *............................................................................*
  *Br  159 :mcshwr_Motherpdg : mcshwr_Motherpdg[no_mcshowers]/I                *
  *Entries :   100000 : Total  Size=     423250 bytes  File Size  =      26391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.87     *
  *............................................................................*
  *Br  160 :mcshwr_MotherTrkId : mcshwr_MotherTrkId[no_mcshowers]/I            *
  *Entries :   100000 : Total  Size=     423658 bytes  File Size  =      26791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.65     *
  *............................................................................*
  *Br  161 :mcshwr_MotherstartX : mcshwr_MotherstartX[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  162 :mcshwr_MotherstartY : mcshwr_MotherstartY[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  163 :mcshwr_MotherstartZ : mcshwr_MotherstartZ[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  164 :mcshwr_MotherendX : mcshwr_MotherendX[no_mcshowers]/I              *
  *Entries :   100000 : Total  Size=     423454 bytes  File Size  =      26591 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.76     *
  *............................................................................*
  *Br  165 :mcshwr_MotherendY : mcshwr_MotherendY[no_mcshowers]/I              *
  *Entries :   100000 : Total  Size=     423454 bytes  File Size  =      26591 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.76     *
  *............................................................................*
  *Br  166 :mcshwr_MotherendZ : mcshwr_MotherendZ[no_mcshowers]/I              *
  *Entries :   100000 : Total  Size=     423454 bytes  File Size  =      26591 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.76     *
  *............................................................................*
  *Br  167 :mcshwr_Ancestorpdg : mcshwr_Ancestorpdg[no_mcshowers]/I            *
  *Entries :   100000 : Total  Size=     423658 bytes  File Size  =      26791 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.65     *
  *............................................................................*
  *Br  168 :mcshwr_AncestorTrkId : mcshwr_AncestorTrkId[no_mcshowers]/I        *
  *Entries :   100000 : Total  Size=     424066 bytes  File Size  =      27191 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.43     *
  *............................................................................*
  *Br  169 :mcshwr_AncestorstartX : mcshwr_AncestorstartX[no_mcshowers]/I      *
  *Entries :   100000 : Total  Size=     424270 bytes  File Size  =      27391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.33     *
  *............................................................................*
  *Br  170 :mcshwr_AncestorstartY : mcshwr_AncestorstartY[no_mcshowers]/I      *
  *Entries :   100000 : Total  Size=     424270 bytes  File Size  =      27391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.33     *
  *............................................................................*
  *Br  171 :mcshwr_AncestorstartZ : mcshwr_AncestorstartZ[no_mcshowers]/I      *
  *Entries :   100000 : Total  Size=     424270 bytes  File Size  =      27391 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.33     *
  *............................................................................*
  *Br  172 :mcshwr_AncestorendX : mcshwr_AncestorendX[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  173 :mcshwr_AncestorendY : mcshwr_AncestorendY[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  174 :mcshwr_AncestorendZ : mcshwr_AncestorendZ[no_mcshowers]/I          *
  *Entries :   100000 : Total  Size=     423862 bytes  File Size  =      26991 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  15.54     *
  *............................................................................*
  *Br  175 :nshowers  : nshowers/I                                             *
  *Entries :   100000 : Total  Size=     419906 bytes  File Size  =      22960 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  18.10     *
  *............................................................................*
  *Br  176 :shwID     : shwI[nshowers]/I                                       *
  *Entries :   100000 : Total  Size=     420987 bytes  File Size  =      24194 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  17.22     *
  *............................................................................*
  *Br  177 :BestPlaneShw : BestPlaneShw[nshowers]/I                            *
  *Entries :   100000 : Total  Size=     422418 bytes  File Size  =      25591 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.33     *
  *............................................................................*
  *Br  178 :LengthShw : LengthShw[nshowers]/D                                  *
  *Entries :   100000 : Total  Size=     421821 bytes  File Size  =      24993 *
  *Baskets :      200 : Basket Size=      47225 bytes  Compression=  16.70     *
  *............................................................................*
  *Br  179 :CosStartShw : CosStartShw[3][1000]/D                               *
  *Entries :100000 : Total  Size= 2407811583 bytes  File Size  = 41997108 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  57.30     *
  *............................................................................*
  *Br  180 :CosStartXYZShw : CosStartXYZShw[3][1000]/D                         *
  *Entries :100000 : Total  Size= 2408043612 bytes  File Size  = 41242943 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  58.35     *
  *............................................................................*
  *Br  181 :TotalEShw : TotalEShw[2][1000]/D                                   *
  *Entries :   100000 : Total  Size= 1607656897 bytes  File Size  =   35184419 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  45.65     *
  *............................................................................*
  *Br  182 :dEdxPerPlaneShw : dEdxPerPlaneShw[2][1000]/D                       *
  *Entries :   100000 : Total  Size= 1608120955 bytes  File Size  =   35767562 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  44.92     *
  *............................................................................*
  *Br  183 :TotalMIPEShw : TotalMIPEShw[2][1000]/D                             *
  *Entries :   100000 : Total  Size= 1607888926 bytes  File Size  =   35284839 *
  *Baskets :    77339 : Basket Size=   23612631 bytes  Compression=  45.52     *
  *............................................................................*
  
