//
// RooFit model of LArIAT Time of Flight System
//


#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooFormulaVar.h"
#include "RooPlot.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TH1.h"
#include "TFile.h"
#include "TTree.h"
using namespace RooFit;

void tofRooFit()
{
   // Construct observable -- notice they match the tree variable names
   RooRealVar mass2("mass2","Reco Mass Squared [MeV^{2}]",-5e4,3e6);
   RooRealVar mass("mass","Reco Mass [MeV]",0, 1500);
   RooRealVar reco_tof("reco_tof","Reco TOF [ns]",0,100);
   RooRealVar reco_momo("reco_momo","Reco Momentum [MeV/c]",0,2000);

   // Read in dataset
   // ---------------

   TFile* infile = new TFile("momentumTest.root");
   TTree* intree = (TTree*) infile->Get("lowlevel/Mass Tree");
   //infile->cd("lowlevel");
   //infile->ls();
   //intree->Print();

   // This is our data in RooFit format
   RooDataSet* data = new RooDataSet("data","data",RooArgSet(mass2,mass,reco_tof,reco_momo),Import(*intree));
   // This is how you cut on that data (notice that the result is a pointer
   RooDataSet* dataMassGt500 = (RooDataSet*) data->reduce("mass>500.");
   RooDataSet* dataMassGt800 = (RooDataSet*) data->reduce("mass>800.");
   RooDataSet* dataMassGt800Momo650to750 = (RooDataSet*) dataMassGt800->reduce("reco_momo > 650. && reco_momo < 750.");

   // S e t u p   c o m p o n e n t   p d f s 
   // ---------------------------------------

   // Construct nuisance parameters
   RooRealVar true_mass("true_mass","True Mass [MeV]",938.27);
   RooRealVar d("d","Distance [m]",6.683);
   RooRealVar true_p("true_p","True Momentum [MeV]",700);

   RooRealVar sigma_p("sigma_p","Momentum Smearing Sigma [MeV]",50,1.,70.);
   RooRealVar sigma_dt("sigma_dt","#Delta t Smearing Sigma [ns]",0.5);
   RooRealVar shift_p2("shift_p2","Shift in Momentum Squared [MeV^{2}]",0.);//,-100,100);
   RooRealVar shift_dt2("shift_dt2","Shift in #Delta t Squared [ns^{2}]",250.,-1000,1000);

   // Construct dependent parameters

   // Compute true_dt from d, true_mass, and true_p
   RooFormulaVar true_dt2("true_dt2","True #Delta t Squared [ns^{2}]",
                        "@2*@2/0.29979/0.29979*(1+@1*@1/@0/@0)",
                        RooArgList(true_p,true_mass,d));

   RooFormulaVar true_mass2("true_mass2","True Mass Squared [MeV^{2}]",
                        "pow(@0,2)",
                        RooArgList(true_mass));

   RooFormulaVar true_p2("true_p2","True Momentum Squared [MeV^{2}]",
                        "pow(@0,2)",
                        RooArgList(true_p));
   RooFormulaVar true_dt("true_dt","True #Delta t [ns]",
                        "sqrt(@0)",
                        RooArgList(true_dt2));

   RooFormulaVar measured_dt2_mean("measured_dt_mean","Mean Measured #Delta t Squared [ns^{2}]",
                        "@0+@1",
                        RooArgList(true_dt2,shift_dt2));
   RooFormulaVar measured_p2_mean("measured_p2_mean","Mean Measured Momentum Squared [MeV^{2}]",
                        "@0+@1",
                        RooArgList(true_p2,shift_p2));

   RooFormulaVar variance_p("variance_p","Variance of Momentum [MeV^{2}]",
                        "pow(@0,2)",
                        RooArgList(sigma_p));

   RooFormulaVar variance_dt("variance_dt","Variance of #Delta t [ns^{2}]",
                        "pow(@0,2)",
                        RooArgList(sigma_dt));

   RooFormulaVar d2("d2","Distance^{2} [m^{2}]","pow(@0,2)",RooArgList(d));

   RooFormulaVar variance_mass2("variance_mass2","Mass Squared Variance [MeV^4]",
                        "4/true_dt2*pow(true_mass2+true_p2,2)*variance_dt + 4*pow(true_mass2,2)/true_p2*variance_p",
                        RooArgList(true_mass2,true_p2,true_dt2,d2,variance_p,variance_dt));

   RooFormulaVar sigma_mass2("sigma_mass2","Mass Squared Sigma [MeV^2]",
                        "sqrt(@0)",
                        RooArgList(variance_mass2));

   RooFormulaVar measured_mass2_mean("measured_mass2_mean","Measured Mass Squared Mean [MeV]","@0*(@1*pow(0.29979,2)/@2-1)",RooArgList(measured_p2_mean,measured_dt2_mean,d2));

   //true_mass2.Print();
   //true_p2.Print();
   //true_dt2.Print();
   //d2.Print();
   //variance_p.Print();
   //variance_dt.Print();
   //variance_mass2.Print();
   //sigma_mass2.Print();

   //RooFormulaVar mean_mass2("true_mass2","True Mass Squared [MeV]",
   //                     "@0*@0*(@1*@1*0.29979*0.29979/@2/@2-1.)",
   //                     RooArgList(true_p,true_dt,d));

   // Construct PDFs
   //RooGaussian gauss("gauss","Gaussian",mass2,true_mass2,sigma_mass2);
   RooGaussian gauss("gauss","Gaussian",mass2,measured_mass2_mean,sigma_mass2);

   RooAbsPdf* modelPtr = dynamic_cast<RooAbsPdf*>(&gauss);

   // S a m p l e ,   f i t   a n d   p l o t   c o n v o l u t e d   p d f 
   // ----------------------------------------------------------------------

   // Sample 1000 events in x from gxlx
//   RooDataSet* toy_data = gauss.generate(RooArgList(mass2),5000);

   modelPtr->fitTo(*data);//,Range(950e3,1150e3));

   // Plot data, landau pdf, landau (X) gauss pdf
   RooPlot* frame2 = mass2.frame(Title(""));
//   toy_data->plotOn(frame);
   dataMassGt800Momo650to750->plotOn(frame2);
   gauss.plotOn(frame2);//,Range(0.,3000.));

   // Draw frame on canvas
   TCanvas* c = new TCanvas("c");
   //gPad->SetLeftMargin(0.15); frame->GetYaxis()->SetTitleOffset(1.4);
   frame2->Draw();
   c->SaveAs("FitTOF2.png");
   c->SaveAs("FitTOF2.pdf");

   // Plot data, landau pdf, landau (X) gauss pdf
   RooPlot* frame = mass.frame(Title(""));
//   toy_data->plotOn(frame);
   data->plotOn(frame);

   // Draw frame on canvas
   frame->Draw();
   c->SaveAs("FitTOF.png");
   c->SaveAs("FitTOF.pdf");


   RooPlot* frame_momo = reco_momo.frame(Title(""));
   data->plotOn(frame_momo);
   frame_momo->Draw();
   c->SaveAs("FitTOF_momentum.png");
   c->SaveAs("FitTOF_momentum.pdf");

   RooPlot* frame_tof = reco_tof.frame(Title(""));
   data->plotOn(frame_tof);
   frame_tof->Draw();
   c->SaveAs("FitTOF_tof.png");
   c->SaveAs("FitTOF_tof.pdf");
}



