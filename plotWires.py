#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import numpy
import matplotlib.pyplot as mpl
import matplotlib.patches as patches
import matplotlib.colors

def plotAllWholeWires(tree,fileprefix,maxEvents=100,cutFunc=lambda x: True):
  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if "wireData" == branchName[:8]:
        if branchName[-1] == "C":
            collectionWireBranchNames.append(branchName)
        else:
            inductionWireBranchNames.append(branchName)
        
  nEvents = min(maxEvents,tree.GetEntries())
  for iEvent in range(nEvents):
    tree.GetEntry(iEvent)
    if not cutFunc(tree):
        continue
    fig, (axc,axi) = mpl.subplots(nrows=2,figsize=(8.5,11),dpi=200)
    nSamples = 4096
    nWiresC = len(collectionWireBranchNames)
    nWiresI = len(inductionWireBranchNames)
    dataArrayC = numpy.zeros((nWiresC,nSamples))
    dataArrayI = numpy.zeros((nWiresI,nSamples))
    for iWire in range(nWiresC):
      wireData = getattr(tree,collectionWireBranchNames[iWire])
      for i in range(wireData.size()):
          dataArrayC[iWire,i] = wireData[i]
    for iWire in range(nWiresI):
      wireData = getattr(tree,inductionWireBranchNames[iWire])
      for i in range(wireData.size()):
          dataArrayI[iWire,i] = wireData[i]
    dataMaxC = dataArrayC.max()
    dataMinC = dataArrayC.min()
    dataWidthC = (dataMaxC - dataMinC)*0.75
    dataMaxI = dataArrayI.max()
    dataMinI = dataArrayI.min()
    dataWidthI = (dataMaxI - dataMinI)*0.75
    for iWire in range(nWiresC):
        axc.plot(dataArrayC[iWire]+dataWidthC*iWire,'-b',lw=0.2)
        hitStartsC = getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitStarts"))
        hitEndsC = getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitEnds"))
        axc.plot(hitStartsC,dataWidthC*iWire*numpy.ones(len(hitStartsC)),',g')
        axc.plot(hitEndsC,dataWidthC*iWire*numpy.ones(len(hitEndsC)),',r')
        #if hitStartsC.size() > 0:
        #  axc.plot(numpy.argmax(dataArrayC[iWire]),dataWidthC*iWire,',m')
    for iWire in range(nWiresI):
        axi.plot(dataArrayI[iWire]+dataWidthI*iWire,'-b',lw=0.2)
        hitStartsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitStarts"))
        hitEndsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitEnds"))
        axi.plot(hitStartsI,dataWidthI*iWire*numpy.ones(len(hitStartsI)),',g')
        axi.plot(hitEndsI,dataWidthI*iWire*numpy.ones(len(hitEndsI)),',r')
        #if hitStartsI.size() > 0:
        #  axi.plot(numpy.argmax(dataArrayI[iWire]),dataWidthI*iWire,',m')
    axc.set_xlim(0,4096)
    axc.set_ylim(dataMinC,dataMinC+dataWidthC*nWiresC)
    axi.set_xlim(0,4096)
    axi.set_ylim(dataMinI,dataMinI+dataWidthI*nWiresC)
    axi.set_xlabel("Time Tick")
    axc.set_ylabel("Collection Wire Response")
    axi.set_ylabel("Induction Wire Response")
    title = "Run {} Subrun {} Event {}".format(tree.runNumber,tree.subRunNumber,tree.eventNumber)
    isMCStr = ""
    if tree.isMC:
      title = "MC " + title
      isMCStr = "_MC"
    fig.suptitle(title)
    fig.savefig("{}{}_r{:04d}_sr{:03d}_e{:04d}.pdf".format(fileprefix,isMCStr,tree.runNumber,tree.subRunNumber,tree.eventNumber))
    mpl.close()

def plotAroundMaxWires(tree,fileprefix,maxEvents=100,normToAmp=False,cutFunc=lambda x: True):
  nBeforeC = 100
  nAfterC = 100
  nBeforeI = 100
  nAfterI = 100
  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if "wireData" == branchName[:8]:
        if branchName[-1] == "C":
            collectionWireBranchNames.append(branchName)
        else:
            inductionWireBranchNames.append(branchName)
        
  nEvents = min(maxEvents,tree.GetEntries())
  for iEvent in range(nEvents):
    tree.GetEntry(iEvent)
    if not cutFunc(tree):
        continue
    fig, (axc,axi) = mpl.subplots(nrows=2,figsize=(8.5,11),dpi=200)
    nSamples = 4096
    nWiresC = len(collectionWireBranchNames)
    nWiresI = len(inductionWireBranchNames)
    dataArrayC = numpy.zeros((nWiresC,nSamples))
    dataArrayI = numpy.zeros((nWiresI,nSamples))
    for iWire in range(nWiresC):
      wireData = getattr(tree,collectionWireBranchNames[iWire])
      for i in range(wireData.size()):
          dataArrayC[iWire,i] = wireData[i]
    for iWire in range(nWiresI):
      wireData = getattr(tree,inductionWireBranchNames[iWire])
      for i in range(wireData.size()):
          dataArrayI[iWire,i] = wireData[i]
    dataMaxC = dataArrayC.max()
    dataMinC = dataArrayC.min()
    dataWidthC = (dataMaxC - dataMinC)*0.75
    dataMaxI = dataArrayI.max()
    dataMinI = dataArrayI.min()
    dataWidthI = (dataMaxI - dataMinI)*0.75
    for iWire in range(nWiresC):
        amplitude = numpy.max(dataArrayC[iWire])
        rms = numpy.std(dataArrayC[iWire])
        if amplitude / rms < 8.:
            continue
        iMax = numpy.argmax(dataArrayC[iWire])
        iStart = max(iMax-nBeforeC,0)
        iEnd = min(iMax+nAfterC,nSamples)
        if normToAmp:
            data = dataArrayC[iWire,iStart:iEnd] / amplitude
        else:
            data = dataArrayC[iWire,iStart:iEnd]
        axc.plot(numpy.arange(nBeforeC+nAfterC)-nBeforeC,data,'-b',lw=0.2)
        hitStartsC = getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitStarts"))
        hitEndsC = getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitEnds"))
        for x in hitStartsC:
          axc.axvline(x-iStart-nBeforeC,ymax=0.05,c='g',lw=0.2)
        for x in hitEndsC:
          axc.axvline(x-iStart-nBeforeC,ymax=0.05,c='r',lw=0.2)
    for iWire in range(nWiresI):
        amplitude = numpy.max(dataArrayI[iWire])
        rms = numpy.std(dataArrayI[iWire])
        if amplitude / rms < 8.:
            continue
        iMax = numpy.argmax(dataArrayI[iWire])
        iStart = max(iMax-nBeforeI,0)
        iEnd = min(iMax+nAfterI,nSamples)
        if normToAmp:
            data = dataArrayI[iWire,iStart:iEnd] / amplitude
        else:
            data = dataArrayI[iWire,iStart:iEnd]
        axi.plot(numpy.arange(nBeforeI+nAfterI)-nBeforeI,data,'-b',lw=0.2)
        hitStartsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitStarts"))
        hitEndsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitEnds"))
        for x in hitStartsI:
          axi.axvline(x-iStart-nBeforeI,ymax=0.05,c='g',lw=0.2)
        for x in hitEndsI:
          axi.axvline(x-iStart-nBeforeI,ymax=0.05,c='r',lw=0.2)
    axc.set_xlim(-nBeforeC,nAfterC)
    #axc.set_ylim(dataMinC,dataMinC+dataWidthC*nWiresC)
    axi.set_xlim(-nBeforeI,nAfterI)
    #axi.set_ylim(dataMinI,dataMinI+dataWidthI*nWiresC)
    axi.set_xlabel("Time Tick - Time Tick of Max")
    yLabelSuffix = ""
    if normToAmp:
      yLabelSuffix = " (Normalized to Max)"
    axc.set_ylabel("Collection Wire Response"+yLabelSuffix)
    axi.set_ylabel("Induction Wire Response"+yLabelSuffix)
    title = "Run {} Subrun {} Event {}".format(tree.runNumber,tree.subRunNumber,tree.eventNumber)
    isMCStr = ""
    if tree.isMC:
      title = "MC " + title
      isMCStr = "_MC"
    fig.suptitle(title)
    fig.savefig("{}{}_r{:05d}_sr{:03d}_e{:04d}.pdf".format(fileprefix,isMCStr,tree.runNumber,tree.subRunNumber,tree.eventNumber))
    mpl.close()

def plotMultiEventAroundMaxWires(tree,fileprefix,maxEvents=100,normToAmp=False,cutFunc=lambda x: True,logz=False):
  nBeforeC = 100
  nAfterC = 100
  nBeforeI = 100
  nAfterI = 100

  nBinsC = 400
  yMinC = -20
  yMaxC = 300

  nBinsI = 400
  yMinI = -50
  yMaxI = 200

  if normToAmp:
    yMinC = -0.1
    yMinI = -0.4
    yMaxC = 1.1
    yMaxI = 1.1

  arangeC = numpy.arange(nBeforeC+nAfterC,dtype="float64") - nBeforeC
  arangeI = numpy.arange(nBeforeI+nAfterI,dtype="float64") - nBeforeI

  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if "wireData" == branchName[:8]:
        if branchName[-1] == "C":
            collectionWireBranchNames.append(branchName)
        else:
            inductionWireBranchNames.append(branchName)

  nEvents = min(maxEvents,tree.GetEntries())
  #allHistC = Hist2D(nBeforeC+nAfterC,-nBeforeC,nAfterC,50,-20,400)
  allHistC = None
  xEdgesC = None
  yEdgesC = None
  allHistI = None
  xEdgesI = None
  yEdgesI = None
  hitStartsC = []
  hitEndsC = []
  hitStartsI = []
  hitEndsI = []
  isMCStr = ""
  for iEvent in range(nEvents):
    tree.GetEntry(iEvent)
    if not cutFunc(tree):
        continue
    if tree.isMC:
        isMCStr = "_MC"
    nSamples = 4096
    nWiresC = len(collectionWireBranchNames)
    nWiresI = len(inductionWireBranchNames)
    for iWire in range(nWiresC):
      wireData = getattr(tree,collectionWireBranchNames[iWire])
      dataArray = numpy.zeros((nSamples))
      for i in range(wireData.size()):
        dataArray[i] = wireData[i]
      amplitude = numpy.max(dataArray)
      rms = numpy.std(dataArray)
      if amplitude / rms < 8.:
          continue
      iMax = numpy.argmax(dataArray)
      iStart = max(iMax-nBeforeC,0)
      iEnd = min(iMax+nAfterC,nSamples)
      if normToAmp:
          data = dataArray[iStart:iEnd] / amplitude
      else:
          data = dataArray[iStart:iEnd]
      hist, xedgesC, yedgesC = numpy.histogram2d(arangeC,data,bins=[nBeforeC+nAfterC,nBinsC],range=[[-nBeforeC,nAfterC],[yMinC,yMaxC]])
      if allHistC is None:
          allHistC = hist
      else:
          allHistC += hist
      hitStartsC.extend(numpy.array(getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitStarts")))-iStart-nBeforeC)
      hitEndsC.extend(numpy.array(getattr(tree,collectionWireBranchNames[iWire].replace("wireData","wireHitEnds")))-iStart-nBeforeC)
    for iWire in range(nWiresI):
      wireData = getattr(tree,inductionWireBranchNames[iWire])
      dataArray = numpy.zeros((nSamples))
      for i in range(wireData.size()):
        dataArray[i] = wireData[i]
      amplitude = numpy.max(dataArray)
      rms = numpy.std(dataArray)
      if amplitude / rms < 8.:
          continue
      iMax = numpy.argmax(dataArray)
      iStart = max(iMax-nBeforeI,0)
      iEnd = min(iMax+nAfterI,nSamples)
      if normToAmp:
          data = dataArray[iStart:iEnd] / amplitude
      else:
          data = dataArray[iStart:iEnd]
      hist, xedgesI, yedgesI = numpy.histogram2d(arangeI,data,bins=[nBeforeI+nAfterI,nBinsI],range=[[-nBeforeI,nAfterI],[yMinI,yMaxI]])
      if allHistI is None:
          allHistI = hist
      else:
          allHistI += hist
      hitStartsI.extend(numpy.array(getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitStarts"))) -iStart-nBeforeI)
      hitEndsI.extend(numpy.array(getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitEnds"))) -iStart-nBeforeI)
  allHistC[allHistC == 0.] = 0.5
  allHistI[allHistI == 0.] = 0.5
  fig, (axc,axi) = mpl.subplots(nrows=2,figsize=(8.5,11),dpi=200)
  xC, yC = numpy.meshgrid(xedgesC, yedgesC)
  norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=max(allHistI.max(),allHistC.max()))
  axc.pcolormesh(xC,yC,allHistC.T,norm=norm,cmap="Blues_r")
  xI, yI = numpy.meshgrid(xedgesI, yedgesI)
  normI = matplotlib.colors.LogNorm(vmin=allHistI.min(), vmax=allHistI.max())
  pcolormeshi = axi.pcolormesh(xI,yI,allHistI.T,norm=norm,cmap="Blues_r")
  axc.set_xlim(-nBeforeC,nAfterC)
  axc.set_ylim(yMinC,yMaxC)
  axi.set_xlim(-nBeforeI,nAfterI)
  axi.set_ylim(yMinI,yMaxI)
  axi.set_xlabel("Time Tick - Time Tick of Max")
  yLabelSuffix = ""
  if normToAmp:
    yLabelSuffix = " (Normalized to Max)"
  axc.set_ylabel("Collection Wire Response"+yLabelSuffix)
  axi.set_ylabel("Induction Wire Response"+yLabelSuffix)
  #axc.hist(hitStartsC,range=[-nBeforeC,nAfterC],bins=100,normed=True,histtype="step",color="g")
  #axc.hist(hitEndsC,range=[-nBeforeC,nAfterC],bins=100,normed=True,histtype="step",color="r")
  #axi.hist(hitStartsI,range=[-nBeforeI,nAfterI],bins=100,normed=True,histtype="step",color="g")
  #axi.hist(hitEndsI,range=[-nBeforeI,nAfterI],bins=100,normed=True,histtype="step",color="r")
  #for x in hitStartsC:
  #  axc.axvline(x,ymax=0.05,c='g',lw=0.2)
  #for x in hitEndsC:
  #  axc.axvline(x,ymax=0.05,c='r',lw=0.2)
  #for x in hitStartsI:
  #  axi.axvline(x,ymax=0.05,c='g',lw=0.2)
  #for x in hitEndsI:
  #  axi.axvline(x,ymax=0.05,c='r',lw=0.2)
  title = "Data"
  if len(isMCStr) > 0:
    title = "MC"
  fig.suptitle(title)
  #fig.colorbar(pcolormeshi,ax=[axc,axi])
  fig.savefig("{}{}.png".format(fileprefix,isMCStr))
  mpl.close()

if __name__ == "__main__":

  f = root.TFile("CosmicsWires.root")
  #f.ls()
  tree = f.Get("cosmicanalyzer/tree")
  #tree.Print()

  def makeCuts(tree,phiGeq0=False,phiLt0=False):
    pi = math.pi
    result = True
    if tree.nTracks != 1:
        return False
    if tree.iBestMatch < 0:
        return False
    if phiGeq0 and not tree.primTrkStartPhi >= 0.:
        return False
    if phiLt0 and not tree.primTrkStartPhi < 0.:
        return False
    if not (tree.isMC or ((tree.triggerBits >> 10) & 1)):
        return False
    if not ((not tree.isMC) or (tree.trueHitCosmic1 and tree.trueHitCosmic2) or (tree.trueHitCosmic3 and tree.trueHitCosmic4)):
        return False
    if not ((tree.primTrkStartTheta > 27*pi/180.) and (tree.primTrkStartTheta < 42*pi/180.) and (tree.primTrkStartPhi > -57*pi/180. and tree.primTrkStartPhi < 60*pi/180.) and (tree.primTrkStartPhi < -15*pi/180. or tree.primTrkStartPhi > 22*pi/180.)):
        return False
    return True

  #plotAllWholeWires(tree,"all",10,cutFunc=makeCuts)
  #plotAroundMaxWires(tree,"allMax",10,cutFunc=makeCuts)
  plotAllWholeWires(tree,"phiLt0",20,cutFunc=lambda x: makeCuts(x,phiLt0=True))
  plotAroundMaxWires(tree,"phiLt0Max",20,cutFunc=lambda x: makeCuts(x,phiLt0=True))
  plotAroundMaxWires(tree,"phiLt0MaxNorm",20,cutFunc=lambda x: makeCuts(x,phiLt0=True),normToAmp=True)
  plotAllWholeWires(tree,"phiGeq0",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
  plotAroundMaxWires(tree,"phiGeq0Max",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
  plotAroundMaxWires(tree,"phiGeq0MaxNorm",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True),normToAmp=True)

  plotMultiEventAroundMaxWires(tree,"phiLt0Hist",20,cutFunc=lambda x: makeCuts(x,phiLt0=True))
  plotMultiEventAroundMaxWires(tree,"phiGeq0Hist",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
  plotMultiEventAroundMaxWires(tree,"phiLt0HistNorm",20,cutFunc=lambda x: makeCuts(x,phiLt0=True),normToAmp=True)
  plotMultiEventAroundMaxWires(tree,"phiGeq0HistNorm",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True),normToAmp=True)

