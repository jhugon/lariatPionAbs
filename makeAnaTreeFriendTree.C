
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
#define MAXTRACKS 1000
#define MAXTRACKHITS 1000

const double minx = -0.8;
const double miny = -25;
const double minz = -5;
const double maxx = 49.17;
const double maxy = 25;
const double maxz = 95;

void makeFriendTree (TString inputFileName,TString outputFileName, unsigned maxEvents)
{
  using namespace std;

  cout << "makeFriendTree for "<< inputFileName.Data() << " in file " << outputFileName.Data() << endl;

  TChain * tree = new TChain("anatree/anatree");
  tree->Add(inputFileName);

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

  int ntracks_reco;
  tree->SetBranchAddress("ntracks_reco",&ntracks_reco);

  int ntrkhits[MAXTRACKS];
  tree->SetBranchAddress("ntrkhits",&ntrkhits);

  double trklength[MAXTRACKS];
  tree->SetBranchAddress("trklength",&trklength);

  double trkpidlh_pi[MAXTRACKS][2], trkpidlh_p[MAXTRACKS][2];
  tree->SetBranchAddress("trkpidlh_pi",&trkpidlh_pi);
  tree->SetBranchAddress("trkpidlh_p",&trkpidlh_p);

  double trkz[MAXTRACKS][MAXTRACKHITS];
  tree->SetBranchAddress("trkz",&trkz);

  ///////////////////////////////
  ///////////////////////////////
  ///////////////////////////////
  // Friend Tree

  TFile* outFile = new TFile(outputFileName,"RECREATE");
  outFile->cd();

  TTree* friendTree = new TTree("friend","");
  double P[MAXGEANT];
  bool startsInTPC[MAXGEANT];
  bool endsInTPC[MAXGEANT];
  bool allSecondariesEndInTPC;
  bool allSecondaryPionsEndInTPC;
  bool allSecondaryProtonsEndInTPC;
  bool allSecondaryPhotonsEndInTPC;

  friendTree->Branch("geant_list_size",&geant_list_size,"geant_list_size/I"); // just in case
  friendTree->Branch("ntracks_reco",&ntracks_reco,"ntracks_reco/I"); // just in case
  friendTree->Branch("P",P,"P[geant_list_size]/D");
  friendTree->Branch("startsInTPC",startsInTPC,"startsInTPC[geant_list_size]/O");
  friendTree->Branch("endsInTPC",endsInTPC,"endsInTPC[geant_list_size]/O");
  friendTree->Branch("allSecondariesEndInTPC",&allSecondariesEndInTPC,"allSecondariesEndInTPC/O");
  friendTree->Branch("allSecondaryPionsEndInTPC",&allSecondaryPionsEndInTPC,"allSecondaryPionsEndInTPC/O");
  friendTree->Branch("allSecondaryProtonsEndInTPC",&allSecondaryProtonsEndInTPC,"allSecondaryProtonsEndInTPC/O");
  friendTree->Branch("allSecondaryPhotonsEndInTPC",&allSecondaryPhotonsEndInTPC,"allSecondaryPhotonsEndInTPC/O");

  int nSecondaryPiPlus;
  int nSecondaryPi0;
  int nSecondaryPiMinus;
  int nSecondaryProton;
  int nSecondaryPhoton;
  int nSecondaryNeutron;

  friendTree->Branch("nSecondaryPiPlus",&nSecondaryPiPlus,"nSecondaryPiPlus/I");
  friendTree->Branch("nSecondaryPi0",&nSecondaryPi0,"nSecondaryPi0/I");
  friendTree->Branch("nSecondaryPiMinus",&nSecondaryPiMinus,"nSecondaryPiMinus/I");
  friendTree->Branch("nSecondaryProton",&nSecondaryProton,"nSecondaryProton/I");
  friendTree->Branch("nSecondaryPhoton",&nSecondaryPhoton,"nSecondaryPhoton/I");
  friendTree->Branch("nSecondaryNeutron",&nSecondaryNeutron,"nSecondaryNeutron/I");

  float trkpidlhr_pi_p[MAXTRACKS][2];
  friendTree->Branch("trkpidlhr_pi_p",&trkpidlhr_pi_p,"trkpidlhr_pi_p[ntracks_reco][2]/O");

  int nTracksFirst2cm, nTracksFirst14cm;
  friendTree->Branch("nTracksFirst2cm",&nTracksFirst2cm,"nTracksFirst2cm/I");
  friendTree->Branch("nTracksFirst14cm",&nTracksFirst14cm,"nTracksFirst14cm/I");

  int nTracksLengthLt5cm;
  friendTree->Branch("nTracksLengthLt5cm",&nTracksLengthLt5cm,"nTracksLengthLt5cm/I");

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

    // reset friend tree variables
    for (unsigned iGeant= 0; iGeant < MAXGEANT; iGeant++)
    {
      P[iGeant] = -1.;
      startsInTPC[iGeant] = false;
      endsInTPC[iGeant] = false;
    }
    allSecondariesEndInTPC = true;
    allSecondaryPionsEndInTPC = true;
    allSecondaryProtonsEndInTPC = true;
    allSecondaryPhotonsEndInTPC = true;
    nSecondaryPiPlus = 0;
    nSecondaryPi0 = 0;
    nSecondaryPiMinus = 0;
    nSecondaryProton = 0;
    nSecondaryPhoton = 0;
    nSecondaryNeutron = 0;
    nTracksFirst2cm = 0;
    nTracksFirst14cm = 0;
    nTracksLengthLt5cm = 0;

    tree->GetEvent(iEvent);
    if (iEvent % reportEach == 0) cout << "Event: " << iEvent << endl;

    for (int iPart=0; iPart<geant_list_size; iPart++)
    {
      startsInTPC[iPart] = StartPointx[iPart] > minx && StartPointx[iPart] < maxx 
               && StartPointy[iPart] > miny && StartPointy[iPart] < maxy
               && StartPointz[iPart] > minz && StartPointz[iPart] < maxz;
      endsInTPC[iPart] = EndPointx[iPart] > minx && EndPointx[iPart] < maxx 
                    && EndPointy[iPart] > miny && EndPointy[iPart] < maxy
                    && EndPointz[iPart] > minz && EndPointz[iPart] < maxz;
      P[iPart] = pow(Px[iPart]*Px[iPart] + Py[iPart]*Py[iPart] + Pz[iPart]*Pz[iPart],0.5);
      if (Mother[iPart] == 1 && !endsInTPC[iPart] && abs(pdg[iPart]) < 1000000000)
      {
        allSecondariesEndInTPC = false;
        if (abs(pdg[iPart])==211)
        {
          allSecondaryPionsEndInTPC = false;
        }
        else if (pdg[iPart]==2212)
        {
          allSecondaryProtonsEndInTPC = false;
        }
        else if (pdg[iPart]==22)
        {
          allSecondaryPhotonsEndInTPC = false;
        }
      }
      if (Mother[iPart] == 1)
      {
        if (pdg[iPart] == 211)
        {
          nSecondaryPiPlus += 1;
        }
        else if (pdg[iPart] == 111)
        {
          nSecondaryPi0 += 1;
        }
        else if (pdg[iPart] == -211)
        {
          nSecondaryPiMinus += 1;
        }
        else if (pdg[iPart] == 2212)
        {
          nSecondaryProton += 1;
        }
        else if (pdg[iPart] == 22)
        {
          nSecondaryPhoton += 1;
        }
        else if (pdg[iPart] == 2112)
        {
          nSecondaryNeutron += 1;
        }
      } // if Mother == 1

      //cout << pdg[iPart] << ", " << TrackId[iPart] << ", "<< Mother[iPart] << ", " << startsInTPC[iPart] << ", " << endsInTPC[iPart]  << ", " << P[iPart] << endl;
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

    for(int iTrack=0; iTrack<ntracks_reco; iTrack++)
    {
      for(int iPlane=0; iPlane<2; iPlane++)
      {
        trkpidlhr_pi_p[iTrack][iPlane] = trkpidlh_pi[iTrack][iPlane] - trkpidlh_p[iTrack][iPlane];
      }

      if(trklength[iTrack] < 5.0)
      {
        nTracksLengthLt5cm++;
      }

      bool trkInFirst2cm = false;
      bool trkInFirst14cm = false;
      for(int iTrkHit=0; iTrkHit < ntrkhits[iTrack]; iTrkHit++)
      {
        if (trkz[iTrack][iTrkHit] < 2.)
        {
            trkInFirst2cm = true;
        }
        if (trkz[iTrack][iTrkHit] < 14.)
        {
            trkInFirst14cm = true;
            break;
        }
      } // for iTrkHit
      if(trkInFirst2cm)
      {
        nTracksFirst2cm++;
      }
      if(trkInFirst14cm)
      {
        nTracksFirst14cm++;
      }
    } // for iTrack

    friendTree->Fill();
  } // for iEvent

  friendTree->Write();
  outFile->Close();

}
