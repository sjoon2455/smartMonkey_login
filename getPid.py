#-*- coding: utf-8 -*-
import subprocess

### input: string, partial name of certain process
### output: -
### get pid of certain process

def pcGetPid(process):
    cmd = "ps | grep {0}".format(process)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    decode_out = out.decode('utf-8')
    #print(type(decode_out), decode_out)
    decode_out_split = decode_out.split("\n")
    ps = decode_out_split[0]
    #print(type(ps), ps)
    index = getIndex(ps)
    res = ps[:index]
    return int(res)

def androidGetPid(process):
    cmd = "adb shell ps | grep {0}".format(process)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    out = b'shell         6468  1987 1188536  72988 binder_thread_read abe8eac4 S com.android.commands.monkey\n'
    #print(type(out), out)
    decode_out = out.decode('utf-8')
    #print(type(decode_out), decode_out)
    decode_out_split = decode_out.split(" ")
    #print(decode_out_split[9])
    res = decode_out_split[9]
    return int(res)

### input: string
### output: int
### given a string, get an index until int.
def getIndex(ps):
    count = -1
    for i in ps:
        count += 1
        try:
            int(i)
        except ValueError: 
            return count
            
#print(getIndex("1 dsd")) # should print 1
#print(pcGetPid("qemu"))
androidGetPid("monkey")