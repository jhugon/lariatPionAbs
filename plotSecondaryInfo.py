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
    fn: filename REQUIRED
    pdg: PDG ID number (unused)
    name: name of sample (unused)
    title: title of sample: will be used for legends
    color: will be used for line/marker color
    scaleFactor: scale histograms by this much after filling
  histConfig options:
    name: name of histogram, used for savename REQUIRED
    xtitle: x axis title
    ytitle: y axis title
    var: variable to draw, first argument to tree.Draw REQUIRED
    cuts: cut string, second argument to tree.Draw REQUIRED
    xlim: xlimits, a two element list of xlimits for plot
    ylim: ylimits, a two element list of ylimits for plot
    caption, captionleft1, captionleft2, captionleft3, captionright1,
        captionright2, captionright3, preliminaryString:
        all are passed to drawStandardCaptions
    normToBinWidth: if True, normalize histogram to bin width (after applying
        scaleFactor)
  """
  
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get(treename)
    fileConfig['f'] = f
    fileConfig['tree'] = tree

  for histConfig in histConfigs:
    # setup
    hists = []
    binning = histConfig['binning']
    var = histConfig['var']
    cuts = histConfig['cuts']
    xtitle = ""
    ytitle = "Events/bin"
    if "xtitle" in histConfig: xtitle = histConfig['xtitle']
    if "ytitle" in histConfig: ytitle = histConfig['ytitle']
    xlim = []
    ylim = []
    if "xlim" in histConfig: xlim = histConfig['xlim']
    if "ylim" in histConfig: ylim = histConfig['ylim']
    caption = ""
    captionleft1 = ""
    captionleft2 = ""
    captionleft3 = ""
    captionright1 = ""
    captionright2 = ""
    captionright3 = ""
    preliminaryString = ""
    if "caption" in histConfig: caption = histConfig['caption']
    if "captionleft1" in histConfig: captionleft1 = histConfig['captionleft1']
    if "captionleft2" in histConfig: captionleft2 = histConfig['captionleft2']
    if "captionleft3" in histConfig: captionleft3 = histConfig['captionleft3']
    if "captionright1" in histConfig: captionright1 = histConfig['captionright1']
    if "captionright2" in histConfig: captionright2 = histConfig['captionright2']
    if "captionright3" in histConfig: captionright3 = histConfig['captionright3']
    if "preliminaryString" in histConfig: preliminaryString = histConfig['preliminaryString']
    # now on to the real work
    for fileConfig in fileConfigs:
      hist = Hist(*binning)
      hist.SetLineColor(fileConfig['color'])
      varAndHist = var + " >> " + hist.GetName()
      tree = fileConfig['tree']
      f = fileConfig['f']
      tree.Draw(varAndHist,cuts)
      scaleFactor = 1.
      if "scaleFactor" in fileConfig: scaleFactor = fileConfig['scaleFactor']
      hist.Scale(scaleFactor)
      if "normToBinWidth" in histConfig and histConfig["normToBinWidth"]:
        normToBinWidth(hist)
      hists.append(hist)
    axisHist = makeStdAxisHist(hists,freeTopSpace=0.35,xlim=xlim,ylim=ylim)
    setHistTitles(axisHist,xtitle,ytitle)
    axisHist.Draw()
    for h in reversed(hists):
      h.Draw("histsame")
    labels = [fileConfig['title'] for fileConfig in fileConfigs]
    leg = drawNormalLegend(hists,labels)
    drawStandardCaptions(canvas,caption,captionleft1=captionleft1,captionleft2=captionleft2,captionleft3=captionleft3,captionright1=captionright1,captionright2=captionright2,captionright3=captionright3,preliminaryString=preliminaryString)
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
      'xtitle': "Primary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,1500],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "process_primary",
    },
    {
      'name': "pSecondary",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "!process_primary && Mother == 1 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && abs(pdg) < 1000000",
      #'cuts': "!process_primary && pdg != 2112",
    },
    {
      'name': "pTertiary",
      'xtitle': "Tertiary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "!process_primary && Mother != 1 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01 && abs(pdg) < 1000000",
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
