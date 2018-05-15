{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 100;

  TString histfn = "piAbs_v2/weights_Pos_100A.root";

//  makeFriendTree("piAbs_v2/piAbsSelector_Neg_RunII_current100_v02_all.root","piAbs_v2/friendTrees/friendTree_piAbsSelector_Neg_RunII_current100_v02_all.root",histfn,"pz_Pos_100A_all",maxEvents);
//  makeFriendTree("piAbs_v2/piAbsSelector_Neg_RunII_current60_v02_all.root","piAbs_v2/friendTrees/friendTree_piAbsSelector_Neg_RunII_current60_v02_all.root",histfn,"pz_Pos_100A_all",maxEvents);
//  makeFriendTree("piAbs_v2/piAbsSelector_Pos_RunII_current100_v02_all.root","piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current100_v02_all.root",histfn,"pz_Pos_100A_all",maxEvents);
//  makeFriendTree("piAbs_v2/piAbsSelector_Pos_RunII_current60_v02_all.root","piAbs_v2/friendTrees/friendTree_piAbsSelector_Pos_RunII_current60_v02_all.root",histfn,"pz_Pos_100A_all",maxEvents);
//
//  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_211.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_211.root",histfn,"pz_Pos_100A_pip",maxEvents);
//  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_2212.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_2212.root",histfn,"pz_Pos_100A_p",maxEvents);
//  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-11.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-11.root",histfn,"pz_Pos_100A_ep",maxEvents);
//  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-13.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-13.root",histfn,"pz_Pos_100A_mup",maxEvents);
//  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_321.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_321.root",histfn,"pz_Pos_100A_kp",maxEvents);

//  makeFriendTree("cosmicBeamData_v2/cosmicAna_beam_Pos_RunII_current100_v02_all.root","cosmicBeamData_v2/friendTrees/cosmicAna_beam_Pos_RunII_current100_v02_all.root",histfn,"pz_Pos_100A_all",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear10_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear10_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear15_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear20_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear20_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear25_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");
//  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear30_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_pip_presmear30_v5.root",histfn,"pz_Pos_100A_pip",maxEvents,"cosmicanalyzer/tree");

  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");
  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear10_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");
  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear15_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");
  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear20_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");
  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear25_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");
  makeFriendTree("cosmicBeamMC/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root","cosmicBeamMC/friendTrees/CosmicAna_lariat_PiAbsAndChEx_flat_p_presmear30_v5.root",histfn,"pz_Pos_100A_p",maxEvents,"cosmicanalyzer/tree");

}
