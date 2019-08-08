#-*- coding:utf-8 -*-
import subprocess
from dumpXml import dumpXml
from sendAlarm import suspendAlarmResume
from typeIdPwd import isEditTextClass
from isGui import isLoginGUI, isPwGui
from isWhichClassText import isViewClass

### main function!
### get current GUI xml. If it's login page, do what I want.
def main():
    xml = dumpXml()
    #이 알고리즘을 짜야함. xml에 로그인이 있으면? 등등으로. 그래서 불리안으로 넘겨주고,
    if isLoginGUI(xml):
        parsedList = getXml()
        suspendAlarmResume(parsedList)


### get xml & parsing
### input: none
### output: list of string
def getXml():
    out = dumpXml()
    omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    parsedList = parseXml(out, omit)
    for i in parsedList:
        print(i+'\n')
    print('--------------Getting xml hierarchy and parsing...--------------')
    return parsedList
    

### parse the given xml with only View and editText class
### input: bytes xml file, attributes to be omitted
### output: list of string of parsed xml file
def parseXml(xml, omit):
    pr = xml.decode('utf-8').split('<')
    parsedList = []
    for p in pr:
        #extracting only VIEWs
        li = ''
        if isViewClass(p) or isEditTextClass(p):
        #if isViewClass(p):            
            ll = p.split(' ')
            for l in ll:
                llhs = l.split("=")[0]
                #lrhs = l.split("=")[1]
                count = 0
                for ele in omit:
                    if ele in llhs:
                        count += 1
                if count == 0:
                    li += l+" "
            parsedList.append(li)   
    
    parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    return parsedList

