#-*- coding:utf-8 -*-
import subprocess
from locateIdPwd import locateId, locatePwd

### type id or pwd in the android according to number of editText
### input: id(str), password(str), page description(parsed list-of-string)
### output: -
def typeIdPwd(parsedList, id, pwd):
    list_of_editText = getEditText(parsedList)
    numEditText = len(list_of_editText)
    if numEditText == 1:
        locateId(list_of_editText)
        typeToPos(id)
        # 몇몇 경우엔 id 먼저 치고, 다음 화면에서 비밀번호를 친다
        global id
        id = pwd

    elif numEditText == 2:
        locateId(list_of_editText)
        typeToPos(id)
        locatePwd(list_of_editText)
        typeToPos(pwd)
    
    else:
        #이런 경우가 있긴 함..Flo ㅠ editText 개수 3개임 ㅠ
        return 1

### input: list of string of each node
### output: list of node with editText class
### get only editText nodes
def getEditText(parsedList):
    list_of_editText = []
    for p in parsedList:
        # if 'EditText' class
        if isEditTextClass(p):
            list_of_editText.append(p)   
    return parsedList
    

### input: list of string, node with class of EditText
### output: int
### return number of editText class node
def numEditText(parsedList):
    list_of_editText = getEditText(parsedList)
    return len(list_of_editText)    

### input: string, each node
### output: boolean
### whether a given string has editText as its class value
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
    # 이런 경우는 없긴 할텐데
    else:
        return 0


### input: string, id or pwd
### output: -
### type in a given id or pwd
def typeToPos(idOrPwd):
    cmd = 'adb shell input text "{0}"'.format(idOrPwd)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    print("--------------Successfully typed in!--------------")