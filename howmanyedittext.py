#-*- coding:utf-8 -*-
import os
import subprocess
from loginClassifier import parseXml
from typeIdPwd import isEditTextClass, getEditText, numEditText


def is_password_text(p):
    #print(p)
    if 'text="' in p:
        #print("HI!!!!!!!!!!")
        ps = p.split('text="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'password' in ps[1][:index] or 'Password' in ps[1][:index]:
            #print("HI!!!!!!!!!!")
            return 1
    else: 
        return 0

#print(is_password_text('index="0" text="password" resource-i'))
'''
def isEditTextClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        # consider every subclass of EditText
        if 'EditText' in ps[1][:index] or 'AutoCompleteTextView' in ps[1][:index] or 'ExtractEditText' in ps[1][:index] or 'MultiAutoCompleteTextView' in ps[1][:index]:
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
'''

def isLoginGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        if 'Login' or 'login' or '로그인' in p:
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
        #print(p)
        #if 'password' or 'Password' in p:
        #if 'Password' in p:
        if is_password_text(p):
            #print("HI!!!!!!!!!!")
            count += 1
    if count > 0:
        return 'YES!!!!!!!!!!!'
    else:
        return 'ㅠ'
        

def main_isPwGui():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #if filename.endswith(".xml") & filename.startswith("Pw_tumblr"): 
        if filename.endswith(".xml"):
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()
            omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected']
            #print(type(out))
            out = parseXml(out, omit)
            print(filename, " - ", isPwGUI(out))
    

def main_numEditText():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    #print(os.getcwd())
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        #if filename.endswith(".xml") and filename.startswith("Pw_booking"): 
        if filename.endswith(".xml"):
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()            
            omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected']
            #print(type(out))
            out = parseXml(out, omit)
            print(filename,' - ',numEditText(out))
            
            



#main_numEditText()
main_isPwGui()