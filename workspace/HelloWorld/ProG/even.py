n=input("Enter a no.")
n=int(n)
b=0
c=0
v=0
f=n
while n>0:
    b=n%10
    c=c+1 
    n=int(n/10)
while(f>0):
    v=f%10
    if(c%2==0):
        print("%d"%v)
    c=c-1
    f=int(f/10)