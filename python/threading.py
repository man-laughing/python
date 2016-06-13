#!/usr/bin/env python

import threading
import time

def print_ok():
    print 'I was to listen music',time.ctime()
    time.sleep(2)

def print_err():
    print 'I was to watch movices',time.ctime()
    time.sleep(5)

ttt = []
t1 = threading.Thread(target=print_ok)
t2 = threading.Thread(target=print_err)
ttt.append(t1)
ttt.append(t2)
for i in ttt:
    i.start()
    i.join()

#print_ok()
#print_err()
print 'The time is: ',time.ctime()
