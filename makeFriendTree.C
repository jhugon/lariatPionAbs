
#include <TSystem.h>
#include <TROOT.h>
#include <TFile.h>
#include <TChain.h>
//#include <TTree.h>
//#include <TH2F.h>
//#include <TH1F.h>
//#include <TF1.h>
//#include <TRandom3.h>

#include <iostream>
#include <vector>

void makeFriendTree (TString inputFileName,TString outputFileName, unsigned maxEvents)
{
  using namespace std;

  TChain * tree = new TChain("anatree/anatree");
  tree->Add(inputFileName);

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  // These are the dimuon mass, pt, rapidity, and phi
  //float recoCandMass, recoCandPt, recoCandY, recoCandPhi;
  //float recoCandMassRes, recoCandMassResCov;

  //tree->SetBranchAddress("recoCandMass",       &recoCandMass);
  //tree->SetBranchAddress("recoCandPt",         &recoCandPt);
  //tree->SetBranchAddress("recoCandY",          &recoCandY);
  //tree->SetBranchAddress("recoCandPhi",        &recoCandPhi);
  //tree->SetBranchAddress("recoCandMassRes",    &recoCandMassRes);
  //tree->SetBranchAddress("recoCandMassResCov", &recoCandMassResCov);

  unsigned nEvents = tree->GetEntries();
  unsigned reportEach=100;

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Event Loop

  for(unsigned iEvent=0; iEvent<nEvents;iEvent++)
  {
    if(iEvent >= maxEvents)
      break;

    tree->GetEvent(iEvent);
    if (iEvent % reportEach == 0) cout << "Event: " << iEvent << endl;

  }

}
