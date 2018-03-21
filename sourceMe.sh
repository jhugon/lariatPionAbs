hostname=$(hostname)
if [ "$hostname" == "cyril" ]; then
  echo sourcing thisroot.sh
  source /opt/root-5.34.36/bin/thisroot.sh
else
  echo setting up larsoft
  source /cvmfs/lariat.opensciencegrid.org/setup_lariat.sh
  setup git
  version=v06_34_01
  qualifier=e14:debug
  setup larsoft $version -q $qualifier
fi
