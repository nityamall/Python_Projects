n=input("ENTER THE NO. OF LINES")
n=int(n)
for i in range (1,n+1):
    for j in range(i,n):
        print(end=" ")
    z=0
    for k in range (0,i):
        z=z+1
        print(z,end=" ")
    y=i
    for o in range (1,i):
        y=y-1
        print(y,end=" ")

    print()
