{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 10000;

  //TString datafn = "/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/data_Pos_RunI_piAbsSelector.root";

  //makeFriendTree(datafn,"friendTree_Pos_RunI_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/pip_piAbsSelector.root","friendTree_pip_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/p_piAbsSelector.root","friendTree_p_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/ep_piAbsSelector.root","friendTree_ep_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/mup_piAbsSelector.root","friendTree_mup_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/kp_piAbsSelector.root","friendTree_kp_v0.root",datafn,maxEvents);
  //makeFriendTree("/lariat/app/users/jhugon/lariatsoft_v06_15_00/srcs/lariatsoft/JobConfigurations/gam_piAbsSelector.root","friendTree_gam_v0.root",datafn,maxEvents);
  
  TString datafn = "/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_data_Lovely1_Pos_RunI_elanag_v02_v03/anahist.root";

  makeFriendTree(datafn,"friendTree_Pos_RunI_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_pip_v3/anahist.root","friendTree_pip_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_p_v3/anahist.root","friendTree_p_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_ep_v3/anahist.root","friendTree_ep_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_mup_v3/anahist.root","friendTree_mup_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_kp_v3/anahist.root","friendTree_kp_v3.root",datafn,maxEvents);
  makeFriendTree("/pnfs/lariat/scratch/users/jhugon/v06_15_00/piAbsSelector/lariat_PiAbsAndChEx_flat_gam_v3/anahist.root","friendTree_gam_v3.root",datafn,maxEvents);
}
