#!/usr/bin/env python

import random
import sys
import re
import os
import time
import subprocess
import string

class FakeSAM(object):

  def __init__(self,first=8000,last=10227):
    self.data = self.genRandomNFiles(self.genRandomNums(first,last))

  def genRandomNums(self,first,last):
    assert(first < last)
    assert((last - first) > 1000)
    result = set()
    for i in range(20):
      center = random.randint(first+10,last-10)
      available = xrange(center - int(10),center + int(10))
      samples = random.sample(available,10)
      for sample in samples:
        if not (sample in result):
          result.add(sample)
    result = list(result)
    result.sort()
    return result
  
  def genRandomNFiles(self,runList):
    result = []
    for run in runList:
      result.append([run,random.randint(5,500)])
    return result

  def count(self,firstRun,lastRun):
    result = 0
    print "Runs: {} {}".format(firstRun,lastRun)
    for iRun in range(len(self.data)):
        run = self.data[iRun][0]
        if run >= firstRun and run < lastRun:
            nfiles = self.data[iRun][1]
            result += nfiles
    print "nFiles: {}".format(result)
    return result

  def __str__(self):
    result = "FakeSAM\n"
    for datum in self.data:
      result += "Run: {0:6} Files: {1:5}\n".format(*datum)
    return result

class TalkToSAM(object):
  def __init__(self,basedefname,pause_time=120,nTries=5):
    """
    basedefname is the definition name to start from
    pause_time is number of seconds to pause after running a samweb command
    nTries is the number of tries to run a samweb command before raising an exception
    """
    self.basedefname = basedefname
    self.pause_time = pause_time
    self.nTries = nTries

  def call(self,commandlist):
      result = None
      pause_time = self.pause_time
      for iTry in range(self.nTries):
        try:
          result = subprocess.check_output(commandlist)
        except Exception as e:
          print "Error: '{}' running: check_output on {}".format(e,commandlist)
        else: # if no exception
          break
        finally: #always
          time.sleep(pause_time)
          #pause_time *= 2
      return result

  def count(self,firstRun,lastRun,onlyPrint=False):
    command = ["samweb","count-files","'defname: {} and run_number >= {} and run_number < {}'".format(self.basedefname,firstRun,lastRun)]
    print " ".join(command)
    result = None
    if not onlyPrint:
      result = self.call(command)
      if result is None:
          raise Exception("Couldn't count files")
      result = int(result)
    print "nFiles: {}".format(result)
    return result

  def createDefinition(self,sub_name,firstRun,lastRun,prefix="",suffix="_v1",onlyPrint=False,stripVersion=False):
    match = re.match(r"(.+)_v\d+",self.basedefname)
    new_basedefname = self.basedefname
    if match:
        new_basedefname = match.group(1)
    newname = "{}{}_{}{}".format(prefix,new_basedefname,sub_name,suffix)
    command = ["samweb","create-definition",newname,"'defname: {} and run_number >= {} and run_number < {}'".format(self.basedefname,firstRun,lastRun)]
    print " ".join(command)
    if not onlyPrint:
      call_result = self.call(command)
      if call_result is None:
          raise Exception("Couldn't create definition")

class MakeSubDatasets(object):
  def __init__(self,first,last,nFilesPerSet=5000,nFilesPerSetError=100):
    assert(first < last)
    self.firstRuns = []
    self.lastRuns = []
    self.nFiles = []
    self.first = first
    self.last = last
    self.nFilesPerSet = nFilesPerSet
    self.nFilesPerSetError = nFilesPerSetError

  def __str__(self):
    result = "MakeSubDatasets(first={},last={},nFilesPerSet={},nFilesPerSetError={})\n".format(self.first,self.last,self.nFilesPerSet,self.nFilesPerSetError)
    for f,l,n in zip(self.firstRuns,self.lastRuns,self.nFiles):
        runsStr = "{}-{}".format(f,l)
        result += "  Runs {:12}: {:5} files\n".format(runsStr,n)
    return result

  def run(self,countFunc):
    totalCount = countFunc(self.first,self.last)
    if totalCount == 0:
      raise Exception("No files found between:",self.first,self.last)
    while True:
      firstRun = self.first
      if len(self.lastRuns) > 0:
        firstRun = self.lastRuns[-1]
      if firstRun == self.last:
        break
      print "\nWorking on dataset starting at {}".format(firstRun)
      allcount = countFunc(firstRun,self.last)
      if allcount <= (self.nFilesPerSet - self.nFilesPerSetError):
        self.firstRuns.append(firstRun)
        self.lastRuns.append(self.last)
        self.nFiles.append(allcount)
        break
      thislast, thiscount = self.binomial(countFunc,firstRun,firstRun,self.last)
      assert(countFunc(firstRun,thislast) == thiscount)
      if thiscount == 0:
        break
      self.firstRuns.append(firstRun)
      self.lastRuns.append(thislast)
      self.nFiles.append(thiscount)
    setsTotalCount = 0
    for n in self.nFiles:
        setsTotalCount += n
    assert(setsTotalCount == totalCount)

  def binomial(self,countFunc,firstRun,lastmin,lastmax):
    lastmid = int(0.5*(lastmin + lastmax))
    count = countFunc(firstRun,lastmid)
    difference = count - self.nFilesPerSet
    #print "binomial: firstRun: {} lastmin: {} lastmid {} lastmax {} countmid {}".format(firstRun,lastmin,lastmid,lastmax,count)
    if abs(difference) <= self.nFilesPerSetError:
        return lastmid, count
    elif lastmax == lastmin: # give up, step is too big
        return lastmax, count
    elif difference > 0:
        return self.binomial(countFunc,firstRun,lastmin,lastmid-1)
    else:
        return self.binomial(countFunc,firstRun,lastmid,lastmax+1)

  def printDefinitions(self,tts):
    print ""
    print "New Definitions:"
    for f,l,n,a in zip(self.firstRuns,self.lastRuns,self.nFiles,string.ascii_lowercase[:len(self.firstRuns)]):
      tts.createDefinition(a,f,l,onlyPrint=True)

if __name__ == "__main__":

  sam = TalkToSAM("Lovely1_Neg_RunII_jhugon_current20_secondary64_v1",pause_time=5,nTries=2)
  sam.count(8000,9000)
  sam.createDefinition("test1",8000,9000)

  #fakesam = FakeSAM()

#  msd = MakeSubDatasets(8000,10227)
#  msd.run(sam.count)
#  #msd.run(fakesam.count)
#  print msd
#  msd.printDefinitions(sam)
