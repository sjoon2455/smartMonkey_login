#-*- coding:utf-8 -*-
# xml parsing
from __future__ import print_function
import subprocess

# get xml file
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
    li = ''
    parsedList = []
    omit = ['index', 'class', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #print(pr)
    for p in pr:
        #print(p+'\n')
        #extracting only VIEWs
        #!!!fix this part view in class of p로 바꾸기!!!
        if 'view' in p:
            ll = p.split(' ')
            for l in ll:
                count = 0
                for ele in omit:
                    if ele in l:
                        count += 1
                if count == 0:
                    #print(l)
                    li += l+" "
            parsedList.append(li)            

    for i in parsedList:
        print(i+'\n')

getXml()