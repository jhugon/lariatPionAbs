
#include <TSystem.h>
#include <TROOT.h>
#include <TFile.h>
#include <TChain.h>
#include <TTree.h>
//#include <TH2F.h>
//#include <TH1F.h>
//#include <TF1.h>
//#include <TRandom3.h>

#include <iostream>
#include <vector>

#define MAXGEANT 1000

const double minx = -0.8;
const double miny = -25;
const double minz = -5;
const double maxx = 49.17;
const double maxy = 25;
const double maxz = 95;

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

  int no_primaries, geant_list_size;
  tree->SetBranchAddress("no_primaries",&no_primaries);
  tree->SetBranchAddress("geant_list_size",&geant_list_size);

  int pdg[MAXGEANT], Process[MAXGEANT], NumberDaughters[MAXGEANT], Mother[MAXGEANT], TrackId[MAXGEANT], process_primary[MAXGEANT];
  tree->SetBranchAddress("pdg",&pdg);
  tree->SetBranchAddress("Process",&Process);
  tree->SetBranchAddress("NumberDaughters",&NumberDaughters);
  tree->SetBranchAddress("Mother",&Mother);
  tree->SetBranchAddress("TrackId",&TrackId);
  tree->SetBranchAddress("process_primary",&process_primary);

  double Eng[MAXGEANT], Px[MAXGEANT], Py[MAXGEANT], Pz[MAXGEANT];
  double EndEng[MAXGEANT], EndPx[MAXGEANT], EndPy[MAXGEANT], EndPz[MAXGEANT];
  tree->SetBranchAddress("Eng",&Eng);
  tree->SetBranchAddress("Px",&Px);
  tree->SetBranchAddress("Py",&Py);
  tree->SetBranchAddress("Pz",&Pz);
  tree->SetBranchAddress("EndEng",&EndEng);
  tree->SetBranchAddress("EndPx",&EndPx);
  tree->SetBranchAddress("EndPy",&EndPy);
  tree->SetBranchAddress("EndPz",&EndPz);

  double StartPointx[MAXGEANT], StartPointy[MAXGEANT], StartPointz[MAXGEANT];
  double EndPointx[MAXGEANT], EndPointy[MAXGEANT], EndPointz[MAXGEANT];
  tree->SetBranchAddress("StartPointx",&StartPointx);
  tree->SetBranchAddress("StartPointy",&StartPointy);
  tree->SetBranchAddress("StartPointz",&StartPointz);
  tree->SetBranchAddress("EndPointx",&EndPointx);
  tree->SetBranchAddress("EndPointy",&EndPointy);
  tree->SetBranchAddress("EndPointz",&EndPointz);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TTree* friendTree = new TTree("friend","");
  double P[MAXGEANT];
  bool startsInTPC[MAXGEANT];
  bool endsInTPC[MAXGEANT];
  bool allSecondariesEndInTPC;

  friendTree->Branch("geant_list_size",&geant_list_size,"geant_list_size/I"); // just in case
  friendTree->Branch("P",P,"P[geant_list_size]/D");
  friendTree->Branch("startsInTPC",startsInTPC,"startsInTPC[geant_list_size]/O");
  friendTree->Branch("endsInTPC",endsInTPC,"endsInTPC[geant_list_size]/O");
  friendTree->Branch("allSecondariesEndInTPC",&allSecondariesEndInTPC,"allSecondariesEndInTPC/O");

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Event Loop

  unsigned nEvents = tree->GetEntries();
  unsigned reportEach=1000;

  for(unsigned iEvent=0; iEvent<nEvents;iEvent++)
  {
    if(iEvent >= maxEvents)
      break;

    // reset friend tree variables
    for (unsigned iGeant= 0; iGeant < MAXGEANT; iGeant++)
    {
      P[iGeant] = -1.;
      startsInTPC[iGeant] = false;
      endsInTPC[iGeant] = false;
    }
    allSecondariesEndInTPC = true;

    tree->GetEvent(iEvent);
    if (iEvent % reportEach == 0) cout << "Event: " << iEvent << endl;

    for (int iPart=0; iPart<geant_list_size; iPart++)
    {
      if (abs(pdg[iPart]) < 1000000000)
      {
        startsInTPC[iPart] = StartPointx[iPart] > minx && StartPointx[iPart] < maxx 
                 && StartPointy[iPart] > miny && StartPointy[iPart] < maxy
                 && StartPointz[iPart] > minz && StartPointz[iPart] < maxz;
        endsInTPC[iPart] = EndPointx[iPart] > minx && EndPointx[iPart] < maxx 
                      && EndPointy[iPart] > miny && EndPointy[iPart] < maxy
                      && EndPointz[iPart] > minz && EndPointz[iPart] < maxz;
        P[iPart] = pow(Px[iPart]*Px[iPart] + Py[iPart]*Py[iPart] + Pz[iPart]*Pz[iPart],0.5);
        if (Mother[iPart] == 1 && !endsInTPC[iPart])
        {
          allSecondariesEndInTPC = false;
        }

        //cout << pdg[iPart] << ", " << TrackId[iPart] << ", "<< Mother[iPart] << ", " << startsInTPC[iPart] << ", " << endsInTPC[iPart]  << ", " << P[iPart] << endl;
      } // if pdg
    } // for iPart in geant_list_size

    //if (endsInTPC[0] && allSecondariesEndInTPC)
    //{
    //  cout << "Event: " << iEvent << endl;
    //  for (int iPart=0; iPart<geant_list_size; iPart++)
    //  {
    //    if (Mother[iPart]<=1 && abs(pdg[iPart]) < 1000000000)
    //    {
    //      cout << pdg[iPart] << ", " << TrackId[iPart] << ", "<< Mother[iPart] << ", " << startsInTPC[iPart] << ", " << endsInTPC[iPart] << ", " << P[iPart] << endl;
    //    } // if pdg
    //  } // for iPart in geant_list_size
    //} // if primary ends in tpc and allSecondariesEndInTPC

    friendTree->Fill();
  } // for iEvent

  friendTree->Write();
  outFile->Close();

}
