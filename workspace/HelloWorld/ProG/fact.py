f=input("Enter a no.")
f=int(f)
b=0
n=0
i=0
s=1
g=0
while f >0:
    b=f%10
    n=b
    if(n==0):
        s=0
    else:
        for i in range (1,n+1):
            s=s*i
    g=s+g
    f=int(f/10)
    s=1
print ("%d"%g)  