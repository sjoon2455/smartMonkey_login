#-*- coding:utf-8 -*-
import subprocess
import psutil
### during some job... if loginpage occured, this function need to be called

def suspendAlarmResume():
    #get current pid
    currentpid = psutil.getPid(some process)
    p = psutil.Process(currentpid)
    
    p.suspend()
    subprocess.call("say 'beep'", shell = True) #beep
    ### get id, pwd from user and type them in. 
    p.resume()