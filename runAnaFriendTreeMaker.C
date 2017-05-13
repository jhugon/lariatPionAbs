{
  gROOT->ProcessLine(".L makeAnaTreeFriendTree.C+");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 1000;

  //makeAnaTreeFriendTree("/dune/app/users/jhugon/likelihoodPID/dunetpc_v06_18_01/ana_hist.root","friendTree_ana_hist.root",maxEvents);
  //makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0/19793205_0/ana_hist.root","friendTree_ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0.root",maxEvents);
  //makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0_v1/","friendTree_ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0.root",maxEvents);
  
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_0p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_1GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_1p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_1p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  //makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_2p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_2p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  //makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_2p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_2p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_3p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_3p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_3p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_3p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_4p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_4p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_4p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_4p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_5p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_5p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_5p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_5p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_6p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_6p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  //makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_6p5GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_6p5GeV_mono_3ms_mcc8.0_v2.root",maxEvents);
  makeAnaTreeFriendTree("/pnfs/dune/scratch/users/jhugon/v06_18_01/ana/ProtoDUNE_pion_7p0GeV_mono_3ms_mcc8.0_v2/anahist.root","friendTree_ProtoDUNE_pion_7p0GeV_mono_3ms_mcc8.0_v2.root",maxEvents);

}
