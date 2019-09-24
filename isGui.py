#-*- coding:utf-8 -*-
import subprocess
from isWhichClassText import is_password_text, isEditTextClass
from printPretty import printPretty

### input: list of string of each node
### output: list of node with editText class
### get only editText nodes
def getEditText(parsedList):
    list_of_editText = []
    for p in parsedList:
        
        if isEditTextClass(p):
            list_of_editText.append(p)   
    return list_of_editText
    

### input: list of string, node with class of EditText
### output: int
### return number of editText class node
def numEditText(parsedList):
    list_of_editText = getEditText(parsedList)
    return len(list_of_editText)  

### boolean function, whether a given xml if login or not
### input: parsed list
### output: boolean
def isLoginGUI(parsedList):
    
    printPretty("Checking whether it's login GUI")
    count = 0
    num = numEditText(parsedList)
    for p in parsedList:
        
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
    
    printPretty("Checking whether it's password GUI")
    
    count = 0
    num = numEditText(parsedList)
    for p in parsedList:
        if is_password_text(p):
            
            count += 1
    if count > 0 and num != 0:
        return 1
    else:
        return 0

### boolean function, whether current top activity is login activity or not
### input: -
### output: boolean
def isLoginActivity():
    
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

