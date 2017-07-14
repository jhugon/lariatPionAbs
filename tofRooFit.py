#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

def fitMass2(c,do_toy_data=False,plot_components=False,binned=True):

    workspace = root.RooWorkspace("w")
    mass = root.RooRealVar("mass","Mass [MeV]",0,2000.)
    mass2 = root.RooRealVar("mass2","Mass Squared [MeV^{2}]",-2e5,3e6)
    true_p = root.RooRealVar("reco_momo","True Momentum [MeV]",500,0,1500.)
    reco_tof = root.RooRealVar("reco_tof","",0,100.)
    observables = root.RooArgSet(mass2)
    mass.setBins(20)
    mass2.setBins(20)
    true_p.setBins(30) # speeds up data-avaraging projection

    data = None
    Ndata = 1.
    if not do_toy_data:
        infile = root.TFile("momentumTest.root")
        intree = infile.Get("lowlevel/Mass Tree");
        intree.Draw("reco_tof:reco_momo >> tofVmomo(150,0,1500,90,0,90)","","colz")
        c.SaveAs("TOF_tofVmomo.pdf")
        c.SaveAs("TOF_tofVmomo.png")
        intree.Draw("mass:reco_momo >> massVmomo(150,0,1500,150,0,1500)","reco_tof < 75.","colz")
        c.SaveAs("TOF_massVmomo.pdf")
        c.SaveAs("TOF_massVmomo.png")
        intree.Draw("mass2:reco_momo >> mass2Vmomo(150,0,1500,200,-2e3,3e6)","","colz")
        c.SaveAs("TOF_mass2Vmomo.pdf")
        c.SaveAs("TOF_mass2Vmomo.png")
        intree.Draw("mass:reco_tof >> massVtof(100,0,100,150,0,1500)","reco_momo > 200","colz")
        c.SaveAs("TOF_massVtof.pdf")
        c.SaveAs("TOF_massVtof.png")
        
        data = root.RooDataSet("data","data",root.RooArgSet(mass2,mass,true_p,reco_tof),root.RooFit.Import(intree))
        data = data.reduce("reco_momo >200 && reco_tof < 75.")

        #data = data.reduce("reco_momo >600 && reco_momo < 605")
        #data = data.reduce("reco_momo >400 && reco_momo < 450")
        #data = data.reduce("reco_momo >700 && reco_momo < 605")
        Ndata = data.sumEntries()
        if binned:
            data = data.binnedClone()

    d = root.RooRealVar("d","Distance",6.683)
    sigma_p = root.RooRealVar("sigma_p","",50.)
    sigma_dt = root.RooRealVar("sigma_dt","",0.5)
    shift_dt2 = root.RooRealVar("shift_dt2","Shift of #Delta t Squared [ns^{2}]",74,-100,200)
    coef1_p = root.RooRealVar("coef1_p","1st Polynomial Coefficient for Momentum",1.120,1.,1.50)

    # Derived parameters
    d2 = root.RooFormulaVar("d2","Distance^{2} [m^{2}]","pow(@0,2)",root.RooArgList(d))
    true_p2 = root.RooFormulaVar("true_p2","True Momentum Squared [MeV^{2}]",
                         "pow(@0,2)",
                         root.RooArgList(true_p))
    measured_p = root.RooFormulaVar("measured_p","Measured Momentum [MeV]",
                         "@0*@1",
                         root.RooArgList(true_p,coef1_p))
    measured_p2 = root.RooFormulaVar("measured_p2","Measured Momentum Squared [MeV^{2}]",
                         "pow(@0,2)",
                         root.RooArgList(measured_p))

    # Make true momentum distribution
    true_p_norm1 = root.RooRealVar("true_p_norm1","",0.02)
    true_p_mean1 = root.RooRealVar("true_p_mean1","",100.)
    true_p_sigma1 = root.RooRealVar("true_p_sigma1","",20.)
    true_p_norm2 = root.RooRealVar("true_p_norm2","",0.02)
    true_p_mean2 = root.RooRealVar("true_p_mean2","",380.)
    true_p_sigma2 = root.RooRealVar("true_p_sigma2","",40.)
    true_p_norm3 = root.RooRealVar("true_p_norm3","",1.)
    true_p_mean3 = root.RooRealVar("true_p_mean3","",660.)
    true_p_sigma3 = root.RooRealVar("true_p_sigma3","",150.)
    true_p_gaus1 = root.RooGaussian("true_p_gaus1","True Momentum Gaus 1",true_p,true_p_mean1,true_p_sigma1)
    true_p_gaus2 = root.RooGaussian("true_p_gaus2","True Momentum Gaus 2",true_p,true_p_mean2,true_p_sigma2)
    true_p_gaus3 = root.RooGaussian("true_p_gaus3","True Momentum Gaus 3",true_p,true_p_mean3,true_p_sigma3)
    true_p_distribution = root.RooAddPdf("true_p_distribution","True Momentum Distribution",root.RooArgList(true_p_gaus1,true_p_gaus2,true_p_gaus3),root.RooArgList(true_p_norm1,true_p_norm2,true_p_norm3))

    particleConfigs = [
      #("electron","Electron",0.511,0.01*Ndata),
      #("muon","Muon",105.658,0.03*Ndata),
      ("pion","Pion",139.57,0.03*Ndata),
      ("kaon","Kaon",493.677,0.007*Ndata),
      ("proton","Proton",938.27,0.8*Ndata),
      #("Deuteron","Deuteron",1875.6,0.002*Ndata),
    ]

    gaussians = []
    gaussians2 = []
    fractions = []

    allVars = []
    for particle_name, particle_title, particle_mass, particle_fraction in particleConfigs:
        fraction = root.RooRealVar("N_"+particle_name,"Number of of "+particle_title,particle_fraction,0.,Ndata)
        true_mass = root.RooRealVar("true_mass_"+particle_name,"True Mass of "+particle_title,particle_mass)

        true_mass2 = root.RooFormulaVar("true_mass2_"+particle_name,"True Mass Squared [MeV^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(true_mass))


        true_dt2 = root.RooFormulaVar("true_dt2_"+particle_name,"True #Delta t Squared [ns^{2}]",
                             "@2/0.29979/0.29979*(1+@1/@0)",
                             root.RooArgList(true_p2,true_mass2,d2))
        true_dt = root.RooFormulaVar("true_dt_"+particle_name,"True #Delta t [ns]",
                             "sqrt(@0)",
                             root.RooArgList(true_dt2))

        variance_p = root.RooFormulaVar("variance_p_"+particle_name,"Variance of Momentum [MeV^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(sigma_p))
        variance_dt = root.RooFormulaVar("variance_dt_"+particle_name,"Variance of #Delta t [ns^{2}]",
                             "pow(@0,2)",
                             root.RooArgList(sigma_dt))

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

        mean_dt2 = root.RooFormulaVar("mean_dt2_"+particle_name,"Mean of #Delta t Squared [ns^{2}]",
                             "@0+@1",
                             root.RooArgList(true_dt2,shift_dt2));
        
        mean_mass2 = root.RooFormulaVar("mean_mass2_"+particle_name,"Mean Mass Squared [MeV^2]",
                             "@0*(@1/@2*0.29979*0.29979-1)",
                             root.RooArgList(measured_p2,mean_dt2,d2))
        mean_mass = root.RooFormulaVar("mean_mass_"+particle_name,"Mean Mass [MeV]",
                             "sqrt(@0)",
                             root.RooArgList(mean_mass2))

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
        mean_dt2.Print()
        mean_mass2.Print()
        mean_mass.Print()

        gauss = root.RooGaussian("gauss_"+particle_name,particle_name,mass,mean_mass,sigma_mass);
        gauss2 = root.RooGaussian("gauss2_"+particle_name,particle_name,mass2,mean_mass2,sigma_mass2);
        gaussians.append(gauss)
        gaussians2.append(gauss2)
        fractions.append(fraction)
        #wImport = getattr(workspace,"import")
        #wImport(gauss)
        #wImport(gauss2)
        l = locals()
        for k in l:
          allVars.append(l[k])
    model = root.RooAddPdf("model","ToF Mass Model",root.RooArgList(*gaussians),root.RooArgList(*fractions))
    model2 = root.RooAddPdf("model2","ToF Mass Squared Model",root.RooArgList(*gaussians2),root.RooArgList(*fractions))
    model_mass_momentum = root.RooProdPdf("model_mass_momentum","ToF Mass Model x Momentum Model",
                                        root.RooArgSet(true_p_distribution),
                                        root.RooFit.Conditional(
                                                                root.RooArgSet(model),
                                                                root.RooArgSet(mass)))
    model_mass2_momentum = root.RooProdPdf("model_mass2_momentum","ToF Mass^{2} Model x Momentum Model",
                                        root.RooArgSet(model2),
                                        root.RooFit.Conditional(
                                                                root.RooArgSet(true_p_distribution),
                                                                root.RooArgSet(true_p)))

    toy_data = None
    toy_data2 = None
    if do_toy_data:
        toy_data = model_mass_momentum.generate(root.RooArgSet(mass,true_p),5000.)
        toy_data2 = model_mass2_momentum.generate(root.RooArgSet(mass2,true_p),5000.)
    else:
        model_mass2_momentum.fitTo(data,
                    root.RooFit.ConditionalObservables(root.RooArgSet(true_p)),
                    root.RooFit.NumCPU(4))

    c.SetRightMargin(0.1)

    gaus_graphs = []
    gaus_titles = []
    frame2 = mass2.frame(root.RooFit.Title(""))
    if do_toy_data:
        toy_data2.plotOn(frame2)
        model2.plotOn(frame2,root.RooFit.ProjWData(toy_data2,True))
    else:
        data.plotOn(frame2)
        model2.plotOn(frame2,root.RooFit.ProjWData(data,True))
    gaus_graphs.append(frame2.getObject(int(frame2.numItems())-1))
    gaus_titles.append("All Particles")
    if plot_components:
        for iGauss, gauss in enumerate(gaussians2):
            if do_toy_data:
                model2.plotOn(frame2,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(toy_data2,True))
            else:
                model2.plotOn(frame2,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(data,True))
            gaus_graphs.append(frame2.getObject(int(frame2.numItems())-1))
            gaus_titles.append(gauss.GetTitle())
    frame2.Draw()
    if plot_components:
        leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
    c.SaveAs("TOFFit2.png")
    c.SaveAs("TOFFit2.pdf")

    gaus_graphs = []
    gaus_titles = []
    frame2_zoom = mass2.frame(root.RooFit.Title(""),root.RooFit.Range(-2e5,2e5))
    if do_toy_data:
        toy_data2.plotOn(frame2_zoom)
        model2.plotOn(frame2_zoom,root.RooFit.ProjWData(toy_data2,True))
    else:
        data.plotOn(frame2_zoom)
        model2.plotOn(frame2_zoom,root.RooFit.ProjWData(data,True))
    gaus_graphs.append(frame2_zoom.getObject(int(frame2_zoom.numItems())-1))
    gaus_titles.append("All Particles")
    if plot_components:
        for iGauss, gauss in enumerate(gaussians2):
            if do_toy_data:
                model2.plotOn(frame2_zoom,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(toy_data2,True))
            else:
                model2.plotOn(frame2_zoom,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(data,True))
            gaus_graphs.append(frame2_zoom.getObject(int(frame2_zoom.numItems())-1))
            gaus_titles.append(gauss.GetTitle())
    frame2_zoom.Draw()
    if plot_components:
        leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
    c.SaveAs("TOFFit2_zoom.png")
    c.SaveAs("TOFFit2_zoom.pdf")
#
#    gaus_graphs = []
#    gaus_titles = []
#    frame = mass.frame(root.RooFit.Title(""))
#    #frame.updateNormVars(root.RooArgSet(mass,true_p)) # makes RooFit contionalize on true_p
#    if do_toy_data:
#        toy_data.plotOn(frame)
#        model.plotOn(frame,root.RooFit.ProjWData(toy_data,True))
#    else:
#        data.plotOn(frame)
#        model.plotOn(frame,root.RooFit.ProjWData(data,True))
#    gaus_graphs.append(frame.getObject(int(frame.numItems())-1))
#    gaus_titles.append("All Particles")
#    if plot_components:
#        for iGauss, gauss in enumerate(gaussians):
#            if do_toy_data:
#                model.plotOn(frame,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(toy_data,True))
#            else:
#                model.plotOn(frame,root.RooFit.Components(gauss.GetName()),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iGauss+1]),root.RooFit.ProjWData(data,True))
#            gaus_graphs.append(frame.getObject(int(frame.numItems())-1))
#            gaus_titles.append(gauss.GetTitle())
#    frame.Draw()
#    if plot_components:
#        leg = drawNormalLegend(gaus_graphs,gaus_titles,option="l",position=(0.55,0.7,0.85,0.89))
#    c.SaveAs("TOFFit.png")
#    c.SaveAs("TOFFit.pdf")

    frame_p = true_p.frame()
    if do_toy_data:
        toy_data.plotOn(frame_p)
    else:
        data.plotOn(frame_p)
    true_p_distribution.plotOn(frame_p)
    frame_p.Draw()
    c.SaveAs("TOFFit_p.png")
    c.SaveAs("TOFFit_p.pdf")

if __name__ == "__main__":

  c = root.TCanvas("c")
  fitMass2(c)
  
