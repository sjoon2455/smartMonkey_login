#-*- coding:utf-8 -*-
import os
import filecmp
from dumpXml import dumpXml
from sendAlarm import suspendAlarmResume
from typeIdPwd import isEditTextClass, doSame
from isGui import isLoginGUI, isPwGUI, isLoginActivity
from isWhichClassText import isViewClass, isButtonClass
from parseSplitList import parseSplitList
from printPretty import printPretty

### main function!
### get current GUI xml. If it's login page, do what I want.
def main():
    
    xml = dumpXml()
    parsedList = getXml()
    if isLoginGUI(parsedList):
    
        if isSameGUI(xml):
    
            doSame(parsedList)
        else:
    
            suspendAlarmResume(parsedList)
    '''
    elif isLoginActivity():
        # Consists of a single view as a whole, use image processing
        suspendAlarmResumeForFacebook()
    '''

### checks if it's the same GUI
### input: xml description of GUI
### output: boolean
def isSameGUI(xml):
    printPretty("Have we met before?")
    
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xml"): 
            with open(filename) as others:
                res = others.read() == xml
                
            
            if res:
                os.chdir("..")
                return True
    
    os.chdir("..")
    
    return False    
    


### dump xml & parsing
### input: none
### output: list of string
def getXml():
    out = dumpXml()
    omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected']
    parsedList = parseXml(out, omit)
    #for i in parsedList:
    #    print(i+'\n')
    printPretty("Getting xml hierarchy and parsing...")
    #dprint('--------------Getting xml hierarchy and parsing...--------------')
    return parsedList
    

### parse the given xml with only View and editText class
### input: bytes xml file, attributes to be omitted
### output: list of string of parsed xml file
def parseXml(xml, omit):
    #print(3)
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