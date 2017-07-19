{
  gROOT->ProcessLine(".L makeCosmicFriendTree.C++");

  unsigned maxEvents = 100000000;
  //unsigned maxEvents = 10000;

//  makeCosmicFriendTree("lariat_data_cosmics_Neg_RunII_v01.root","friendTree_lariat_data_cosmics_Neg_RunII_v01.root",maxEvents);
//  makeCosmicFriendTree("lariat_data_cosmics_Pos_RunII_v01.root","friendTree_lariat_data_cosmics_Pos_RunII_v01.root",maxEvents);
//
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_v3.root",maxEvents);
//
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear20perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear20perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear30perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear30perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear35perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear35perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear40perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear40perc_v3.root",maxEvents);
//
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear10perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear10perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear20perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear20perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear40perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear40perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear60perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear60perc_v3.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear80perc_v3.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear80perc_v3.root",maxEvents);
//
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear30perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear30perc_v4.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear35perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear35perc_v4.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear40perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear40perc_v4.root",maxEvents);
//
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear40perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear40perc_v4.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear60perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear60perc_v4.root",maxEvents);
//  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_postsmear80perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_postsmear80perc_v4.root",maxEvents);

  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_v4.root",maxEvents);
  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear10perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear10perc_v4.root",maxEvents);
  makeCosmicFriendTree("lariat_PiAbsAndChEx_cosmics_vert_presmear20perc_v4.root","friendTree_lariat_PiAbsAndChEx_cosmics_vert_presmear20perc_v4.root",maxEvents);
}
