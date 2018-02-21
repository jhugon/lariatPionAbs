#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import numpy
import matplotlib.pyplot as mpl
import matplotlib.patches as patches

def plotAllWholeWires(tree,fileprefix,maxEvents=100):
  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if "wireData" == branchName[:8]:
        if branchName[-1] == "C":
            collectionWireBranchNames.append(branchName)
        else:
            inductionWireBranchNames.append(branchName)
        
  for iEvent in range(tree.GetEntries()):
    if iEvent > 2: break
    tree.GetEntry(iEvent)

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
        axc.plot(hitStartsC,dataWidthC*iWire*numpy.ones(len(hitStartsC))+dataWidthC,',g')
        axc.plot(hitEndsC,dataWidthC*iWire*numpy.ones(len(hitEndsC))+dataWidthC,',r')
    for iWire in range(nWiresI):
        axi.plot(dataArrayI[iWire]+dataWidthI*iWire,'-b',lw=0.2)
        hitStartsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitStarts"))
        hitEndsI = getattr(tree,inductionWireBranchNames[iWire].replace("wireData","wireHitEnds"))
        axi.plot(hitStartsI,dataWidthI*iWire*numpy.ones(len(hitStartsI)),',g')
        axi.plot(hitEndsI,dataWidthI*iWire*numpy.ones(len(hitEndsI)),',r')
    axc.set_xlim(0,4096)
    axc.set_ylim(dataMinC,dataMinC+dataWidthC*nWiresC)
    axi.set_xlim(0,4096)
    axi.set_ylim(dataMinI,dataMinI+dataWidthI*nWiresC)
    axi.set_xlabel("Time tick")
    axc.set_ylabel("Collection Wire Response")
    axi.set_ylabel("Induction Wire Response")
    fig.savefig("{}_event{}.pdf".format(fileprefix,iEvent))

if __name__ == "__main__":

  f = root.TFile("CosmicsWires.root")
  #f.ls()
  tree = f.Get("cosmicanalyzer/tree")
  #tree.Print()
  plotAllWholeWires(tree,"test",5)

