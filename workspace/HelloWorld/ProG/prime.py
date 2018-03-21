p=input("Enter a no.")
p=int (p)
b=0
while p>0:
    b=p%10
    flag=1
    if(b!=1 and b!=0):
        for steps in range (2,b):
            if(b%steps==0):
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            print("%d"%b)
        p=int(p/10)