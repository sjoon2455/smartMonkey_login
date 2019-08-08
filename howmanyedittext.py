#-*- coding:utf-8 -*-
import os
import subprocess
from loginClassifier import parseXml



def is_password_text(p):
    #print(p)
    if 'text="' in p:
        #print("HI!!!!!!!!!!")
        ps = p.split('text="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'password' in ps[1][:index]:
            #print("HI!!!!!!!!!!")
            return 1
    else: 
        return 0

#print(is_password_text('index="0" text="password" resource-i'))

def isEditTextClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'EditText' in ps[1][:index] or 'AutoCompleteTextView' in ps[1][:index] or 'ExtractEditText' in ps[1][:index] or 'MultiAutoCompleteTextView' in ps[1][:index]:
        #if 'EditText' in ps[1][:index] or 'MultiAutoCompleteTextView' in ps[1][:index]:
            #print(ps[1][:index])
            return 1
    else:
        return 0


def getEditText(xml):
    pr = xml.decode('utf-8').split('<')
    #print(pr)
    parsedList = []
    for p in pr: 
        # if 'EditText' class
        if isEditTextClass(p):
            #print(p)
            parsedList.append(p)   
    
    #parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    return parsedList
    
def numEditText(xml):
    list_of_editText = getEditText(xml)
    #print(list_of_editText)
    return len(list_of_editText)  


def isLoginGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' or '비밀번호' or '로그인' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' or '비밀번호' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' or 'PASSWORD' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' or 'password' in p:
        #if 'Login' or 'login' or 'Log in' or 'log in' in p:
        #if 'Login' or 'login' or 'Log in' in p:
        if 'Login' or 'login' or '로그인' in p:
        #if 'login' in p:
            count += 1
    if count > 0:
        return 'YES!!!!!!!!!!!'
    else:
        return 'ㅠㅠ'

def isPwGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        print(p)
        #if 'password' or 'Password' in p:
        #if 'Password' in p:
        if is_password_text(p):
            print("HI!!!!!!!!!!")
            count += 1
    if count > 0:
        return 'YES!!!!!!!!!!!'
    else:
        return 'ㅠ'
        

def main2():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xml") & filename.startswith("Pw"): 
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()

            print(filename, " - ", isPwGUI(out))
    

def main():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    #print(os.getcwd())
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if filename.endswith(".xml"): 
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()            
            
            print(filename,' - ',numEditText(out))
            
            



main()
#main2()