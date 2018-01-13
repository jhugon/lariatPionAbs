#!/usr/bin/env python

import random
import sys
import os
import time
import subprocess

class FakeSAM(object):

  def __init__(self,first=8000,last=10000):
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
    for iRun in range(len(self.data)):
        run = self.data[iRun][0]
        if run >= firstRun and run < lastRun:
            nfiles = self.data[iRun][1]
            result += nfiles
    return result

  def __str__(self):
    result = "FakeSAM\n"
    for datum in self.data:
      result += "Run: {0:6} Files: {1:5}\n".format(*datum)
    return result

class TalkToSAM(object):
  def __init__(self,basedefname,pause_time=0):
    self.basedefname = basedefname
    self.pause_time = pause_time

  def count(self,firstRun,lastRun):
    command = ["samweb","count-files","'defname: {} and run_number >= {} and run_number < {}'".format(self.basedefname,firstRun,lastRun)]
    print " ".join(command)
    result = subprocess.check_output(command)
    result = int(result)
    time.sleep(self.pause_time)
    return result

  def createDefinition(self,sub_name,firstRun,lastRun,prefix="",suffix="_v1"):
    newname = "{}{}_{}{}".format(prefix,self.basedefname,sub_name,suffix)
    command = ["samweb","create-definition",newname,"'defname: {} and run_number >= {} and run_number < {}'".format(self.basedefname,firstRun,lastRun)]
    print " ".join(command)
    time.sleep(self.pause_time)

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

if __name__ == "__main__":
  sam = FakeSAM()
  msd = MakeSubDatasets(8000,10000)
  msd.run(sam.count)
  print msd
  
  tts = TalkToSAM("aslhglkhasdg_v1",pause_time=0)
  tts.count(1000,2000)
  tts.createDefinition("yay",1000,2000)
