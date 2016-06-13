#!/usr/bin/python
# -*- coding: utf-8 -*- 
import re

class file_grep():

    def __init__(self,filepath):
        self.filepath = filepath

#desc: 在一个文件中查找包含某个字符串的行,类似 grep 'hello' file
#para: <String>
#exam:  patt_s = 'hello'

    def find_str(self,patt_s):
        with open(self.filepath,'r') as f:
            ff = f.readlines()
        patt = re.compile(patt_s)
        coll_list = []
        for i in ff:
            result = re.search(patt,i.strip()) 
            if result:
                coll_list.append(result.string)
        return coll_list
             
    
#desc: 在一个文件中查找以某个字符串开始的行,类似grep '^hello' file
#para: <String>
#exam:  patt_s = 'hello'

    def find_str_start_zero(self,patt_s):
        with open(self.filepath,'r') as f:
            ff = f.readlines()
        patt = re.compile(patt_s)
        coll_list = []
        for i in ff:
            result = re.match(patt,i.strip()) 
            if result:
                coll_list.append(result.string)
        return coll_list

#desc: 在一个文件中查找同时包含两个字符串的行.
#para: <String> <String>
#exam:  patt_one = 'welcome'
#       patt_two = 'andy'

    def find_test(self,patt_one,patt_two):
        with open(self.filepath,'r') as f:
            ff = f.readlines()
        tt_patt = '.*' + patt_one + '.*' + patt_two
        patt = re.compile(tt_patt)
        coll_list = []
        for i in ff:
            result = re.match(patt,i.strip()) 
            if result:
                coll_list.append(result.string)
        return coll_list



################################################################
if __name__ == '__main__':
    aaa = file_grep('/tmp/test')
    print aaa.find_test('welcome','Andy')
