#-*- coding:utf-8 -*-
import subprocess
import os
import psutil
from typeIdPwd import typeIdPwd
from getPid import pcGetPid, androidGetPid
from printPretty import printPretty

### input: parsed list of xml file
### output: -
### during some job... if loginpage occured, this function need to be called
def suspendAlarmResume(parsedList):
    
    #print(33)
    #monkey_pid = pcGetPid("naiveMonkey")
    
    #monkey_pid = androidGetPid("naiveMonkey")
    #cmd = "adb shell kill -STOP {0}".format(monkey_pid)
    #print(4)
    
    #cmd = "kill -STOP {0}".format(monkey_pid)
    #proc1 = subprocess.Popen(cmd, shell = True)
    #proc1.communicate()
    printPretty("Just stopped monkey travel")

    proc2 = subprocess.Popen("say 'beep'", shell = True) #beep
    proc2.communicate()
    # get id, pwd from user and type them in. 
    user_id = input("ID: \n(If not a login page, press return button with empty input)")
    user_pw = input("PASSWORD: \n(If none, press return button with empty input)")
    typeIdPwd(parsedList, user_id, user_pw)
    
    printPretty("Now continue monkey travel")
    #cmd = "kill -CONT {0}".format(monkey_pid)
    #subprocess.call(cmd, shell = True)

'''
### input: -
### output: -
### during some job... if loginpage occured, this function need to be called. In case of facebook.
def suspendAlarmResumeForFacebook():
    monkey_pid = androidGetPid("monkey")
    cmd = "adb shell kill -STOP {0}".format(monkey_pid)
    subprocess.call(cmd, shell = True)
    subprocess.call("say 'beep'", shell = True) #beep
    # get id, pwd from user and type them in. 
    user_id = input("ID: ")
    user_pw = input("PASSWORD: \n(If none, press return button with empty input)")
    
    #typeIdPwd(parsedList, user_id, user_pw) What should I do rather than this?
    
    cmd = "adb shell kill -CONT {0}".format(monkey_pid)
    subprocess.call(cmd, shell = True)
'''

### Just for test. It works!
def Test():
    monkey_pid = androidGetPid("monkey")
    cmd = "adb shell kill -STOP {0}".format(monkey_pid)
    subprocess.call(cmd, shell = True)
    subprocess.call("say 'beep'", shell = True) #beep
    a = input("Hey look at me: ")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print(a)
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    cmd = "adb shell kill -CONT {0}".format(monkey_pid)
    subprocess.call(cmd, shell = True)

#Test()
