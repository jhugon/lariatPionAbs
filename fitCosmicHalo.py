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

def fitLandaus(c,hist):

  t = root.RooRealVar("t","dE/dx [MeV/cm]",0.,10)
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  ##############
  mpvl = root.RooRealVar("mpvl","mpv landau",1.7,0,5)
  wl = root.RooRealVar("wl","width landau",0.42,0.01,10)
  ml = root.RooFormulaVar("ml","first landau param","@0+0.22278*@1",root.RooArgList(mpvl,wl))
  landau = root.RooLandau("lx","lx",t,ml,wl)

  mg = root.RooRealVar("mg","mg",0)
  sg = root.RooRealVar("sg","sg",0.1,0.01,2.)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  t.setBins(10000,"cache")
  langaus = root.RooFFTConvPdf("langaus","landau (X) gauss",t,landau,gauss)
  langaus.setBufferFraction(0.2)

  mpvl2 = root.RooRealVar("mpvl2","mpv landau",1.7,0,5)
  wl2 = root.RooRealVar("wl2","width landau",0.42,0.01,10)
  ml2 = root.RooFormulaVar("ml2","first landau param","@0+0.22278*@1",root.RooArgList(mpvl2,wl2))
  landau2 = root.RooLandau("lx2","lx2",t,ml2,wl2)
  langaus2 = root.RooFFTConvPdf("langaus2","landau (X) gauss",t,landau2,gauss)
  langaus2.setBufferFraction(0.2)
  
  mpvl3 = root.RooRealVar("mpvl3","mpv landau",1.7,0,5)
  wl3 = root.RooRealVar("wl3","width landau",0.42,0.01,10)
  ml3 = root.RooFormulaVar("ml3","first landau param","@0+0.22278*@1",root.RooArgList(mpvl3,wl3))
  landau3 = root.RooLandau("lx3","lx3",t,ml3,wl3)
  langaus3 = root.RooFFTConvPdf("langaus3","landau (X) gauss",t,landau3,gauss)
  langaus3.setBufferFraction(0.2)
  
  ratio = root.RooRealVar("ratio","ratio",0.18,0,1)
  ratio2 = root.RooRealVar("ratio2","ratio2",0.18,0,1)
  twolandaus = root.RooAddPdf("twolandaus","twolandaus",landau,landau2,ratio)
  threelandaus = root.RooAddPdf("threelandaus","threelandaus",root.RooArgList(landau,landau2,landau3),root.RooArgList(ratio,ratio2))
  twolangaus = root.RooAddPdf("twolangaus","twolandaus",langaus,langaus2,ratio)
  threelangaus = root.RooAddPdf("threelangaus","threelandaus",root.RooArgList(langaus,langaus2,langaus3),root.RooArgList(ratio,ratio2))


  model = threelandaus

  ##############

  model.fitTo(data)

  frame = t.frame(root.RooFit.Title("landau (x) gauss convolution"))
  data.plotOn(frame)
  model.plotOn(frame)

  model.plotOn(frame,root.RooFit.Components("lx"),root.RooFit.LineStyle(root.kDashed))
  model.plotOn(frame,root.RooFit.Components("lx2"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))
  model.plotOn(frame,root.RooFit.Components("lx3"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kGreen))

  #model.plotOn(frame,root.RooFit.Components("langaus"),root.RooFit.LineStyle(root.kDashed))
  #model.plotOn(frame,root.RooFit.Components("langaus2"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kRed))
  #model.plotOn(frame,root.RooFit.Components("langaus3"),root.RooFit.LineStyle(root.kDashed),root.RooFit.LineColor(root.kGreen))

  #root.gPad.SetLeftMargin(0.15)
  #frame.GetYaxis().SetTitleOffset(1.4)
  #frame.Draw("same")
  #axisHist = root.TH2F("axisHist","",1,0,50,1,0,1000)
  ##axisHist = root.TH2F("axisHist","",1,-1,1,1,1000,1300)
  #axisHist.Draw()
  #frame.Draw("same")
  frame.Draw()
  c.SaveAs("roofit.pdf")

def fitSlicesLandaus(c,hist):
  histAll = hist.ProjectionY("_pyAll",1,hist.GetNbinsX())
  fitLandaus(c,histAll)

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

def fitLandauCore(c,hist,postfix,caption,fitMin=1.6,fitMax=2.3,fixedLandauWidth=None):

  xMin = hist.GetXaxis().GetBinLowEdge(1)
  xMax = hist.GetXaxis().GetBinUpEdge(hist.GetNbinsX())
  xMax = min(xMax,5.)
  t = root.RooRealVar("t","dE/dx [MeV/cm]",xMin,xMax)
  observables = root.RooArgSet(t)

  data = root.RooDataHist("data_"+hist.GetName(),"Data Hist",root.RooArgList(t),hist)

  ##############
  mpvl = root.RooRealVar("mpvl","mpv landau",1.7,0,5)
  wl = None
  if fixedLandauWidth is None:
    wl = root.RooRealVar("wl","width landau",0.42,0.01,10)
  else:
    wl = root.RooRealVar("wl","width landau",fixedLandauWidth)
  ml = root.RooFormulaVar("ml","first landau param","@0+0.22278*@1",root.RooArgList(mpvl,wl))
  landau = root.RooLandau("lx","lx",t,ml,wl)

  mg = root.RooRealVar("mg","mg",0)
  sg = root.RooRealVar("sg","sg",0.1,0.01,2.)
  gauss = root.RooGaussian("gauss","gauss",t,mg,sg)

  t.setBins(10000,"cache")
  langaus = root.RooFFTConvPdf("langaus","landau (X) gauss",t,landau,gauss)
  langaus.setBufferFraction(0.4)

  model = langaus

  ##############

  fitResult = model.fitTo(data,root.RooFit.Save(),root.RooFit.Range(fitMin,fitMax))

  fwhm = calcFWHM(model,t,1.,4.,0.01)

  frame = t.frame(root.RooFit.Title("landau (x) gauss convolution"))
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
  c.SaveAs("roofit_landau_{}.png".format(postfix))
  c.SaveAs("roofit_landau_{}.pdf".format(postfix))

  return (mpvl.getVal(),wl.getVal(),sg.getVal()), (mpvl.getError(),wl.getError(),sg.getError()), fwhm

def fitSlicesLandauCore(c,hist,fileprefix,nJump=1):
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
      startFit, endFit = getFracMaxVals(histAll,0.4)
      (mpvl,wl,sg),(mpvlErr,wlErr,sgErr), fwhm = fitLandauCore(c,histAll,postfix,caption,startFit,endFit,fixedLandauWidth=0.12)
      if mpvlErr > 0.5 or wlErr > 0.5 or sgErr > 0.5:
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

if __name__ == "__main__":

  c = root.TCanvas("c")
  fCosmics = root.TFile("cosmics_hists.root")
  fCosmics.ls()
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
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"SlicesXRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVx_CosmicMC"),"SlicesXCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"x",rebinX=5,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"SlicesYRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"),"SlicesYCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"y",rebinX=10,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"SlicesZRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVz_CosmicMC"),"SlicesZ_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=10,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_RunIIPos"),"SlicesYFromCenterRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVyFromCenter_CosmicMC"),"SlicesYFromCenterCosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|y|",rebinX=8,xunits="cm",normalize=not logy)

    #plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_RunIIPos"),"SlicesZFromCenterRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"z",rebinX=4,xunits="cm",normalize=not logy)
    #plotSlices(c,fCosmics.Get("primTrkdEdxsVzFromCenter_CosmicMC"),"SlicesZFromCenter_CosmicMC"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"|z-45cm|",rebinX=8,xunits="cm",normalize=not logy)
#
#    plotSlices(c,fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"SlicesRunRunIIPos_Cosmics"+outext,[0,xmax],"dE/dx [MeV/cm]",ytitle,"Run",rebinX=2,normalize=not logy)

  ##############################################

#  c.SetLogy(False)
#  graphConfigs = [
#    (fCosmics.Get("primTrkdEdxsVrun_RunIIPos"),"Slices_modefwhm_run_cosmics","Run Number","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVx_RunIIPos"),"Slices_modefwhm_x_cosmics","Hit x [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVy_RunIIPos"),"Slices_modefwhm_y_cosmics","Hit y [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
#    (fCosmics.Get("primTrkdEdxsVz_RunIIPos"),"Slices_modefwhm_z_cosmics","Hit z [cm]","Mode & FWHM of dE/dx [MeV/cm]"),
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

  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_RunIIPos"))
  #fitSlicesLandaus(c,fCosmics.Get("primTrkdEdxsVy_CosmicMC"))

  hist = fCosmics.Get("primTrkdEdxsVrun_RunIIPos")
  #graphsRuns = fitSlicesLandauCore(c,hist,"Run_1_")
  graphsRuns = fitSlicesLandauCore(c,hist,"Run_10_",nJump=10)

  hist = fCosmics.Get("primTrkdEdxsVrun_phiGeq0_RunIIPos")
  #graphsRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"Run_phiGeq0_1_")
  graphsRuns_phiGeq0 = fitSlicesLandauCore(c,hist,"Run_phiGeq0_10_",nJump=10)

  hist = fCosmics.Get("primTrkdEdxsVrun_phiLt0_RunIIPos")
  #graphsRuns_phiLt0 = fitSlicesLandauCore(c,hist,"Run_phiLt0_1_")
  graphsRuns_phiLt0 = fitSlicesLandauCore(c,hist,"Run_phiLt0_10_",nJump=10)

  graphsRunsList = [graphsRuns,graphsRuns_phiGeq0,graphsRuns_phiLt0]

  hist = fCosmics.Get("primTrkdEdxVwire_RunIIPos")
  #graphsWires = fitSlicesLandauCore(c,hist,"Wire_1_")
  graphsWires = fitSlicesLandauCore(c,hist,"Wire_16_",nJump=8)

  hist = fCosmics.Get("primTrkdEdxVwire_phiGeq0_RunIIPos")
  #graphsWires_phiGeq0 = fitSlicesLandauCore(c,hist,"Wire_phiGeq0_1_")
  graphsWires_phiGeq0 = fitSlicesLandauCore(c,hist,"Wire_phiGeq0_16_",nJump=8)

  hist = fCosmics.Get("primTrkdEdxVwire_phiLt0_RunIIPos")
  #graphsWires_phiLt0 = fitSlicesLandauCore(c,hist,"Wire_phiLt0_1_")
  graphsWires_phiLt0 = fitSlicesLandauCore(c,hist,"Wire_phiLt0_16_",nJump=8)

  graphsWiresList = [graphsWires,graphsWires_phiGeq0,graphsWires_phiLt0]

  hist = fCosmics.Get("primTrkdEdxsVx_phiLt0_RunIIPos")
  graphsX_phiLt0 = fitSlicesLandauCore(c,hist,"X_phiLt0_1_")
  #graphsX_phiLt0 = fitSlicesLandauCore(c,hist,"X_phiLt0_2_",nJump=2)

  hist = fCosmics.Get("primTrkdEdxsVy_phiLt0_RunIIPos")
  graphsY_phiLt0 = fitSlicesLandauCore(c,hist,"Y_phiLt0_1_")
  #graphsY_phiLt0 = fitSlicesLandauCore(c,hist,"Y_phiLt0_2_",nJump=2)

  hist = fCosmics.Get("primTrkdEdxsVz_phiLt0_RunIIPos")
  graphsZ_phiLt0 = fitSlicesLandauCore(c,hist,"Z_phiLt0_1_")
  #graphsZ_phiLt0 = fitSlicesLandauCore(c,hist,"Z_phiLt0_5_",nJump=5)

  c.Clear()

  for graphsList in [graphsRunsList,graphsWiresList]:
    for iColor, graphs in enumerate(graphsList):
      for graph in graphs:
          graph.SetMarkerColor(COLORLIST[iColor])
          graph.SetLineColor(COLORLIST[iColor])
  
  axisHist = drawGraphs(c,[x[0] for x in graphsRunsList],"Run Number","Landau MPV [MeV/cm]",yStartZero=False)
  leg = drawNormalLegend([x[0] for x in graphsRunsList],["All","#phi #geq 0","#phi < 0"],option="ep")
  c.SaveAs("CompareRuns_MPV.png")
  c.SaveAs("CompareRuns_MPV.pdf")

  axisHist = drawGraphs(c,[x[2] for x in graphsRunsList],"Run Number","Gaussian Sigma [MeV/cm]",yStartZero=False)
  leg = drawNormalLegend([x[2] for x in graphsRunsList],["All","#phi #geq 0","#phi < 0"],option="ep")
  c.SaveAs("CompareRuns_Sigma.png")
  c.SaveAs("CompareRuns_Sigma.pdf")

  axisHist = drawGraphs(c,[x[0] for x in graphsWiresList],"Wire Number","Landau MPV [MeV/cm]",yStartZero=False)
  leg = drawNormalLegend([x[0] for x in graphsWiresList],["All","#phi #geq 0","#phi < 0"],option="ep")
  c.SaveAs("CompareWires_MPV.png")
  c.SaveAs("CompareWires_MPV.pdf")

  axisHist = drawGraphs(c,[x[2] for x in graphsWiresList],"Wire Number","Gaussian Sigma [MeV/cm]",yStartZero=False)
  leg = drawNormalLegend([x[2] for x in graphsWiresList],["All","#phi #geq 0","#phi < 0"],option="ep")
  c.SaveAs("CompareWires_Sigma.png")
  c.SaveAs("CompareWires_Sigma.pdf")
