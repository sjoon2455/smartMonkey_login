#-*- coding:utf-8 -*-
import subprocess
from printPretty import printPretty
### xml dump 한 걸로 editText 개수 찾아냄, 한 개면 ID만 넣고, 두 개면 ID, PWD

### input: string, node with class of EditText
### output: -
### locate where to type in ID. Then, tap the input box.
def locateId(list_of_EditText):
    #print(list_of_EditText)
    index = 0
    id_pos = ''
    idBound = getBound(list_of_EditText)

    for i in idBound:
        index += 1
        if i == "]":
            break

    idBound_x1y1 = idBound[:index]
    idBound_x2y2 = idBound[index:]
    #print(idBound_x1y1, type(idBound_x1y1))
    #print(parseList(idBound_x1y1))
    #[0,147][1080,1647]
    #idBound_x1y1 = '[0,147]'
    #idBound_x2y2 = '[1080,1647]'
    #id_pos = '73 1363'
    list_x1y1 = parseList(idBound_x1y1)
    list_x2y2 = parseList(idBound_x2y2)
    #print(list_x1y1, list_x2y2)
    median_x = getMedian(list_x1y1[0], list_x2y2[0])
    median_y = getMedian(list_x1y1[1], list_x2y2[1])
    #print("id: {0}, {1}".format(median_x, median_y))
    id_pos += str(int(median_x)) + " " + str(int(median_y))

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


### input: string, node with class of EditText
### output: -
### locate where to type in PWD. Then, tap the input box.
def locatePwd(list_of_EditText):
    index = 0
    pwd_pos = ''
    idBound = getBound(list_of_EditText)
    
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
    #pwd_pos += median_x + " " + median_y
    #print("pwd: {0}, {1}".format(median_x, median_y))
    pwd_pos += str(int(median_x)) + " " + str(int(median_y))
    

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


### input: ["...class="...EditText"..."] list of string
### output: string
### For each node with editText class, get bound(x1~x2, y1~y2)
def getBound(string_of_EditText):
    index = 0
    isplit = string_of_EditText.split('bounds="')
    #print(isplit)
    for i in isplit[1]:
        index += 1
        if i == '"':
            break
    return isplit[1][:index-1]

#print(getBound('text="Phonenumber,emailorusername" resource-id="com.instagram.android:id/login_username" class="android.widget.EditText" content-desc="" bounds="[74,661][1006,787]"'))

### input: '[0,147]'
### output: [0, 147]
### helper function for un-stringifiy-ing for a given string 
def parseList(s):
    strip_str = s.strip()
    noBracket_str = strip_str[1:-1]
    res = noBracket_str.split(",")
    res = [int(i)  for i in res] 
    return res

#print(type(parseList('[74,661] ')[0]))

### input: int int
### output: int
### helper function for getting median for given two ints
def getMedian(a, b):
    return (a+b)/2
    

