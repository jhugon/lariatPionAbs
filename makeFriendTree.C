
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

void makeFriendTree (TString inputFileName,TString outputFileName,TString dataInFileName, unsigned maxEvents)
{
  using namespace std;

  cout << "makeFriendTree for "<< inputFileName.Data() << " in file " << outputFileName.Data() <<" using data file: "<<dataInFileName.Data()<< endl;

  bool isMC;
  Float_t xWC, yWC, thetaWC, phiWC, pzWC, xWC4Hit, yWC4Hit, zWC4Hit;
  UInt_t nTOFs;
  Float_t TOFs[MAXTOFS];

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

  datatree->SetBranchAddress("nTOFs",&nTOFs);
  datatree->SetBranchAddress("TOFs",&TOFs);

  TH1F* pzHist = new TH1F("pzHist","",200,0,2000);
  TH1F* xWC4Hist = new TH1F("xWCHist","",20,20,40);
  TH1F* yWC4Hist = new TH1F("yWCHist","",20,-10,10);
  TH1F* thetaxzHist = new TH1F("thetaxzHist","",50,-8*pi/180.,2*pi/180.);
  TH1F* sinThetayzHist = new TH1F("sinThetayzHist","",50,-0.05,0.05);

  TH1F* pzHistProton = new TH1F("pzHistProton","",100,0,2000);
  for(unsigned iEvent=0; iEvent<datatree->GetEntries();iEvent++)
  {
    if(iEvent >= maxEvents)
      break;

    datatree->GetEntry(iEvent);
    pzHist->Fill(pzWC);
    xWC4Hist->Fill(xWC4Hit);
    yWC4Hist->Fill(yWC4Hit);
    float thxz = thetaxz(thetaWC,phiWC);
    float sthyz = sinthetayz(thetaWC,phiWC);
    thetaxzHist->Fill(thxz);
    sinThetayzHist->Fill(sthyz);

    if(nTOFs > 0 && TOFs[0] > 28. && TOFs[0] < 55 && pzWC > 450 && pzWC < 1100) pzHistProton->Fill(pzWC);
  } // for iEvent

  delete datatree;

  const char* intOpt = "width";
  cout << "pzHist " << pzHist->Integral(intOpt) << endl;
  cout << "xWC4Hist " << xWC4Hist->Integral(intOpt) << endl;
  cout << "yWC4Hist " << yWC4Hist->Integral(intOpt) << endl;
  cout << "thetaxzHist " << thetaxzHist->Integral(intOpt) << endl;
  cout << "sinThetayzHist " << sinThetayzHist->Integral(intOpt) << endl;
  cout << "pzHistProton " << pzHistProton->Integral(intOpt) << endl;
  if (pzHist->Integral(intOpt) != 0) pzHist->Scale(1./pzHist->Integral(intOpt));
  if (xWC4Hist->Integral(intOpt) != 0) xWC4Hist->Scale(1./xWC4Hist->Integral(intOpt));
  if (yWC4Hist->Integral(intOpt) != 0) yWC4Hist->Scale(1./yWC4Hist->Integral(intOpt));
  if (thetaxzHist->Integral(intOpt) != 0) thetaxzHist->Scale(1./thetaxzHist->Integral(intOpt));
  if (sinThetayzHist->Integral(intOpt) != 0) sinThetayzHist->Scale(1./sinThetayzHist->Integral(intOpt));
  if (pzHistProton->Integral(intOpt) != 0) pzHistProton->Scale(1./pzHistProton->Integral(intOpt));
  TCanvas c1;
  pzHist->Draw();
  c1.SaveAs("weights_pz.png");
  xWC4Hist->Draw();
  c1.SaveAs("weights_xWC4.png");
  yWC4Hist->Draw();
  c1.SaveAs("weights_yWC4.png");
  thetaxzHist->Draw();
  c1.SaveAs("weights_thetaxz.png");
  sinThetayzHist->Draw();
  c1.SaveAs("weights_sinThetayz.png");
  pzHistProton->Draw();
  c1.SaveAs("weights_pzProton.png");

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

  tree->SetBranchAddress("nTOFs",&nTOFs);
  tree->SetBranchAddress("TOFs",&TOFs);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  TTree* friendTree = new TTree("friend","");
  float allWeight, pzWeight, positionWeight, xWeight, yWeight;
  float angleWeight, thetaxzWeight, sinThetayzWeight;

  friendTree->Branch("allWeight",&allWeight,"allWeight/F");
  friendTree->Branch("pzWeight",&pzWeight,"pzWeight/F");
  friendTree->Branch("positionWeight",&positionWeight,"positionWeight/F");
  friendTree->Branch("xWeight",&xWeight,"xWeight/F");
  friendTree->Branch("yWeight",&yWeight,"yWeight/F");
  friendTree->Branch("angleWeight",&angleWeight,"angleWeight/F");
  friendTree->Branch("thetaxzWeight",&thetaxzWeight,"thetaxzWeight/F");
  friendTree->Branch("sinThetayzWeight",&sinThetayzWeight,"sinThetayzWeight/F");

  float pzWeightProton;
  friendTree->Branch("pzWeightProton",&pzWeightProton,"pzWeightProton/F");

  float firstTOF;
  friendTree->Branch("firstTOF",&firstTOF,"firstTOF/F");

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
    positionWeight = 1.;
    xWeight = 1.;
    yWeight = 1.;
    angleWeight = 1.;
    thetaxzWeight = 1.;
    sinThetayzWeight = 1.;
    pzWeightProton = 1.;

    firstTOF = -999999999;
    if (nTOFs > 0) firstTOF = TOFs[0];

    if (isMC)
    {
      pzWeight = pzHist->GetBinContent(pzHist->FindBin(pzWC));
      xWeight = xWC4Hist->GetBinContent(xWC4Hist->FindBin(xWC4Hit));
      yWeight = yWC4Hist->GetBinContent(yWC4Hist->FindBin(yWC4Hit));

      float thxz = thetaxz(thetaWC,phiWC);
      float sthyz = sinthetayz(thetaWC,phiWC);
      thetaxzWeight = thetaxzHist->GetBinContent(thetaxzHist->FindBin(thxz));
      sinThetayzWeight = sinThetayzHist->GetBinContent(sinThetayzHist->FindBin(sthyz));
      
      positionWeight = xWeight * yWeight;
      angleWeight = thetaxzWeight * sinThetayzWeight;
      allWeight = positionWeight * angleWeight * pzWeight;

      if(nTOFs > 0 && TOFs[0] > 28. && TOFs[0] < 55 && pzWC > 450 && pzWC < 1100) 
      {
        pzWeightProton = pzHistProton->GetBinContent(pzHistProton->FindBin(pzWC));
      }
      else
      {
        pzWeightProton = 0;
      }
    }
    friendTree->Fill();
  } // for iEvent

  friendTree->Write();
  outFile->Close();

}
