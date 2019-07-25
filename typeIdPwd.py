#-*- coding:utf-8 -*-
import subprocess

### input: id(str), password(str), page description(xml)
# input text id -> input tap -> (조건문) -> input text pwd
def typeIdPwd(id, pwd, xml):
    cmd = "adb shell input text '{0}'".format(id)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()