#-*- coding:utf-8 -*-
import subprocess
from locateIdPwd import locateId, locatePwd
### input: id(str), password(str), page description(xml)
# input text id -> input tap -> (조건문) -> input text pwd


def typeIdPwd(id, pwd):
    if numEditText() == 1:
        pos = locateId()
        typeToPos(id, pos)
        global id = pwd

    elif numEditText() == 2:
        posId = locateId()
        typeToPos(id, posId)
        posPwd = locatePwd()
        typeToPos(pwd, posPwd)
    
    else:
        #이런 경우가 있나?
    
    
    



def numEditText(xml):
    #가장 최근 저장된 xml 열기
    cmd = "adb shell cat /sdcard/window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    

def typeToPos(idOrPwd, pos):
    cmd = "adb shell input tap {0}".format(pos)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    #out, err = proc.communicate()

    cmd = "adb shell input text '{0}'".format(idOrPwd)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    #out, err = proc.communicate()