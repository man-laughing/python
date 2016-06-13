#!/usr/bin/env python

import os,sys,re,time

file_dir  = '/tmp/'
file_name = 'data.conf'
full_file_name = file_dir + file_name
cont   = sys.argv[1]
cont_z = sys.argv[1].split('=')[0]
ff  = open(file_name,'r').read()
fff = open(file_dir+'newdata.conf','w')
def settime():
    return time.strftime("%y%m%d%H%M%S",time.localtime())
def backupoldfile():
    backup_name = 'data.conf'+ settime()
    aaa = open(full_file_name).read()
    open(file_dir + backup_name,'w').write(aaa)
def working():
    backupoldfile()
    if cont_z in ff:
        fff.write(re.sub(cont_z+'.*',cont,ff))
        os.remove(full_file_name)
        os.rename(file_dir+'newdata.conf',full_file_name)
    else:
        with open(full_file_name,'a+') as w:
            w.write(cont+'\n')
if __name__ == '__main__':
    working()
