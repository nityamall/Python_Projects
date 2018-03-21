import math
n=input("ENTER THE LIMIT")
n=int(n)
a=input("ENTER A NO.")
a=int(a)
s=0
k=0
l=0
for i in range (1,n):
    s=math.pow(a,i+1)
    f=1
    for j in range (1,i+1):
        f=j*f
    k=k+s/f
l=1+k
print("%f"%l)