DOCUMENTATION
=========================

Create the gridpacks
--------------
```
cmsrel CMSSW_9_4_9
cd CMSSW_9_4_9/src/
scram b
git clone https://github.com/cms-sw/genproductions.git
cd genproductions/bin/MadGraph5_aMCatNLO/
```

Create the gridpacks
--------------
```
python genGridpack_ZprimeToMuMu.py
```
/eos/cms/store/group/phys_muon/fernanpe/rootfiles/*tar*

Create the LHE file
--------------
```
tar xvf ZprimeToMuMu5000_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
./runcmsgrid_LO.sh 1000000 $RANDOM 40
```
/eos/cms/store/group/phys_muon/fernanpe/rootfiles/*lhe*

Produce the GEN-SIM
--------------
```
cmsDriver.py step0 --fileout file:ZPrimeToMuMu5000.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 94X_mc2017_realistic_v10 --step GEN,SIM --filetype LHE --filein file:/eos/cms/store/group/phys_muon/fernanpe/rootfiles/ZprimeToMuMu5000.lhe --nThreads 8 --beamspot Realistic25ns13TeVEarly2017Collision --geometry DB:Extended --era Run2_2017 --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
```