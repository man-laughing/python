#!/usr/bin/env python

import os
import time
import sys


def dns():
    ctc_dns = [
         'nameserver 119.84.66.16',
         'nameserver 180.97.75.4',
         'nameserver 121.22.249.143',
         'nameserver 112.80.31.48'
    ]

    cnc_dns = [
         'nameserver 121.22.249.143',
         'nameserver 112.80.31.48',
         'nameserver 119.84.66.16',
         'nameserver 180.97.75.4'
    ]

    hostname  = os.getenv('HOSTNAME')

    if hostname.split('-')[1] == 'ctc':
        with open('/tmp/test','w') as f:
            for i in ctc_dns:
                f.write(i)
                f.write('\n')
    if hostname.split('-')[1] == 'cnc':
        with open('/tmp/test','w') as f:
            for i in cnc_dns:
                f.write(i)
                f.write('\n')
def yum():
    pack = 'libselinux-python wget autoconf gcc gcc-c++ unzip lrzsz nc vim screen  ntpdate curl git python-devel mysql-devel openssl-devel pypthon-setuptools python-setuptools-devel readline-devel  ncurses-devel'
    abc = 'yum -y install ' +'pack'
    command  = os.system(abc)
    if command != 0:
        print 'yum install some packages error,please check it.' 

if  sys.argv[1] == 'dns':
    dns()
