#!/usr/bin/python

from collections import Counter

def test(filepath):
    with open(filepath,'r') as f:
        ff = f.read()
    cc = Counter(ff)
    return cc.most_common(10)

