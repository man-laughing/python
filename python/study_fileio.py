#!/usr/bin/env python


#Copy a file.
def copyfile():
    with open('/tmp/file','r') as f:
        ff = f.read()
    with open('/tmp/filenew','a+') as zl:
        zl.write(ff)


#Print line one by one.
def printline():
    with open('/tmp/file','r') as l:
        ll = l.readlines()
    for ii in ll:
        print ii.strip()

#Print is not empty line.
def noemptyline():
    ff = open('/tmp/file','r') 
    for i in ff.readlines():
        if len(i.strip()) > 0:
            print i.strip()

