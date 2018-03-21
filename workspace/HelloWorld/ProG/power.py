import math
n=input("Enter a no.")
n=int(n)
b=0
c=0
h=n
s=0
while n>0:
    b=n%10
    c=c+1
    n=int(n/10)
while h>0:
    b=h%10
    s=s+math.pow(b,c)
    c=c-1
    h=int(h/10)
print("%d"%s)