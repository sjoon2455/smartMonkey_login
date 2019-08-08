#-*- coding:utf-8 -*-
import subprocess
from locateIdPwd import locateId, locatePwd
from isWhichClassText import isEditTextClass

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




### input: list of string of each node
### output: list of node with editText class
### get only editText nodes
def getEditText(parsedList):
    list_of_editText = []
    for p in parsedList:
        #print(p)
        # if 'EditText' class
        if isEditTextClass(p):
            list_of_editText.append(p)   
    return list_of_editText
    

### input: list of string, node with class of EditText
### output: int
### return number of editText class node
def numEditText(parsedList):
    list_of_editText = getEditText(parsedList)
    return len(list_of_editText)    
