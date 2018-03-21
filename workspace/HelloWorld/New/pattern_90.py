n=input("ENTER THE NO OF LINES")
n=int(n)
l=1
for i in range(1,n+1):
    for j in range(0,i):
        print("%d"%l,end=" ")
        l=l+1
    print()