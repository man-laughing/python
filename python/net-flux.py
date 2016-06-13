#!/usr/bin/python
from __future__ import division
import os

r=open('/sys/class/net/eth0/statistics/rx_bytes','r')
t=open('/sys/class/net/eth0/statistics/tx_bytes','r')
r_int=int(r.read())
t_int=int(t.read())

os.system('sleep 1')

rr=open('/sys/class/net/eth0/statistics/rx_bytes','r')
tt=open('/sys/class/net/eth0/statistics/tx_bytes','r')
rr_int=int(rr.read())
tt_int=int(tt.read())

input_flux =  (rr_int - r_int)  * 8 / 2048
output_flux = (tt_int - t_int) * 8 / 2048
print "eth0_Input:", input_flux,     "eth0_Output:", output_flux
