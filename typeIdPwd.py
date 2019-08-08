#-*- coding:utf-8 -*-
import subprocess
from locateIdPwd import locateId, locatePwd
#from loginClassifier import isLoginGUI, isPwGui

### type id or pwd in the android according to number of editText
### input: id(str), password(str), page description(parsed list-of-string)
### output: -
def typeIdPwd(parsedList, id, pwd):
    list_of_editText = getEditText(parsedList)
    numEditText = len(list_of_editText)
    # 하나 있고 그게 비밀번호
    if numEditText == 1 & isPwGui(parsedList):
        locatePwd(list_of_editText)
        typeToPos(pwd)

    # 하나 있고 그게 로그인
    if numEditText == 1 & isLoginGui(parsedList):
        locateId(list_of_editText)
        typeToPos(id)
    # 두 개 있고 각각 로그인, 비밀번호
    elif numEditText == 2:
        locateId(list_of_editText)
        typeToPos(id)
        locatePwd(list_of_editText)
        typeToPos(pwd)
    
    else:
        #Flo 랑 Facebook 있는데 Facebook 은 커버 가능! 이건 해결해야 할 문제임
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




### boolean function, whether a given xml if login or not
### input: parsed list
### output: boolean
def isLoginGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        if 'Login' or 'login' in p:
            count += 1
    if count > 0:
        return 1
    else:
        return 0

### boolean function, whether a given xml if password enter or not
### input: parsed list
### output: boolean
def isPwGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        if 'password' or 'Password' in p:
            count += 1
    if count > 0:
        return 1
    else:
        return 0