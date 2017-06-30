#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

def fitMass2(c,hist):

    workspace = root.RooWorkspace("w")
    mass2 = root.RooRealVar("mass2","Mass Squared",-5e4,3e6)
    observables = root.RooArgSet(mass2)

    d = root.RooRealVar("d","Distance",6.683)
    true_p = root.RooRealVar("true_p","",1000.)
    sigma_p = root.RooRealVar("sigma_p","",100.)
    sigma_dt = root.RooRealVar("sigma_dt","",0.1)

    particleConfigs = [
      ("electron","Electron",0.511,0.05),
      ("muon","Muon",105.658,0.02),
      ("pion","Pion",139.57,0.1),
      ("kaon","Kaon",493.677,0.02),
      ("proton","Proton",938.27,0.2),
      #("Deuteron","Deuteron",1875.6,0.02),
    ]

    gaussians = []
    fractions = []

    allVars = []
    for particle_name, particle_title, particle_mass, particle_fraction in particleConfigs:
        fraction = root.RooRealVar("fraction_"+particle_name,"Fraction of "+particle_title,particle_fraction,0.,1.)

        true_mass = root.RooRealVar("true_mass_"+particle_name,"True Mass of "+particle_title,particle_mass)

        true_dt = root.RooFormulaVar("true_dt_"+particle_name,"True #Delta t [ns]",
                             "sqrt(@2*@2/0.29979/0.29979*(1+@1*@1/@0/@0))",
                             root.RooArgList(true_p,true_mass,d))

        true_mass2 = root.RooFormulaVar("true_mass2_"+particle_name,"True Mass Squared [MeV^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(true_mass))

        true_p2 = root.RooFormulaVar("true_p2_"+particle_name,"True Momentum Squared [MeV^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(true_p))
        true_dt2 = root.RooFormulaVar("true_dt2_"+particle_name,"True #Delta t Squared [ns^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(true_dt))
        variance_p = root.RooFormulaVar("variance_p_"+particle_name,"Variance of Momentum [MeV^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(sigma_p))
        variance_dt = root.RooFormulaVar("variance_dt_"+particle_name,"Variance of #Delta t [ns^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(sigma_dt))

        d2 = root.RooFormulaVar("d2_"+particle_name,"Distance^{2} [m^{2}]","pow(@0,2)",root.RooArgList(d))

        variance_mass2 = root.RooFormulaVar("variance_mass2_"+particle_name,"Mass Squared Variance [MeV^4]",
                             "4/@2*pow(@0+@1,2)*@5 + 4*pow(@0,2)/@1*@4",
                             root.RooArgList(true_mass2,true_p2,true_dt2,d2,variance_p,variance_dt))

        sigma_mass2 = root.RooFormulaVar("sigma_mass2_"+particle_name,"Mass Squared Sigma [MeV^2]",
                             "sqrt(@0)",
                             root.RooArgList(variance_mass2))

        true_mass2.Print()
        true_p2.Print()
        true_dt2.Print()
        d2.Print()
        variance_p.Print()
        variance_dt.Print()
        variance_mass2.Print()
        sigma_mass2.Print()

        gauss = root.RooGaussian("gauss_"+particle_name,"Gaussian for "+particle_name,mass2,true_mass2,sigma_mass2);
        gaussians.append(gauss)
        fractions.append(fraction)
        wImport = getattr(workspace,"import")
        wImport(gauss)
        l = locals()
        for k in l:
          allVars.append(l[k])
    model = root.RooAddPdf("model","ToF Mass Squared Model",root.RooArgList(*gaussians),root.RooArgList(*fractions))

    toy_data = model.generate(observables,5000.)

    frame = mass2.frame(root.RooFit.Title(""))

    #toy_data.plotOn(frame)
    model.plotOn(frame)

    #for gauss in gaussians:
    #    model.plotOn(frame,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))

    #root.gPad.SetLeftMargin(0.15)
    #frame.GetYaxis().SetTitleOffset(1.4)
    #frame.Draw("same")
    #axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
    ##axisHist = root.TH2F("axisHist","",1,-1,1,1,1000,1300)
    #axisHist.Draw()
    #frame.Draw("same")
    frame.Draw()
    c.SaveAs("TOFFit.png")
    c.SaveAs("TOFFit.pdf")

if __name__ == "__main__":

  c = root.TCanvas("c")
  fitMass2(c,None)
  
