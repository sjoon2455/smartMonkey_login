#-*- coding:utf-8 -*-
import subprocess
### xml dump 한 걸로 editText 개수 찾아냄, 한 개면 ID만 넣고, 두 개면 ID, PWD
### 이제 그 위치를 찾아내야 하는데 무슨 수로 하지?
            

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

    idBound_x = idBound[:index]
    idBound_y = idBound[index:]
    #[0,147][1080,1647]
    #idBound_x = '[0,147]'
    #idBound_y = '[1080,1647]'
    #id_pos = '73 1363'
    id_pos += getMedian(idBound_x) + " "
    id_pos += getMedian(idBound_y)

    cmd = 'adb shell input tap {0}'.format(id_pos)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )


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

    idBound_x = idBound[:index]
    idBound_y = idBound[index:]
    #[0,147][1080,1647]
    #idBound_x = '[0,147]'
    #idBound_y = '[1080,1647]'
    #id_pos = '73 1363'
    id_pos += getMedian(idBound_x) + " "
    id_pos += getMedian(idBound_y)

    cmd = 'adb shell input tap {0}'.format(id_pos)
    proc = subprocess.Popen(
        cmd,
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

#input: [...class="...EditText"..., ..., ....] list of string
#output: [각각의 EditText에서의 bounds] list of string
def getBound(list_of_EditText):
    bounds = []
    index = 0
    for i in list_of_EditText:
        if 'bounds' not in i:
            break
        else:
            isplit = i.split('bounds="')
            for i in isplit[1]:
                index += 1
                if i == '"':
                    break
            bounds.append(isplit[1][:index])
                    



#input: '[0,147]'
#output: '|0-147|/2'
def getMedian(str):
    index = 0
    for i in str:
        index += 1
        if i == ",":
            break
    num1 = int(str[1:index-1])
    num2 = int(str[index:-1])
    med = (num1 - num2)/2
    return str(abs(med))
    

