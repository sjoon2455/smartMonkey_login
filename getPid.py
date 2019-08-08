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

### input: string, partial name of certain process
### output: -
### get pid of certain process
def androidGetPid(process):
    cmd = "adb shell ps | grep {0}".format(process)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = proc.communicate()
    #out = shell         6468  1987 1188536  72988 binder_thread_read abe8eac4 S com.android.commands.monkey
    out = b'shell        13605  1987 1188920  74500 binder_thread_read ab9edac4 S com.android.commands.monkey'
    #print(type(out), out)
    
    decode_out = out.decode('utf-8')
    decode_out_split = decode_out.split(" ")
    index = getIndex2(decode_out_split)
    res = decode_out_split[index]
    return int(res)

### input: string
### output: index
### given a string, get an index where an integer starts
def getIndex2(list):
    count = -1
    for i in list:
        count += 1
        try:
            int(i)
            return count
        except ValueError:
            continue
            

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
print(androidGetPid("monkey"))