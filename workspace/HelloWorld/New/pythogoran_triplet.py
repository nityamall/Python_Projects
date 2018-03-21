n=input("ENTER THE RANGE")
n=int(n)
for i in range (1,n+1):
    for j in range (2,n+1):
        if(j<i):
            a=i*i-j*j
        else:
            a=j*j-i*i
        b=2*j*i
        c=j*j+i*i
        if(c>20):
            break
        if(a==0 or b==0 or c==0):
            break
        if((a*a)+(b*b)==(c*c)):
            print(a,b,c)

