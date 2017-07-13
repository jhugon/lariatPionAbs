
#include <TSystem.h>
#include <TROOT.h>
#include <TFile.h>
#include <TChain.h>
#include <TTree.h>
#include <TH2F.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <TMath.h>
//#include <TF1.h>
//#include <TRandom3.h>

#include <iostream>
#include <vector>
#include <cmath>

#define pi TMath::Pi()

#define MAXTOFS 10

float thetaxz(double theta, double phi)
{
  return atan(tan(theta)*cos(phi));
}
float sinthetayz(double theta, double phi)
{
  return sin(theta)*sin(phi);
}
float thetayz(double theta, double phi)
{
  return asin(sinthetayz(theta,phi));
}

void makeCosmicFriendTree (TString inputFileName,TString outputFileName, unsigned maxEvents)
{
  using namespace std;

  cout << "makeCosmicFriendTree for "<< inputFileName.Data() << " in file " << outputFileName.Data() << endl;

  bool isMC;
  Float_t trueStartMom;

  // infile chain
  TFile * infile;
  TTree * tree;
  infile = new TFile(inputFileName);
  if (!infile)
  {
    cout << "Error: could not open file. exiting." << endl;
    return;
  }
  tree = (TTree*) infile->Get("cosmicanalyzer/tree");
  if (!tree)
  {
    cout << "Error: could not find tree. exiting." << endl;
    return;
  }
  tree->SetCacheSize(10000000);
  tree->AddBranchToCache("*");
  tree->SetBranchAddress("isMC",&isMC);
  tree->SetBranchAddress("trueStartMom",&trueStartMom);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  TTree* friendTree = new TTree("friend","");
  float cosmicMomWeight;
  float cosmicMomWeightNoTurnOn;

  friendTree->Branch("cosmicMomWeight",&cosmicMomWeight,"cosmicMomWeight/F");
  friendTree->Branch("cosmicMomWeightNoTurnOn",&cosmicMomWeightNoTurnOn,"cosmicMomWeightNoTurnOn/F");

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Event Loop

  unsigned nEvents = tree->GetEntries();
  unsigned reportEach=1000;
  cout << "nEvents in tree: " << nEvents << endl;
  cout << "Stopping at " << maxEvents << endl;

  for(unsigned iEvent=0; iEvent<nEvents;iEvent++)
  {
    if(iEvent >= maxEvents)
      break;
    tree->GetEntry(iEvent);
    cosmicMomWeight = 1.;
    cosmicMomWeightNoTurnOn = 1.;

    if (isMC)
    {
        float momGeV = trueStartMom/1000.;
        cosmicMomWeightNoTurnOn = pow(momGeV,-2.7)*pow(10,-0.6*pow(log10(momGeV)-1.6,2)+2.8);
        float sigmoidTurnOnTerm = 0.5*(tanh((momGeV-1.)*5.) + 1.);
        float sigmoidTurnOffTerm = 0.5*(tanh((1-momGeV)*5.) + 1.);
        cosmicMomWeight = cosmicMomWeightNoTurnOn*sigmoidTurnOnTerm;
        cosmicMomWeight += sigmoidTurnOffTerm*18.365383433483444;
    }
    friendTree->Fill();
  } // for iEvent

  friendTree->Write();
  outFile->Close();

}
