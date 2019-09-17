#coding = utf-8

import sys
from random import *
import subprocess
#from dumpScreenSize import dumpSS
from loginClassifier import main
from printPretty import printPretty

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

#print(num)
if(num <= 0):
    printPretty("Not a valid number of actions! Try with positive argument")
    #print("----------------Not a valid number of actions! Try with positive argument----------------")
    raise ValueError



count = 0
#screenSize = dumpSS()
screenSize = "1080x1794"
max_x = int(screenSize[:4])
max_y = int(screenSize[5:])
#print(max_y, max_x)

while count < num:
    try:
        random_x = randrange(max_x)
        random_y = randrange(max_y)
        cmd = "adb shell input tap {0} {1}".format(random_x, random_y)
        proc = subprocess.Popen(
            cmd, 
            shell = True,
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE
        )
        proc.communicate()
        printPretty("Just touched {0}, {1}!!!".format(random_x, random_y))
        #print("-----------------Just touched {0}, {1}!!!-----------------".format(random_x, random_y))
        main()
        count += 1
    except Exception as e:
        print(e)
        