import math
n=input("ENTER THE RANGE")
n=int(n)
a=input("ENTER ANY NO.")
a=int(a)
o=0
for i in range (1,n):
    h=1
    l=i*2
    for j in range (1,l+1):
        h=j*h
    p=math.pow(a,l)
    m=math.pow(-1,i+1)
    u=m*(p/h)
    o=o+u
b=1+o
print("%f"%b)