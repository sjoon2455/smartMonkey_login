#-*- coding:utf-8 -*-
import subprocess
from isWhichClassText import is_password_text
from printPretty import printPretty
from typeIdPwd import numEditText
### boolean function, whether a given xml if login or not
### input: parsed list
### output: boolean
def isLoginGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #parsedList = parseXml(xml, omit)
    #print("----------------------Checking whether it's login GUI----------------------")
    printPretty("Checking whether it's login GUI")
    count = 0
    num = numEditText(parsedList)
    for p in parsedList:
        #print(p)
        if 'Login' in p or 'login' in p or 'Log in' in p or 'Log In' in p or 'email' in p or '로그인' in p:
            count += 1
    if count > 0 and num != 0:
        return 1
    else:
        return 0


### boolean function, whether a given xml if password enter or not
### input: parsed list
### output: boolean
def isPwGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
    #parsedList = parseXml(xml, omit)
    #print("----------------------Checking whether it's password GUI----------------------")
    printPretty("Checking whether it's password GUI")
    print(parsedList)
    count = 0
    for p in parsedList:
        if is_password_text(p):
            #print(p)
            count += 1
    if count > 0:
        return 1
    else:
        return 0

### boolean function, whether current top activity is login activity or not
### input: -
### output: boolean
def isLoginActivity():
    #print("----------------------Checking whether it's login activity----------------------")
    printPretty("Checking whether it's login activity")
    cmd = "adb shell dumpsys activity | grep realActivity"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    decoded = out.decode("utf-8")
    activity_list = decoded.replace(" ", "")
    current_activity = activity_list.split("\n")[0]
    return 'login' in current_activity or 'Login' in current_activity

#print(isLoginActivity())