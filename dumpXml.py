#-*- coding:utf-8 -*-
import subprocess
import datetime

def dumpXml():
    cmd = "adb shell uiautomator dump"
    proc = subprocess.Popen(
        cmd, 
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()

    cmd = "adb pull /sdcard/window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    cmd = "cat window_dump.xml"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    pr = out.decode('utf-8')
    print(pr)

    cmd = "mv window_dump.xml window_dump_{0}.xml".format(datetime.datetime.now().time())
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

dumpXml()