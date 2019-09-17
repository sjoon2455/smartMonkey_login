#-*- coding:utf-8 -*-
import subprocess
from printPretty import printPretty
### xml dump 한 걸로 editText 개수 찾아냄, 한 개면 ID만 넣고, 두 개면 ID, PWD

### input: list of string, node with class of EditText
### output: -
### locate where to type in ID. Then, tap the input box.
def locateId(list_of_EditText):
    index = 0
    id_pos = ''
    li = getBound(list_of_EditText)
    idBoun = li[0]
    idBound = idBoun.strip()
    for i in idBound:
        index += 1
        if i == "]":
            break

    idBound_x1y1 = idBound[:index]
    idBound_x2y2 = idBound[index:]
    #[0,147][1080,1647]
    #idBound_x1y1 = '[0,147]'
    #idBound_x2y2 = '[1080,1647]'
    #id_pos = '73 1363'
    list_x1y1 = parseList(idBound_x1y1)
    list_x2y2 = parseList(idBound_x2y2)
    median_x = getMedian(list_x1y1[0], list_x2y2[0])
    median_y = getMedian(list_x1y1[1], list_x2y2[1])
    id_pos += median_x + " " + median_y

    cmd = 'adb shell input tap {0}'.format(id_pos)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()
    printPretty("Touched ID.....")
    #print('----------------Touched ID.....----------------')
    return 1


### input: list of string, node with class of EditText
### output: -
### locate where to type in PWD. Then, tap the input box.
def locatePwd(list_of_EditText):
    index = 0
    id_pos = ''
    li = getBound(list_of_EditText)
    idBoun = li[0]
    idBound = idBoun.strip()
    for i in idBound:
        index += 1
        if i == "]":
            break

    idBound_x1y1 = idBound[:index]
    idBound_x2y2 = idBound[index:]
    #[0,147][1080,1647]
    #idBound_x1y1 = '[0,147]'
    #idBound_x2y2 = '[1080,1647]'
    #pwd_pos = '540 897'
    list_x1y1 = parseList(idBound_x1y1)
    list_x2y2 = parseList(idBound_x2y2)
    median_x = getMedian(list_x1y1[0], list_x2y2[0])
    median_y = getMedian(list_x1y1[1], list_x2y2[1])
    pwd_pos += median_x + " " + median_y
    

    cmd = 'adb shell input tap {0}'.format(pwd_pos)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    proc.communicate()
    printPretty("Touched PWD.....")
    #print('----------------Touched PWD.....----------------')
    return 1


### input: [...class="...EditText"..., ..., ....] list of string
### output: [각각의 EditText에서의 bounds] list of string
### For each node with editText class, get bound(x1~x2, y1~y2)
def getBound(list_of_EditText):
    bounds = []
    index = 0
    for i in list_of_EditText:
        if 'bounds' not in i:
            #continue 가 아니라 이건 그냥 이상한거니깐 break
            break
        else:
            isplit = i.split('bounds="')
            for i in isplit[1]:
                index += 1
                if i == '"':
                    break
            bounds.append(isplit[1][:index])
                    

### input: '[0,147]'
### output: [0, 147]
### helper function for un-stringifiy-ing for a given string 
def parseList(str):
    noBracket_str = str[1:-1]
    res = noBracket_str.split(",")
    res = [int(i)  for i in res] 


### input: int int
### output: int
### helper function for getting median for given two ints
def getMedian(a, b):
    return (a+b)/2
    

