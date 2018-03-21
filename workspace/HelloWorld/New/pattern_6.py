n=input("enter the no of lines")
n=int(n)
a=1
b=n+1
c=n+1
if(n%2!=0):
    mid=int((n+1)/2)
else:
    mid=int(n/2)
for i in range (1,c):
    for j in range (1,n+2):
        if(j==a):
            if(a>mid):
                print((j-1), end=" ")
            else:
                print(j,end=" ")
        elif(j==b):
            if(b<mid):
                print(j,end=" ")
            else:
                print((j - 1), end=" ")
        else:
            print(end=" ")
    if(i==mid):
        a=a+2
        b=b-2
    else:
        a=a+1
        b=b-1
    print()
