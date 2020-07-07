### Author: Shu-Xiao Liu
### Department of Physics, National Central University
#ZprimeToMuMu_template
import os
import shutil

exe = 1
sub = 0
def mkDir(dirName):
    if not os.path.isdir(dirName): os.mkdir(dirName)

def main():

    # mZp grid
    mZpList = [5000] 

    print "produce MZp list: ", mZpList
    print
    for mZp in mZpList:

        dirName = 'ZprimeToMuMu'+str(mZp)
        
        mkDir('cards/'+dirName)
        print('create '+dirName)
        shutil.copyfile('cards/ZprimeToMuMu_template/ZprimeToMuMu_run_card.dat','cards/'+dirName+'/'+dirName+'_run_card.dat')
        shutil.copyfile('cards/ZprimeToMuMu_template/ZprimeToMuMu_extramodels.dat','cards/'+dirName+'/'+dirName+'_extramodels.dat')

        f_proc0 = open('cards/ZprimeToMuMu_template/ZprimeToMuMu_proc_card.dat','r')
        f_proc1 = open('cards/'+dirName+'/'+dirName+'_proc_card.dat','w')
        for line in f_proc0:
            if line.find('ZprimeToMuMu') > 0: 
                f_proc1.write(line.replace('ZprimeToMuMu',dirName))
            else:f_proc1.write(line)                    
        f_proc0.close()
        f_proc1.close()

        f_cust0 = open('cards/ZprimeToMuMu_template/ZprimeToMuMu_customizecards.dat','r')
        f_cust1 = open('cards/'+dirName+'/'+dirName+'_customizecards.dat','w')
        for line in f_cust0:
            if line.find('3.500000e+02') > 0: f_cust1.write(line.replace('3.500000e+02',str(mZp)))
            else: f_cust1.write(line)
        f_cust0.close()
        f_cust1.close()
            
        command = './gridpack_generation.sh ' + dirName + ' cards/' + dirName
        subcom = './submit_condor_gridpack_generation.sh ' + dirName + ' cards/' + dirName
        print(command)
        if (exe): os.system(command)
        elif (sub): os.system(subcom)

if __name__ == "__main__":
    main()
    #os.system('cp *.tarball.tar.xz ~/public/gridpackDir')
