#!/usr/bin/env python

a = [1,2]

for i in range(10):
    a.append(a[-2]+a[-1])
    print a
