n=input("ENTER A NO.")
n=int (n)
f=n
b=0
s=1
l=f
m=0
if(n%2==0):
    for i in range (1,f+1):
        s=s*i
    print("%d"%s)
else:
    for j in range (1,l):
        if(l%j==0):
            m=m+j
    print("%d"%m)
             
        