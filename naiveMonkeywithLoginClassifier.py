#coding = utf-8

import sys
from random import *
import subprocess
#from dumpScreenSize import dumpSS
from loginClassifier import main
from printPretty import printPretty
import time

num = int(sys.argv[1])

try:    
    pack = str(sys.argv[2])
    cmd = "adb shell pm list package"
    proc = subprocess.Popen(
        cmd, 
        shell = True,
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE
    )
    out, err = proc.communicate()
    packlist = out.decode("utf-8")
    if pack not in packlist:
        printPretty("Not a valid package name! Try again")
        raise ValueError
    else:
        cmd = "adb shell monkey -p {0} 1".format(pack)
        proc = subprocess.Popen(
        cmd, 
        shell = True,
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE
        )
        out, err = proc.communicate()
        printPretty("App Opened!")
except:
    pass


if(num <= 0):
    printPretty("Not a valid number of actions! Try with positive argument")
    raise ValueError



count = 0

screenSize = "1080x1794"
max_x = int(screenSize[:4])
max_y = int(screenSize[5:])

#hide keyboard when testing
cmd = "adb shell settings put secure show_ime_with_hard_keyboard 0"
proc = subprocess.Popen(
    cmd,
    shell = True
)
proc.communicate()
time.sleep(3)
while count < num:
    try:
        random_x = randrange(max_x)
        random_y = randrange(max_y)
        if count == 3:
            random_x = 600
            random_y = 1750
        cmd = "adb shell input tap {0} {1}".format(random_x, random_y)
        proc = subprocess.Popen(
            cmd, 
            shell = True,
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE
        )
        proc.communicate()
        printPretty("Action #{0} injected: Just touched {1}, {2}!!!".format(count+1, random_x, random_y))
        
        printPretty("Start of check")
        main()
        printPretty("End of check...Repeat")
        count += 1
    except Exception as e:
        print(e)

#return keyboard show
cmd = "adb shell settings put secure show_ime_with_hard_keyboard 1"
proc = subprocess.Popen(
    cmd,
    shell = True
)
proc.communicate()
