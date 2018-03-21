low=input("Input the lower range")
high=input("Input the higher range")
low=int(low)
high=int(high)
b=0
m=0
u=0
i=low
while i<=high:
    n=i
    f=0
    while n>0:
        b=n%10
        f=b*b*b
        m=m+f
        n=int(n/10)
    if (m==i):
        print("%d"%i)
        u=1
    m=0
    i=i+1
if(u==0):
    print("NO armstrong no. in this particular range")