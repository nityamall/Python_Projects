n=[]
s=0
max=0
min=999999999999999999999999999
f=input("ENTER THE NO. OF NOS.")
f=int(f)
for i in range (0,f):
    p=input("ENTER THE NO.")
    p=int(p)
    s=s+p
    n.append (p)
print(" sum = %d"%s)
for k in range (0,f):
    if(n[k]<min):
        min = n[k]
    if(n[k]>max):
        max=n[k]
print("the minimum no. is %d"%min)
print("the maximum no. is %d"%max)



