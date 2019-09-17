# coding = utf-8
import subprocess
#from getPid import getIndex2

### find a screen size of current adv, only works for that of thousandsXthousands
def dumpSS():
    cmd = "adb shell dumpsys window displays | grep init"
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE
    )
    out, err = proc.communicate()
    res = out.decode("utf-8")
        
    start = getIndex2(res)
    res1 = res[start:start+9]
    
    return res1

print(dumpSS())