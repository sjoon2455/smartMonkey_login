#-*- coding:utf-8 -*-
import subprocess
# 1. get xml & parsing
def getXml():
    cmd = "adb shell uiautomator dump"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    '''
    cmd = "adb pull /sdcard/window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    #out, err = proc.communicate()
    '''
    cmd = "adb shell cat /sdcard/window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    pr = out.decode('utf-8').split('<')
    parsedList = []
    omit = ['index', 'class', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #print(pr)
    for p in pr:
        #print(p+'\n')
        #extracting only VIEWs
        li = ''
        if isViewClass(p):
        #if 'view' in p or 'View' in p:
            ll = p.split(' ')
            #print(ll)
            for l in ll:
                #print(l)
                count = 0
                for ele in omit:
                    if ele in l:
                        count += 1
                if count == 0:
                    #print(l)
                    li += l+" "
            parsedList.append(li)            

    for i in parsedList:
        i = i[5:-3]
        print(i+'\n')

# boolean function, whether a class of p is view(or View)
def isViewClass(p):
    if "class="" in p:
        ps = p.split('class="')
        for i in len(ps[1]):
            if ps[1][i] == '"':
                index = i
                break
            else:
                return 0
        if 'view' in ps[1][:index] or 'View' in ps[1][:index]:
            return 1
    else:
        return 0

def camelCaseBreak():
    return 1
def removeStopWords():
    return 1
def stemming():
    return 1
def computeTf():
    return 1
    
getXml()