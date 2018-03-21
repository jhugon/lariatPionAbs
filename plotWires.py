#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
import numpy
import matplotlib.pyplot as mpl
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.colors
import matplotlib.gridspec as gridspec

def getHitName(wireName,start=True):
  firstPart = wireName.split("_")[0]
  if start:
    return wireName.replace(firstPart,"wireHitStarts")
  else:
    return wireName.replace(firstPart,"wireHitEnds")

def getBranchNames(tree,branchPrefix,branchSuffix):
  branchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if branchPrefix == branchName[:len(branchPrefix)] and branchSuffix == branchName[-1*len(branchSuffix):]:
        branchNames.append(branchName)
  return branchNames

def makeWireHists(tree,maxEvents,cutFunc,nBefore=150,nAfter=150,yMin=-400,yMax=400,nBins=800):
  nSamples = 4096
  dataArray = numpy.zeros(nSamples)
  rawDataArray = numpy.zeros(nSamples)
  arange = numpy.arange(nBefore+nAfter,dtype="float64") - nBefore
  xedges = None
  yedges = None
  yedgesNorm = None
  yedgesRaw = None
  yedgesNormRaw = None
  rawHists = []
  deconvHists = []
  rawAtDeconvHists = []
  rawHistNorms = []
  deconvHistNorms = []
  rawAtDeconvHistNorms = []
  allHitStarts = []
  allHitStartsRaw = []
  allHitEnds = []
  allHitEndsRaw = []
  for suffix in ["C","I"]:
    wireBranchNames = getBranchNames(tree,"wireData",suffix)
    rawWireBranchNames = getBranchNames(tree,"rawWireData",suffix)
    assert(len(wireBranchNames)==len(rawWireBranchNames))
    nEvents = min(tree.GetEntries(),maxEvents)
    rawHist = None
    deconvHist = None
    rawAtDeconvHist = None
    rawHistNorm = None
    deconvHistNorm = None
    rawAtDeconvHistNorm = None
    hitStarts = []
    hitStartsRaw = []
    hitEnds = []
    hitEndsRaw = []
    for iEvent in range(nEvents):
      tree.GetEntry(iEvent)
      if not cutFunc(tree):
          continue
      for iWire in range(len(wireBranchNames)):
        dataArray[:] = 0
        rawDataArray[:] = 0
        wireData = getattr(tree,wireBranchNames[iWire])
        rawWireData = getattr(tree,rawWireBranchNames[iWire])
        for i in range(wireData.size()):
          dataArray[i] = wireData[i]
        for i in range(rawWireData.size()):
          rawDataArray[i] = rawWireData[i]
        signif = numpy.max(dataArray) / numpy.std(dataArray)
        signifRaw = numpy.max(rawDataArray) / numpy.std(rawDataArray)
        if signifRaw > 8.:
          iMax = numpy.argmax(rawDataArray)
          if iMax > nBefore and iMax < (nSamples - nAfter):
            iStart = max(iMax-nBefore,0)
            iEnd = min(iMax+nAfter,nSamples)
            data = rawDataArray[iStart:iEnd]
            hist, xedges, yedgesRaw = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,int(yMax-yMin)],range=[[-nBefore,nAfter],[yMin,yMax]])
            data /= numpy.max(data)
            histNorm, xedges, yedgesNormRaw = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,int(yMax-yMin)],range=[[-nBefore,nAfter],[-2.,2.]])
            if rawHist is None:
                rawHist = hist
                rawHistNorm = histNorm
            else:
                rawHist += hist
                rawHistNorm += histNorm
            hitStartsRaw.extend(numpy.array(getattr(tree,getHitName(rawWireBranchNames[iWire],start=True)))-iStart-nBefore)
            hitEndsRaw.extend(numpy.array(getattr(tree,getHitName(rawWireBranchNames[iWire],start=False)))-iStart-nBefore)
        if signif > 8.:
          iMax = numpy.argmax(dataArray)
          if iMax > nBefore and iMax < (nSamples - nAfter):
            iStart = max(iMax-nBefore,0)
            iEnd = min(iMax+nAfter,nSamples)
            data = dataArray[iStart:iEnd]
            rawData = rawDataArray[iStart:iEnd]
            hist, xedges, yedges = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            histRaw, xedges, yedges = numpy.histogram2d(arange,rawData,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            data /= numpy.max(data)
            rawData /= numpy.max(rawData)
            histNorm, xedges, yedgesNorm = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[-2.,2.]])
            histRawNorm, xedges, yedgesNorm = numpy.histogram2d(arange,rawData,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[-2.,2.]])
            if deconvHist is None:
                deconvHist = hist
                rawAtDeconvHist = histRaw
                deconvHistNorm = histNorm
                rawAtDeconvHistNorm = histRawNorm
            else:
                deconvHist += hist
                rawAtDeconvHist += histRaw
                deconvHistNorm += histNorm
                rawAtDeconvHistNorm += histRawNorm
            hitStarts.extend(numpy.array(getattr(tree,getHitName(wireBranchNames[iWire],start=True)))-iStart-nBefore)
            hitEnds.extend(numpy.array(getattr(tree,getHitName(wireBranchNames[iWire],start=False)))-iStart-nBefore)
    hitStarts = numpy.array(hitStarts)
    hitEnds = numpy.array(hitEnds)
    hitStartsRaw = numpy.array(hitStartsRaw)
    hitEndsRaw = numpy.array(hitEndsRaw)

    rawHists.append(rawHist)
    deconvHists.append(deconvHist)
    rawAtDeconvHists.append(rawAtDeconvHist)
    rawHistNorms.append(rawHistNorm)
    deconvHistNorms.append(deconvHistNorm)
    rawAtDeconvHistNorms.append(rawAtDeconvHistNorm)
    allHitStarts.append(hitStarts)
    allHitStartsRaw.append(hitStartsRaw)
    allHitEnds.append(hitEnds)
    allHitEndsRaw.append(hitEndsRaw)
  return rawHists, rawHistNorms, deconvHists, deconvHistNorms, rawAtDeconvHists, rawAtDeconvHistNorms, xedges, yedges, yedgesNorm, yedgesRaw, yedgesNormRaw, allHitStarts, allHitEnds, allHitStartsRaw, allHitEndsRaw

def justPlot(hist,hitStarts,hitEnds,xedges,yedges,fn,xMin,xMax,yMin,yMax,xLabel,yLabel,title):
  gs = {'height_ratios':[4,1],'hspace':0}
  fig, (ax1,ax2) = mpl.subplots(nrows=2,sharex=True,gridspec_kw=gs)
  if hist is None:
    print "Error: hist is None, no events passed amplitude cut for: ",fn
  else:
    histToPlot = numpy.array(hist)
    histToPlot[histToPlot == 0.] = 0.5
    x, y = numpy.meshgrid(xedges, yedges)
    norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=histToPlot.max())
    p = ax1.pcolormesh(x,y,histToPlot.T,norm=norm,cmap="Blues_r")
  ax2.hist(hitStarts,range=[xMin,xMax],bins=100,normed=True,histtype="step",color="b")
  ax2.hist(hitEnds,range=[xMin,xMax],bins=100,normed=True,histtype="step",color="b",ls=':')
  ax1.set_xlim(xMin,xMax)
  ax1.set_ylim(yMin,yMax)
  yLabelSuffix = ""
  ax1.set_ylabel(yLabel)
  ax2.set_xlabel(xLabel)
  ax2.set_ylabel("Hits / Bin")
  ax2.set_yticks([])
  ax2.set_ylim(0,ax2.get_ylim()[1]*1.5)
  ##
  line1 = lines.Line2D([],[],color='k',label="Hit Start")
  line2 = lines.Line2D([],[],color='k',ls=":",label="Hit End")
  ax2.legend(handles=[line1,line2],ncol=2,fontsize='small')
  ax1.set_title(title)

  fig.savefig(fn)
  mpl.close()

def plotWireHists(*args,**kargs):

  if len(args) != 15:
    print "plotWireHists n args isn't 15 as expected is ", len(args)
    sys.exit(1)
  rawHists = args[0]
  rawHistNorms = args[1]
  deconvHists = args[2]
  deconvHistNorms = args[3]
  rawAtDeconvHists = args[4]
  rawAtDeconvHistNorms = args[5]
  xedges = args[6]
  yedges = args[7]
  yedgesNorm = args[8]
  yedgesRaw = args[9]
  yedgesNormRaw = args[10]
  allHitStarts = args[11]
  allHitEnds = args[12]
  allHitStartsRaw = args[13]
  allHitEndsRaw = args[14]

  filePrefix=""
  fileSuffixes=["C","I"]
  xMins=[-70,-50]
  xMaxs=[70,100]
  yMins=[-50,-150]
  yMaxs=[300,150]
  yLabels=["Collection Wire Response","Induction Wire Response"]
  xLabel="Time Tick - Time Tick of Max"
  title=""

  try:
    filePrefix = kargs["filePrefix"]
  except KeyError:
    raise Exception("plotWireHists: filePrefix=<prefix> argument required")
  try:
    fileSuffixes = kargs["fileSuffixes"]
  except:
    pass
  try:
    title = kargs["title"]
  except:
    pass
  try:
    xMins = kargs["xMins"]
  except:
    pass
  try:
    yMins = kargs["yMins"]
  except:
    pass
  try:
    xMins = kargs["xMaxs"]
  except:
    pass
  try:
    yMaxs = kargs["yMaxs"]
  except:
    pass

  if len(fileSuffixes) != len(rawHists):
    raise ValueError("fileSuffixes length should be: ", len(rawHists), " is ", len(fileSuffixes))
  if len(xMins) != len(rawHists):
    raise ValueError("xMins length should be: ", len(rawHists), " is ", len(xMins))
  if len(yMins) != len(rawHists):
    raise ValueError("yMins length should be: ", len(rawHists), " is ", len(yMins))
  if len(xMaxs) != len(rawHists):
    raise ValueError("xMaxs length should be: ", len(rawHists), " is ", len(xMaxs))
  if len(yMaxs) != len(rawHists):
    raise ValueError("yMaxs length should be: ", len(rawHists), " is ", len(yMaxs))
  if len(yLabels) != len(rawHists):
    raise ValueError("yLabels length should be: ", len(rawHists), " is ", len(yLabels))

  for rawHist, rawHistNorm, deconvHist, deconvHistNorm, rawAtDeconvHist, rawAtDeconvHistNorm, hitStarts, hitEnds, hitStartsRaw, hitEndsRaw, fileSuffix, xMin, xMax, yMin, yMax, yLabel in zip(
            rawHists, rawHistNorms, deconvHists, deconvHistNorms, rawAtDeconvHists, rawAtDeconvHistNorms,
            allHitStarts, allHitEnds, allHitStartsRaw, allHitEndsRaw,
            fileSuffixes, xMins, xMaxs, yMins, yMaxs, yLabels
        ):
    
    justPlot(rawHist,hitStartsRaw,hitEndsRaw,xedges,yedgesRaw,"{}_raw_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    justPlot(rawHistNorm,hitStartsRaw,hitEndsRaw,xedges,yedgesNormRaw,"{}_raw_norm_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-2,2,xLabel,yLabel+" Normalized to Max",title)
    justPlot(deconvHist,hitStarts,hitEnds,xedges,yedges,"{}_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    justPlot(deconvHistNorm,hitStarts,hitEnds,xedges,yedgesNorm,"{}_deconv_norm_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-2,2,xLabel,yLabel+" Normalized to Max",title)
    justPlot(rawAtDeconvHist,hitStarts,hitEnds,xedges,yedges,"{}_raw_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    justPlot(rawAtDeconvHistNorm,hitStarts,hitEnds,xedges,yedgesNorm,"{}_raw_norm_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-2,2,xLabel,yLabel+" Normalized to Max",title)

def plotAllWholeWires(tree,fileprefix,maxEvents=100,cutFunc=lambda x: True,branchNamePrefix="wireData",getHits=True):
  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if branchNamePrefix == branchName[:len(branchNamePrefix)]:
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
    zScoreC = []
    zScoreI = []
    for iWire in range(nWiresC):
        axc.plot(dataArrayC[iWire]+dataWidthC*iWire,'-b',lw=0.2)
        if getHits:
          hitStartsC = getattr(tree,getHitName(collectionWireBranchNames[iWire],start=True))
          hitEndsC = getattr(tree,getHitName(collectionWireBranchNames[iWire],start=False))
          axc.plot(hitStartsC,dataWidthC*iWire*numpy.ones(len(hitStartsC)),',g')
          axc.plot(hitEndsC,dataWidthC*iWire*numpy.ones(len(hitEndsC)),',r')
        amp = numpy.max(dataArrayC[iWire])
        rms = numpy.std(dataArrayC[iWire])
        zScoreC.append(amp/rms)
    for iWire in range(nWiresI):
        axi.plot(dataArrayI[iWire]+dataWidthI*iWire,'-b',lw=0.2)
        if getHits:
          hitStartsI = getattr(tree,getHitName(inductionWireBranchNames[iWire],start=True))
          hitEndsI = getattr(tree,getHitName(inductionWireBranchNames[iWire],start=False))
          axi.plot(hitStartsI,dataWidthI*iWire*numpy.ones(len(hitStartsI)),',g')
          axi.plot(hitEndsI,dataWidthI*iWire*numpy.ones(len(hitEndsI)),',r')
        amp = numpy.max(dataArrayI[iWire])
        rms = numpy.std(dataArrayI[iWire])
        zScoreI.append(amp/rms)
    axc.set_xlim(0,4096)
    axc.set_ylim(dataMinC,dataMinC+dataWidthC*nWiresC)
    axi.set_xlim(0,4096)
    axi.set_ylim(dataMinI,dataMinI+dataWidthI*nWiresC)
    axi.set_xlabel("Time Tick")
    axc.set_ylabel("Collection Wire Response")
    axi.set_ylabel("Induction Wire Response")
    title = "Run {} Subrun {} Event {}\n $\phi$: {:.1f}$^\circ$, Track Length: {:.1f} cm".format(tree.runNumber,tree.subRunNumber,tree.eventNumber,tree.primTrkStartPhi*180/math.pi,tree.primTrkLength)
    isMCStr = ""
    if tree.isMC:
      title = "MC " + title
      isMCStr = "_MC"
    fig.suptitle(title)
    fig.savefig("{}{}_r{:04d}_sr{:03d}_e{:04d}.pdf".format(fileprefix,isMCStr,tree.runNumber,tree.subRunNumber,tree.eventNumber))
    axc.cla()
    axi.cla()
    axc.hist(zScoreC,bins=20)
    axi.hist(zScoreI,bins=20)
    axi.set_xlabel("Max amplitude / RMS")
    axc.set_ylabel("N Collection Wires / bin")
    axi.set_ylabel("N Induction Wires / bin")
    fig.savefig("ZScore_{}{}_r{:04d}_sr{:03d}_e{:04d}.pdf".format(fileprefix,isMCStr,tree.runNumber,tree.subRunNumber,tree.eventNumber))
    mpl.close()

def plotAroundMaxWires(tree,fileprefix,maxEvents=100,normToAmp=False,cutFunc=lambda x: True,branchNamePrefix="wireData"):
  nBeforeC = 100
  nAfterC = 100
  nBeforeI = 100
  nAfterI = 100
  collectionWireBranchNames = []
  inductionWireBranchNames = []
  for branch in tree.GetListOfBranches():
    branchName = branch.GetName()
    if branchNamePrefix == branchName[:len(branchNamePrefix)]:
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
        axc.plot(numpy.arange(iStart,iEnd)-iMax,data,'-b',lw=0.2)
        hitStartsC = getattr(tree,getHitName(collectionWireBranchNames[iWire],start=True))
        hitEndsC = getattr(tree,getHitName(collectionWireBranchNames[iWire],start=False))
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
        axi.plot(numpy.arange(iStart,iEnd)-iMax,data,'-b',lw=0.2)
        hitStartsI = getattr(tree,getHitName(inductionWireBranchNames[iWire],start=True))
        hitEndsI = getattr(tree,getHitName(inductionWireBranchNames[iWire],start=False))
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
    title = "Run {} Subrun {} Event {}\n $\phi$: {:.1f}$^\circ$, Track Length: {:.1f} cm".format(tree.runNumber,tree.subRunNumber,tree.eventNumber,tree.primTrkStartPhi*180/math.pi,tree.primTrkLength)
    isMCStr = ""
    if tree.isMC:
      title = "MC " + title
      isMCStr = "_MC"
    fig.suptitle(title)
    fig.savefig("{}{}_r{:05d}_sr{:03d}_e{:04d}.pdf".format(fileprefix,isMCStr,tree.runNumber,tree.subRunNumber,tree.eventNumber))
    mpl.close()

def compareMultiEventAroundMaxWires(trees,fileprefix,maxEvents=100,normToAmp=False,
                                    cutFuncs=[lambda x: True,lambda x: True],
                                    branchNamePrefixes=["wireData","wireData"],
                                    labels=["1","2"],
                                    logz=False
                                    ):
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
    yMinC = -0.4
    yMinI = -0.4
    yMaxC = 1.1
    yMaxI = 1.1

  arangeC = numpy.arange(nBeforeC+nAfterC,dtype="float64") - nBeforeC
  arangeI = numpy.arange(nBeforeI+nAfterI,dtype="float64") - nBeforeI
  xEdgesC = None
  yEdgesC = None
  xEdgesI = None
  yEdgesI = None

  histsC = []
  histsI = []
  hitStartsCList = []
  hitStartsIList = []
  hitEndsCList = []
  hitEndsIList = []
  for tree, cutFunc, branchNamePrefix in zip(trees,cutFuncs,branchNamePrefixes):
    collectionWireBranchNames = []
    inductionWireBranchNames = []
    for branch in tree.GetListOfBranches():
      branchName = branch.GetName()
      if branchNamePrefix == branchName[:len(branchNamePrefix)]:
          if branchName[-1] == "C":
              collectionWireBranchNames.append(branchName)
          else:
              inductionWireBranchNames.append(branchName)

    nEvents = min(maxEvents,tree.GetEntries())
    #allHistC = Hist2D(nBeforeC+nAfterC,-nBeforeC,nAfterC,50,-20,400)
    allHistC = None
    allHistI = None
    hitStartsC = []
    hitEndsC = []
    hitStartsI = []
    hitEndsI = []
    for iEvent in range(nEvents):
      tree.GetEntry(iEvent)
      if not cutFunc(tree):
          continue
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
        if iMax < nBeforeC:
            continue
        if iMax > (nSamples-nAfterC):
            continue
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
        hitStartsC.extend(numpy.array(getattr(tree,getHitName(collectionWireBranchNames[iWire],start=True)))-iStart-nBeforeC)
        hitEndsC.extend(numpy.array(getattr(tree,getHitName(collectionWireBranchNames[iWire],start=False)))-iStart-nBeforeC)
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
        if iMax < nBeforeI:
            continue
        if iMax > (nSamples-nAfterI):
            continue
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
        hitStartsI.extend(numpy.array(getattr(tree,getHitName(inductionWireBranchNames[iWire],start=True)))-iStart-nBeforeI)
        hitEndsI.extend(numpy.array(getattr(tree,getHitName(inductionWireBranchNames[iWire],start=False)))-iStart-nBeforeI)
    histsC.append(allHistC)
    histsI.append(allHistI)
    hitStartsCList.append(hitStartsC)
    hitStartsIList.append(hitStartsI)
    hitEndsCList.append(hitEndsC)
    hitEndsIList.append(hitEndsI)

  transparent_cmaps = []
  for cmap in [mpl.cm.Greens,mpl.cm.Blues,mpl.cm.Reds,mpl.cm.Purples,mpl.cm.Oranges]:
    frac_transparent = 0.5
    cmap_colors = cmap(numpy.arange(cmap.N))
    cmap_colors[:int(frac_transparent*cmap.N),-1] = numpy.linspace(0,1,int(frac_transparent*cmap.N)) # bottom frac linearly increases opacity
    transparent_cmap = matplotlib.colors.ListedColormap(cmap_colors)
    transparent_cmaps.append(transparent_cmap)
  colors = ['g','b','r','purple','o']

  gs = {'height_ratios':[5,1],'hspace':0}

  fig, (ax,ax2) = mpl.subplots(nrows=2,figsize=(8.5,8.5),sharex=True,gridspec_kw=gs,dpi=200)
  for i, allHistC in enumerate(histsC):
    if allHistC is None:
      print "Error: allHistC is None, no events passed amplitude cut for fileprefix: ",fileprefix
    else:
      xC, yC = numpy.meshgrid(xedgesC, yedgesC)
      norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=allHistC.max())
      ax.pcolormesh(xC,yC,allHistC.T,norm=norm,cmap=transparent_cmaps[i])
    ax2.hist(hitStartsCList[i],range=[-nBeforeC,nAfterC],bins=100,normed=True,histtype="step",color=colors[i])
    ax2.hist(hitEndsCList[i],range=[-nBeforeC,nAfterC],bins=100,normed=True,histtype="step",color=colors[i],ls=':')
  ax.set_xlim(-nBeforeC,nAfterC)
  ax.set_ylim(yMinC,yMaxC)
  yLabelSuffix = ""
  if normToAmp:
    yLabelSuffix = " (Normalized to Max)"
  ax.set_ylabel("Collection Wire Response"+yLabelSuffix)
  ax2.set_xlabel("Time Tick - Time Tick of Max")
  ax2.set_ylabel("Normalized\nHits / Bin")
  ax2.set_yticks([])
  ax2.set_ylim(0,ax2.get_ylim()[1]*1.1)
  patchList = []
  for i in range(len(histsC)):
    patchList.append(
        patches.Patch(color=colors[i], label=labels[i])
        )
  ax.legend(handles=patchList)
  line1 = lines.Line2D([],[],color='k',label="Hit Start")
  line2 = lines.Line2D([],[],color='k',ls=":",label="Hit End")
  ax2.legend(handles=[line1,line2])
  fig.savefig("{}_Collection.png".format(fileprefix))
  mpl.close()

  ###

  fig, (ax,ax2) = mpl.subplots(nrows=2,figsize=(8.5,8.5),sharex=True,gridspec_kw=gs,dpi=200)
  for i, allHistI in enumerate(histsI):
    if allHistI is None:
      print "Error: allHistI is None, no events passed amplitude cut for fileprefix: ",fileprefix
    else:
      xI, yI = numpy.meshgrid(xedgesI, yedgesI)
      norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=allHistI.max())
      ax.pcolormesh(xI,yI,allHistI.T,norm=norm,cmap=transparent_cmaps[i])
    ax2.hist(hitStartsIList[i],range=[-nBeforeI,nAfterI],bins=100,normed=True,histtype="step",color=colors[i])
    ax2.hist(hitEndsIList[i],range=[-nBeforeI,nAfterI],bins=100,normed=True,histtype="step",color=colors[i],ls=':')
  ax.set_xlim(-nBeforeI,nAfterI)
  ax.set_ylim(yMinI,yMaxI)
  yLabelSuffix = ""
  if normToAmp:
    yLabelSuffix = " (Normalized to Max)"
  ax.set_ylabel("Induction Wire Response"+yLabelSuffix)
  ax2.set_xlabel("Time Tick - Time Tick of Max")
  ax2.set_ylabel("Normalized\nHits / Bin")
  ax2.set_yticks([])
  ax2.set_ylim(0,ax2.get_ylim()[1]*1.1)
  patchList = []
  for i in range(len(histsI)):
    patchList.append(
        patches.Patch(color=colors[i], label=labels[i])
        )
  ax.legend(handles=patchList)
  line1 = lines.Line2D([],[],color='k',label="Hit Start")
  line2 = lines.Line2D([],[],color='k',ls=":",label="Hit End")
  ax2.legend(handles=[line1,line2])
  fig.savefig("{}_Induction.png".format(fileprefix))
  mpl.close()

if __name__ == "__main__":

  import matplotlib
  import cPickle

  #f = root.TFile("WireData_RIIP100_64a.root")
  #f = root.TFile("WireData_RIIP100_64a_nocrct.root")
  #f = root.TFile("WireData_RIIP60_64a.root")
  f = root.TFile("Wires_RIIP60a_v3.root")
  #fMC = root.TFile("WiresMC_v3.root")
  #f.ls()
  tree = f.Get("cosmicanalyzer/tree")
  #treeMC = fMC.Get("cosmicanalyzer/tree")
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

  nMax = 10
  dataAllHists = None
  try:
    with open("dataAllHists.pkl") as infile:
      dataAllHists = cPickle.load(infile)
  except IOError:
    dataAllHists = makeWireHists(tree,nMax,makeCuts)
    with open("dataAllHists.pkl",'wb') as outfile:
      cPickle.dump(dataAllHists,outfile)
  plotWireHists(*dataAllHists,filePrefix="TestPlot")
  sys.exit(0)
#  dataPhiGeq0Hists = makeWireHists(tree,nMax,lambda x: makeCuts(x,phiGeq0=True))
#  dataPhiLt0Hists = makeWireHists(tree,nMax,lambda x: makeCuts(x,phiLt0=True))
#  mcAllHists = makeWireHists(treeMC,nMax,makeCuts)
#  mcPhiGeq0Hists = makeWireHists(treeMC,nMax,lambda x: makeCuts(x,phiGeq0=True))
#  mcPhiLt0Hists = makeWireHists(treeMC,nMax,lambda x: makeCuts(x,phiLt0=True))

#  plotAllWholeWires(tree,"all",100,cutFunc=makeCuts)
#  plotAllWholeWires(tree,"rawAll",100,cutFunc=makeCuts,branchNamePrefix="rawWireData")
#  plotAroundMaxWires(tree,"allMax",100,cutFunc=makeCuts)
#  plotAroundMaxWires(tree,"rawAllMax",100,cutFunc=makeCuts,branchNamePrefix="rawWireData")
#  plotMultiEventAroundMaxWires(tree,"allHist",20,cutFunc=makeCuts)
#  plotMultiEventAroundMaxWires(tree,"rawAllHist",100,cutFunc=makeCuts,branchNamePrefix="rawWireData",nAfterC=150,nAfterI=150,yMinC=-50,yMinI=-200,yMaxC=400,yMaxI=250,nBinsC=450,nBinsI=450)
#  plotMultiEventAroundMaxWires(tree,"rawAllHistNorm",10,normToAmp=True,cutFunc=makeCuts,branchNamePrefix="rawWireData",nAfterC=150,nAfterI=150,yMinC=-50,yMinI=-200,yMaxC=400,yMaxI=250,nBinsC=450,nBinsI=450)
#  plotAllWholeWires(tree,"phiLt0",20,cutFunc=lambda x: makeCuts(x,phiLt0=True))
#  plotAroundMaxWires(tree,"phiLt0Max",20,cutFunc=lambda x: makeCuts(x,phiLt0=True))
#  plotAroundMaxWires(tree,"phiLt0MaxNorm",20,cutFunc=lambda x: makeCuts(x,phiLt0=True),normToAmp=True)
#  plotAllWholeWires(tree,"phiGeq0",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
#  plotAroundMaxWires(tree,"phiGeq0Max",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
#  plotAroundMaxWires(tree,"phiGeq0MaxNorm",20,cutFunc=lambda x: makeCuts(x,phiGeq0=True),normToAmp=True)
#
#  plotMultiEventAroundMaxWires(tree,"phiLt0Hist",100,cutFunc=lambda x: makeCuts(x,phiLt0=True))
#  plotMultiEventAroundMaxWires(tree,"phiGeq0Hist",100,cutFunc=lambda x: makeCuts(x,phiGeq0=True))
#  plotMultiEventAroundMaxWires(tree,"phiLt0HistNorm",100,cutFunc=lambda x: makeCuts(x,phiLt0=True),normToAmp=True)
#  plotMultiEventAroundMaxWires(tree,"phiGeq0HistNorm",100,cutFunc=lambda x: makeCuts(x,phiGeq0=True),normToAmp=True)
#
#  compareMultiEventAroundMaxWires([tree,tree],"ComparePhi",100,
#                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiGeq0=True)],
#                    labels=["$\phi < 0$", "$\phi \geq 0$"]
#                    )
#  compareMultiEventAroundMaxWires([tree,tree],"ComparePhiNorm",100,normToAmp=True,
#                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiGeq0=True)],
#                    labels=["$\phi < 0$", "$\phi \geq 0$"]
#                    )
#  compareMultiEventAroundMaxWires([tree,treeMC],"CompareMCPhiLt0",100,
#                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
#                    labels=["Data","MC"]
#                    )
#  compareMultiEventAroundMaxWires([tree,treeMC],"CompareMCPhiLt0Norm",100,normToAmp=True,
#                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
#                    labels=["Data","MC"]
#                    )
#  compareMultiEventAroundMaxWires([tree,treeMC],"CompareMCPhiGeq0",100,
#                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
#                    labels=["Data","MC"]
#                    )
#  compareMultiEventAroundMaxWires([tree,treeMC],"CompareMCPhiGeq0Norm",100,normToAmp=True,
#                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
#                    labels=["Data","MC"]
#                    )


  compareMultiEventAroundMaxWires([tree,tree],"ComparePhiRaw",100,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["$\phi < 0$", "$\phi \geq 0$"]
                    )
  compareMultiEventAroundMaxWires([tree,tree],"ComparePhiRawNorm",100,normToAmp=True,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["$\phi < 0$", "$\phi \geq 0$"]
                    )


  compareMultiEventAroundMaxWires([treeMC,tree],"CompareMCRawPhiLt0",100,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["MC","Data"]
                    )
  compareMultiEventAroundMaxWires([treeMC,tree],"CompareMCRawPhiLt0Norm",100,normToAmp=True,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["MC","Data"]
                    )
  compareMultiEventAroundMaxWires([treeMC,tree],"CompareMCRawPhiGeq0",100,
                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["MC","Data"]
                    )
  compareMultiEventAroundMaxWires([treeMC,tree],"CompareMCRawPhiGeq0Norm",100,normToAmp=True,
                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","rawWireData"],
                    labels=["MC","Data"]
                    )


  compareMultiEventAroundMaxWires([tree,tree],"CompareRawPhiLt0",100,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
                    branchNamePrefixes=["rawWireData","wireData"],
                    labels=["Raw","De-convolved"]
                    )
  compareMultiEventAroundMaxWires([tree,tree],"CompareRawPhiLt0Norm",100,normToAmp=True,
                    cutFuncs=[lambda x: makeCuts(x,phiLt0=True),lambda x: makeCuts(x,phiLt0=True)],
                    branchNamePrefixes=["rawWireData","wireData"],
                    labels=["Raw","De-convolved"]
                    )
  compareMultiEventAroundMaxWires([tree,tree],"CompareRawPhiGeq0",100,
                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","wireData"],
                    labels=["Raw","De-convolved"]
                    )
  compareMultiEventAroundMaxWires([tree,tree],"CompareRawPhiGeq0Norm",100,normToAmp=True,
                    cutFuncs=[lambda x: makeCuts(x,phiGeq0=True),lambda x: makeCuts(x,phiGeq0=True)],
                    branchNamePrefixes=["rawWireData","wireData"],
                    labels=["Raw","De-convolved"]
                    )
