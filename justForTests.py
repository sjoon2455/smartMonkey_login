#-*- coding:utf-8 -*-
import os
import subprocess
from loginClassifier import parseXml
from isGui import isLoginGUI, isPwGUI
from typeIdPwd import numEditText, typeIdPwd


        

def main_isPwGui():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xml") & filename.startswith("Pw_tumblr"): 
        #if filename.endswith(".xml"):
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
            print(out)
            #print(filename, " - ", isPwGUI(out))
    

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
            


def main_isLoginGui():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #if filename.endswith(".xml") and filename.startswith("Pw_tumblr"): 
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
            out = parseXml(out, omit)
            print(filename,' - ',isLoginGUI(out))


def main_typeIdPwd():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #if filename.endswith(".xml") and filename.startswith("Pw_tumblr"): 
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
            out = parseXml(out, omit)
            
            print(filename,' - ', numEditText(out), ' - ', typeIdPwd(out, "1", "2"))


def main_facebook():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xml") and filename.startswith("facebook"): 
        #if filename.endswith(".xml"):
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()            
            omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected']
            out = parseXml(out, omit)
            
            print(filename,' - ',isPwGUI(out))              # return 0
            print(filename,' - ',typeIdPwd(out, "", ""))    # return 1
            print(filename,' - ',numEditText(out))    # return 1


#main_numEditText()
main_isPwGui()
#main_isLoginGui()
#main_typeIdPwd()
#main_facebook()