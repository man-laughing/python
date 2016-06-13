#!/usr/bin/env python

for num in range(1,11):
    sum = 1
    for i in range(1,num + 1):
        sum = sum * i
    print 'Number',num,'is',sum