n=input("Enter a no.")
n=int(n)
b=0
m=0
while n>0:
    b=n%10
    if(b>m):
        m=b
    n=int(n/10)
print ("%d"%m)