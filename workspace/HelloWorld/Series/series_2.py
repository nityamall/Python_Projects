n=input("ENTER THE LIMIT")
n=int(n)
for i in range (1,n+1):
    s=1
    for j in range (1,i+1):
        s=s*j
    print("%d"%s,end=" ")
