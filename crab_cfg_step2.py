from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'ZprimeToMuMu5000_GEN_SIM_PREMIX_RECO' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step2_RECO.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 10000

config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'ZprimeToMuMu5000_GEN_SIM_PREMIX_RECO'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/fernanpe/'
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/fernanpe-ZprimeToMuMu5000_GEN_SIM-33cc5165aa796edde06dc091a315917f/USER'

config.section_("Site")
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_ES_IFCA'
