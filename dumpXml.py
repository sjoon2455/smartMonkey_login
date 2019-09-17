#-*- coding:utf-8 -*-
import subprocess
import datetime
from printPretty import printPretty
### input: -
### output: bytes xml file
### dump current GUI xml file
str(datetime.datetime.now().time())[:-7]
def dumpXml():
    printPretty("Dumping hierarchy...")
    #print("----------------------Dumping hierarchy...----------------------")
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
    
    cmd = "mv window_dump.xml xmlDump/window_dump_{0}.xml".format(str(datetime.datetime.now().time())[:-7])
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()
    printPretty("Dump Done!")
    #print("----------------------Dump Done!----------------------")
    return out

if __name__ == "__main__":
#if __name__ == "dumpXml":
#print(__name__)
    dumpXml()