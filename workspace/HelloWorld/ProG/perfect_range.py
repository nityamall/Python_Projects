low=input("Enter the LR ")
high=input("Enter the UR ")
low=int(low)
high=int(high)
s=0
while(low<=high):
    n=low
    if(low>0):
        for i in range (1,low):
            if(low%i==0):
                s=s+i
        if(s==n):
            print("%d"%s)
        low=low+1
    else:
        low=low+1
    s=0