#-*- coding:utf-8 -*-
import subprocess
from locateIdPwd import locateId, locatePwd
### input: id(str), password(str), page description(xml)
# input text id -> input tap -> (조건문) -> input text pwd


def typeIdPwd(xml, id, pwd):
    list_of_editText = getEditText(xml)
    numEditText = len(list_of_editText)
    if numEditText == 1:
        locateId(list_of_editText)
        typeToPos(id)
        global id
        id = pwd

    elif numEditText == 2:
        locateId(list_of_editText)
        typeToPos(id)
        locatePwd(list_of_editText)
        typeToPos(pwd)
    
    else:
        return 1
        #이런 경우가 있긴 함..Flo ㅠ


def getEditText(xml):
    pr = xml.decode('utf-8').split('<')
    parsedList = []
    for p in pr:
        # if 'EditText' class
        if isEditTextClass(p):
            parsedList.append(p)   
    
    #parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    return parsedList
    
def numEditText(xml):
    list_of_editText = getEditText(xml)
    return len(list_of_editText)    

def isEditTextClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'EditText' in ps[1][:index]:
            return 1
    else:
        return 0

def typeToPos(idOrPwd, pos):
    cmd = 'adb shell input text "{0}"'.format(idOrPwd)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    print("--------------Successfully typed in!--------------")