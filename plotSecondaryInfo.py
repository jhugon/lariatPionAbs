#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def plotManyFilesOneAxis(fileConfigs,histConfigs,canvas,treename):
  """
  fileConfigs is a list of dictionaries configuring the files
  histConfigs is a list of dictionaries configuring the histograms
  canvas is a root TCanvas
  treename is where to find the tree in each file

  fileConfig options:
    fn: filename
    pdg: PDG ID number (unused)
    name: name of sample (unused)
    title: title of sample: will be used for legends
    color: will be used for line/marker color
    scaleFactor: scale histograms by this much after filling
  histConfig options:
    name: name of histogram, used for savename
    xtitle: x axis title
    ytitle: y axis title
    var: variable to draw, first argument to tree.Draw
    cuts: cut string, second argument to tree.Draw
  """
  
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get(treename)
    fileConfig['f'] = f
    fileConfig['tree'] = tree

  for histConfig in histConfigs:
    hists = []
    binning = histConfig['binning']
    var = histConfig['var']
    cuts = histConfig['cuts']
    for fileConfig in fileConfigs:
      hist = Hist(*binning)
      hist.SetLineColor(fileConfig['color'])
      varAndHist = var + " >> " + hist.GetName()
      tree = fileConfig['tree']
      f = fileConfig['f']
      tree.Draw(varAndHist,cuts)
      scaleFactor = 1.
      if "scaleFactor" in fileConfig:
        scaleFactor = fileConfig['scaleFactor']
      hist.Scale(scaleFactor)
      hists.append(hist)
    axisHist = makeStdAxisHist(hists,freeTopSpace=0.35)
    xtitle = ""
    ytitle = "Events/bin"
    if "xtitle" in histConfig:
      xtitle = histConfig['xtitle']
    if "ytitle" in histConfig:
      ytitle = histConfig['ytitle']
    setHistTitles(axisHist,xtitle,ytitle)
    axisHist.Draw()
    for h in reversed(hists):
      h.Draw("histsame")
    labels = [fileConfig['title'] for fileConfig in fileConfigs]
    leg = drawNormalLegend(hists,labels)
    canvas.RedrawAxis()
    saveNameBase = histConfig['name'] + "Hist"
    canvas.SaveAs(saveNameBase+".png")
    canvas.SaveAs(saveNameBase+".pdf")


if __name__ == "__main__":

  binningArg = [325,0.,26.,200,0.,100.]
  evalFrac = 0.1
  fileConfigs = [
    {
      'fn': "/scratch/jhugon/catalogue/anaTree_p_v10.root",
      'pdg': 2212,
      'name': "p",
      'title': "p",
      'color': root.kGreen+1,
    },
    {
      'fn': "/scratch/jhugon/catalogue/anaTree_pip_v11.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+}",
      'color': root.kBlack,
      'scaleFactor' : 0.5,
    },
    {
      'fn': "/scratch/jhugon/catalogue/anaTree_mup_v10.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+}",
      'color': root.kRed,
    },
    {
      'fn': "/scratch/jhugon/catalogue/anaTree_kp_v10.root",
      'pdg': 321,
      'name': "kp",
      'title': "K^{+}",
      'color': root.kBlue,
    },
  ]

  histConfigs = [
    {
      'name': "pPrimary",
      'xtitle': "Primary particle |p| [GeV/c]",
      'binning': [100,0,1.5],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)",
      'cuts': "process_primary",
    },
    {
      'name': "pSecondary",
      'xtitle': "Secondary particle |p| [GeV/c]",
      'ytitle': "Entries/bin",
      'binning': [100,0,0.75],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)",
      'cuts': "!process_primary && Mother == 1 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && abs(pdg) < 1000000",
      #'cuts': "!process_primary && pdg != 2112",
    },
    #{
    #  'name': "motherPecondary",
    #  'xtitle': "Mother TrackID",
    #  'ytitle': "Entries/bin",
    #  'binning': [21,-0.5,20.5],
    #  'var': "Mother",
    #  'cuts': "process_primary && abs(pdg) < 1000000",
    #},
    #{
    #  'name': "motherSecondary",
    #  'xtitle': "Mother TrackID",
    #  'ytitle': "Entries/bin",
    #  'binning': [21,-0.5,20.5],
    #  'var': "Mother",
    #  'cuts': "!process_primary && abs(pdg) < 1000000",
    #},
  ]

  c = root.TCanvas()
  plotManyFilesOneAxis(fileConfigs,histConfigs,c,"anatree/anatree")

  if False:
    pdgSecondariesSet = set()
    pdgTertiariesSet = set()
    for fileConfig in fileConfigs:
      tree = fileConfig['tree']
      for iEntry in range(min(tree.GetEntries(),100)):
        tree.GetEntry()
        #print "tree.pdg[iGeant], tree.TrackId[iGeant], tree.Mother[iGeant], tree.NumberDaughters[iGeant]"
        for iGeant in range(tree.geant_list_size):
          #print tree.pdg[iGeant], tree.TrackId[iGeant], tree.Mother[iGeant], tree.NumberDaughters[iGeant]
          if not tree.process_primary[iGeant]:
            pdg = tree.pdg[iGeant]
            motherNum = tree.Mother[iGeant]
            if motherNum == 1 and not pdg in pdgSecondariesSet:
              pdgSecondariesSet.add(pdg)
            elif motherNum != 1 and not pdg in pdgTertiariesSet:
              pdgTertiariesSet.add(pdg)
    
    pdgSecondariesList = sorted(list(pdgSecondariesSet))
    print "PDG IDs of Secondary Particles:"
    for pdg in pdgSecondariesList:
      print pdg
    pdgTertiariesList = sorted(list(pdgTertiariesSet))
    print "PDG IDs of Tertiary Particles:"
    for pdg in pdgTertiariesList:
      print pdg
