x=4
x=int(x)
r=x
for i in range (0,x+1):
    for j in range(0,i):
        print(end="  ")
    for k in range (r,0,-1):
        print("*",end=" ")
    r=r-1
    print()

