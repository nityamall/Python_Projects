range1=input("Input the lower range")
range2=input("Input the highest range")
range1=int(range1)
range2=int(range2)
for steps in range(range1,range2+1):
    flag=1
    for steps1 in range(2,steps):
        if((steps%steps1)==0):
            flag=0
            break
    if (flag==1):
        print("%d "%steps)