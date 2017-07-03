#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

def fitMass2(c,hist):

    workspace = root.RooWorkspace("w")
    mass = root.RooRealVar("mass","Mass [MeV]",0,2000.)
    mass2 = root.RooRealVar("mass2","Mass Squared [MeV^{2}]",-2e5,3e6)
    observables = root.RooArgSet(mass2)

    d = root.RooRealVar("d","Distance",6.683)
    true_p = root.RooRealVar("true_p","",500)
    sigma_p = root.RooRealVar("sigma_p","",50.)
    sigma_dt = root.RooRealVar("sigma_dt","",0.5)

    particleConfigs = [
      ("electron","Electron",0.511,0.1),
      ("muon","Muon",105.658,0.1),
      ("pion","Pion",139.57,0.1),
      ("kaon","Kaon",493.677,0.005),
      ("proton","Proton",938.27,0.2),
      ("Deuteron","Deuteron",1875.6,0.002),
    ]

    gaussians = []
    gaussians2 = []
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

        variance_mass = root.RooFormulaVar("variance_mass_"+particle_name,"Mass Variance [MeV^4]",
                             "@4/@2*pow((@0+@1)/@5,2) + @0/@1*@3",
                             root.RooArgList(true_mass2,true_p2,true_dt2,variance_p,variance_dt,true_mass))

        sigma_mass = root.RooFormulaVar("sigma_mass_"+particle_name,"Mass Sigma [MeV^2]",
                             "sqrt(@0)",
                             root.RooArgList(variance_mass))

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
        variance_mass.Print()
        sigma_mass.Print()
        variance_mass2.Print()
        sigma_mass2.Print()

        gauss = root.RooGaussian("gauss_"+particle_name,particle_name,mass,true_mass,sigma_mass);
        gauss2 = root.RooGaussian("gauss2_"+particle_name,particle_name,mass2,true_mass2,sigma_mass2);
        gaussians.append(gauss)
        gaussians2.append(gauss2)
        fractions.append(fraction)
        wImport = getattr(workspace,"import")
        wImport(gauss)
        l = locals()
        for k in l:
          allVars.append(l[k])
    model = root.RooAddPdf("model","ToF Mass Model",root.RooArgList(*gaussians),root.RooArgList(*fractions))
    model2 = root.RooAddPdf("model2","ToF Mass Squared Model",root.RooArgList(*gaussians2),root.RooArgList(*fractions))

    #toy_data2 = model2.generate(root.RooArgSet(mass2),5000.)

    c.SetRightMargin(0.1)

    gaus_graphs = []
    gaus_titles = []
    frame2 = mass2.frame(root.RooFit.Title(""))
    model2.plotOn(frame2)
    gaus_graphs.append(frame2.getObject(int(frame2.numItems())-1))
    gaus_titles.append("All Particles")
    for iGauss, gauss in enumerate(gaussians2):
        gaus_graph = model2.plotOn(frame2,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]))
        gaus_graph.SetLineColor(COLORLIST[iGauss+1])
        gaus_graph.SetLineStyle(root.kDashed)
        gaus_graphs.append(frame2.getObject(int(frame2.numItems())-1))
        gaus_titles.append(gauss.GetTitle())
    #toy_data2.plotOn(frame2)
    frame2.Draw()
    leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
    c.SaveAs("TOFFit2.png")
    c.SaveAs("TOFFit2.pdf")

    gaus_graphs = []
    gaus_titles = []
    frame2_zoom = mass2.frame(root.RooFit.Title(""),root.RooFit.Range(-2e5,2e5))
    model2.plotOn(frame2_zoom)
    gaus_graphs.append(frame2_zoom.getObject(int(frame2_zoom.numItems())-1))
    gaus_titles.append("All Particles")
    for iGauss, gauss in enumerate(gaussians2):
        model2.plotOn(frame2_zoom,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]))
        gaus_graph.SetLineColor(COLORLIST[iGauss+1])
        gaus_graph.SetLineStyle(root.kDashed)
        gaus_graphs.append(frame2_zoom.getObject(int(frame2_zoom.numItems())-1))
        gaus_titles.append(gauss.GetTitle())
    frame2_zoom.Draw()
    leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
    c.SaveAs("TOFFit2_zoom.png")
    c.SaveAs("TOFFit2_zoom.pdf")

    gaus_graphs = []
    gaus_titles = []
    frame = mass.frame(root.RooFit.Title(""))
    model.plotOn(frame)
    gaus_graphs.append(frame.getObject(int(frame.numItems())-1))
    gaus_titles.append("All Particles")
    for iGauss, gauss in enumerate(gaussians):
        model.plotOn(frame,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]))
        gaus_graph.SetLineColor(COLORLIST[iGauss+1])
        gaus_graph.SetLineStyle(root.kDashed)
        gaus_graphs.append(frame.getObject(int(frame.numItems())-1))
        gaus_titles.append(gauss.GetTitle())
    #toy_data.plotOn(frame)
    frame.Draw()
    leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
    c.SaveAs("TOFFit.png")
    c.SaveAs("TOFFit.pdf")

if __name__ == "__main__":

  c = root.TCanvas("c")
  fitMass2(c,None)
  
