#-*- coding:utf-8 -*-


### input: list of string, integer index
### output: list of string
### concat current list element of a given index to the one in front of it, and pull all the elements that are behind it forward
def appendTail_pull(li, i):
    if i < 1: 
        raise ValueError
    else:
        li[i-1] += li[i]
        for j in range(len(li)-i-1):
            li[i+j] = li[i+j+1]
        li = li[:-1]
    return li

### input: list of string
### output: list of string
### handle the split list so that ones in the quotation mark would not be divided
def parseSplitList(li):
    i=1
    while i < len(li):
        if "=" not in li[i]:
            li = appendTail_pull(li, i)
            #print(i, " - ", li) 
        else:
            i += 1
    return li
        
#s = 'a="pass word" b="as dca sc" c="12 12312"'
#li = s.split(" ")