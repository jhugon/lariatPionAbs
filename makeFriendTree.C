
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

void makeFriendTree (TString inputFileName,TString outputFileName,TString histFileName, TString histName, unsigned maxEvents, TString inputTreeName="PiAbsSelector/tree")
{
  using namespace std;

  cout << "makeFriendTree for "<< inputFileName.Data() << " in file " << outputFileName.Data() <<" using hist file: "<< histFileName.Data() << " histogram name: " << histName.Data() << endl;

  bool isMC;
  Float_t pzWC;
  Float_t trueStartMom;

  // Histograms
  TFile* histFile = new TFile(histFileName);
  if (histFile == NULL)
  {
    cout << "Error histFile is null, exiting." << endl;
    return;
  }

  TH1F* pzHist = (TH1F*) histFile->Get(histName);
  if (pzHist == NULL)
  {
    cout << "Error pzHist is null, exiting." << endl;
    return;
  }

  Float_t pzHistIntegral = pzHist->Integral();
  if (pzHistIntegral == 0)
  {
    cout << "Error pzHist integral is 0, exiting." << endl;
    return;
  }
  cout << "pzHist Integral: " << pzHistIntegral << endl;

  // infile chain
  TChain * tree = new TChain(inputTreeName);
  tree->Add(inputFileName);
  tree->SetBranchAddress("isMC",&isMC);
  tree->SetBranchAddress("pzWC",&pzWC);
  tree->SetBranchAddress("trueStartMom",&trueStartMom);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  TTree* friendTree = new TTree("friend","");
  float allWeight, pzWeight;

  friendTree->Branch("allWeight",&allWeight,"allWeight/F");
  friendTree->Branch("pzWeight",&pzWeight,"pzWeight/F");

  Double_t pzWeightSum=0;
  Double_t nEventsSum=0;

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Event Loop

  unsigned nEvents = tree->GetEntries();
  unsigned reportEach=1000;
  cout << "nEvents in tree: " << nEvents << endl;
  cout << "Stopping at " << maxEvents << endl;

  // Go through first to see what total pzWeightSum would be.
  pzWeight = 0.;
  nEventsSum = 0.;
  for(unsigned iEvent=0; iEvent<nEvents;iEvent++)
  {
    if(iEvent >= maxEvents)
      break;
    tree->GetEntry(iEvent);
    allWeight = 1.;
    pzWeight = 1.;

    if (isMC)
    {
      float pz = pzWC;
      if (pzWC < -100.)
      {
        pz = trueStartMom;
      }
      pzWeight = pzHist->GetBinContent(pzHist->FindBin(pz));
      allWeight = pzWeight;
    }
    pzWeightSum += pzWeight;
    nEventsSum++;
  } // for iEvent

  cout << "Initial sum of pzWeight: " << pzWeightSum << endl;
  float pzWeightScaleFactor = nEventsSum * pzHistIntegral / pzWeightSum;
  cout << "pzWeightScaleFactor: " << pzWeightScaleFactor << endl;

  // Now actually fill the tree
  pzWeightSum = 0.;
  nEventsSum = 0.;
  for(unsigned iEvent=0; iEvent<nEvents;iEvent++)
  {
    if(iEvent >= maxEvents)
      break;
    tree->GetEntry(iEvent);
    allWeight = 1.;
    pzWeight = 1.;

    if (isMC)
    {
      float pz = pzWC;
      if (pzWC < -100.)
      {
        pz = trueStartMom;
      }
      pzWeight = pzHist->GetBinContent(pzHist->FindBin(pz)) * pzWeightScaleFactor;
      allWeight = pzWeight;
    }
    pzWeightSum += pzWeight;
    friendTree->Fill();
  } // for iEvent
  cout << "Final sum of pzWeight: " << pzWeightSum << endl;

  friendTree->Write();
  outFile->Close();

}
