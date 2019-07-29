#-*- coding:utf-8 -*-
import subprocess
from dumpXml import dumpXml
from sendAlarm import sendAlarm



def main():
    xml = getXml()
    #이 알고리즘을 짜야함. xml에 로그인이 있으면? 등등으로. 그래서 불리안으로 넘겨주고,
    if loginGUI(xml):
        suspendAlarmResume(xml)

def loginGUI(xml):
    return 1


# get xml & parsing
def getXml():
    out = dumpXml()
    omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    parsedList = parseXml(out, omit)
    for i in parsedList:
        print(i+'\n')
    return parsedList
    

# input: .txt xml file, attributes to be omitted
# output: .txt parsed xml file
# parse the given xml
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
### input: xml file
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