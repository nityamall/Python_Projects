range1=input("Input the higher range")
range1=int(range1)
r=0
u=0
v=1
r=u+v
print ("%d"%u)
print ("%d"%v)
print ("%d"%r)
for  i in range (range1):
    if(r<range1):
        u=v
        v=r
        r=u+v
        if(r>range1):
            break
        print("%d"%r)