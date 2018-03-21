def dr (dl):
    u=[]
    d=[]
    for i in dl:
        if i not in u:
            u.append(i)
        else:
            d.append(i)
    return u,d
print (dr([10,20,30,10,20,60,89,60]))