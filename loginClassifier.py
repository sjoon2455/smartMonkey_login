#-*- coding:utf-8 -*-
import subprocess
from dumpXml import dumpXml
from sendAlarm import suspendAlarmResume, suspendAlarmResumeForFacebook
from typeIdPwd import isEditTextClass
from isGui import isLoginGUI, isPwGUI, isLoginActivity
from isWhichClassText import isViewClass, isButtonClass
from parseSplitList import parseSplitList

### main function!
### get current GUI xml. If it's login page, do what I want.
def main():
    xml = dumpXml()
    if isLoginGUI(xml):
        parsedList = getXml()
        suspendAlarmResume(parsedList)
    elif isLoginActivity():
        # Consists of a single view as a whole, use image processing
        suspendAlarmResumeForFacebook()


### get xml & parsing
### input: none
### output: list of string
def getXml():
    out = dumpXml()
    omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
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
        li = ''
        if isViewClass(p) or isEditTextClass(p) or isButtonClass(p): 
            ll = p.split(' ')
            ll = parseSplitList(ll)
            for l in ll:
                llhs = l.split("=")[0]    
            
                count = 0
                for ele in omit:
                    if ele in llhs:
                        count += 1
                if count == 0:
                    
                    li += l+" "
            
            parsedList.append(li)   
    
    parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    #for i in parsedList:
    #    print(i)
    return parsedList

