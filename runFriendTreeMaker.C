{
  gROOT->ProcessLine(".L makeFriendTree.C++");

  unsigned maxEvents = 100;

  makeFriendTree("/scratch/jhugon/catalogue/anaTree_pip_v11.root","friendTree_pip_v11.root",maxEvents);
  makeFriendTree("/scratch/jhugon/catalogue/anaTree_p_v10.root","friendTree_p_v10.root",maxEvents);
  makeFriendTree("/scratch/jhugon/catalogue/anaTree_mup_v10.root","friendTree_mup_v10.root",maxEvents);
  makeFriendTree("/scratch/jhugon/catalogue/anaTree_kp_v10.root","friendTree_kp_v10.root",maxEvents);

}
