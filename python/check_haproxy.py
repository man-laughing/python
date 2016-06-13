#!/usr/bin/env python
import socket
import os

host , port = '192.168.0.200',1111

def start_haproxy():
    comm = '/usr/local/haproxy-1.6.2/sbin/haproxy -f /usr/local/haproxy-1.6.2/conf/haproxy.cfg'
    os.system(comm)
    
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        s.close()
    except socket.error:
#        print 'port %s is down.'  % port   
        start_haproxy()

if __name__ == '__main__':
    main()
