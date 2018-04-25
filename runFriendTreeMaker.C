{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 100;

  TString histfn = "/home/jhugon/weights_Pos_100A.root";
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorData/Pos_RunII_60A_b_v02_triggerFilter.root","/scratch/jhugon/lariat/pionAbsSelectorData/friendTrees/friend_Pos_RunII_60A_b_v02_triggerFilter.root",histfn,"pz_Pos_100A_all",maxEvents);
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorData/Pos_RunII_60A_b_v02_NoTriggerFilter.root","/scratch/jhugon/lariat/pionAbsSelectorData/friendTrees/friend_Pos_RunII_60A_b_v02_NoTriggerFilter.root",histfn,"pz_Pos_100A_all",maxEvents);

  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_211.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_211.root",histfn,"pz_Pos_100A_pip",maxEvents);
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_2212.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_2212.root",histfn,"pz_Pos_100A_p",maxEvents);
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-11.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-11.root",histfn,"pz_Pos_100A_ep",maxEvents);
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_-13.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_-13.root",histfn,"pz_Pos_100A_mup",maxEvents);
  makeFriendTree("/scratch/jhugon/lariat/pionAbsSelectorMC1/MC1_PDG_321.root","/scratch/jhugon/lariat/pionAbsSelectorMC1/friendTrees/friend_MC1_PDG_321.root",histfn,"pz_Pos_100A_kp",maxEvents);

}
