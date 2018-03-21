n=input("Enter 1st no.")
m=input("Enter 2nd no.")
n=int(n)
m=int(m)
for i in range (2,n):
    flag=1
    if(n%i==0):
        flag=0
        break
    else:
        flag=1
for i in range (2,m):
    f=1
    if(m%i==0):
        f=0
        break
    else:
        f=1
if(flag==1 and f==1):
    if(n>m):
        if(n-m==2):
            print("TWIN PRIME")
        else:
            print("NOT TWIN PRIME")
    elif (m>n):
        if(m-n==2):
            print("TWIN PRIME")
        else:
            print("NOT TWIN PRIME")
else:
    print("NOT twin PRIME")