#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Create time:    2015-04-15
author:         fire
Function:
zabbix报警统计

'''
import MySQLdb
import time
import sys
from settings import *

def mysqlconn():
    conn = MySQLdb.connect(
        host = mysql_host,
        user = mysql_user,
        passwd = mysql_pw,
        db = mysql_db,
        charset = mysql_charset)
    cur = conn.cursor()
    return (conn,cur)
def mysqlclose(cur,conn):
    cur.close()
    conn.close()
def select(sql,conn,cur):
    #sql = "select * from test;"
    try:
        cur.execute(sql)
        data = cur.fetchall()
        return data
    except MySQLdb.Error,e:
        conn.rollback()
        print "Mysql Error: %s" %e
        sys.exit(2)
def timeStamp_to_date(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
    return otherStyleTime
def main():
    now = int(time.time()) 
    fix = now - 86400
    timeStamp_now = timeStamp_to_date(now)
    timeStamp_fix = timeStamp_to_date(fix)
    sql1 = "SELECT objectid FROM events WHERE value=1 AND objectid >10000 AND clock>=%s AND clock<=%s ORDER BY clock DESC LIMIT 100" %(fix,now)
    conn,cur = mysqlconn()
    result1 = select(sql1,conn,cur)
    objectid = [ str(object[0]) for object in result1 ]
    dic_objectid = {}          #用于存放每个objectid重复出现的次数
    for k in objectid:
        if objectid.count(k) >= 1:
            dic_objectid[k] = objectid.count(k)
    sql2 = "SELECT priority,triggerid FROM triggers t WHERE t.triggerid BETWEEN 000000000000000 AND 099999999999999 AND t.triggerid IN (%s)" %','.join(objectid)
    result2 = select(sql2,conn,cur)
    dic_priority = {                               #初始化
                    1:0,    #灾难问题
                    2:0,    #严重问题
                    3:0,    #一般问题
                    4:0,    #警告问题
                    5:0     #普通问题
                    }
    for k,v in result2:
        k,v = int(k),str(v)    
        dic_priority[k] += dic_objectid[v]
    mysqlclose(cur,conn)
    print """
        ZBX-ALERTS 
        (%s ~ %s)
******************************************
        灾难问题：%d个   
        严重问题：%d个  
        一般问题：%d个  
        警告问题：%d个  
        普通问题：%d个  
******************************************    
""" % tuple([timeStamp_fix,timeStamp_now] + [dic_priority[k] for k in range(1,6)[::-1]])
    
if "__main__" == __name__:
    main()
    
    
    
    
    
    
    