#-*- coding:utf-8 -*-
import subprocess
import datetime

### input: -
### output: bytes xml file
### dump current GUI xml file
def dumpXml():
    cmd = "adb shell uiautomator dump"
    proc = subprocess.Popen(
        cmd, 
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()

    cmd = "adb pull /sdcard/window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()

    cmd = "cat window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    
    cmd = "mv window_dump.xml xmlDump/window_dump_{0}.xml".format(datetime.datetime.now().time())
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()

    return out

dumpXml()