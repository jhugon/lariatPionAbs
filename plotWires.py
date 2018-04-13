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
  hitStartsHists = []
  hitEndsHists = []
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
    hitStartsHist = None
    hitEndsHist = None
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
            rawMax = numpy.max(data)
            data /= rawMax
            histNorm, xedges, yedgesNormRaw = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,int(yMax-yMin)],range=[[-nBefore,nAfter],[-2.,2.]])
            if rawHist is None:
                rawHist = hist
                rawHistNorm = histNorm
            else:
                rawHist += hist
                rawHistNorm += histNorm
            tmpHitStarts = numpy.array(getattr(tree,getHitName(rawWireBranchNames[iWire],start=True)))-iStart-nBefore
            tmpHitEnds = numpy.array(getattr(tree,getHitName(rawWireBranchNames[iWire],start=False)))-iStart-nBefore
            hitStartsRaw.extend(tmpHitStarts)
            hitEndsRaw.extend(tmpHitEnds)
        if signif > 8.:
          iMax = numpy.argmax(dataArray)
          if iMax > nBefore and iMax < (nSamples - nAfter):
            iStart = max(iMax-nBefore,0)
            iEnd = min(iMax+nAfter,nSamples)
            data = dataArray[iStart:iEnd]
            rawData = rawDataArray[iStart:iEnd]
            hist, xedges, yedges = numpy.histogram2d(arange,data,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            histRaw, xedges, yedges = numpy.histogram2d(arange,rawData,bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            deconvMax = numpy.max(data)
            rawMax = numpy.max(rawData)
            data /= deconvMax
            rawData /= rawMax
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
            tmpHitStarts = numpy.array(getattr(tree,getHitName(wireBranchNames[iWire],start=True)))-iStart-nBefore
            tmpHitEnds = numpy.array(getattr(tree,getHitName(wireBranchNames[iWire],start=False)))-iStart-nBefore
            hitStarts.extend(tmpHitStarts)
            hitEnds.extend(tmpHitEnds)
            hist, xedges, yedges = numpy.histogram2d(tmpHitStarts,deconvMax*numpy.ones(len(tmpHitStarts)),bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            if hitStartsHist is None:
                hitStartsHist = hist
            else:
                hitStartsHist += hist
            hist, xedges, yedges = numpy.histogram2d(tmpHitEnds,deconvMax*numpy.ones(len(tmpHitEnds)),bins=[nBefore+nAfter,nBins],range=[[-nBefore,nAfter],[yMin,yMax]])
            if hitEndsHist is None:
                hitEndsHist = hist
            else:
                hitEndsHist += hist
            
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
    hitStartsHists.append(hitStartsHist)
    hitEndsHists.append(hitEndsHist)
    allHitStarts.append(hitStarts)
    allHitStartsRaw.append(hitStartsRaw)
    allHitEnds.append(hitEnds)
    allHitEndsRaw.append(hitEndsRaw)
  return rawHists, rawHistNorms, deconvHists, deconvHistNorms, rawAtDeconvHists, rawAtDeconvHistNorms, xedges, yedges, yedgesNorm, yedgesRaw, yedgesNormRaw, allHitStarts, allHitEnds, allHitStartsRaw, allHitEndsRaw, hitStartsHists, hitEndsHists

def makeWireHistsAndPkl(filePrefix, tree, maxEvents, cutFunc,**kargs):
  fn = "{0}_{1:d}.pkl".format(filePrefix,nMax)
  result = None
  try:
    with open(fn) as infile:
      result = cPickle.load(infile)
  except IOError:
    result = makeWireHists(tree,nMax,cutFunc)
    with open(fn,'wb') as outfile:
      cPickle.dump(result,outfile)
  return result

def justDraw(hist,hitStarts,hitEnds,xedges,yedges,fn,xMin,xMax,yMin,yMax,xLabel,yLabel,title,labels=[],compare=False):
  gs = {'height_ratios':[4,1],'hspace':0}
  fig, (ax1,ax2) = mpl.subplots(nrows=2,sharex=True,gridspec_kw=gs)
  patchList = []
  if compare:
    if len(hist) != len(labels):
        raise Exception("Length of hist doesn't equal length of labels. Maybe you forgot to add labels")
    if len(hist) != len(hitStarts):
        raise Exception("Length of hist doesn't equal length of hitStarts")
    if len(hist) != len(hitEnds):
        raise Exception("Length of hist doesn't equal length of hitEnds")

    transparent_cmaps = []
    for cmap in [mpl.cm.Greens,mpl.cm.Blues,mpl.cm.Reds,mpl.cm.Purples,mpl.cm.Oranges]:
      frac_transparent = 0.5
      cmap_colors = cmap(numpy.arange(cmap.N))
      cmap_colors[:int(frac_transparent*cmap.N),-1] = numpy.linspace(0,1,int(frac_transparent*cmap.N)) # bottom frac linearly increases opacity
      transparent_cmap = matplotlib.colors.ListedColormap(cmap_colors)
      transparent_cmaps.append(transparent_cmap)
    colors = ['g','b','r','purple','o']

    for h, xed, yed, starts, ends, label, t_cmap, col in zip(hist, xedges , yedges, hitStarts, hitEnds, labels, transparent_cmaps[:len(hist)], colors[:len(hist)]):
      if h is None:
        print "Error: element of hist is None, no events passed amplitude cut for: ",fn," label: ",label
      else:
        histToPlot = numpy.array(h)
        histToPlot[histToPlot == 0.] = 0.5
        x, y = numpy.meshgrid(xed, yed)
        norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=histToPlot.max())
        p = ax1.pcolormesh(x,y,histToPlot.T,norm=norm,cmap=t_cmap)
      ax2.hist(starts,range=[xMin,xMax],bins=100,normed=True,histtype="step",color=col)
      ax2.hist(ends,range=[xMin,xMax],bins=100,normed=True,histtype="step",color=col,ls=':')
      patchList.append(
            patches.Patch(color=col, label=label)
          )
  else:
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
  if len(patchList) > 0:
    ax1.legend(handles=patchList)
  ax1.set_title(title)

  fig.savefig(fn)
  mpl.close()

def drawHitVAmpHists(hist,xedges,yedges,fn,xMin,xMax,yMin,yMax,xLabel,yLabel,title,compare=False):
  fig, ax1 = mpl.subplots()
  if hist is None:
    print "Error: hist is None, no events passed amplitude cut for: ",fn
  else:
    histToPlot = numpy.array(hist).T
    histToPlot[histToPlot == 0.] = 0.5
    x, y = numpy.meshgrid(xedges, yedges)
    norm = matplotlib.colors.LogNorm(vmin=0.5, vmax=histToPlot.max())
    p = ax1.pcolormesh(x,y,histToPlot,norm=norm,cmap="Blues_r")
  ax1.set_xlim(xMin,xMax)
  ax1.set_ylim(yMin,yMax)
  yLabelSuffix = ""
  ax1.set_ylabel(yLabel)
  ax1.set_xlabel(xLabel)
  ax1.set_title(title)

  fig.savefig(fn)
  mpl.close()

def plotWireHists(*args,**kargs):

  if len(args) != 17:
    print "plotWireHists n args isn't 17 as expected is ", len(args)
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
  hitStartsHists = args[15]
  hitEndsHists = args[16]

  filePrefix=""
  fileSuffixes=["C","I"]
  xMins=[-150,-150]
  xMaxs=[150,150]
  yMins=[-50,-250]
  yMaxs=[400,300]
  yMinNorms=[-0.2,-1.8]
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

  nRawHists = len(rawHists)
  if len(fileSuffixes) != nRawHists:
    raise ValueError("fileSuffixes length should be: ", nRawHists, " is ", len(fileSuffixes))
  if len(xMins) != nRawHists:
    raise ValueError("xMins length should be: ", nRawHists, " is ", len(xMins))
  if len(yMins) != nRawHists:
    raise ValueError("yMins length should be: ", nRawHists, " is ", len(yMins))
  if len(xMaxs) != nRawHists:
    raise ValueError("xMaxs length should be: ", nRawHists, " is ", len(xMaxs))
  if len(yMaxs) != nRawHists:
    raise ValueError("yMaxs length should be: ", nRawHists, " is ", len(yMaxs))
  if len(yLabels) != nRawHists:
    raise ValueError("yLabels length should be: ", nRawHists, " is ", len(yLabels))

  for rawHist, rawHistNorm, deconvHist, deconvHistNorm, rawAtDeconvHist, \
      rawAtDeconvHistNorm, hitStarts, hitEnds, hitStartsRaw, hitEndsRaw, \
      fileSuffix, xMin, xMax, yMin, yMax, yMinNorm, yLabel, \
      hitStartsHist, hitEndsHist in zip(
            rawHists, rawHistNorms, deconvHists, deconvHistNorms, rawAtDeconvHists, 
            rawAtDeconvHistNorms, allHitStarts, allHitEnds, allHitStartsRaw, allHitEndsRaw,
            fileSuffixes, xMins, xMaxs, yMins, yMaxs, yMinNorms, yLabels,
            hitStartsHists, hitEndsHists
        ):
    
    justDraw(rawHist,hitStartsRaw,hitEndsRaw,xedges,yedgesRaw,"{}_raw_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    justDraw(rawHistNorm,hitStartsRaw,hitEndsRaw,xedges,yedgesNormRaw,"{}_raw_norm_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMinNorm,1.2,xLabel,yLabel+" Normalized to Max",title)
    justDraw(deconvHist,hitStarts,hitEnds,xedges,yedges,"{}_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    justDraw(deconvHistNorm,hitStarts,hitEnds,xedges,yedgesNorm,"{}_deconv_norm_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-0.8,1.1,xLabel,yLabel+" Normalized to Max",title)
    #justDraw(rawAtDeconvHist,hitStarts,hitEnds,xedges,yedges,"{}_raw_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title)
    #justDraw(rawAtDeconvHistNorm,hitStarts,hitEnds,xedges,yedgesNorm,"{}_raw_norm_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-2,2,xLabel,yLabel+" Normalized to Max",title)
    drawHitVAmpHists(hitStartsHist,xedges,yedges,"{}_hitStartVAmp_{}.png".format(filePrefix,fileSuffix),xMin,xMax,0,400,"Hit Start Time - Time of Hit Maximum","Amplitude of "+yLabel,title)
    drawHitVAmpHists(hitEndsHist,xedges,yedges,"{}_hitEndVAmp_{}.png".format(filePrefix,fileSuffix),xMin,xMax,0,400,"Hit End Time - Time of Hit Maximum","Amplitude of "+yLabel,title)

def compareWireHists(*cases,**kargs):

  filePrefix=""
  fileSuffixes=["C","I"]
  xMins=[-150,-150]
  xMaxs=[150,150]
  yMins=[-50,-150]
  yMaxs=[400,300]
  yLabels=["Collection Wire Response","Induction Wire Response"]
  xLabel="Time Tick - Time Tick of Max"
  title=""
  labels=[]

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
  try:
    labels = kargs["labels"]
  except KeyError:
    raise Exception("plotWireHists: labels=[<label1>,<label2>,...] argument required")

  rawHists = []
  rawHistNorms = []
  deconvHists = []
  deconvHistNorms = []
  rawAtDeconvHists = []
  rawAtDeconvHistNorms = []
  xedges = []
  yedges = []
  yedgesNorm = []
  yedgesRaw = []
  yedgesNormRaw = []
  allHitStarts = []
  allHitEnds = []
  allHitStartsRaw = []
  allHitEndsRaw = []

  for args in cases:
    if len(args) != 17:
      print "compareWireHists n args isn't 17 as expected is ", len(args)
      sys.exit(1)
    rawHists.append(args[0])
    rawHistNorms.append(args[1])
    deconvHists.append(args[2])
    deconvHistNorms.append(args[3])
    rawAtDeconvHists.append(args[4])
    rawAtDeconvHistNorms.append(args[5])
    xedges.append(args[6])
    yedges.append(args[7])
    yedgesNorm.append(args[8])
    yedgesRaw.append(args[9])
    yedgesNormRaw.append(args[10])
    allHitStarts.append(args[11])
    allHitEnds.append(args[12])
    allHitStartsRaw.append(args[13])
    allHitEndsRaw.append(args[14])
    hitStartsHists.append(args[15])
    hitEndsHists.append(args[16])

    nRawHists = len(args[0])
    if len(fileSuffixes) != nRawHists:
      raise ValueError("fileSuffixes length should be: ", nRawHists, " is ", len(fileSuffixes))
    if len(xMins) != nRawHists:
      raise ValueError("xMins length should be: ", nRawHists, " is ", len(xMins))
    if len(yMins) != nRawHists:
      raise ValueError("yMins length should be: ", nRawHists, " is ", len(yMins))
    if len(xMaxs) != nRawHists:
      raise ValueError("xMaxs length should be: ", nRawHists, " is ", len(xMaxs))
    if len(yMaxs) != nRawHists:
      raise ValueError("yMaxs length should be: ", nRawHists, " is ", len(yMaxs))
    if len(yLabels) != nRawHists:
      raise ValueError("yLabels length should be: ", nRawHists, " is ", len(yLabels))

  for iPlane in range(len(fileSuffixes)):
    justDraw([x[iPlane] for x in rawHists],
             [x[iPlane] for x in allHitStartsRaw],
             [x[iPlane] for x in allHitEndsRaw],
             xedges,
             yedgesRaw,
             "{}_raw_{}.png".format(filePrefix,fileSuffixes[iPlane]),
             xMins[iPlane],xMaxs[iPlane],yMins[iPlane],yMaxs[iPlane],
             xLabel,yLabels[iPlane],title,labels=labels,compare=True)
    yMinNorm = [-0.2,-1.8][iPlane]
    yMaxNorm = [1.8,2.2][iPlane]
    justDraw([x[iPlane] for x in rawHistNorms],
             [x[iPlane] for x in allHitStartsRaw],
             [x[iPlane] for x in allHitEndsRaw],
             xedges,
             yedgesNormRaw,
             "{}_raw_norm_{}.png".format(filePrefix,fileSuffixes[iPlane]),
             xMins[iPlane],xMaxs[iPlane],yMinNorm,yMaxNorm,
             xLabel,yLabels[iPlane]+" Normalized to Max",title,labels=labels,compare=True)
    justDraw([x[iPlane] for x in deconvHists],
             [x[iPlane] for x in allHitStarts],
             [x[iPlane] for x in allHitEnds],
             xedges,
             yedgesRaw,
             "{}_deconv_{}.png".format(filePrefix,fileSuffixes[iPlane]),
             xMins[iPlane],xMaxs[iPlane],yMins[iPlane],yMaxs[iPlane],
             xLabel,yLabels[iPlane],title,labels=labels,compare=True)
    justDraw([x[iPlane] for x in deconvHistNorms],
             [x[iPlane] for x in allHitStarts],
             [x[iPlane] for x in allHitEnds],
             xedges,
             yedgesNormRaw,
             "{}_deconv_norm_{}.png".format(filePrefix,fileSuffixes[iPlane]),
             xMins[iPlane],xMaxs[iPlane],-0.5,1.6,
             xLabel,yLabels[iPlane]+" Normalized to Max",title,labels=labels,compare=True)

    #justDraw(rawAtDeconvHist,hitStarts,hitEnds,xedges,yedges,"{}_raw_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,yMin,yMax,xLabel,yLabel,title,labels=labels,compare=True)
    #justDraw(rawAtDeconvHistNorm,hitStarts,hitEnds,xedges,yedgesNorm,"{}_raw_norm_on_deconv_{}.png".format(filePrefix,fileSuffix),xMin,xMax,-2,2,xLabel,yLabel+" Normalized to Max",title,labels=labels,compare=True)

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

if __name__ == "__main__":

  import matplotlib
  import cPickle

  #f = root.TFile("WireData_RIIP100_64a.root")
  #f = root.TFile("WireData_RIIP100_64a_nocrct.root")
  #f = root.TFile("WireData_RIIP60_64a.root")
  f = root.TFile("Wires_RIIP60a_v3.root")
  fBeam100A = root.TFile("Wires_Lovely1_Pos_RunII_jhugon_current100_secondary64_d_v1_v01.root")
  #fMC = root.TFile("WiresMC_v3.root")
  #f.ls()
  tree = f.Get("cosmicanalyzer/tree")
  treeBeam100A = fBeam100A.Get("cosmicanalyzer/tree")
  #treeMC = fMC.Get("cosmicanalyzer/tree")
  #tree.Print()

  def makeCuts(tree,phiGeq0=False,phiLt0=False,beam=False,tofLt25=False,tofGeq25=False):
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
    if not (tree.isMC or beam or ((tree.triggerBits >> 10) & 1)):
        return False
    if not ((not tree.isMC) or (tree.trueHitCosmic1 and tree.trueHitCosmic2) or (tree.trueHitCosmic3 and tree.trueHitCosmic4)):
        return False
    if (not beam) and not ((tree.primTrkStartTheta > 27*pi/180.) and (tree.primTrkStartTheta < 42*pi/180.) and (tree.primTrkStartPhi > -57*pi/180. and tree.primTrkStartPhi < 60*pi/180.) and (tree.primTrkStartPhi < -15*pi/180. or tree.primTrkStartPhi > 22*pi/180.)):
        return False
    if tofLt25 and not (tree.firstTOF < 25.):
        return False
    if tofGeq25 and not (tree.firstTOF >= 25.):
        return False
    return True

  nMax = 100

  dataAllHists = makeWireHistsAndPkl("dataAllHists",tree,nMax,makeCuts)
  dataPhiLt0Hists = makeWireHistsAndPkl("dataPhiLt0Hists",tree,nMax,lambda x: makeCuts(x,phiLt0=True))
  dataPhiGeq0Hists = makeWireHistsAndPkl("dataPhiGeq0Hists",tree,nMax,lambda x: makeCuts(x,phiGeq0=True))
  dataBeam100AHists = makeWireHistsAndPkl("dataBeam100AHists",treeBeam100A,nMax,lambda x: makeCuts(x,beam=True))
  dataBeam100ATOFLt25Hists = makeWireHistsAndPkl("dataBeam100ATOFLt25Hists",treeBeam100A,nMax,lambda x: makeCuts(x,beam=True,tofLt25=True))
  dataBeam100ATOFGeq25Hists = makeWireHistsAndPkl("dataBeam100ATOFGeq25Hists",treeBeam100A,nMax,lambda x: makeCuts(x,beam=True,tofGeq25=True))
  #mcAllHists = makeWireHistsAndPkl("mcAllHists",treeMC,nMax,makeCuts)
  #mcPhiLt0Hists = makeWireHistsAndPkl("mcPhiLt0Hists",treeMC,nMax,lambda x: makeCuts(x,phiLt0=True))
  #mcPhiGeq0Hists = makeWireHistsAndPkl("mcPhiGeq0Hists",treeMC,nMax,lambda x: makeCuts(x,phiGeq0=True))

  #plotWireHists(*dataAllHists,filePrefix="Scope_All")
  plotWireHists(*dataPhiLt0Hists,filePrefix="Scope_PhiLt0")
  plotWireHists(*dataPhiGeq0Hists,filePrefix="Scope_PhiGeq0")
  plotWireHists(*dataBeam100ATOFLt25Hists,filePrefix="Scope_Beam100ATOFLt25")
  plotWireHists(*dataBeam100ATOFGeq25Hists,filePrefix="Scope_Beam100ATOFGeq25")
  compareWireHists(dataPhiLt0Hists,dataPhiGeq0Hists,filePrefix="ScopeCompare_Phi",
                                    labels=["$\phi < 0$", "$\phi \geq 0$"])
  compareWireHists(dataPhiLt0Hists,dataPhiGeq0Hists,dataBeam100ATOFLt25Hists,filePrefix="ScopeCompare_PhiBeam",
                                    labels=["$\phi < 0$", "$\phi \geq 0$",r"+100A TOF < 25 ns"])
  compareWireHists(dataBeam100ATOFGeq25Hists,dataBeam100ATOFLt25Hists,filePrefix="ScopeCompare_Beam",
                                    labels=["+100A TOF $\geq$ 25 ns",r"+100A TOF < 25 ns"])

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
