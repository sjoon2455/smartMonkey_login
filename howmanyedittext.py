import os
import subprocess

def isEditTextClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'EditText' in ps[1][:index]:
            return 1
    else:
        return 0


def getEditText(xml):
    pr = xml.decode('utf-8').split('<')
    #print(pr)
    parsedList = []
    for p in pr:
        # if 'EditText' class
        if isEditTextClass(p):
            parsedList.append(p)   
    
    #parsedList = [i[5:-3] if i[-2] == ">" else i[5:] for i in parsedList] 
    return parsedList
    
def numEditText(xml):
    list_of_editText = getEditText(xml)
    #print(list_of_editText)
    return len(list_of_editText)  

def main():
    cwd = os.getcwd() + '/xmlDump'
    os.chdir(cwd)
    directory = os.fsencode(cwd)
    #print(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if filename.endswith(".xml"): 
            cmd = 'cat {0}'.format(filename)
            proc = subprocess.Popen(
                cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, err = proc.communicate()            
            
            print(numEditText(out))
            
main()



