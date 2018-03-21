for steps in range(40,70):
    flag=1
    for steps1 in range(2,steps):
        if((steps%steps1)==0):
            flag=0
            break
    if (flag==1):
        print("%d "%steps)