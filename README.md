LArIAT Pion Absorption Analysis
===============================

This repository holds code for the LArIAT pion absorption analysis. The code
here processes the anaTree files produced by LArIATSoft.

The .C parts of the code are meant to create tree friends for the main anaTrees
with higher-level variables. the .py parts of the code use tree.Draw() to
create histograms and paint them to image files

Setting up LariatSoft Code on Fermilab lariatgpvm
-------------------------------------------------

Create a directory where you want your work to be e.g.

```
mkdir -p /lariat/app/users/$USER/lariatsoft_v06_34_01_pionAbs
cd /lariat/app/users/$USER/lariatsoft_v06_34_01_pionAbs
```

Then create a new lariatsoft area 
([more instructions here](https://redmine.fnal.gov/redmine/projects/lardbt/wiki/Setting_up_the_Offline_Software_CVMFS))

```
source /cvmfs/lariat.opensciencegrid.org/setup_lariat.sh
setup ninja v1_7_2
version=v06_34_01
qual=e14:debug
setup larsoft $version -q $qual
mrb newDev
source localProducts*/setup
cd srcs
```
  
Now we need to get the necessary larsoft packages. Make sure you are in the
srcs dir of your area and run:

```
git clone http://cdcvs.fnal.gov/projects/lariatsoft
git clone http://cdcvs.fnal.gov/projects/larana
git clone http://cdcvs.fnal.gov/projects/larreco
git clone http://cdcvs.fnal.gov/projects/lardataobj
cd lariatsoft
git checkout feature/jhugon_PionAbsAndChEx
cd ..
cd larana
git checkout feature/jhugon_likelihoodPID
cd ..
cd larreco
git checkout feature/jhugon_caloTruth
cd ..
cd lardataobj
git checkout feature/jhugon_caloTruth
cd ..
mrb uc # updates the build dependencies to use the packages you just got
```

**IF YOU ARE A DEVELPER OF LARIATSOFT AND LARSOFT**, then you can clone these instead:

```
git clone ssh://p-lariatsoft@cdcvs.fnal.gov/cvs/projects/lariatsoft
git clone ssh://p-larana@cdcvs.fnal.gov/cvs/projects/larana
git clone ssh://p-larreco@cdcvs.fnal.gov/cvs/projects/larreco
git clone ssh://p-lardataobj@cdcvs.fnal.gov/cvs/projects/lardataobj
```

Now we need to compile everything

```
mrbsetenv
nice mrb i --generator ninja -j8
```

Finally, create a script setup.sh with this in in e.g.
`/lariat/app/users/$USER/lariatsoft_v06_34_01_pionAbs`:

```
source /cvmfs/lariat.opensciencegrid.org/setup_lariat.sh
setup ninja v1_7_2
version=v06_34_01
qual=e14:debug
setup larsoft $version -q $qual
source localProducts*/setup
mrbsetenv
setup lariatsoft $version -q $qual
setup lariatsoft $version -q $qual
```

Running source setup.sh will setup your environment on a new login.

Setting up LariatSoft Code on p04
---------------------------------

Create a directory where you want your work to be and cd in it.

Then create a new lariatsoft area 

```
source /hepsoft/LAr/setup
setup mrb
setup git
setup gitflow
setup ninja v1_7_2
export MRB_PROJECT=larsoft
export PROJECT=lariat
version=v06_34_01
qual=e14:debug
setup larsoft $version -q $qual
mrb newDev
source localProducts*/setup
cd srcs
```
  
Now we need to get the necessary larsoft packages. Make sure you are in the
srcs dir of your area and run:

```
git clone http://cdcvs.fnal.gov/projects/lariatsoft
git clone http://cdcvs.fnal.gov/projects/larana
git clone http://cdcvs.fnal.gov/projects/larreco
git clone http://cdcvs.fnal.gov/projects/lardataobj
git clone http://cdcvs.fnal.gov/projects/lariat-online-lariatfragments lariatfragments
git clone http://cdcvs.fnal.gov/projects/lardbt-lariatutil lariatutil
cd lariatsoft
git checkout feature/jhugon_PionAbsAndChEx
cd ..
cd larana
git checkout feature/jhugon_likelihoodPID
cd ..
cd larreco
git checkout feature/jhugon_caloTruth
cd ..
cd lardataobj
git checkout feature/jhugon_caloTruth
cd ..
cd lariatfragments
git checkout v06_32_00
cd ..
cd lariatutil
git checkout v06_34_01
cd ..
mrb uc # updates the build dependencies to use the packages you just got
```

Now we need to compile everything

```
mrbsetenv
nice mrb i --generator ninja -j8
```

Finally, create a script setup.sh with this in it the top level directory of
your project:

```
source /hepsoft/LAr/setup
setup mrb
setup git
setup gitflow
setup ninja v1_7_2
export MRB_PROJECT=larsoft
export PROJECT=lariat
version=v06_34_01
qual=e14:debug
setup larsoft $version -q $qual
source localProducts*/setup
mrbsetenv
setup lariatsoft $version -q $qual
setup lariatsoft $version -q $qual
```

Running source setup.sh will setup your environment on a new login.

Updating lariatsoft to latest git version
-----------------------------------------

These are the steps to update your code to the version of
feature/jhugon_PionAbsAndChEx that is on the git server.

First, you should have your larsoft environment setup, because it loads a newer
version of git. Then, go into your lariatsoft directory.

I recommend you commit whatever you have been working on. You can use `git
status` and `git diff` to see what changes you have made from the last commit
you made (or got from the server). You can use `git add <filename>` to track
new files with git. When you are happy with the changes you've made, run `git
commit -a` to commit all changes.

Run `git fetch` to have your local git repository load information about the
git server repository. This doesn't change any files.

Finally, run `git merge origin/feature/jhugon_PionAbsAndChEx`. This merges any
changes on the server (by convention called "origin") version of
feature/jhugon_PionAbsAndChEx into your local working copy. If it is a trivial
merge, just adding new commits on top of what you have, then the command will
talk about a "fast-forward". Otherwise, git tries to merge things
automatically. If there are problems with the automatic merging, then you will
get an error about "conflicts". `git status` will tell you which files have
conflicts and you can try to fix them manually. You can run `git merge --abort`
to give up on the merge process if you have problems.

Tree Info
---------

trueEndProcess type numbers:

```
0 primary // created via particle gun or something
1 pi-Inelastic
2 neutronInelastic
3 hadElastic
4 nCapture
5 CHIPSNuclearCaptureAtRest
6 Decay
7 KaonZeroLInelastic
8 CoulombScat
9 muMinusCaptureAtRest
10 protonInelastic
11 kaon+Inelastic
12 hBertiniCaptureAtRest
13 pi+Inelastic
14 LArVoxelReadoutScoringProcess // just ionizes
15 CoupledTransportation // exits world
16 annihil // positron
```

in the file it is usually "anatree/anatree" and the branches are:

```
******************************************************************************
*Br    0 :isMC      : isMC/O                                                 *
*Br    1 :runNumber : runNumber/i                                            *
*Br    2 :subRunNumber : subRunNumber/i                                      *
*Br    3 :eventNumber : eventNumber/i                                        *
*Br    4 :nWCTracks : nWCTracks/i                                            *
*Br    5 :xWC       : xWC/F                                                  *
*Br    6 :yWC       : yWC/F                                                  *
*Br    7 :thetaWC   : thetaWC/F                                              *
*Br    8 :phiWC     : phiWC/F                                                *
*Br    9 :pzWC      : pzWC/F                                                 *
*Br   10 :pWC       : pWC/F                                                  *
*Br   11 :eWC       : eWC/F                                                  *
*Br   12 :kinWC     : kinWC/F                                                *
*Br   13 :kinWCInTPC : kinWCInTPC/F                                          *
*Br   14 :yKinkWC   : yKinkWC/F                                              *
*Br   15 :nHitsWC   : nHitsWC/i                                              *
*Br   16 :xWC4Hit   : xWC4Hit/F                                              *
*Br   17 :yWC4Hit   : yWC4Hit/F                                              *
*Br   18 :zWC4Hit   : zWC4Hit/F                                              *
*Br   19 :nTOFs     : nTOFs/i                                                *
*Br   20 :TOFs      : TOFs[nTOFs]/F                                          *
*Br   21 :TOFTimeStamps : TOFTimeStamps[nTOFs]/i                             *
*Br   22 :firstTOF  : firstTOF/F                                             *
*Br   23 :trueEndProcess : trueEndProcess/I                                  *
*Br   24 :trueNDaughters : trueNDaughters/i                                  *
*Br   25 :trueNSecondaryChPions : trueNSecondaryChPions/i                    *
*Br   26 :trueNSecondaryPiZeros : trueNSecondaryPiZeros/i                    *
*Br   27 :trueNSecondaryProtons : trueNSecondaryProtons/i                    *
*Br   28 :trueStartX : trueStartX/F                                          *
*Br   29 :trueStartY : trueStartY/F                                          *
*Br   30 :trueStartZ : trueStartZ/F                                          *
*Br   31 :trueEndX  : trueEndX/F                                             *
*Br   32 :trueEndY  : trueEndY/F                                             *
*Br   33 :trueEndZ  : trueEndZ/F                                             *
*Br   34 :trueStartTheta : trueStartTheta/F                                  *
*Br   35 :trueStartPhi : trueStartPhi/F                                      *
*Br   36 :trueStartMom : trueStartMom/F                                      *
*Br   37 :trueStartE : trueStartE/F                                          *
*Br   38 :trueStartKin : trueStartKin/F                                      *
*Br   39 :trueEndMom : trueEndMom/F                                          *
*Br   40 :trueEndE  : trueEndE/F                                             *
*Br   41 :trueEndKin : trueEndKin/F                                          *
*Br   42 :trueSecondToEndMom : trueSecondToEndMom/F                          *
*Br   43 :trueSecondToEndE : trueSecondToEndE/F                              *
*Br   44 :trueSecondToEndKin : trueSecondToEndKin/F                          *
*Br   45 :trueXFrontTPC : trueXFrontTPC/F                                    *
*Br   46 :trueYFrontTPC : trueYFrontTPC/F                                    *
*Br   47 :nTracks   : nTracks/i                                              *
*Br   48 :nTracksInFirstZ : nTracksInFirstZ[95]/i                            *
*Br   49 :nTracksLengthLt : nTracksLengthLt[20]/i                            *
*Br   50 :trackStartX : trackStartX[nTracks]/F                               *
*Br   51 :trackStartY : trackStartY[nTracks]/F                               *
*Br   52 :trackStartZ : trackStartZ[nTracks]/F                               *
*Br   53 :trackStartTheta : trackStartTheta[nTracks]/F                       *
*Br   54 :trackStartPhi : trackStartPhi[nTracks]/F                           *
*Br   55 :trackEndX : trackEndX[nTracks]/F                                   *
*Br   56 :trackEndY : trackEndY[nTracks]/F                                   *
*Br   57 :trackEndZ : trackEndZ[nTracks]/F                                   *
*Br   58 :trackLength : trackLength[nTracks]/F                               *
*Br   59 :trackXFront : trackXFront[nTracks]/F                               *
*Br   60 :trackYFront : trackYFront[nTracks]/F                               *
*Br   61 :trackCaloKin : trackCaloKin[nTracks]/F                             *
*Br   62 :trackLLHPion : trackLLHPion[nTracks]/F                             *
*Br   63 :trackLLHProton : trackLLHProton[nTracks]/F                         *
*Br   64 :trackLLHMuon : trackLLHMuon[nTracks]/F                             *
*Br   65 :trackLLHKaon : trackLLHKaon[nTracks]/F                             *
*Br   66 :trackPIDA : trackPIDA[nTracks]/F                                   *
*Br   67 :trackStartDistToPrimTrkEnd : trackStartDistToPrimTrkEnd[nTracks]/F *
*Br   68 :trackEndDistToPrimTrkEnd : trackEndDistToPrimTrkEnd[nTracks]/F     *
*Br   69 :iBestMatch : iBestMatch/I                                          *
*Br   70 :trackMatchDeltaX : trackMatchDeltaX[nTracks]/F                     *
*Br   71 :trackMatchDeltaY : trackMatchDeltaY[nTracks]/F                     *
*Br   72 :trackMatchDeltaR : trackMatchDeltaR[nTracks]/F                     *
*Br   73 :trackMatchDeltaAngle : trackMatchDeltaAngle[nTracks]/F             *
*Br   74 :trackMatchLowestZ : trackMatchLowestZ[nTracks]/F                   *
*Br   75 :nMatchedTracks : nMatchedTracks/i                                  *
*Br   76 :primTrkStartMomTrking : primTrkStartMomTrking/F                    *
*Br   77 :primTrkStartTheta : primTrkStartTheta/F                            *
*Br   78 :primTrkStartPhi : primTrkStartPhi/F                                *
*Br   79 :primTrkLength : primTrkLength/F                                    *
*Br   80 :primTrkStartX : primTrkStartX/F                                    *
*Br   81 :primTrkStartY : primTrkStartY/F                                    *
*Br   82 :primTrkStartZ : primTrkStartZ/F                                    *
*Br   83 :primTrkEndX : primTrkEndX/F                                        *
*Br   84 :primTrkEndY : primTrkEndY/F                                        *
*Br   85 :primTrkEndZ : primTrkEndZ/F                                        *
*Br   86 :primTrkEndInFid : primTrkEndInFid/O                                *
*Br   87 :primTrkCaloKin : primTrkCaloKin/F                                  *
*Br   88 :primTrkEndKin : primTrkEndKin/F                                    *
*Br   89 :primTrkEndKinFid : primTrkEndKinFid/F                              *
*Br   90 :primTrkKinInteract : primTrkKinInteract/F                          *
*Br   91 :primTrkLLHPion : primTrkLLHPion/F                                  *
*Br   92 :primTrkLLHProton : primTrkLLHProton/F                              *
*Br   93 :primTrkLLHMuon : primTrkLLHMuon/F                                  *
*Br   94 :primTrkLLHKaon : primTrkLLHKaon/F                                  *
*Br   95 :primTrkPIDA : primTrkPIDA/F                                        *
*Br   96 :primTrkdEdxs : vector<float>                                       *
*Br   97 :primTrkResRanges : vector<float>                                   *
*Br   98 :primTrkKins : vector<float>                                        *
*Br   99 :primTrkInFids : vector<bool>                                       *
```
