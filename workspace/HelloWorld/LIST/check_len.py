def mw (arr):
    c=0
    for i in arr :
        if len (i)>=2 and i[0]==i[-1]:
            c=c+1
    return c
print(mw (['abc','efg','aba','1221']))        