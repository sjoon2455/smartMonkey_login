#-*- coding:utf-8 -*-
from isWhichClassText import is_password_text

### boolean function, whether a given xml if login or not
### input: parsed list
### output: boolean
def isLoginGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds', ]
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        if 'Login' in p or 'login' in p or 'Log in' in p or 'Log In' in p or 'email' in p or '로그인' in p:
            count += 1
    if count > 0:
        return 1
    else:
        return 0


### boolean function, whether a given xml if password enter or not
### input: parsed list
### output: boolean
def isPwGUI(parsedList):
    #omit = ['index', 'package', 'checkable', 'checked', 'clickable', 'enabled', 'focusable', 'focused', 'scrollable', 'long-clickable', 'password', 'selected', 'bounds']
    #parsedList = parseXml(xml, omit)
    count = 0
    for p in parsedList:
        if is_password_text(p):
            #print(p)
            count += 1
    if count > 0:
        return 1
    else:
        return 0