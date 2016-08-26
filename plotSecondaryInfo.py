#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def plotManyFilesOnePlot(fileConfigs,histConfigs,canvas,treename):
  """
  Plots the same histogram and cuts for a variety of files on one plot. Use to
    compare the same histogram from different samples. 

  fileConfigs is a list of dictionaries configuring the files
  histConfigs is a list of dictionaries configuring the histograms. It is a
    list so you can do multiple plots.
  canvas is a root TCanvas
  treename is where to find the tree in each file

  fileConfig options:
    fn: filename REQUIRED
    title: title of sample: will be used for legends
    color: will be used for line/marker color
    scaleFactor: scale histograms by this much after filling
    pdg: PDG ID number (unused)
    name: name of sample (unused)
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
    normalize: if True normalize histogram (after normToBinWidth)
    title: (unused)
    color: (unused)
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
      tree.Draw(varAndHist,cuts)
      scaleFactor = 1.
      if "scaleFactor" in fileConfig: scaleFactor = fileConfig['scaleFactor']
      hist.Scale(scaleFactor)
      if "normToBinWidth" in histConfig and histConfig["normToBinWidth"]:
        normToBinWidth(hist)
      if "normalize" in histConfig and histConfig['normalize']:
        integral = hist.Integral()
        hist.Scale(1./integral)
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

def plotManyHistsOnePlot(fileConfigs,histConfigs,canvas,treename):
  """
  For each file, plots multiple different histograms (cuts and/or variables) on one plot. Use to
    compare different cuts or variables on the same sample. 

  fileConfigs is a list of dictionaries configuring the files. fileConfigs is a
    list so you can plots for multiple samples.
  histConfigs is a list of dictionaries configuring the histograms
  canvas is a root TCanvas
  treename is where to find the tree in each file

  fileConfig options:
    fn: filename REQUIRED
    pdg: PDG ID number (unused)
    name: name of sample, used for savename REQUIRED
    title: title of sample (unused)
    color:  (unused)
    scaleFactor: scale histograms by this much after filling
  histConfig options:
    name: (unused)
    title: title of histogram, used for legend
    color: sets line/marker color of histogram
    xtitle: x axis title, the first one found in the list is used
    ytitle: y axis title, the first one found in the list is used
    var: variable to draw, first argument to tree.Draw REQUIRED
    cuts: cut string, second argument to tree.Draw REQUIRED
    xlim: xlimits, a two element list of xlimits for plot, first one found is used
    ylim: ylimits, a two element list of ylimits for plot, first one found is used
    caption, captionleft1, captionleft2, captionleft3, captionright1,
        captionright2, captionright3, preliminaryString:
        all are passed to drawStandardCaptions, first set of captions found is
        used
    normToBinWidth: if True, normalize histogram to bin width (after applying
        scaleFactor)
    normalize: if True normalize histogram (after normToBinWidth)
  """
  
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get(treename)
    fileConfig['f'] = f
    fileConfig['tree'] = tree
    xtitle = ""
    ytitle = "Events/bin"
    for histConfig in histConfigs:
      if "xtitle" in histConfig: 
        xtitle = histConfig['xtitle']
        break
    for histConfig in histConfigs:
      if "ytitle" in histConfig: 
        ytitle = histConfig['ytitle']
        break
    xlim = []
    ylim = []
    for histConfig in histConfigs:
      if "xlim" in histConfig: 
        xlim = histConfig['xlim']
        break
    for histConfig in histConfigs:
      if "ylim" in histConfig: 
        ylim = histConfig['ylim']
        break
    caption = ""
    captionleft1 = ""
    captionleft2 = ""
    captionleft3 = ""
    captionright1 = ""
    captionright2 = ""
    captionright3 = ""
    preliminaryString = ""
    for histConfig in histConfigs:
        if "caption" in histConfig \
                or "captionleft1" in histConfig \
                or "captionleft2" in histConfig \
                or "captionleft3" in histConfig \
                or "captionright1" in histConfig \
                or "captionright2" in histConfig \
                or "captionright3" in histConfig \
                or "preliminaryString" in histConfig:
            if "caption" in histConfig: caption = histConfig['caption']
            if "captionleft1" in histConfig: captionleft1 = histConfig['captionleft1']
            if "captionleft2" in histConfig: captionleft2 = histConfig['captionleft2']
            if "captionleft3" in histConfig: captionleft3 = histConfig['captionleft3']
            if "captionright1" in histConfig: captionright1 = histConfig['captionright1']
            if "captionright2" in histConfig: captionright2 = histConfig['captionright2']
            if "captionright3" in histConfig: captionright3 = histConfig['captionright3']
            if "preliminaryString" in histConfig: preliminaryString = histConfig['preliminaryString']

    hists = []
    for histConfig in histConfigs:
      binning = histConfig['binning']
      var = histConfig['var']
      cuts = histConfig['cuts']
      hist = Hist(*binning)
      hist.SetLineColor(histConfig['color'])
      varAndHist = var + " >> " + hist.GetName()
      tree.Draw(varAndHist,cuts)
      scaleFactor = 1.
      if "scaleFactor" in fileConfig: scaleFactor = fileConfig['scaleFactor']
      hist.Scale(scaleFactor)
      if "normToBinWidth" in histConfig and histConfig["normToBinWidth"]:
        normToBinWidth(hist)
      if "normalize" in histConfig and histConfig['normalize']:
        integral = hist.Integral()
        hist.Scale(1./integral)
      hists.append(hist)
    axisHist = makeStdAxisHist(hists,freeTopSpace=0.35,xlim=xlim,ylim=ylim)
    setHistTitles(axisHist,xtitle,ytitle)
    axisHist.Draw()
    for h in reversed(hists):
      h.Draw("histsame")
    labels = [histConfig['title'] for histConfig in histConfigs]
    leg = drawNormalLegend(hists,labels)
    drawStandardCaptions(canvas,caption,captionleft1=captionleft1,captionleft2=captionleft2,captionleft3=captionleft3,captionright1=captionright1,captionright2=captionright2,captionright3=captionright3,preliminaryString=preliminaryString)
    canvas.RedrawAxis()
    saveNameBase = fileConfig['name'] + "Hist"
    canvas.SaveAs(saveNameBase+".png")
    canvas.SaveAs(saveNameBase+".pdf")

def printAllPDGs(tree):
  pdgSecondariesSet = set()
  pdgTertiariesSet = set()
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

if __name__ == "__main__":

  binningArg = [325,0.,26.,200,0.,100.]
  evalFrac = 0.1
  fileConfigs = [
    {
      #'fn': "/scratch/jhugon/catalogue/anaTree_p_v10.root",
      'fn': "anaTree_p_v10.root",
      'pdg': 2212,
      'name': "p",
      'title': "p MC Sample",
      'caption': "p MC Sample",
      'color': root.kGreen+1,
    },
    {
      #'fn': "/scratch/jhugon/catalogue/anaTree_pip_v11.root",
      'fn': "anaTree_pip_v11.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+} MC Sample",
      'caption': "#pi^{+} MC Sample",
      'color': root.kBlack,
      'scaleFactor' : 0.5,
    },
    {
      #'fn': "/scratch/jhugon/catalogue/anaTree_mup_v10.root",
      'fn': "anaTree_mup_v10.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+} MC Sample",
      'caption': "#mu^{+} MC Sample",
      'color': root.kRed,
    },
    {
      #'fn': "/scratch/jhugon/catalogue/anaTree_kp_v10.root",
      'fn': "anaTree_kp_v10.root",
      'pdg': 321,
      'name': "kp",
      'title': "K^{+} MC Sample",
      'caption': "K^{+} MC Sample",
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
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"anatree/anatree")

  histConfigs = [
    {
      'name': "pip",
      'title': "#pi^{+}",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "Mother == 1 && pdg==211 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01",
      'color': root.kBlack,
    },
    {
      'name': "pi0",
      'title': "#pi^{0}",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "Mother == 1 && pdg==111 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01",
      'color': root.kCyan,
    },
    {
      'name': "p",
      'title': "p",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "Mother == 1 && pdg==2212 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01",
      'color': root.kGreen+1,
    },
    {
      'name': "gam",
      'title': "#gamma",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "Mother == 1 && pdg==22 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01",
      'color': root.kBlue,
    },
    {
      'name': "mup",
      'title': "#mu^{+}",
      'xtitle': "Secondary particle |p| [MeV/c]",
      'ytitle': "Particles per MeV/c",
      'normToBinWidth': True,
      'binning': [75,0,750],
      'var': "sqrt(Px*Px+Py*Py+Pz*Pz)*1000",
      'cuts': "Mother == 1 && pdg==-13 && sqrt(Px*Px+Py*Py+Pz*Pz)>0.01",
      'color': root.kRed,
    },
  ]

  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"anatree/anatree")

