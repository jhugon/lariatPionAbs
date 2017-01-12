
#include <TSystem.h>
#include <TROOT.h>
#include <TFile.h>
#include <TChain.h>
#include <TTree.h>
#include <TH2F.h>
#include <TH1F.h>
#include <TCanvas.h>
//#include <TF1.h>
//#include <TRandom3.h>

#include <iostream>
#include <vector>

void makeFriendTree (TString inputFileName,TString outputFileName,TString dataInFileName, unsigned maxEvents)
{
  using namespace std;

  cout << "makeFriendTree for "<< inputFileName.Data() << " in file " << outputFileName.Data() <<" using data file: "<<dataInFileName.Data()<< endl;

  bool isMC;
  Float_t xWC, yWC, thetaWC, phiWC, pzWC, xWC4Hit, yWC4Hit, zWC4Hit;

  // datafile chain
  TChain * datatree = new TChain("PiAbsSelector/tree");
  datatree->Add(dataInFileName);
  datatree->SetBranchAddress("isMC",&isMC);
  datatree->SetBranchAddress("xWC",&xWC);
  datatree->SetBranchAddress("yWC",&yWC);
  datatree->SetBranchAddress("thetaWC",&thetaWC);
  datatree->SetBranchAddress("phiWC",&phiWC);
  datatree->SetBranchAddress("pzWC",&pzWC);
  datatree->SetBranchAddress("xWC4Hit",&xWC4Hit);
  datatree->SetBranchAddress("yWC4Hit",&yWC4Hit);
  datatree->SetBranchAddress("zWC4Hit",&zWC4Hit);

  TH1F* pzHist = new TH1F("pzHist","",100,0,2000);
  TH1F* xWC4Hist = new TH1F("xWCHist","",20,20,40);
  TH1F* yWC4Hist = new TH1F("yWCHist","",20,-10,10);
  for(unsigned iEvent=0; iEvent<datatree->GetEntries();iEvent++)
  {
    if(iEvent >= maxEvents)
      break;

    datatree->GetEntry(iEvent);
    pzHist->Fill(pzWC);
    xWC4Hist->Fill(xWC4Hit);
    yWC4Hist->Fill(yWC4Hit);
  } // for iEvent

  delete datatree;

  cout << "pzHist " << pzHist->Integral() << endl;
  cout << "xWC4Hist " << xWC4Hist->Integral() << endl;
  cout << "yWC4Hist " << yWC4Hist->Integral() << endl;
  if (pzHist->Integral() != 0) pzHist->Scale(1./pzHist->Integral());
  if (xWC4Hist->Integral() != 0) xWC4Hist->Scale(1./xWC4Hist->Integral());
  if (yWC4Hist->Integral() != 0) yWC4Hist->Scale(1./yWC4Hist->Integral());
  TCanvas c1;
  pzHist->Draw();
  c1.SaveAs("weights_pz.png");
  xWC4Hist->Draw();
  c1.SaveAs("weights_xWC4.png");
  yWC4Hist->Draw();
  c1.SaveAs("weights_yWC4.png");

  // infile chain
  TChain * tree = new TChain("PiAbsSelector/tree");
  tree->Add(inputFileName);
  tree->SetBranchAddress("isMC",&isMC);
  tree->SetBranchAddress("xWC",&xWC);
  tree->SetBranchAddress("yWC",&yWC);
  tree->SetBranchAddress("thetaWC",&thetaWC);
  tree->SetBranchAddress("phiWC",&phiWC);
  tree->SetBranchAddress("pzWC",&pzWC);
  tree->SetBranchAddress("xWC4Hit",&xWC4Hit);
  tree->SetBranchAddress("yWC4Hit",&yWC4Hit);
  tree->SetBranchAddress("zWC4Hit",&zWC4Hit);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  TTree* friendTree = new TTree("friend","");
  float allWeight, pzWeight, spaceWeight, xWeight, yWeight, angleWeight;

  friendTree->Branch("allWeight",&allWeight,"allWeight/F");
  friendTree->Branch("pzWeight",&pzWeight,"pzWeight/F");
  friendTree->Branch("spaceWeight",&spaceWeight,"spaceWeight/F");
  friendTree->Branch("xWeight",&xWeight,"xWeight/F");
  friendTree->Branch("yWeight",&yWeight,"yWeight/F");
  friendTree->Branch("angleWeight",&angleWeight,"angleWeight/F");

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
    allWeight = 1.;
    pzWeight = 1.;
    spaceWeight = 1.;
    xWeight = 1.;
    yWeight = 1.;
    angleWeight = 1.;

    pzWeight = pzHist->GetBinContent(pzHist->FindBin(pzWC));
    xWeight = xWC4Hist->GetBinContent(xWC4Hist->FindBin(xWC4Hit));
    yWeight = yWC4Hist->GetBinContent(yWC4Hist->FindBin(yWC4Hit));
    
    spaceWeight = xWeight*yWeight*angleWeight;
    allWeight = spaceWeight * pzWeight;
    friendTree->Fill();
  } // for iEvent

  friendTree->Write();
  outFile->Close();

}
