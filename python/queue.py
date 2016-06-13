#!/usr/bin/python
'''
 开启2个线程a和b
 a线程取出10（包含10）的偶数并且放到队列里
 b线程实时读队里的值
 同时运行

'''

import threading
from Queue import Queue
import time

print "Now time is %s" %time.ctime()
print "#"*40
q = Queue()


def put_values():
    x = [x for x in range(11) if x % 2 == 0]
    for i in x:
        q.put(i)
        time.sleep(1)

def get_values():
    while bool(q.qsize()):
        print q.get()

ttt = []
t1 = threading.Thread(target=put_values)
t2 = threading.Thread(target=get_values)
ttt.append(t1)
ttt.append(t2)
for i in ttt:
    i.start()
    i.join()

print "#"*40
print "Finish time is  %s" %time.ctime()

