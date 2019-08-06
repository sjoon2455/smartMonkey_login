#-*- coding:utf-8 -*-
import subprocess
import os
import psutil
from typeIdPwd import typeIdPwd
from getPid import androidGetPid

### input: parsed list of xml file
### during some job... if loginpage occured, this function need to be called
def suspendAlarmResume(parsedList):
    # 일단 Monkey로
    monkey_pid = androidGetPid(monkey)
    p = psutil.Process(monkey_pid)
    p.suspend()
    subprocess.call("say 'beep'", shell = True) #beep
    # get id, pwd from user and type them in. 
    user_id = input("ID: ")
    user_pw = input("PASSWORD: \n(If none, press return button with empty input)")
    typeIdPwd(parsedList, user_id, user_pw)
    p.resume()

def Test():
    monkey_pid = androidGetPid("monkey")
    p = psutil.Process(monkey_pid)
    p.suspend()
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
    p.resume()

Test()