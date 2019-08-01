#-*- coding:utf-8 -*-
import subprocess
from dumpXml import dumpXml
from sendAlarm import suspendAlarmResume


### main function!
### get current GUI xml. If it's login page, do what I want.
def main():
    xml = dumpXml()
    #이 알고리즘을 짜야함. xml에 로그인이 있으면? 등등으로. 그래서 불리안으로 넘겨주고,
    if isLoginGUI(xml):
        xmlList = getXml()
        suspendAlarmResume(xmlList)


### boolean function, whether a given xml if login or not
### input: xml 
### output: boolean
def isLoginGUI(xml):
    omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' or '비밀번호' or '로그인' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' or '비밀번호' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' in p:
        #if 'Login' or 'login' or 'Log in' in p:
        if 'Login' or 'login' in p:
        #if 'login' in p:
            count += 1
    if count > 0:
        return 1
    else:
        return 0




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
    

### parse the given xml
### input: bytes xml file, attributes to be omitted
### output: .txt parsed xml file
def parseXml(xml, omit):
    pr = xml.decode('utf-8').split('<')
    parsedList = []
    for p in pr:
        #extracting only VIEWs
        li = ''
        if isViewClass(p):
        #if 'view' in p or 'View' in p:
            ll = p.split(' ')
            for l in ll:
                count = 0
                for ele in omit:
                    if ele in l:
                        count += 1
                if count == 0:
                    li += l+" "
            parsedList.append(li)   
    
    parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    return parsedList

### boolean function, whether a class of p is view(or View)
### input: string(each node of xml file)
### output: boolean
def isViewClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'view' in ps[1][:index] or 'View' in ps[1][:index]:
            return 1
    else:
        return 0