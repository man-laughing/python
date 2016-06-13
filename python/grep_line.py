#!/usr/bin/env python
#This script can help you grep between 100 and 200 lines.


import time

file1 = open('/tmp/syslog','r') 
file2 = open('/tmp/newfile','w') 

   
i = 0 

while 1:
    line = file1.readline()
    i += 1   
    if 100 <=i and i <=200:
        file2.write(line)
    if i > 200:
        break
    if not line:
        break
        
file1.close()
file2.close()
         
