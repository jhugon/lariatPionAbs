{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 10000;

  TString datafn = "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_data_Lovely1_Pos_RunI_elanag_v02_v03/anahist.root";
  makeFriendTree(datafn,"friendTree_Pos_RunI_v03.root",datafn,maxEvents);
  //TString datafn = "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_data_Lovely1_Pos_RunII_elanag_v02_v03/anahist.root";
  //makeFriendTree(datafn,"friendTree_Pos_RunII_v03.root",datafn,maxEvents);

  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_pip_v4/anahist.root","friendTree_pip_v4.root",datafn,maxEvents);
  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_p_v4/anahist.root","friendTree_p_v4.root",datafn,maxEvents);
  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_ep_v4/anahist.root","friendTree_ep_v4.root",datafn,maxEvents);
  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_mup_v4/anahist.root","friendTree_mup_v4.root",datafn,maxEvents);
  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_kp_v4/anahist.root","friendTree_kp_v4.root",datafn,maxEvents);
  //makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector2/lariat_PiAbsAndChEx_flat_gam_v4/anahist.root","friendTree_gam_v4.root",datafn,maxEvents);

  makeFriendTree("piAbs_pip_v5.root","friendTree_pip_v5.root",datafn,maxEvents);
  makeFriendTree("piAbs_p_v5.root","friendTree_p_v5.root",datafn,maxEvents);
  makeFriendTree("piAbs_ep_v5.root","friendTree_ep_v5.root",datafn,maxEvents);
  makeFriendTree("piAbs_mup_v5.root","friendTree_mup_v5.root",datafn,maxEvents);
  makeFriendTree("piAbs_kp_v5.root","friendTree_kp_v5.root",datafn,maxEvents);
}
