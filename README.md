LArIAT Pion Absorption Analysis
===============================

This repository holds code for the LArIAT pion absorption analysis. The code
here processes the anaTree files produced by LArIATSoft.

The .C parts of the code are meant to create tree friends for the main anaTrees
with higher-level variables. the .py parts of the code use tree.Draw() to
create histograms and paint them to image files

Setting up LariatSoft Code on Fermilab lariatgpvm or p0X Machines
-----------------------------------------------------------------

Create a directory where you want your work to be e.g.

```
mkdir -p /lariat/app/users/$USER/lariatsoft_v06_47_01_pionAbs_CNN
cd /lariat/app/users/$USER/lariatsoft_v06_47_01_pionAbs_CNN
```

Then create a new lariatsoft area 
([more instructions here](https://redmine.fnal.gov/redmine/projects/lardbt/wiki/Setting_up_the_Offline_Software_CVMFS))

```
source /cvmfs/lariat.opensciencegrid.org/setup_lariat.sh
setup ninja v1_7_2
version=v06_47_01
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
git checkout feature/jhugon_PionAbsAndChEx_CNN
cd ..
cd larana
git checkout feature/jhugon_likelihoodPID_forlarsoftv06_47_01
cd ..
cd larreco
git checkout feature/jhugon_caloTruth_forlarsoftv06_47_01
cd ..
cd lardataobj
git checkout feature/jhugon_caloTruth_forlarsoftv06_47_01
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
`/lariat/app/users/$USER/lariatsoft_v06_47_01_pionAbs`:

```
source /cvmfs/lariat.opensciencegrid.org/setup_lariat.sh
setup ninja v1_7_2
version=v06_47_01
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

