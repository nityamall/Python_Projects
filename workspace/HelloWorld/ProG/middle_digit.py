n=input("Enter a no.")
n=int(n)
b=0
c=0
f=n
v=0
z=0
while n>0:
    b=n%10
    c=c+1
    n=int(n/10)
if(c%2!=0):
    c=c+1
else:
    c=c+2
c=int(c/2)
while f>0:
    v=f%10
    z=z+1
    if(z==c):
        print("%d"%v)
        break
    f=int(f/10)