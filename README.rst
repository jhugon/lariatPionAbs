protoDUNE Pion Absorption Analysis
==================================

This branch holds code for the protoDUNE pion absorption analysis. The code
here processes the anaTree files produced by dunetpc.

The .C parts of the code are meant to create tree friends for the main anaTrees
with higher-level variables. the .py parts of the code use tree.Draw() to
create histograms and paint them to image files

Tree Info
---------

in the file it is usually "analysistree/anatree" and the branches are:

  ::

  *Br    0 :run       : run/I                                                  *
  *Br    1 :subrun    : subrun/I                                               *
  *Br    2 :event     : event/I                                                *
  *Br    3 :evttime   : evttime/D                                              *
  *Br    4 :beamtime  : beamtime/D                                             *
  *Br    5 :pot       : pot/D                                                  *
  *Br    6 :isdata    : isdata/B                                               *
  *Br    7 :taulife   : taulife/D                                              *
  *Br    8 :triggernumber : triggernumber/i                                    *
  *Br    9 :triggertime : triggertime/D                                        *
  *Br   10 :beamgatetime : beamgatetime/D                                      *
  *Br   11 :triggerbits : triggerbits/i                                        *
  *Br   12 :potbnb    : potbnb/D                                               *
  *Br   13 :potnumitgt : potnumitgt/D                                          *
  *Br   14 :potnumi101 : potnumi101/D                                          *
  *Br   15 :no_hits   : no_hits/I                                              *
  *Br   16 :no_hits_stored : no_hits_stored/I                                  *
  *Br   17 :hit_tpc   : hit_tpc[no_hits_stored]/S                              *
  *Br   18 :hit_plane : hit_plane[no_hits_stored]/S                            *
  *Br   19 :hit_wire  : hit_wire[no_hits_stored]/S                             *
  *Br   20 :hit_channel : hit_channel[no_hits_stored]/S                        *
  *Br   21 :hit_peakT : hit_peakT[no_hits_stored]/F                            *
  *Br   22 :hit_charge : hit_charge[no_hits_stored]/F                          *
  *Br   23 :hit_ph    : hit_ph[no_hits_stored]/F                               *
  *Br   24 :hit_startT : hit_startT[no_hits_stored]/F                          *
  *Br   25 :hit_endT  : hit_endT[no_hits_stored]/F                             *
  *Br   26 :hit_rms   : hit_rms[no_hits_stored]/F                              *
  *Br   27 :hit_trueX : hit_trueX[no_hits_stored]/F                            *
  *Br   28 :hit_goodnessOfFit : hit_goodnessOfFit[no_hits_stored]/F            *
  *Br   29 :hit_multiplicity : hit_multiplicity[no_hits_stored]/S              *
  *Br   30 :hit_trkid : hit_trkid[no_hits_stored]/S                            *
  *Br   31 :hit_trkKey : hit_trkKey[no_hits_stored]/S                          *
  *Br   32 :hit_clusterid : hit_clusterid[no_hits_stored]/S                    *
  *Br   33 :hit_clusterKey : hit_clusterKey[no_hits_stored]/S                  *
  *Br   34 :hit_nelec : hit_nelec[no_hits_stored]/F                            *
  *Br   35 :hit_energy : hit_energy[no_hits_stored]/F                          *
  *Br   36 :nclusters : nclusters/S                                            *
  *Br   37 :clusterId : clusterId[nclusters]/S                                 *
  *Br   38 :clusterView : clusterView[nclusters]/S                             *
  *Br   39 :cluster_StartCharge : cluster_StartCharge[nclusters]/F             *
  *Br   40 :cluster_StartAngle : cluster_StartAngle[nclusters]/F               *
  *Br   41 :cluster_EndCharge : cluster_EndCharge[nclusters]/F                 *
  *Br   42 :cluster_EndAngle : cluster_EndAngle[nclusters]/F                   *
  *Br   43 :cluster_Integral : cluster_Integral[nclusters]/F                   *
  *Br   44 :cluster_IntegralAverage : cluster_IntegralAverage[nclusters]/F     *
  *Br   45 :cluster_SummedADC : cluster_SummedADC[nclusters]/F                 *
  *Br   46 :cluster_SummedADCaverage : cluster_SummedADCaverage[nclusters]/F   *
  *Br   47 :cluster_MultipleHitDensity :                                       *
  *         | cluster_MultipleHitDensity[nclusters]/F                          *
  *Br   48 :cluster_Width : cluster_Width[nclusters]/F                         *
  *Br   49 :cluster_NHits : cluster_NHits[nclusters]/S                         *
  *Br   50 :cluster_StartWire : cluster_StartWire[nclusters]/S                 *
  *Br   51 :cluster_StartTick : cluster_StartTick[nclusters]/S                 *
  *Br   52 :cluster_EndWire : cluster_EndWire[nclusters]/S                     *
  *Br   53 :cluster_EndTick : cluster_EndTick[nclusters]/S                     *
  *Br   54 :cluncosmictags_tagger : cluncosmictags_tagger[nclusters]/S         *
  *Br   55 :clucosmicscore_tagger : clucosmicscore_tagger[nclusters]/F         *
  *Br   56 :clucosmictype_tagger : clucosmictype_tagger[nclusters]/S           *
  *Br   57 :no_flashes : no_flashes/I                                          *
  *Br   58 :flash_time : flash_time[no_flashes]/F                              *
  *Br   59 :flash_pe  : flash_pe[no_flashes]/F                                 *
  *Br   60 :flash_ycenter : flash_ycenter[no_flashes]/F                        *
  *Br   61 :flash_zcenter : flash_zcenter[no_flashes]/F                        *
  *Br   62 :flash_ywidth : flash_ywidth[no_flashes]/F                          *
  *Br   63 :flash_zwidth : flash_zwidth[no_flashes]/F                          *
  *Br   64 :flash_timewidth : flash_timewidth[no_flashes]/F                    *
  *Br   65 :no_ExternCounts : no_ExternCounts/I                                *
  *Br   66 :externcounts_time : externcounts_time[no_ExternCounts]/F           *
  *Br   67 :externcounts_id : externcounts_id[no_ExternCounts]/F               *
  *Br   68 :kNTracker : kNTracker/B                                            *
  *Br   69 :kNVertexAlgos : kNVertexAlgos/B                                    *
  *Br   70 :mcevts_truthcry : mcevts_truthcry/I                                *
  *Br   71 :cry_no_primaries : cry_no_primaries/I                              *
  *Br   72 :cry_primaries_pdg : cry_primaries_pdg[cry_no_primaries]/I          *
  *Br   73 :cry_Eng   : cry_Eng[cry_no_primaries]/F                            *
  *Br   74 :cry_Px    : cry_Px[cry_no_primaries]/F                             *
  *Br   75 :cry_Py    : cry_Py[cry_no_primaries]/F                             *
  *Br   76 :cry_Pz    : cry_Pz[cry_no_primaries]/F                             *
  *Br   77 :cry_P     : cry_P[cry_no_primaries]/F                              *
  *Br   78 :cry_StartPointx : cry_StartPointx[cry_no_primaries]/F              *
  *Br   79 :cry_StartPointy : cry_StartPointy[cry_no_primaries]/F              *
  *Br   80 :cry_StartPointz : cry_StartPointz[cry_no_primaries]/F              *
  *Br   81 :cry_StartPointt : cry_StartPointt[cry_no_primaries]/F              *
  *Br   82 :cry_status_code : cry_status_code[cry_no_primaries]/I              *
  *Br   83 :cry_mass  : cry_mass[cry_no_primaries]/F                           *
  *Br   84 :cry_trackID : cry_trackID[cry_no_primaries]/I                      *
  *Br   85 :cry_ND    : cry_ND[cry_no_primaries]/I                             *
  *Br   86 :cry_mother : cry_mother[cry_no_primaries]/I                        *
  *Br   87 :no_primaries : no_primaries/I                                      *
  *Br   88 :geant_list_size : geant_list_size/I                                *
  *Br   89 :geant_list_size_in_tpcAV : geant_list_size_in_tpcAV/I              *
  *Br   90 :pdg       : pdg[geant_list_size]/I                                 *
  *Br   91 :status    : status[geant_list_size]/I                              *
  *Br   92 :Mass      : Mass[geant_list_size]/F                                *
  *Br   93 :Eng       : Eng[geant_list_size]/F                                 *
  *Br   94 :EndE      : EndE[geant_list_size]/F                                *
  *Br   95 :Px        : Px[geant_list_size]/F                                  *
  *Br   96 :Py        : Py[geant_list_size]/F                                  *
  *Br   97 :Pz        : Pz[geant_list_size]/F                                  *
  *Br   98 :P         : P[geant_list_size]/F                                   *
  *Br   99 :StartPointx : StartPointx[geant_list_size]/F                       *
  *Br  100 :StartPointy : StartPointy[geant_list_size]/F                       *
  *Br  101 :StartPointz : StartPointz[geant_list_size]/F                       *
  *Br  102 :StartT    : StartT[geant_list_size]/F                              *
  *Br  103 :EndPointx : EndPointx[geant_list_size]/F                           *
  *Br  104 :EndPointy : EndPointy[geant_list_size]/F                           *
  *Br  105 :EndPointz : EndPointz[geant_list_size]/F                           *
  *Br  106 :EndT      : EndT[geant_list_size]/F                                *
  *Br  107 :theta     : theta[geant_list_size]/F                               *
  *Br  108 :phi       : phi[geant_list_size]/F                                 *
  *Br  109 :theta_xz  : theta_xz[geant_list_size]/F                            *
  *Br  110 :theta_yz  : theta_yz[geant_list_size]/F                            *
  *Br  111 :pathlen   : pathlen[geant_list_size]/F                             *
  *Br  112 :inTPCActive : inTPCActive[geant_list_size]/I                       *
  *Br  113 :StartPointx_tpcAV : StartPointx_tpcAV[geant_list_size]/F           *
  *Br  114 :StartPointy_tpcAV : StartPointy_tpcAV[geant_list_size]/F           *
  *Br  115 :StartPointz_tpcAV : StartPointz_tpcAV[geant_list_size]/F           *
  *Br  116 :StartT_tpcAV : StartT_tpcAV[geant_list_size]/F                     *
  *Br  117 :StartE_tpcAV : StartE_tpcAV[geant_list_size]/F                     *
  *Br  118 :StartP_tpcAV : StartP_tpcAV[geant_list_size]/F                     *
  *Br  119 :StartPx_tpcAV : StartPx_tpcAV[geant_list_size]/F                   *
  *Br  120 :StartPy_tpcAV : StartPy_tpcAV[geant_list_size]/F                   *
  *Br  121 :StartPz_tpcAV : StartPz_tpcAV[geant_list_size]/F                   *
  *Br  122 :EndPointx_tpcAV : EndPointx_tpcAV[geant_list_size]/F               *
  *Br  123 :EndPointy_tpcAV : EndPointy_tpcAV[geant_list_size]/F               *
  *Br  124 :EndPointz_tpcAV : EndPointz_tpcAV[geant_list_size]/F               *
  *Br  125 :EndT_tpcAV : EndT_tpcAV[geant_list_size]/F                         *
  *Br  126 :EndE_tpcAV : EndE_tpcAV[geant_list_size]/F                         *
  *Br  127 :EndP_tpcAV : EndP_tpcAV[geant_list_size]/F                         *
  *Br  128 :EndPx_tpcAV : EndPx_tpcAV[geant_list_size]/F                       *
  *Br  129 :EndPy_tpcAV : EndPy_tpcAV[geant_list_size]/F                       *
  *Br  130 :EndPz_tpcAV : EndPz_tpcAV[geant_list_size]/F                       *
  *Br  131 :pathlen_drifted : pathlen_drifted[geant_list_size]/F               *
  *Br  132 :inTPCDrifted : inTPCDrifted[geant_list_size]/I                     *
  *Br  133 :StartPointx_drifted : StartPointx_drifted[geant_list_size]/F       *
  *Br  134 :StartPointy_drifted : StartPointy_drifted[geant_list_size]/F       *
  *Br  135 :StartPointz_drifted : StartPointz_drifted[geant_list_size]/F       *
  *Br  136 :StartT_drifted : StartT_drifted[geant_list_size]/F                 *
  *Br  137 :StartE_drifted : StartE_drifted[geant_list_size]/F                 *
  *Br  138 :StartP_drifted : StartP_drifted[geant_list_size]/F                 *
  *Br  139 :StartPx_drifted : StartPx_drifted[geant_list_size]/F               *
  *Br  140 :StartPy_drifted : StartPy_drifted[geant_list_size]/F               *
  *Br  141 :StartPz_drifted : StartPz_drifted[geant_list_size]/F               *
  *Br  142 :EndPointx_drifted : EndPointx_drifted[geant_list_size]/F           *
  *Br  143 :EndPointy_drifted : EndPointy_drifted[geant_list_size]/F           *
  *Br  144 :EndPointz_drifted : EndPointz_drifted[geant_list_size]/F           *
  *Br  145 :EndT_drifted : EndT_drifted[geant_list_size]/F                     *
  *Br  146 :EndE_drifted : EndE_drifted[geant_list_size]/F                     *
  *Br  147 :EndP_drifted : EndP_drifted[geant_list_size]/F                     *
  *Br  148 :EndPx_drifted : EndPx_drifted[geant_list_size]/F                   *
  *Br  149 :EndPy_drifted : EndPy_drifted[geant_list_size]/F                   *
  *Br  150 :EndPz_drifted : EndPz_drifted[geant_list_size]/F                   *
  *Br  151 :NumberDaughters : NumberDaughters[geant_list_size]/I               *
  *Br  152 :Mother    : Mother[geant_list_size]/I                              *
  *Br  153 :TrackId   : TrackId[geant_list_size]/I                             *
  *Br  154 :MergedId  : MergedId[geant_list_size]/I                            *
  *Br  155 :origin    : origin[geant_list_size]/I                              *
  *Br  156 :MCTruthIndex : MCTruthIndex[geant_list_size]/I                     *
  *Br  157 :process_primary : process_primary[geant_list_size]/I               *
  *Br  158 :processname : vector<string>                                       *
  *Br  159 :ntracks_pmtrack : ntracks_pmtrack/S                                *
  *Br  160 :trkId_pmtrack : trkId_pmtrack[ntracks_pmtrack]/S                   *
  *Br  161 :trkncosmictags_tagger_pmtrack :                                    *
  *         | trkncosmictags_tagger_pmtrack[ntracks_pmtrack]/S                 *
  *Br  162 :trkcosmicscore_tagger_pmtrack :                                    *
  *         | trkcosmicscore_tagger_pmtrack[ntracks_pmtrack]/F                 *
  *Br  163 :trkcosmictype_tagger_pmtrack :                                     *
  *         | trkcosmictype_tagger_pmtrack[ntracks_pmtrack]/S                  *
  *Br  164 :trkncosmictags_containmenttagger_pmtrack :                         *
  *         | trkncosmictags_containmenttagger_pmtrack[ntracks_pmtrack]/S      *
  *Br  165 :trkcosmicscore_containmenttagger_pmtrack :                         *
  *         | trkcosmicscore_containmenttagger_pmtrack[ntracks_pmtrack]/F      *
  *Br  166 :trkcosmictype_containmenttagger_pmtrack :                          *
  *         | trkcosmictype_containmenttagger_pmtrack[ntracks_pmtrack]/S       *
  *Br  167 :trkncosmictags_flashmatch_pmtrack :                                *
  *         | trkncosmictags_flashmatch_pmtrack[ntracks_pmtrack]/S             *
  *Br  168 :trkcosmicscore_flashmatch_pmtrack :                                *
  *         | trkcosmicscore_flashmatch_pmtrack[ntracks_pmtrack]/F             *
  *Br  169 :trkcosmictype_flashmatch_pmtrack :                                 *
  *         | trkcosmictype_flashmatch_pmtrack[ntracks_pmtrack]/S              *
  *Br  170 :trkke_pmtrack : trkke_pmtrack[ntracks_pmtrack][3]/F                *
  *Br  171 :trkrange_pmtrack : trkrange_pmtrack[ntracks_pmtrack][3]/F          *
  *Br  172 :trkidtruth_pmtrack : trkidtruth_pmtrack[ntracks_pmtrack][3]/I      *
  *Br  173 :trkorigin_pmtrack : trkorigin_pmtrack[ntracks_pmtrack][3]/S        *
  *Br  174 :trkpdgtruth_pmtrack : trkpdgtruth_pmtrack[ntracks_pmtrack][3]/I    *
  *Br  175 :trkefftruth_pmtrack : trkefftruth_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  176 :trkpurtruth_pmtrack : trkpurtruth_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  177 :trkpitchc_pmtrack : trkpitchc_pmtrack[ntracks_pmtrack][3]/F        *
  *Br  178 :ntrkhits_pmtrack : ntrkhits_pmtrack[ntracks_pmtrack][3]/S          *
  *Br  179 :trkdedx_pmtrack : trkdedx_pmtrack[ntracks_pmtrack][3][2000]/F      *
  *Br  180 :trkdqdx_pmtrack : trkdqdx_pmtrack[ntracks_pmtrack][3][2000]/F      *
  *Br  181 :trkresrg_pmtrack : trkresrg_pmtrack[ntracks_pmtrack][3][2000]/F    *
  *Br  182 :trktpc_pmtrack : trktpc_pmtrack[ntracks_pmtrack][3][2000]/I        *
  *Br  183 :trkxyz_pmtrack : trkxyz_pmtrack[ntracks_pmtrack][3][2000][3]/F     *
  *Br  184 :trkstartx_pmtrack : trkstartx_pmtrack[ntracks_pmtrack]/F           *
  *Br  185 :trkstarty_pmtrack : trkstarty_pmtrack[ntracks_pmtrack]/F           *
  *Br  186 :trkstartz_pmtrack : trkstartz_pmtrack[ntracks_pmtrack]/F           *
  *Br  187 :trkstartd_pmtrack : trkstartd_pmtrack[ntracks_pmtrack]/F           *
  *Br  188 :trkendx_pmtrack : trkendx_pmtrack[ntracks_pmtrack]/F               *
  *Br  189 :trkendy_pmtrack : trkendy_pmtrack[ntracks_pmtrack]/F               *
  *Br  190 :trkendz_pmtrack : trkendz_pmtrack[ntracks_pmtrack]/F               *
  *Br  191 :trkendd_pmtrack : trkendd_pmtrack[ntracks_pmtrack]/F               *
  *Br  192 :trkflashT0_pmtrack : trkflashT0_pmtrack[ntracks_pmtrack]/F         *
  *Br  193 :trktrueT0_pmtrack : trktrueT0_pmtrack[ntracks_pmtrack]/F           *
  *Br  194 :trkg4id_pmtrack : trkg4id_pmtrack[ntracks_pmtrack]/I               *
  *Br  195 :trkorig_pmtrack : trkorig_pmtrack[ntracks_pmtrack]/I               *
  *Br  196 :trkpurity_pmtrack : trkpurity_pmtrack[ntracks_pmtrack]/F           *
  *Br  197 :trkcompleteness_pmtrack :                                          *
  *         | trkcompleteness_pmtrack[ntracks_pmtrack]/F                       *
  *Br  198 :trktheta_pmtrack : trktheta_pmtrack[ntracks_pmtrack]/F             *
  *Br  199 :trkphi_pmtrack : trkphi_pmtrack[ntracks_pmtrack]/F                 *
  *Br  200 :trkstartdcosx_pmtrack : trkstartdcosx_pmtrack[ntracks_pmtrack]/F   *
  *Br  201 :trkstartdcosy_pmtrack : trkstartdcosy_pmtrack[ntracks_pmtrack]/F   *
  *Br  202 :trkstartdcosz_pmtrack : trkstartdcosz_pmtrack[ntracks_pmtrack]/F   *
  *Br  203 :trkenddcosx_pmtrack : trkenddcosx_pmtrack[ntracks_pmtrack]/F       *
  *Br  204 :trkenddcosy_pmtrack : trkenddcosy_pmtrack[ntracks_pmtrack]/F       *
  *Br  205 :trkenddcosz_pmtrack : trkenddcosz_pmtrack[ntracks_pmtrack]/F       *
  *Br  206 :trkthetaxz_pmtrack : trkthetaxz_pmtrack[ntracks_pmtrack]/F         *
  *Br  207 :trkthetayz_pmtrack : trkthetayz_pmtrack[ntracks_pmtrack]/F         *
  *Br  208 :trkmom_pmtrack : trkmom_pmtrack[ntracks_pmtrack]/F                 *
  *Br  209 :trkmomrange_pmtrack : trkmomrange_pmtrack[ntracks_pmtrack]/F       *
  *Br  210 :trkmommschi2_pmtrack : trkmommschi2_pmtrack[ntracks_pmtrack]/F     *
  *Br  211 :trkmommsllhd_pmtrack : trkmommsllhd_pmtrack[ntracks_pmtrack]/F     *
  *Br  212 :trklen_pmtrack : trklen_pmtrack[ntracks_pmtrack]/F                 *
  *Br  213 :trksvtxid_pmtrack : trksvtxid_pmtrack[ntracks_pmtrack]/S           *
  *Br  214 :trkevtxid_pmtrack : trkevtxid_pmtrack[ntracks_pmtrack]/S           *
  *Br  215 :trkpidmvamu_pmtrack : trkpidmvamu_pmtrack[ntracks_pmtrack]/F       *
  *Br  216 :trkpidmvae_pmtrack : trkpidmvae_pmtrack[ntracks_pmtrack]/F         *
  *Br  217 :trkpidmvapich_pmtrack : trkpidmvapich_pmtrack[ntracks_pmtrack]/F   *
  *Br  218 :trkpidmvaphoton_pmtrack :                                          *
  *         | trkpidmvaphoton_pmtrack[ntracks_pmtrack]/F                       *
  *Br  219 :trkpidmvapr_pmtrack : trkpidmvapr_pmtrack[ntracks_pmtrack]/F       *
  *Br  220 :trkpidpdg_pmtrack : trkpidpdg_pmtrack[ntracks_pmtrack][3]/I        *
  *Br  221 :trkpidchi_pmtrack : trkpidchi_pmtrack[ntracks_pmtrack][3]/F        *
  *Br  222 :trkpidchipr_pmtrack : trkpidchipr_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  223 :trkpidchika_pmtrack : trkpidchika_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  224 :trkpidchipi_pmtrack : trkpidchipi_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  225 :trkpidchimu_pmtrack : trkpidchimu_pmtrack[ntracks_pmtrack][3]/F    *
  *Br  226 :trkpidpida_pmtrack : trkpidpida_pmtrack[ntracks_pmtrack][3]/F      *
  *Br  227 :trkpidbestplane_pmtrack :                                          *
  *         | trkpidbestplane_pmtrack[ntracks_pmtrack]/S                       *
  *Br  228 :trkhasPFParticle_pmtrack :                                         *
  *         | trkhasPFParticle_pmtrack[ntracks_pmtrack]/S                      *
  *Br  229 :trkPFParticleID_pmtrack :                                          *
  *         | trkPFParticleID_pmtrack[ntracks_pmtrack]/S                       *
  *Br  230 :ntracks_pandora : ntracks_pandora/S                                *
  *Br  231 :trkId_pandora : trkId_pandora[ntracks_pandora]/S                   *
  *Br  232 :trkncosmictags_tagger_pandora :                                    *
  *         | trkncosmictags_tagger_pandora[ntracks_pandora]/S                 *
  *Br  233 :trkcosmicscore_tagger_pandora :                                    *
  *         | trkcosmicscore_tagger_pandora[ntracks_pandora]/F                 *
  *Br  234 :trkcosmictype_tagger_pandora :                                     *
  *         | trkcosmictype_tagger_pandora[ntracks_pandora]/S                  *
  *Br  235 :trkncosmictags_containmenttagger_pandora :                         *
  *         | trkncosmictags_containmenttagger_pandora[ntracks_pandora]/S      *
  *Br  236 :trkcosmicscore_containmenttagger_pandora :                         *
  *         | trkcosmicscore_containmenttagger_pandora[ntracks_pandora]/F      *
  *Br  237 :trkcosmictype_containmenttagger_pandora :                          *
  *         | trkcosmictype_containmenttagger_pandora[ntracks_pandora]/S       *
  *Br  238 :trkncosmictags_flashmatch_pandora :                                *
  *         | trkncosmictags_flashmatch_pandora[ntracks_pandora]/S             *
  *Br  239 :trkcosmicscore_flashmatch_pandora :                                *
  *         | trkcosmicscore_flashmatch_pandora[ntracks_pandora]/F             *
  *Br  240 :trkcosmictype_flashmatch_pandora :                                 *
  *         | trkcosmictype_flashmatch_pandora[ntracks_pandora]/S              *
  *Br  241 :trkke_pandora : trkke_pandora[ntracks_pandora][3]/F                *
  *Br  242 :trkrange_pandora : trkrange_pandora[ntracks_pandora][3]/F          *
  *Br  243 :trkidtruth_pandora : trkidtruth_pandora[ntracks_pandora][3]/I      *
  *Br  244 :trkorigin_pandora : trkorigin_pandora[ntracks_pandora][3]/S        *
  *Br  245 :trkpdgtruth_pandora : trkpdgtruth_pandora[ntracks_pandora][3]/I    *
  *Br  246 :trkefftruth_pandora : trkefftruth_pandora[ntracks_pandora][3]/F    *
  *Br  247 :trkpurtruth_pandora : trkpurtruth_pandora[ntracks_pandora][3]/F    *
  *Br  248 :trkpitchc_pandora : trkpitchc_pandora[ntracks_pandora][3]/F        *
  *Br  249 :ntrkhits_pandora : ntrkhits_pandora[ntracks_pandora][3]/S          *
  *Br  250 :trkdedx_pandora : trkdedx_pandora[ntracks_pandora][3][2000]/F      *
  *Br  251 :trkdqdx_pandora : trkdqdx_pandora[ntracks_pandora][3][2000]/F      *
  *Br  252 :trkresrg_pandora : trkresrg_pandora[ntracks_pandora][3][2000]/F    *
  *Br  253 :trktpc_pandora : trktpc_pandora[ntracks_pandora][3][2000]/I        *
  *Br  254 :trkxyz_pandora : trkxyz_pandora[ntracks_pandora][3][2000][3]/F     *
  *Br  255 :trkstartx_pandora : trkstartx_pandora[ntracks_pandora]/F           *
  *Br  256 :trkstarty_pandora : trkstarty_pandora[ntracks_pandora]/F           *
  *Br  257 :trkstartz_pandora : trkstartz_pandora[ntracks_pandora]/F           *
  *Br  258 :trkstartd_pandora : trkstartd_pandora[ntracks_pandora]/F           *
  *Br  259 :trkendx_pandora : trkendx_pandora[ntracks_pandora]/F               *
  *Br  260 :trkendy_pandora : trkendy_pandora[ntracks_pandora]/F               *
  *Br  261 :trkendz_pandora : trkendz_pandora[ntracks_pandora]/F               *
  *Br  262 :trkendd_pandora : trkendd_pandora[ntracks_pandora]/F               *
  *Br  263 :trkflashT0_pandora : trkflashT0_pandora[ntracks_pandora]/F         *
  *Br  264 :trktrueT0_pandora : trktrueT0_pandora[ntracks_pandora]/F           *
  *Br  265 :trkg4id_pandora : trkg4id_pandora[ntracks_pandora]/I               *
  *Br  266 :trkorig_pandora : trkorig_pandora[ntracks_pandora]/I               *
  *Br  267 :trkpurity_pandora : trkpurity_pandora[ntracks_pandora]/F           *
  *Br  268 :trkcompleteness_pandora :                                          *
  *         | trkcompleteness_pandora[ntracks_pandora]/F                       *
  *Br  269 :trktheta_pandora : trktheta_pandora[ntracks_pandora]/F             *
  *Br  270 :trkphi_pandora : trkphi_pandora[ntracks_pandora]/F                 *
  *Br  271 :trkstartdcosx_pandora : trkstartdcosx_pandora[ntracks_pandora]/F   *
  *Br  272 :trkstartdcosy_pandora : trkstartdcosy_pandora[ntracks_pandora]/F   *
  *Br  273 :trkstartdcosz_pandora : trkstartdcosz_pandora[ntracks_pandora]/F   *
  *Br  274 :trkenddcosx_pandora : trkenddcosx_pandora[ntracks_pandora]/F       *
  *Br  275 :trkenddcosy_pandora : trkenddcosy_pandora[ntracks_pandora]/F       *
  *Br  276 :trkenddcosz_pandora : trkenddcosz_pandora[ntracks_pandora]/F       *
  *Br  277 :trkthetaxz_pandora : trkthetaxz_pandora[ntracks_pandora]/F         *
  *Br  278 :trkthetayz_pandora : trkthetayz_pandora[ntracks_pandora]/F         *
  *Br  279 :trkmom_pandora : trkmom_pandora[ntracks_pandora]/F                 *
  *Br  280 :trkmomrange_pandora : trkmomrange_pandora[ntracks_pandora]/F       *
  *Br  281 :trkmommschi2_pandora : trkmommschi2_pandora[ntracks_pandora]/F     *
  *Br  282 :trkmommsllhd_pandora : trkmommsllhd_pandora[ntracks_pandora]/F     *
  *Br  283 :trklen_pandora : trklen_pandora[ntracks_pandora]/F                 *
  *Br  284 :trksvtxid_pandora : trksvtxid_pandora[ntracks_pandora]/S           *
  *Br  285 :trkevtxid_pandora : trkevtxid_pandora[ntracks_pandora]/S           *
  *Br  286 :trkpidmvamu_pandora : trkpidmvamu_pandora[ntracks_pandora]/F       *
  *Br  287 :trkpidmvae_pandora : trkpidmvae_pandora[ntracks_pandora]/F         *
  *Br  288 :trkpidmvapich_pandora : trkpidmvapich_pandora[ntracks_pandora]/F   *
  *Br  289 :trkpidmvaphoton_pandora :                                          *
  *         | trkpidmvaphoton_pandora[ntracks_pandora]/F                       *
  *Br  290 :trkpidmvapr_pandora : trkpidmvapr_pandora[ntracks_pandora]/F       *
  *Br  291 :trkpidpdg_pandora : trkpidpdg_pandora[ntracks_pandora][3]/I        *
  *Br  292 :trkpidchi_pandora : trkpidchi_pandora[ntracks_pandora][3]/F        *
  *Br  293 :trkpidchipr_pandora : trkpidchipr_pandora[ntracks_pandora][3]/F    *
  *Br  294 :trkpidchika_pandora : trkpidchika_pandora[ntracks_pandora][3]/F    *
  *Br  295 :trkpidchipi_pandora : trkpidchipi_pandora[ntracks_pandora][3]/F    *
  *Br  296 :trkpidchimu_pandora : trkpidchimu_pandora[ntracks_pandora][3]/F    *
  *Br  297 :trkpidpida_pandora : trkpidpida_pandora[ntracks_pandora][3]/F      *
  *Br  298 :trkpidbestplane_pandora :                                          *
  *         | trkpidbestplane_pandora[ntracks_pandora]/S                       *
  *Br  299 :trkhasPFParticle_pandora :                                         *
  *         | trkhasPFParticle_pandora[ntracks_pandora]/S                      *
  *Br  300 :trkPFParticleID_pandora :                                          *
  *         | trkPFParticleID_pandora[ntracks_pandora]/S                       *
  *Br  301 :ntracks_pmtrajfit : ntracks_pmtrajfit/S                            *
  *Br  302 :trkId_pmtrajfit : trkId_pmtrajfit[ntracks_pmtrajfit]/S             *
  *Br  303 :trkncosmictags_tagger_pmtrajfit :                                  *
  *         | trkncosmictags_tagger_pmtrajfit[ntracks_pmtrajfit]/S             *
  *Br  304 :trkcosmicscore_tagger_pmtrajfit :                                  *
  *         | trkcosmicscore_tagger_pmtrajfit[ntracks_pmtrajfit]/F             *
  *Br  305 :trkcosmictype_tagger_pmtrajfit :                                   *
  *         | trkcosmictype_tagger_pmtrajfit[ntracks_pmtrajfit]/S              *
  *Br  306 :trkncosmictags_containmenttagger_pmtrajfit :                       *
  *         | trkncosmictags_containmenttagger_pmtrajfit[ntracks_pmtrajfit]/S  *
  *Br  307 :trkcosmicscore_containmenttagger_pmtrajfit :                       *
  *         | trkcosmicscore_containmenttagger_pmtrajfit[ntracks_pmtrajfit]/F  *
  *Br  308 :trkcosmictype_containmenttagger_pmtrajfit :                        *
  *         | trkcosmictype_containmenttagger_pmtrajfit[ntracks_pmtrajfit]/S   *
  *Br  309 :trkncosmictags_flashmatch_pmtrajfit :                              *
  *         | trkncosmictags_flashmatch_pmtrajfit[ntracks_pmtrajfit]/S         *
  *Br  310 :trkcosmicscore_flashmatch_pmtrajfit :                              *
  *         | trkcosmicscore_flashmatch_pmtrajfit[ntracks_pmtrajfit]/F         *
  *Br  311 :trkcosmictype_flashmatch_pmtrajfit :                               *
  *         | trkcosmictype_flashmatch_pmtrajfit[ntracks_pmtrajfit]/S          *
  *Br  312 :trkke_pmtrajfit : trkke_pmtrajfit[ntracks_pmtrajfit][3]/F          *
  *Br  313 :trkrange_pmtrajfit : trkrange_pmtrajfit[ntracks_pmtrajfit][3]/F    *
  *Br  314 :trkidtruth_pmtrajfit : trkidtruth_pmtrajfit[ntracks_pmtrajfit][3]/I*
  *Br  315 :trkorigin_pmtrajfit : trkorigin_pmtrajfit[ntracks_pmtrajfit][3]/S  *
  *Br  316 :trkpdgtruth_pmtrajfit :                                            *
  *         | trkpdgtruth_pmtrajfit[ntracks_pmtrajfit][3]/I                    *
  *Br  317 :trkefftruth_pmtrajfit :                                            *
  *         | trkefftruth_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  318 :trkpurtruth_pmtrajfit :                                            *
  *         | trkpurtruth_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  319 :trkpitchc_pmtrajfit : trkpitchc_pmtrajfit[ntracks_pmtrajfit][3]/F  *
  *Br  320 :ntrkhits_pmtrajfit : ntrkhits_pmtrajfit[ntracks_pmtrajfit][3]/S    *
  *Br  321 :trkdedx_pmtrajfit : trkdedx_pmtrajfit[ntracks_pmtrajfit][3][2000]/F*
  *Br  322 :trkdqdx_pmtrajfit : trkdqdx_pmtrajfit[ntracks_pmtrajfit][3][2000]/F*
  *Br  323 :trkresrg_pmtrajfit :                                               *
  *         | trkresrg_pmtrajfit[ntracks_pmtrajfit][3][2000]/F                 *
  *Br  324 :trktpc_pmtrajfit : trktpc_pmtrajfit[ntracks_pmtrajfit][3][2000]/I  *
  *Br  325 :trkxyz_pmtrajfit :                                                 *
  *         | trkxyz_pmtrajfit[ntracks_pmtrajfit][3][2000][3]/F                *
  *Br  326 :trkstartx_pmtrajfit : trkstartx_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  327 :trkstarty_pmtrajfit : trkstarty_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  328 :trkstartz_pmtrajfit : trkstartz_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  329 :trkstartd_pmtrajfit : trkstartd_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  330 :trkendx_pmtrajfit : trkendx_pmtrajfit[ntracks_pmtrajfit]/F         *
  *Br  331 :trkendy_pmtrajfit : trkendy_pmtrajfit[ntracks_pmtrajfit]/F         *
  *Br  332 :trkendz_pmtrajfit : trkendz_pmtrajfit[ntracks_pmtrajfit]/F         *
  *Br  333 :trkendd_pmtrajfit : trkendd_pmtrajfit[ntracks_pmtrajfit]/F         *
  *Br  334 :trkflashT0_pmtrajfit : trkflashT0_pmtrajfit[ntracks_pmtrajfit]/F   *
  *Br  335 :trktrueT0_pmtrajfit : trktrueT0_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  336 :trkg4id_pmtrajfit : trkg4id_pmtrajfit[ntracks_pmtrajfit]/I         *
  *Br  337 :trkorig_pmtrajfit : trkorig_pmtrajfit[ntracks_pmtrajfit]/I         *
  *Br  338 :trkpurity_pmtrajfit : trkpurity_pmtrajfit[ntracks_pmtrajfit]/F     *
  *Br  339 :trkcompleteness_pmtrajfit :                                        *
  *         | trkcompleteness_pmtrajfit[ntracks_pmtrajfit]/F                   *
  *Br  340 :trktheta_pmtrajfit : trktheta_pmtrajfit[ntracks_pmtrajfit]/F       *
  *Br  341 :trkphi_pmtrajfit : trkphi_pmtrajfit[ntracks_pmtrajfit]/F           *
  *Br  342 :trkstartdcosx_pmtrajfit :                                          *
  *         | trkstartdcosx_pmtrajfit[ntracks_pmtrajfit]/F                     *
  *Br  343 :trkstartdcosy_pmtrajfit :                                          *
  *         | trkstartdcosy_pmtrajfit[ntracks_pmtrajfit]/F                     *
  *Br  344 :trkstartdcosz_pmtrajfit :                                          *
  *         | trkstartdcosz_pmtrajfit[ntracks_pmtrajfit]/F                     *
  *Br  345 :trkenddcosx_pmtrajfit : trkenddcosx_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  346 :trkenddcosy_pmtrajfit : trkenddcosy_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  347 :trkenddcosz_pmtrajfit : trkenddcosz_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  348 :trkthetaxz_pmtrajfit : trkthetaxz_pmtrajfit[ntracks_pmtrajfit]/F   *
  *Br  349 :trkthetayz_pmtrajfit : trkthetayz_pmtrajfit[ntracks_pmtrajfit]/F   *
  *Br  350 :trkmom_pmtrajfit : trkmom_pmtrajfit[ntracks_pmtrajfit]/F           *
  *Br  351 :trkmomrange_pmtrajfit : trkmomrange_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  352 :trkmommschi2_pmtrajfit :                                           *
  *         | trkmommschi2_pmtrajfit[ntracks_pmtrajfit]/F                      *
  *Br  353 :trkmommsllhd_pmtrajfit :                                           *
  *         | trkmommsllhd_pmtrajfit[ntracks_pmtrajfit]/F                      *
  *Br  354 :trklen_pmtrajfit : trklen_pmtrajfit[ntracks_pmtrajfit]/F           *
  *Br  355 :trksvtxid_pmtrajfit : trksvtxid_pmtrajfit[ntracks_pmtrajfit]/S     *
  *Br  356 :trkevtxid_pmtrajfit : trkevtxid_pmtrajfit[ntracks_pmtrajfit]/S     *
  *Br  357 :trkpidmvamu_pmtrajfit : trkpidmvamu_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  358 :trkpidmvae_pmtrajfit : trkpidmvae_pmtrajfit[ntracks_pmtrajfit]/F   *
  *Br  359 :trkpidmvapich_pmtrajfit :                                          *
  *         | trkpidmvapich_pmtrajfit[ntracks_pmtrajfit]/F                     *
  *Br  360 :trkpidmvaphoton_pmtrajfit :                                        *
  *         | trkpidmvaphoton_pmtrajfit[ntracks_pmtrajfit]/F                   *
  *Br  361 :trkpidmvapr_pmtrajfit : trkpidmvapr_pmtrajfit[ntracks_pmtrajfit]/F *
  *Br  362 :trkpidpdg_pmtrajfit : trkpidpdg_pmtrajfit[ntracks_pmtrajfit][3]/I  *
  *Br  363 :trkpidchi_pmtrajfit : trkpidchi_pmtrajfit[ntracks_pmtrajfit][3]/F  *
  *Br  364 :trkpidchipr_pmtrajfit :                                            *
  *         | trkpidchipr_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  365 :trkpidchika_pmtrajfit :                                            *
  *         | trkpidchika_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  366 :trkpidchipi_pmtrajfit :                                            *
  *         | trkpidchipi_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  367 :trkpidchimu_pmtrajfit :                                            *
  *         | trkpidchimu_pmtrajfit[ntracks_pmtrajfit][3]/F                    *
  *Br  368 :trkpidpida_pmtrajfit : trkpidpida_pmtrajfit[ntracks_pmtrajfit][3]/F*
  *Br  369 :trkpidbestplane_pmtrajfit :                                        *
  *         | trkpidbestplane_pmtrajfit[ntracks_pmtrajfit]/S                   *
  *Br  370 :trkhasPFParticle_pmtrajfit :                                       *
  *         | trkhasPFParticle_pmtrajfit[ntracks_pmtrajfit]/S                  *
  *Br  371 :trkPFParticleID_pmtrajfit :                                        *
  *         | trkPFParticleID_pmtrajfit[ntracks_pmtrajfit]/S                   *
  *Br  372 :nvtx_linecluster : nvtx_linecluster/S                              *
  *Br  373 :vtxId_linecluster : vtxId_linecluster[nvtx_linecluster]/S          *
  *Br  374 :vtxx_linecluster : vtxx_linecluster[nvtx_linecluster]/F            *
  *Br  375 :vtxy_linecluster : vtxy_linecluster[nvtx_linecluster]/F            *
  *Br  376 :vtxz_linecluster : vtxz_linecluster[nvtx_linecluster]/F            *
  *Br  377 :vtxhasPFParticle_linecluster :                                     *
  *         | vtxhasPFParticle_linecluster[nvtx_linecluster]/S                 *
  *Br  378 :vtxPFParticleID_linecluster :                                      *
  *         | vtxPFParticleID_linecluster[nvtx_linecluster]/S                  *
  *Br  379 :nvtx_lineclusterdc : nvtx_lineclusterdc/S                          *
  *Br  380 :vtxId_lineclusterdc : vtxId_lineclusterdc[nvtx_lineclusterdc]/S    *
  *Br  381 :vtxx_lineclusterdc : vtxx_lineclusterdc[nvtx_lineclusterdc]/F      *
  *Br  382 :vtxy_lineclusterdc : vtxy_lineclusterdc[nvtx_lineclusterdc]/F      *
  *Br  383 :vtxz_lineclusterdc : vtxz_lineclusterdc[nvtx_lineclusterdc]/F      *
  *Br  384 :vtxhasPFParticle_lineclusterdc :                                   *
  *         | vtxhasPFParticle_lineclusterdc[nvtx_lineclusterdc]/S             *
  *Br  385 :vtxPFParticleID_lineclusterdc :                                    *
  *         | vtxPFParticleID_lineclusterdc[nvtx_lineclusterdc]/S              *
  *Br  386 :nvtx_pmtrack : nvtx_pmtrack/S                                      *
  *Br  387 :vtxId_pmtrack : vtxId_pmtrack[nvtx_pmtrack]/S                      *
  *Br  388 :vtxx_pmtrack : vtxx_pmtrack[nvtx_pmtrack]/F                        *
  *Br  389 :vtxy_pmtrack : vtxy_pmtrack[nvtx_pmtrack]/F                        *
  *Br  390 :vtxz_pmtrack : vtxz_pmtrack[nvtx_pmtrack]/F                        *
  *Br  391 :vtxhasPFParticle_pmtrack : vtxhasPFParticle_pmtrack[nvtx_pmtrack]/S*
  *Br  392 :vtxPFParticleID_pmtrack : vtxPFParticleID_pmtrack[nvtx_pmtrack]/S  *
  *Br  393 :nvtx_pmtrackdc : nvtx_pmtrackdc/S                                  *
  *Br  394 :vtxId_pmtrackdc : vtxId_pmtrackdc[nvtx_pmtrackdc]/S                *
  *Br  395 :vtxx_pmtrackdc : vtxx_pmtrackdc[nvtx_pmtrackdc]/F                  *
  *Br  396 :vtxy_pmtrackdc : vtxy_pmtrackdc[nvtx_pmtrackdc]/F                  *
  *Br  397 :vtxz_pmtrackdc : vtxz_pmtrackdc[nvtx_pmtrackdc]/F                  *
  *Br  398 :vtxhasPFParticle_pmtrackdc :                                       *
  *         | vtxhasPFParticle_pmtrackdc[nvtx_pmtrackdc]/S                     *
  *Br  399 :vtxPFParticleID_pmtrackdc :                                        *
  *         | vtxPFParticleID_pmtrackdc[nvtx_pmtrackdc]/S                      *
  *Br  400 :nvtx_pandora : nvtx_pandora/S                                      *
  *Br  401 :vtxId_pandora : vtxId_pandora[nvtx_pandora]/S                      *
  *Br  402 :vtxx_pandora : vtxx_pandora[nvtx_pandora]/F                        *
  *Br  403 :vtxy_pandora : vtxy_pandora[nvtx_pandora]/F                        *
  *Br  404 :vtxz_pandora : vtxz_pandora[nvtx_pandora]/F                        *
  *Br  405 :vtxhasPFParticle_pandora : vtxhasPFParticle_pandora[nvtx_pandora]/S*
  *Br  406 :vtxPFParticleID_pandora : vtxPFParticleID_pandora[nvtx_pandora]/S  *
  *Br  407 :nvtx_pandoradc : nvtx_pandoradc/S                                  *
  *Br  408 :vtxId_pandoradc : vtxId_pandoradc[nvtx_pandoradc]/S                *
  *Br  409 :vtxx_pandoradc : vtxx_pandoradc[nvtx_pandoradc]/F                  *
  *Br  410 :vtxy_pandoradc : vtxy_pandoradc[nvtx_pandoradc]/F                  *
  *Br  411 :vtxz_pandoradc : vtxz_pandoradc[nvtx_pandoradc]/F                  *
  *Br  412 :vtxhasPFParticle_pandoradc :                                       *
  *         | vtxhasPFParticle_pandoradc[nvtx_pandoradc]/S                     *
  *Br  413 :vtxPFParticleID_pandoradc :                                        *
  *         | vtxPFParticleID_pandoradc[nvtx_pandoradc]/S                      *
