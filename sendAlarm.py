#-*- coding:utf-8 -*-
import subprocess
import os
import psutil
from typeIdPwd import typeIdPwd
### during some job... if loginpage occured, this function need to be called

def suspendAlarmResume(xml):
    currentpid = os.getpid() #get current pid
    p = psutil.Process(currentpid)
    
    p.suspend()
    subprocess.call("say 'beep'", shell = True) #beep
    ### get id, pwd from user and type them in. 
    user_id = input("ID: ")
    user_pw = input("PASSWORD: \n(If none, press return button with empty input)")
    typeIdPwd(xml, user_id, user_pw)
    p.resume()