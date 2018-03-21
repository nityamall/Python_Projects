import math
n= input("ENTER A NO.")
n=int(n)
s=0
f=0
h=n
g=0
while n>0:
    b=n%10
    s=s+1
    n=int(n/10)
n=h
while n>0:
    b=n%10
    g=g+math.pow(b,s)
    n=int(n/10)
if(g==h):
    print("AUTOMORPHIC NOS,")
else:
    print("NOT AUTOMORPHIC")


