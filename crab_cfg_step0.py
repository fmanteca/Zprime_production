from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'ZprimeToMuMu5000_GEN_SIM'
config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'step0_GEN_SIM.py'
config.JobType.numCores = 8
config.JobType.inputFiles = ['/eos/cms/store/group/phys_muon/fernanpe/rootfiles/ZprimeToMuMu5000_100k_1.lhe']
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 500
config.Data.totalUnits 	    = 100000
config.Data.outputDatasetTag = 'ZprimeToMuMu5000_GEN_SIM'
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/user/fernanpe/'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
