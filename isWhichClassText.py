#-*- coding:utf-8 -*-


### boolean function, whether a class of p is view(or View)
### input: string(each node of xml file)
### output: boolean
def isViewClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'view' in ps[1][:index] or 'View' in ps[1][:index]:
            return 1
    else:
        return 0


def is_password_text(p):
    #print(p)
    if 'text="' in p:
        #print("HI!!!!!!!!!!")
        ps = p.split('text="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        if 'password' in ps[1][:index] or 'Password' in ps[1][:index]:
            #print("HI!!!!!!!!!!")
            return 1
    else: 
        return 0

### input: string, each node
### output: boolean
### whether a given string has editText as its class value
def isEditTextClass(p):
    if 'class="' in p:
        ps = p.split('class="')
        for i in range(len(ps[1])):
            if ps[1][i] == '"':
                index = i
                break
        # consider every subclass of EditText
        if 'EditText' in ps[1][:index] or 'AutoCompleteTextView' in ps[1][:index] or 'ExtractEditText' in ps[1][:index] or 'MultiAutoCompleteTextView' in ps[1][:index]:
            #print(ps[1][:index])
            return 1
    else:
        return 0