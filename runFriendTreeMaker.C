{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100000000;

  makeFriendTree("anaTree_pip_v1.root","friendTree_pip_v1.root",maxEvents);
  makeFriendTree("anaTree_p_v1.root","friendTree_p_v1.root",maxEvents);
  //makeFriendTree("anaTree_mup_v10.root","friendTree_mup_v10.root",maxEvents);
  //makeFriendTree("anaTree_kp_v10.root","friendTree_kp_v10.root",maxEvents);

}
