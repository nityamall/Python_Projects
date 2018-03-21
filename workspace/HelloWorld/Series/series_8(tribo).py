n=input("ENTER THE NO. OF TERMS")
n=int(n)
f=0
s=1
l=2
k=0
print("0 1 2")
for i in range (4,n+1):
    k=f+s+l
    print("%d"%k,end=" ")
    f=s
    s=l
    l=k

