#!/usr/bin/env python2
import ROOT as root
from ROOT import gStyle as gStyle
root.gROOT.SetBatch(True)
from helpers import *

def plotSlices(c,hist,savename,xlimits,xtitle,ytitle,xvarname,rebinX=1,rebinY=1,xunits=None,normalize=False):
  print(hist)
  if not hist:
    return
  hist = hist.Clone(uuid.uuid1().hex)

  hist.RebinX(rebinX)
  hist.RebinY(rebinY)
  histAll = hist.ProjectionY("_pyAll",1,hist.GetNbinsX())
  if normalize:
    integral = histAll.Integral()
    if integral != 0.:
        histAll.Scale(1./integral)
  ymax = histAll.GetMaximum()
  histAll.SetLineColor(root.kBlack)
  histAll.SetMarkerColor(root.kBlack)
  labels = ["All"]

  nBinsX = hist.GetNbinsX()
  sliceHists = []
  for iBin in range(1,nBinsX+1):
    sliceHist = getXBinHist(hist,iBin)
    if normalize:
      integral = sliceHist.Integral()
      if integral != 0.:
          sliceHist.Scale(1./integral)
    ymax = max(sliceHist.GetMaximum(),ymax)
    sliceHist.SetLineColor(COLORLIST[iBin-1])
    sliceHist.SetMarkerColor(COLORLIST[iBin-1])
    sliceHists.append(sliceHist)
    xlow = hist.GetXaxis().GetBinLowEdge(iBin)
    xhigh = hist.GetXaxis().GetBinUpEdge(iBin)
    if xunits:
      labels.append("{0:.4g} {3} < {1} < {2:.4g} {3}".format(xlow,xvarname,xhigh,xunits))
    else:
      labels.append("{0:.4g} < {1} < {2:.4g}".format(xlow,xvarname,xhigh))
  if c.GetLogy() == 1:
    ybound = ymax * 10**((log10(ymax)+1)*0.5)
    axisHist = Hist2D(1,xlimits[0],xlimits[1],1,0.1,ybound)
  else:
    axisHist = Hist2D(1,xlimits[0],xlimits[1],1,0,ymax*1.1)
  setHistTitles(axisHist,xtitle,ytitle)
  axisHist.Draw()
  for sliceHist in sliceHists:
    sliceHist.Draw("histsame")
  histAll.Draw("histsame")
  leg = drawNormalLegend([histAll]+sliceHists,labels)
  c.SaveAs(savename+".png")
  c.SaveAs(savename+".pdf")

def getMaxAndFWHM(hist,xBin):
  sliceHist = getXBinHist(hist,xBin)
  nBins = sliceHist.GetNbinsX()
  contentMax = sliceHist.GetMaximum()
  halfContentMax = 0.5*contentMax
  iMax = sliceHist.GetMaximumBin()
  xMax = sliceHist.GetXaxis().GetBinCenter(iMax)
  xHalfMaxAbove = float('nan')
  xHalfMaxBelow = float('nan')
  for iBin in range(iMax,nBins+2):
    if sliceHist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxAbove = sliceHist.GetXaxis().GetBinLowEdge(iBin)
        break
  for iBin in range(iMax,-1,-1):
    if sliceHist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxBelow = sliceHist.GetXaxis().GetBinUpEdge(iBin)
        break
  fwhm = xHalfMaxAbove-xHalfMaxBelow
  return xMax, fwhm

def getFracMaxVals(hist,frac=0.5):
  nBins = hist.GetNbinsX()
  contentMax = hist.GetMaximum()
  halfContentMax = frac*contentMax
  iMax = hist.GetMaximumBin()
  xMax = hist.GetXaxis().GetBinCenter(iMax)
  xHalfMaxAbove = float('nan')
  xHalfMaxBelow = float('nan')
  for iBin in range(iMax,nBins+2):
    if hist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxAbove = hist.GetXaxis().GetBinLowEdge(iBin)
        break
  for iBin in range(iMax,-1,-1):
    if hist.GetBinContent(iBin) <= halfContentMax:
        xHalfMaxBelow = hist.GetXaxis().GetBinUpEdge(iBin)
        break
  return xHalfMaxBelow, xHalfMaxAbove


def makeGraphsModeAndFWHM(hist):
  hist = hist.Clone(uuid.uuid1().hex)
  graph = root.TGraph()
  graphFWHM = root.TGraph()
  for iBin in range(1,hist.GetNbinsX()+1):
    yMax, fwhm = getMaxAndFWHM(hist,iBin)
    x = hist.GetXaxis().GetBinCenter(iBin)
    graph.SetPoint(iBin-1,x,yMax)
    graphFWHM.SetPoint(iBin-1,x,fwhm)
  return graph, graphFWHM

def fitLandaus(c,hist,nLandaus=3,smearGauss=True,samplename=""):
  if nLandaus <= 0:
    raise ValueError("nLandaus must be > 0")

  t = root.RooRealVar("t","dE/dx [MeV/cm]",0.,10)
  t.setBins(10000,"cache")
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  ##############

  mg = root.RooRealVar("mg","mg",0)
  sg = root.RooRealVar("sg","sg",0.1,0.01,2.)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  landauParams = []
  landaus = []
  langauses = []

  for iLandau in range(1,nLandaus+1):
    iLandauStr = str(iLandau)
    mpvl = root.RooRealVar("mpvl"+iLandauStr,"mpv landau "+iLandauStr,1.7,0,5)
    wl = root.RooRealVar("wl"+iLandauStr,"width landau "+iLandauStr,0.42,0.01,10)
    ml = root.RooFormulaVar("ml"+iLandauStr,"first landau param "+iLandauStr,"@0+0.22278*@1",root.RooArgList(mpvl,wl))
    landau = root.RooLandau("lx"+iLandauStr,"lx "+iLandauStr,t,ml,wl)

    landauParams += [mpvl,wl,ml]
    landaus.append(landau)

    langaus = root.RooFFTConvPdf("langaus"+iLandauStr,"landau (X) gauss "+iLandauStr,t,landau,gauss)
    langaus.setBufferFraction(0.2)
    langauses.append(langaus)

  ratioParams = []

  for iRatio in range(1,nLandaus):
    iRatioStr = str(iRatio)
    ratio = root.RooRealVar("ratio"+iRatioStr,"ratio "+iRatioStr,0.18,0,1)
    ratioParams.append(ratio)

  model = landaus[0]
  multiLandaus = None
  multiLangaus = None
  if nLandaus > 1:
    multiLandaus = root.RooAddPdf("multiLandaus","multiLandaus",root.RooArgList(*landaus),root.RooArgList(*ratioParams))
    multiLangaus = root.RooAddPdf("multiLangaus","multiLangaus",root.RooArgList(*langauses),root.RooArgList(*ratioParams))
    model = multiLandaus
    if smearGauss:
      model = multiLangaus

  ##############

  model.fitTo(data)

  frame = t.frame(root.RooFit.Title(""))
  data.plotOn(frame)
  model.plotOn(frame)

  for iLandau in range(2,nLandaus+1):
    iLandauStr = str(iLandau)
    if smearGauss:
      model.plotOn(frame,root.RooFit.Components("langaus"+iLandauStr),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iLandau]))
    else:
      model.plotOn(frame,root.RooFit.Components("lx"+iLandauStr),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(COLORLIST[iLandau]))

  #root.gPad.SetLeftMargin(0.15)
  #frame.GetYaxis().SetTitleOffset(1.4)
  #frame.Draw("same")
  #axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
  ##axisHist = root.TH2F("axisHist","",1,-1,1,1,1000,1300)
  #axisHist.Draw()
  #frame.Draw("same")
  frame.Draw()
  c.SaveAs("roofit_{}.png".format(samplename))

  bestFits = []
  errs = []
  for iLandau in range(nLandaus):
    for iParam in range(2):
      param = landauParams[iParam+iLandau*3]
      bestFits.append(param.getVal())
      bestFits.append(param.getError())

  return bestFits, errs

def fitSlicesLandaus(c,hist,fileprefix,nJump=1,nLandaus=1,smearGauss=False):
  xaxis = hist.GetXaxis()
  xTitle = xaxis.GetTitle()
  yaxis = hist.GetYaxis()
  yTitle = yaxis.GetTitle()
  mpvlGraph = root.TGraphErrors()
  wlGraph = root.TGraphErrors()
  sgGraph = root.TGraphErrors()
  fwhmGraph = root.TGraphErrors()
  iPoint=0
  for i in range(hist.GetNbinsX()//nJump):
      firstBin = i*nJump+1
      lastBin = (i+1)*(nJump)
      lastBin = min(lastBin,hist.GetNbinsX())
      histAll = hist.ProjectionY("_pyAll",firstBin,lastBin)
      if histAll.GetEntries() < 10:
        continue
      postfix = "_"+fileprefix+"bins{}".format(i)
      xMin = xaxis.GetBinLowEdge(firstBin)
      xMax = xaxis.GetBinUpEdge(lastBin)
      caption = "{} from {} to {}".format(xTitle,xMin,xMax)
      xMiddle = 0.5*(xMax+xMin)
      xError = 0.5*(xMax-xMin)
      startFit = 0.
      endFit = 0.
      #startFit, endFit = getFracMaxVals(histAll,fracMax)
      bestFits,errors = fitLandaus(c,histAll,nLandaus,smearGauss,postfix)
      #if and (mpvlErr > 0.5 or wlErr > 0.5 or sgErr > 0.5):
      #      continue
      mpvlGraph.SetPoint(iPoint,xMiddle,bestFits[0])
      wlGraph.SetPoint(iPoint,xMiddle,bestFits[1])
      mpvlGraph.SetPointError(iPoint,xError,bestFits[0])
      wlGraph.SetPointError(iPoint,xError,bestFits[1])
      iPoint += 1
  graphs = [mpvlGraph,wlGraph]
  labels = ["Landau MPV", "Landau Width"]
  #graphs = [mpvlGraph,sgGraph]
  #labels = ["Landau MPV", "Gaussian #sigma"]
  for i, graph in enumerate(graphs):
    graph.SetLineColor(COLORLIST[i])
    graph.SetMarkerColor(COLORLIST[i])
  pad1 = root.TPad("pad1"+hist.GetName(),"",0.02,0.50,0.98,0.98,0)
  pad2 = root.TPad("pad2"+hist.GetName(),"",0.02,0.01,0.98,0.49,0)
  c.cd()
  c.Clear()
  pad1.Draw()
  pad2.Draw()
  pad1.cd()
  axis1 = drawGraphs(pad1,[mpvlGraph],xTitle,"Landau MPV [MeV/cm]",yStartZero=False)
  pad2.cd()
  axis2 = drawGraphs(pad2,[sgGraph],xTitle,"Gaussian #sigma [MeV/cm]")
  #leg = drawNormalLegend(graphs,labels,option="lep",position=[0.2,0.50,0.6,0.70])
  c.cd()
  c.SaveAs(fileprefix+".png")
  c.SaveAs(fileprefix+".pdf")
  return mpvlGraph,wlGraph

def fitGaussCore(c,hist,postfix,caption,fitMin=1.4,fitMax=2.4):

  xMin = hist.GetXaxis().GetBinLowEdge(1)
  xMax = hist.GetXaxis().GetBinUpEdge(hist.GetNbinsX())
  t = root.RooRealVar("t","dE/dx [MeV/cm]",xMin,xMax)
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  ##############
  mg = root.RooRealVar("mg","mg",1.7,0.,5.)
  sg = root.RooRealVar("sg","sg",0.1,0.01,2.)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  model = gauss

  ##############

  fitResult = model.fitTo(data,root.RooFit.Save(),root.RooFit.Range(fitMin,fitMax))

  frame = t.frame(root.RooFit.Title(""))
  data.plotOn(frame)
  model.plotOn(frame,root.RooFit.Range(fitMin,fitMax))

  #root.gPad.SetLeftMargin(0.15)
  #frame.GetYaxis().SetTitleOffset(1.4)
  #frame.Draw("same")
  #axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
  ##axisHist = root.TH2F("axisHist","",1,-1,1,1,1000,1300)
  #axisHist.Draw()
  #frame.Draw("same")
  frame.Draw()
  frame.SetTitle(caption)
  c.SaveAs("roofit_gauss_{}.png".format(postfix))
  c.SaveAs("roofit_gauss_{}.pdf".format(postfix))

  fwhm = calcFWHM(model,t,1.,4.,0.01)

  return (mg.getVal(),float('nan'),sg.getVal()), (mg.getError(),float('nan'),sg.getError()), fwhm

def fitLandauCore(c,hist,postfix,caption,fitMin=1.6,fitMax=2.3,fixedLandauWidth=None,dQdx=False):

  xMin = hist.GetXaxis().GetBinLowEdge(1)
  xMax = hist.GetXaxis().GetBinUpEdge(hist.GetNbinsX())
  if not dQdx:
    xMax = min(xMax,5.)
  xTitle = "dE/dx [MeV/cm]"
  if dQdx:
    xTitle = "dQ/dx [ADC ns / cm]"
  t = root.RooRealVar("t",xTitle,xMin,xMax)
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  mpvl = None
  wl = None
  ml = None
  mg = None
  sg = None
  ##############
  if dQdx:
    mpvl = root.RooRealVar("mpvl","mpv landau",0.5*(fitMin+fitMax),0,xMax*1.5)
    if fixedLandauWidth is None:
      wl = root.RooRealVar("wl","width landau",0.5*(fitMax-fitMin),0.01*(fitMax-fitMin),2*(fitMax-fitMin))
    else:
      wl = root.RooRealVar("wl","width landau",fixedLandauWidth)
    ml = root.RooFormulaVar("ml","first landau param","@0+0.22278*@1",root.RooArgList(mpvl,wl))

    mg = root.RooRealVar("mg","mg",0)
    sg = root.RooRealVar("sg","sg",0.5*(fitMax-fitMin),0.01*(fitMax-fitMin),2*(fitMax-fitMin))
  else:
    mpvl = root.RooRealVar("mpvl","mpv landau",1.7,0,5)
    if fixedLandauWidth is None:
      wl = root.RooRealVar("wl","width landau",0.42,0.01,10)
    else:
      wl = root.RooRealVar("wl","width landau",fixedLandauWidth)
    ml = root.RooFormulaVar("ml","first landau param","@0+0.22278*@1",root.RooArgList(mpvl,wl))

    mg = root.RooRealVar("mg","mg",0)
    sg = root.RooRealVar("sg","sg",0.1,0.01,2.)

  t.Print()
  mpvl.Print()
  wl.Print()
  ml.Print()
  mg.Print()
  sg.Print()

  landau = root.RooLandau("lx","lx",t,ml,wl)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  t.setBins(10000,"cache")
  langaus = root.RooFFTConvPdf("langaus","landau (X) gauss",t,landau,gauss)
  langaus.setBufferFraction(0.4)

  model = langaus

  ##############

  fitResult = model.fitTo(data,root.RooFit.Save(),root.RooFit.Range(fitMin,fitMax))

  fwhm = None
  if dQdx:
    fwhm = calcFWHM(model,t,0.5*fitMin,fitMax*1.5,(fitMax-fitMin)/200.)
  else:
    fwhm = calcFWHM(model,t,1.,4.,0.01)

  if False:
    frame = t.frame(root.RooFit.Title("landau (x) gauss convolution"))
    data.plotOn(frame)
    model.plotOn(frame,root.RooFit.Range(fitMin,fitMax))

    frame.Draw()
    frame.SetTitle(caption)
    c.SaveAs("roofit_landau_{}.png".format(postfix))
    c.SaveAs("roofit_landau_{}.pdf".format(postfix))

  return (mpvl.getVal(),wl.getVal(),sg.getVal()), (mpvl.getError(),wl.getError(),sg.getError()), fwhm

def fitSlicesLandauCore(c,hist,fileprefix,nJump=1,fracMax=0.4,fixedLandauWidth=0.12,dQdx=False):
  xaxis = hist.GetXaxis()
  xTitle = xaxis.GetTitle()
  yaxis = hist.GetYaxis()
  yTitle = yaxis.GetTitle()
  mpvlGraph = root.TGraphErrors()
  wlGraph = root.TGraphErrors()
  sgGraph = root.TGraphErrors()
  fwhmGraph = root.TGraphErrors()
  iPoint=0
  for i in range(hist.GetNbinsX()//nJump):
      firstBin = i*nJump+1
      lastBin = (i+1)*(nJump)
      lastBin = min(lastBin,hist.GetNbinsX())
      histAll = hist.ProjectionY("_pyAll",firstBin,lastBin)
      if histAll.GetEntries() < 10:
        continue
      postfix = "_"+fileprefix+"bins{}".format(i)
      xMin = xaxis.GetBinLowEdge(firstBin)
      xMax = xaxis.GetBinUpEdge(lastBin)
      caption = "{} from {} to {}".format(xTitle,xMin,xMax)
      xMiddle = 0.5*(xMax+xMin)
      xError = 0.5*(xMax-xMin)
      startFit = 0.
      endFit = 0.
      if dQdx:
        histAllRebin = histAll.Clone(histAll.GetName()+"_rebin")
        histAllRebin.Rebin(2)
        startFit, endFit = getFracMaxVals(histAllRebin,fracMax)
      else:
        startFit, endFit = getFracMaxVals(histAll,fracMax)
      (mpvl,wl,sg),(mpvlErr,wlErr,sgErr), fwhm = fitLandauCore(c,histAll,postfix,caption,startFit,endFit,fixedLandauWidth=fixedLandauWidth,dQdx=dQdx)
      if (not dQdx) and (mpvlErr > 0.5 or wlErr > 0.5 or sgErr > 0.5):
            continue
      if dQdx and mpvl > 4000 :
            continue
      mpvlGraph.SetPoint(iPoint,xMiddle,mpvl)
      wlGraph.SetPoint(iPoint,xMiddle,wl)
      sgGraph.SetPoint(iPoint,xMiddle,sg)
      fwhmGraph.SetPoint(iPoint,xMiddle,fwhm)
      mpvlGraph.SetPointError(iPoint,xError,mpvlErr)
      wlGraph.SetPointError(iPoint,xError,wlErr)
      sgGraph.SetPointError(iPoint,xError,sgErr)
      iPoint += 1
  graphs = [mpvlGraph,wlGraph,sgGraph,fwhmGraph]
  labels = ["Landau MPV", "Landau Width", "Gaussian #sigma","FWHM"]
  #graphs = [mpvlGraph,sgGraph]
  #labels = ["Landau MPV", "Gaussian #sigma"]
  for i, graph in enumerate(graphs):
    graph.SetLineColor(COLORLIST[i])
    graph.SetMarkerColor(COLORLIST[i])
  pad1 = root.TPad("pad1"+hist.GetName(),"",0.02,0.50,0.98,0.98,0)
  pad2 = root.TPad("pad2"+hist.GetName(),"",0.02,0.01,0.98,0.49,0)
  c.cd()
  c.Clear()
  pad1.Draw()
  pad2.Draw()
  pad1.cd()
  axis1 = drawGraphs(pad1,[mpvlGraph],xTitle,"Landau MPV [MeV/cm]",yStartZero=False)
  pad2.cd()
  axis2 = drawGraphs(pad2,[sgGraph],xTitle,"Gaussian #sigma [MeV/cm]")
  #leg = drawNormalLegend(graphs,labels,option="lep",position=[0.2,0.50,0.6,0.70])
  c.cd()
  c.SaveAs(fileprefix+".png")
  c.SaveAs(fileprefix+".pdf")
  return mpvlGraph,wlGraph,sgGraph

def fitSlicesLandauCore3D(c,hist,fileprefix,nJump=1,fracMax=0.4,fixedLandauWidth=0.12,dQdx=False):
  xaxis = hist.GetXaxis()
  xTitle = xaxis.GetTitle()
  yaxis = hist.GetYaxis()
  yTitle = yaxis.GetTitle()
  zaxis = hist.GetZaxis()
  zTitle = zaxis.GetTitle()
  binning = [xaxis.GetNbins(),xaxis.GetXmin(),xaxis.GetXmax(),
             yaxis.GetNbins(),yaxis.GetXmin(),yaxis.GetXmax()
  ]
  zBinning = [zaxis.GetNbins(),zaxis.GetXmin(),zaxis.GetXmax()]
  mpvlHist = Hist2D(*binning)
  wlHist = Hist2D(*binning)
  sgHist = Hist2D(*binning)
  mpvlErrorHist = Hist2D(*binning)
  wlErrorHist = Hist2D(*binning)
  sgErrorHist = Hist2D(*binning)
  fwhmHist = Hist2D(*binning)
  minMPV = 1e9
  minWL = 1e9
  minSG = 1e9
  maxMPV = -1e9
  maxWL = -1e9
  maxSG = -1e9
  for iBinX in range(1,xaxis.GetNbins()+1):
    for iBinY in range(1,yaxis.GetNbins()+1):
      postfix = "_"+fileprefix+"bins{}_{}".format(iBinX,iBinY)
      xMin = xaxis.GetBinLowEdge(iBinX)
      xMax = xaxis.GetBinUpEdge(iBinX)
      yMin = yaxis.GetBinLowEdge(iBinY)
      yMax = yaxis.GetBinUpEdge(iBinY)
      caption = "{} in [{},{}), {} in [{},{})".format(xTitle,xMin,xMax,yTitle,yMin,yMax)
      histForFit = Hist(*zBinning)
      histForFit.GetXaxis().SetTitle(zTitle)
      for iBinZ in range(1,zaxis.GetNbins()+1):
        histForFit.SetBinContent(iBinZ,hist.GetBinContent(iBinX,iBinY,iBinZ))
      if histForFit.Integral(1,zaxis.GetNbins()+1) < 10:
        continue
      if dQdx:
        histForFit.Rebin(2)

      startFit = 0.
      endFit = 0.
      startFit, endFit = getFracMaxVals(histForFit,fracMax)
      (mpvl,wl,sg),(mpvlErr,wlErr,sgErr), fwhm = fitLandauCore(c,histForFit,postfix,caption,startFit,endFit,fixedLandauWidth=fixedLandauWidth,dQdx=dQdx)
      if (mpvlErr/mpvl > 0.02 or wlErr/wl > 0.2 or sgErr/sg > 0.2):
            continue
      mpvlHist.SetBinContent(iBinX,iBinY,mpvl)
      wlHist.SetBinContent(iBinX,iBinY,wl)
      sgHist.SetBinContent(iBinX,iBinY,sg)
      fwhmHist.SetBinContent(iBinX,iBinY,fwhm)
      mpvlErrorHist.SetBinContent(iBinX,iBinY,mpvlErr/mpvl)
      wlErrorHist.SetBinContent(iBinX,iBinY,wlErr/wl)
      sgErrorHist.SetBinContent(iBinX,iBinY,sgErr/sg)
      minMPV = min(mpvl,minMPV)
      minWL = min(wl,minWL)
      minSG = min(sg,minSG)
      maxMPV = max(mpvl,maxMPV)
      maxWL = max(wl,maxWL)
      maxSG = max(sg,maxSG)
  if maxMPV > minMPV:
    mpvlHist.GetZaxis().SetRangeUser(minMPV,maxMPV)
  if maxWL > minWL:
    wlHist.GetZaxis().SetRangeUser(minWL,maxWL)
  if maxSG > minSG:
    sgHist.GetZaxis().SetRangeUser(minSG,maxSG)
  graphs = [mpvlHist,wlHist,sgHist,mpvlErrorHist,wlErrorHist,sgErrorHist,fwhmHist]
  labels = ["Best-Fit Landau MPV", "Best-Fit Landau Width", "Best-Fit Gaussian #sigma",
            "Relative Error Landau MPV", "Relative Error Landau Width", "Relative Error Gaussian #sigma",
            "FWHM"]
  names = ["bfMPV", "bfWL", "bfSigma",
            "relerrMPV", "relerrWL", "relerrSigma",
            "FWHM"]
  setupCOLZFrame(c)
  for graph,label,name in zip(graphs,labels,names):
    graph.Draw("colz")
    print xTitle,yTitle
    setHistTitles(graph,xTitle,yTitle)
    drawStandardCaptions(c,label)
    c.SaveAs(fileprefix+name+".png")
    c.SaveAs(fileprefix+name+".pdf")
  setupCOLZFrame(c,True)
  return mpvlHist,wlHist,sgHist

def compareGraphs(c,outfilePrefix,graphsList,histIndex,xTitle,yTitle,legendTitles,yStartZero=False):
  c.Clear()
  for iColor, graphs in enumerate(graphsList):
        graphs[histIndex].SetMarkerColor(COLORLIST[iColor])
        graphs[histIndex].SetLineColor(COLORLIST[iColor])
  axisHist = drawGraphs(c,[x[histIndex] for x in graphsList],xTitle,yTitle,yStartZero=yStartZero,freeTopSpace=0.4)
  leg = drawNormalLegend([x[histIndex] for x in graphsList],legendTitles,option="ep")
  c.SaveAs(outfilePrefix+".png")
  c.SaveAs(outfilePrefix+".pdf")
  c.Clear()


if __name__ == "__main__":

  c = root.TCanvas("c")
  fCosmics = root.TFile("cosmics_hists.root")
  fCosmics.ls()

  hist3D1 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunIINocrct")
  hist3D1 = hist3D1.Clone("hist3D1")
  hist3D1.Rebin3D(20,1,1)
  fitSlicesLandauCore3D(c,hist3D1,"Fit3D_dEdxVWireAndY_phiLt0_RunIINocrct_manyY")

  hist3D2 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunIINocrct")
  hist3D2 = hist3D2.Clone("hist3D2")
  hist3D2.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D2,"Fit3D_dEdxVWireAndY_phiLt0_RunIINocrct_manyWire")

  hist3D3 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiGeq0_RunIINocrct")
  hist3D3 = hist3D3.Clone("hist3D3")
  hist3D3.Rebin3D(20,1,1)
  fitSlicesLandauCore3D(c,hist3D3,"Fit3D_dEdxVWireAndY_phiGeq0_RunIINocrct_manyY")

  hist3D4 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiGeq0_RunIINocrct")
  hist3D4 = hist3D4.Clone("hist3D4")
  hist3D4.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D4,"Fit3D_dEdxVWireAndY_phiGeq0_RunIINocrct_manyWire")

  hist3D5 = fCosmics.Get("primTrkdQdxsVHitWireAndHitY_phiLt0_RunIINocrct")
  hist3D5.Rebin3D(10,2,1)
  fitSlicesLandauCore3D(c,hist3D5,"Fit3D_dQdxVWireAndY_phiLt0_RunIINocrct",dQdx=True)

  hist3D6 = fCosmics.Get("primTrkdQdxsVrunAndHitX_phiLt0_RunIINocrct")
  hist3D6.Rebin3D(10,2,1)
  fitSlicesLandauCore3D(c,hist3D6,"Fit3D_dQdxVrunAndX_phiLt0_RunIINocrct",dQdx=True)

  hist3D7 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunII")
  hist3D7 = hist3D7.Clone("hist3D7")
  hist3D7.Rebin3D(20,1,1)
  fitSlicesLandauCore3D(c,hist3D7,"Fit3D_dEdxVWireAndY_phiLt0_RunII_manyY")

  hist3D8 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunII")
  hist3D8 = hist3D8.Clone("hist3D8")
  hist3D8.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D8,"Fit3D_dEdxVWireAndY_phiLt0_RunII_manyWire")

  hist3D9 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunII")
  hist3D9 = hist3D9.Clone("hist3D9")
  hist3D9.Rebin3D(20,1,1)
  fitSlicesLandauCore3D(c,hist3D9,"Fit3D_dEdxVWireAndY_phiLt0_RunII_manyY")

  hist3D10 = fCosmics.Get("primTrkdEdxsVHitWireAndHitY_phiLt0_RunII")
  hist3D10 = hist3D10.Clone("hist3D10")
  hist3D10.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D10,"Fit3D_dEdxVWireAndY_phiLt0_RunII_manyWire")

  hist3D100 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiLt0_RunIINocrct")
  hist3D100 = hist3D100.Clone("hist3D100")
  hist3D100.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D100,"Fit3D_dEdxVZAndY_phiLt0_RunIINocrct")

  hist3D101 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiLt0_RunII")
  hist3D101 = hist3D101.Clone("hist3D101")
  hist3D101.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D101,"Fit3D_dEdxVZAndY_phiLt0_RunII")

  hist3D102 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiGeq0_RunII")
  hist3D102 = hist3D102.Clone("hist3D102")
  hist3D102.Rebin3D(5,5,1)
  fitSlicesLandauCore3D(c,hist3D102,"Fit3D_dEdxVZAndY_phiGeq0_RunII")

  hist3D103 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiLt0_RunII")
  hist3D103 = hist3D103.Clone("hist3D103")
  hist3D103.Rebin3D(2,10,1)
  fitSlicesLandauCore3D(c,hist3D103,"Fit3D_dEdxVZAndY_phiLt0_RunII_moreZ")

  hist3D104 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiGeq0_RunII")
  hist3D104 = hist3D104.Clone("hist3D104")
  hist3D104.Rebin3D(2,10,1)
  fitSlicesLandauCore3D(c,hist3D104,"Fit3D_dEdxVZAndY_phiGeq0_RunII_moreZ")

  hist3D105 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiLt0_RunII")
  hist3D105 = hist3D105.Clone("hist3D105")
  hist3D105.Rebin3D(10,2,1)
  fitSlicesLandauCore3D(c,hist3D105,"Fit3D_dEdxVZAndY_phiLt0_RunII_moreY")

  hist3D106 = fCosmics.Get("primTrkdEdxsVHitZAndHitY_phiGeq0_RunII")
  hist3D106 = hist3D106.Clone("hist3D106")
  hist3D106.Rebin3D(10,2,1)
  fitSlicesLandauCore3D(c,hist3D106,"Fit3D_dEdxVZAndY_phiGeq0_RunII_moreY")

  sys.exit(0)

  nameLists = []
  paramLists = []
  errorLists = []
  paramGausLists = []
  errorGausLists = []
  fwhmLists = []
  for key in fCosmics.GetListOfKeys():
    name = key.GetName()
    if "primTrkdEdxs_zoom3_phiGeq0" in name:
        hist = key.ReadObj()
        hist.Rebin(2)
        startFit, endFit = getFracMaxVals(hist,0.4)
        #####
        params, errs, fwhm = fitLandauCore(c,hist,name,name,startFit,endFit,fixedLandauWidth=0.12)
        #params, errs, fwhm = fitLandauCore(c,hist,name,name,1.,4.)
        #params, errs, fwhm = fitLandauCore(c,hist,name,name,1.4,2.)
        nameLists.append(name)
        paramLists.append(params)
        errorLists.append(errs)
        fwhmLists.append(fwhm)
        #xMin,xMax = getHistFracMaxVals(hist,0.25)
        #params, errs = fitGaussCore(c,hist,name,name,xMin,xMax)
        #params, errs, fwhm = fitGaussCore(c,hist,name,name,startFit,endFit)
        #paramGausLists.append(params)
        #errorGausLists.append(errs)
    elif "primTrkdEdxs_zoom3_phiLt0" in name:
      pass
    elif "primTrkdEdxs_zoom3" in name:
      pass
    elif "primTrkdQdxs_phiLt0" in name:
      hist = key.ReadObj()
      hist.Print()
      startFit, endFit = getFracMaxVals(hist,0.5)
      params, errs, fwhm = fitLandauCore(c,hist,name,name,startFit,endFit,fixedLandauWidth=180,dQdx=True)
    elif "primTrkdQdxs_phiGeq0" in name:
      hist = key.ReadObj()
      hist.Print()
      startFit, endFit = getFracMaxVals(hist,0.5)
      params, errs, fwhm = fitLandauCore(c,hist,name,name,startFit,endFit,fixedLandauWidth=280,dQdx=True)
    elif "primTrkdQdxs" in name:
      pass
  dataParamsErrs = []
  dataFWHMs = []
  dataLabels = []
  mcSmearingVals = []
  mcParams = []
  mcErrs = []
  fwhmVals = []
  for name, params, errors, fwhm in zip(nameLists,paramLists,errorLists,fwhmLists):
    printStr = "{:55} ".format(name)
    for i in range(len(params)):
        printStr += "{:6.3f} +/- {:8.3g} ".format(params[i],errors[i])
    printStr += "FWHM: {:6.3f} ".format(fwhm)
    print(printStr)
    if "RunII" in name:
        print("name",name)
        dataParamsErrs.append((params,errors))
        dataFWHMs.append(fwhm)
        match = re.search(r"RunIIP([0-9]+)",name)
        if match:
          current = match.group(1)
          dataLabels.append("Run II + {} Data".format(current))
        else:
          dataLabels.append("Run II Data")
    else:
        match = re.match(r".*_presmear(\d+)perc$",name)
        if match:
            mcParams.append(params)
            mcErrs.append(errors)
            fwhmVals.append(fwhm)
            mcSmearingVals.append(float(match.group(1)))
        else:
            mcParams.append(params)
            mcErrs.append(errors)
            fwhmVals.append(fwhm)
            mcSmearingVals.append(0.)

  try:
    import numpy
    from matplotlib import pyplot as mpl

    mcParams = numpy.array(mcParams)
    mcErrs = numpy.array(mcErrs)
    fig, ax = mpl.subplots(figsize=(7,7))
    for dataLabel, dataParamsErr in zip(dataLabels,dataParamsErrs):
      ax.axhspan(dataParamsErr[0][2]-dataParamsErr[1][2],dataParamsErr[0][2]+dataParamsErr[1][2],facecolor='k',edgecolor='k',alpha=0.3)
      ax.axhline(dataParamsErr[0][2],c='k')
    ax.errorbar(mcSmearingVals,mcParams[:,2],yerr=mcErrs[:,2],fmt=".b")
    #ax.set_xlim(-10,50)
    ax.set_xlabel("MC Smearing [%]")
    ax.set_ylabel("Gaussian $\sigma$ Parameter [MeV/cm]")
    for dataLabel, dataParamsErr in zip(dataLabels,dataParamsErrs):
      ax.annotate(dataLabel,(45,dataParamsErr[0][2]+0.5*dataParamsErr[1][2]),ha='right',va='center')
    fig.savefig("Cosmic_Gaus_Widths.png")
    fig.savefig("Cosmic_Gaus_Widths.pdf")

    fig, ax = mpl.subplots(figsize=(7,7))
    for dataLabel, dataParamsErr in zip(dataLabels,dataParamsErrs):
      ax.axhspan(dataParamsErr[0][0]-dataParamsErr[1][0],dataParamsErr[0][0]+dataParamsErr[1][0],facecolor='k',edgecolor='k',alpha=0.3)
      ax.axhline(dataParamsErr[0][0],c='k')
    ax.errorbar(mcSmearingVals,mcParams[:,0],yerr=mcErrs[:,0],fmt=".b")
    #ax.set_xlim(-10,50)
    ax.set_xlabel("MC Smearing [%]")
    ax.set_ylabel("Landau MPV Parameter [MeV/cm]")
    for dataLabel, dataParamsErr in zip(dataLabels,dataParamsErrs):
      ax.annotate(dataLabel,(45,dataParamsErr[0][0]+0.5*dataParamsErr[1][0]),ha='right',va='center')
    fig.savefig("Cosmic_Gaus_MPV.png")
    fig.savefig("Cosmic_Gaus_MPV.pdf")

    fig, ax = mpl.subplots(figsize=(7,7))
    for dataLabel, dataFWHM in zip(dataLabels,dataFWHMs):
      ax.axhline(dataFWHM,c='k',lw=2)
    ax.errorbar(mcSmearingVals,fwhmVals,fmt="ob")
    #ax.set_xlim(-10,50)
    ax.set_xlabel("MC Smearing [%]")
    ax.set_ylabel("Full Width Half Max of Fit PDF [MeV/cm]")
    for dataLabel, dataFWHM in zip(dataLabels,dataFWHMs):
      ax.annotate(dataLabel,(45,dataFWHM),ha='right',va='bottom')
    fig.savefig("Cosmic_FWHM.png")
    fig.savefig("Cosmic_FWHM.pdf")
  except ImportError:
    pass

#  for logy,xmax,outext,ytitle in [(False,4,"","Normalized--Hits"),(True,50,"_logy","Hits/bin")]:
#    c.SetLogy(logy)
#
#    plotSlices(c,fCosmics.Get("primTrkdEdxVwire_RunIIP60"),"SlicesWireRunIIP60_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"wire",rebinX=1,xunits="",normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxVwire_RunIIP100"),"SlicesWireRunIIP100_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"wire",rebinX=1,xunits="",normalize=not logy)
#
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_RunII"),"SlicesXRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_CosmicMC"),"SlicesXCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVy_RunII"),"SlicesYRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"),"SlicesYCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVz_RunII"),"SlicesZRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVz_CosmicMC"),"SlicesZ_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_RunII"),"SlicesYFromCenterRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_CosmicMC"),"SlicesYFromCenterCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_RunII"),"SlicesZFromCenterRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=4,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_CosmicMC"),"SlicesZFromCenter_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|z-45cm|",rebinX=8,xunits="cm",normalize=not logy)
#
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVrun_RunII"),"SlicesRunRunII_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)

  ##############################################

#  c.SetLogy(False)
#  graphConfigs = [
#    (fCosmics.Get("primTrkdEdxsVrun_RunII"),"Slices_modefwhm_run_cosmics","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVx_RunII"),"Slices_modefwhm_x_cosmics","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVy_RunII"),"Slices_modefwhm_y_cosmics","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVz_RunII"),"Slices_modefwhm_z_cosmics","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#  ]
#
#  for hist, savename, xtitle, ytitle, in graphConfigs:
#    graphMode,graphFWHM = makeGraphsModeAndFWHM(hist)
#    axisHist = makeStdAxisHist([graphMode,graphFWHM],ylim=[0,4])
#    axisHist.Draw()
#    graphMode.Draw("P")
#    graphFWHM.Draw("P")
#    graphFWHM.SetMarkerColor(COLORLIST[0])
#    graphFWHM.SetLineColor(COLORLIST[0])
#    setHistTitles(axisHist,xtitle,ytitle)
#    c.SaveAs(savename+".png")
#    c.SaveAs(savename+".pdf")

  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_RunII"))
  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"))

  hist = fCosmics.Get("primTrkdQdxsVrun_RunIINocrct")
  #graphsdQdxRuns = fitSlicesLandauCore(c,hist,"Run_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxRuns = fitSlicesLandauCore(c,hist,"dQdxRun_10_",nJump=10,dQdx=True,fixedLandauWidth=None)

  hist = fCosmics.Get("primTrkdQdxsVrun_phiGeq0_RunIINocrct")
  #graphsdQdxRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"dQdxRun_phiGeq0_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"dQdxRun_phiGeq0_10_",nJump=10,dQdx=True,fixedLandauWidth=None)

  hist = fCosmics.Get("primTrkdQdxsVrun_phiLt0_RunIINocrct")
  #graphsdQdxRuns_phiLt0 = fitSlicesLandauCore(c,hist,"dQdxRun_phiLt0_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxRuns_phiLt0 = fitSlicesLandauCore(c,hist,"dQdxRun_phiLt0_10_",nJump=10,dQdx=True,fixedLandauWidth=None)

  graphsdQdxRunsList = [graphsdQdxRuns,graphsdQdxRuns_phiGeq0,graphsdQdxRuns_phiLt0]
  compareGraphs(c,"ComparedQdxRuns_MPV",graphsdQdxRunsList,0,"Run Number","Landau MPV [ADC ns / cm]",["All","#phi #geq 0","#phi < 0"])
  compareGraphs(c,"ComparedQdxRuns_Sigma",graphsdQdxRunsList,2,"Run Number","Gaussian Sigma [ADC ns / cm]",["All","#phi #geq 0","#phi < 0"])


  hist = fCosmics.Get("primTrkdQdxVwire_RunIINocrct")
  #graphsdQdxWires = fitSlicesLandauCore(c,hist,"dQdxWire_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxWires = fitSlicesLandauCore(c,hist,"dQdxWire_8_",nJump=8,dQdx=True,fixedLandauWidth=None)

  hist = fCosmics.Get("primTrkdQdxVwire_phiGeq0_RunIINocrct")
  #graphsdQdxWires_phiGeq0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiGeq0_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxWires_phiGeq0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiGeq0_8_",nJump=8,dQdx=True,fixedLandauWidth=None)

  hist = fCosmics.Get("primTrkdQdxVwire_phiLt0_RunIINocrct")
  #graphsdQdxWires_phiLt0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiLt0_1_",dQdx=True,fixedLandauWidth=None)
  graphsdQdxWires_phiLt0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiLt0_8_",nJump=8,dQdx=True,fixedLandauWidth=None)

  graphsdQdxWiresList = [graphsdQdxWires,graphsdQdxWires_phiGeq0,graphsdQdxWires_phiLt0]
  compareGraphs(c,"ComparedQdxWires_MPV",graphsdQdxWiresList,0,"Wire Number","Landau MPV [ADC ns / cm]",["All","#phi #geq 0","#phi < 0"])
  compareGraphs(c,"ComparedQdxWires_Sigma",graphsdQdxWiresList,2,"Wire Number","Gaussian Sigma [ADC ns / cm]",["All","#phi #geq 0","#phi < 0"])

  #################################################

  hist = fCosmics.Get("primTrkdEdxsVrun_RunIINocrct")
  #graphsRuns = fitSlicesLandauCore(c,hist,"Run_1_")
  graphsRuns = fitSlicesLandauCore(c,hist,"Run_10_",nJump=10)

  hist = fCosmics.Get("primTrkdEdxsVrun_phiGeq0_RunIINocrct")
  #graphsRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"Run_phiGeq0_1_")
  graphsRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"Run_phiGeq0_10_",nJump=10)

  hist = fCosmics.Get("primTrkdEdxsVrun_phiLt0_RunIINocrct")
  #graphsRuns_phiLt0 = fitSlicesLandauCore(c,hist,"Run_phiLt0_1_")
  graphsRuns_phiLt0 = fitSlicesLandauCore(c,hist,"Run_phiLt0_10_",nJump=10)

  graphsRunsList = [graphsRuns,graphsRuns_phiGeq0,graphsRuns_phiLt0]
  compareGraphs(c,"CompareRuns_MPV",graphsRunsList,0,"Run Number","Landau MPV [MeV/cm]",["All","#phi #geq 0","#phi < 0"])
  compareGraphs(c,"CompareRuns_Sigma",graphsRunsList,2,"Run Number","Gaussian Sigma [MeV/cm]",["All","#phi #geq 0","#phi < 0"])


  hist = fCosmics.Get("primTrkdEdxVwire_RunIINocrct")
  #graphsWires = fitSlicesLandauCore(c,hist,"Wire_1_")
  graphsWires = fitSlicesLandauCore(c,hist,"Wire_8_",nJump=8)

  hist = fCosmics.Get("primTrkdEdxVwire_phiGeq0_RunIINocrct")
  #graphsWires_phiGeq0 = fitSlicesLandauCore(c,hist,"Wire_phiGeq0_1_")
  graphsWires_phiGeq0 = fitSlicesLandauCore(c,hist,"Wire_phiGeq0_8_",nJump=8)

  hist = fCosmics.Get("primTrkdEdxVwire_phiLt0_RunIINocrct")
  #graphsWires_phiLt0 = fitSlicesLandauCore(c,hist,"Wire_phiLt0_1_")
  graphsWires_phiLt0 = fitSlicesLandauCore(c,hist,"Wire_phiLt0_8_",nJump=8)

  graphsWiresList = [graphsWires,graphsWires_phiGeq0,graphsWires_phiLt0]
  compareGraphs(c,"CompareWires_MPV",graphsWiresList,0,"Wire Number","Landau MPV [MeV/cm]",["All","#phi #geq 0","#phi < 0"])
  compareGraphs(c,"CompareWires_Sigma",graphsWiresList,2,"Wire Number","Gaussian Sigma [MeV/cm]",["All","#phi #geq 0","#phi < 0"])

  hist = fCosmics.Get("primTrkdEdxsVx_phiLt0_RunIINocrct")
  graphsX_phiLt0 = fitSlicesLandauCore(c,hist,"X_phiLt0_1_")
  #graphsX_phiLt0 = fitSlicesLandauCore(c,hist,"X_phiLt0_2_",nJump=2)

  hist = fCosmics.Get("primTrkdEdxsVy_phiLt0_RunIINocrct")
  graphsY_phiLt0 = fitSlicesLandauCore(c,hist,"Y_phiLt0_1_")
  #graphsY_phiLt0 = fitSlicesLandauCore(c,hist,"Y_phiLt0_2_",nJump=2)

  hist = fCosmics.Get("primTrkdEdxsVz_phiLt0_RunIINocrct")
  graphsZ_phiLt0 = fitSlicesLandauCore(c,hist,"Z_phiLt0_1_")
  #graphsZ_phiLt0 = fitSlicesLandauCore(c,hist,"Z_phiLt0_5_",nJump=5)

#  hist = fCosmics.Get("primTrkdQdxVwire_RunII")
#  graphsdQdxWires = fitSlicesLandauCore(c,hist,"dQdxWire_8_",nJump=8)
#
#  hist = fCosmics.Get("primTrkdQdxVwire_phiGeq0_RunII")
#  graphsdQdxWires_phiGeq0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiGeq0_8_",nJump=8)
#
#  hist = fCosmics.Get("primTrkdQdxVwire_phiLt0_RunII")
#  graphsdQdxWires_phiLt0 = fitSlicesLandauCore(c,hist,"dQdxWire_phiLt0_8_",nJump=8)
#
#  graphsdQdxWiresList = [graphsdQdxWires,graphsdQdxWires_phiGeq0,graphsdQdxWires_phiLt0]
#  compareGraphs(c,"ComparedQdxWires_MPV",graphsdQdxWiresList,0,"Wire Number","dQ/dx Landau MPV [MeV/cm]",["All","#phi #geq 0","#phi < 0"])
#  compareGraphs(c,"ComparedQdxWires_Sigma",graphsdQdxWiresList,2,"Wire Number","dQ/dx Gaussian Sigma [MeV/cm]",["All","#phi #geq 0","#phi < 0"])
