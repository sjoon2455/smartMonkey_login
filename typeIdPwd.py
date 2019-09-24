#-*- coding:utf-8 -*-
import subprocess
import os
from locateIdPwd import locateId, locatePwd
from isWhichClassText import isEditTextClass
from isGui import isPwGUI
from printPretty import printPretty

### input: list of string of each node
### output: list of node with editText class
### get only editText nodes
def getEditText(parsedList):
    list_of_editText = []
    for p in parsedList:
        
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

### type id or pwd in the android according to number of editText
### input: id(str), password(str), page description(parsed list-of-string)
### output: -
def typeIdPwd(parsedList, id, pwd):
    
    list_of_editText = getEditText(parsedList)
    
    numEditText = len(list_of_editText)
    # isLoginGui 는 이미 충족함!
    
    # 로그인 페이지가 아님
    if id == "" and pwd == "":
        printPretty("Not a login GUI!")
        return 1
    
    # 하나 있고 그게 비밀번호
    if numEditText == 1 and isPwGUI(parsedList):
        printPretty("Only PWD")
        #return "PW"
        onlyPw(list_of_editText, pwd)
        record(parsedList, id, pwd, "pwd")
        return 0

    # 하나 있고 그게 아이디
    if numEditText == 1:
        printPretty("Only ID")
        #return "ID"
        onlyId(list_of_editText, id)
        record(parsedList, id, pwd, "id")
        return 0

    # 두 개 있고 각각 로그인, 비밀번호
    if numEditText == 2:
        printPretty("ID & PWD both exists")
        
        IdPwd(list_of_editText, id, pwd)
        
        record(parsedList, id, pwd, "idpwd")
        return 0
        #return "ID & PW"
    
    else:
        printPretty("What is this?")
        return 1

### check whether there exists an lower folder /record, and record.txt inside it. If not, create one
### input: boolean
### output: -
def checkRecord():
    
    fileName = "record.txt"
    

    try:
        file = open(fileName, "r")
        printPretty("File {0} already exists".format(fileName))
        #os.chdir("..")
        return 0
    except IOError:
        file = open(fileName, "w")
        print("File " , fileName ,  " Created ")
        #os.chdir("..")
        return 0


### record an information of loginGUI, typed id and password, type of typed one(s)
### input: an information of loginGUI, typed id and password, type of typed one(s)
### output: modified file
def record(parsedList, id, pwd, identity):
    
    checkRecord()
    cwd = os.getcwd()
    directory = os.fsencode(cwd)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename == "record.txt": 
            content = open(file, "a")
            content.write("\n" + str(parsedList))
            content.write("\n" + identity)
            content.write("\n" + id)
            content.write("\n" + pwd)
            content.close()
    #os.chdir('..')
    return 0


### locate and type in only password
### input: list of editText, password
### output: -
def onlyPw(list_of_editText, pwd):
    locatePwd(list_of_editText[0])
    typeToPos(pwd)
    return 0

### locate and type in only id
### input: list of editText, id
### output: -
def onlyId(list_of_editText, id):
    locateId(list_of_editText[0])
    typeToPos(id)
    return 0

### locate and type in id and password
### input: list of editText, id, password
### output: -
def IdPwd(list_of_editText, id, pwd):
    
    locateId(list_of_editText[0])
    
    typeToPos(id)
    
    locatePwd(list_of_editText[1])
    
    typeToPos(pwd)    
    
    return 0

### input: string, id or pwd
### output: -
### type in a given id or pwd
def typeToPos(idOrPwd):
    printPretty("Finally typing in!!!")
    
    cmd = 'adb shell input text "{0}"'.format(idOrPwd)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    printPretty("Successfully typed in!")
    
    return 0

### if same gui comes up again, do the same
### input: parsedList of current GUI
### output: -
def doSame(parsedList):
    printPretty("Then let me do the same")
    
    #cwd = os.getcwd() + '/record'
    #os.chdir(cwd)
    #directory = os.fsencode(cwd)
    directory = os.fsencode(os.getcwd()+'/record')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            content = open(file, "r")
            lines = content.readlines()
            
            count = 1
            #index = 0
            for line in lines:
                line = line.replace("\n", "")
                #print("this line is: "+str(count) + line)
                if line == str(parsedList):
                    #print(line)
                    index = count
                    break
                else:
                    count += 1
            
            whichTyped = lines[index].replace("\n", "")            
            id = lines[index+1].replace("\n", "")            
            pwd = lines[index+2].replace("\n", "")
            list_of_editText = getEditText(parsedList)
            
            if whichTyped == "id":
                onlyId(list_of_editText, id)
            elif whichTyped == "pwd":
                onlyPw(list_of_editText, pwd)
            elif whichTyped == "idpwd":
                IdPwd(list_of_editText, id, pwd)
            else:
                #os.chdir("..")
                return "NO MATCH... ABORT AND CONTINUE"
            #os.chdir("..")
            return "GOT FROM THE HISTORY! NOW CONTINUE"
            
#record(['1','2'], "id", "pwd", "id")
#record(['1', '1'], "id", "pdddddwd", "id")
#doSame(['1','2'])
#doSame(['1', '1'])

 
