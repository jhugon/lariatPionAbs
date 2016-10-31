{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 5000;

  makeFriendTree("anaTree_pip_v2.root","friendTree_pip_v2.root",maxEvents);
  makeFriendTree("anaTree_p_v2.root","friendTree_p_v2.root",maxEvents);
  makeFriendTree("anaTree_mup_v2.root","friendTree_mup_v2.root",maxEvents);
  makeFriendTree("anaTree_kp_v2.root","friendTree_kp_v2.root",maxEvents);
  makeFriendTree("anaTree_ep_v2.root","friendTree_ep_v2.root",maxEvents);

  makeFriendTree("anaTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root","friendTree_data_Lovely1_Pos_RunI_elanag_v02_v01.root",maxEvents);

}
