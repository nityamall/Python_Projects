n=input("ENTER THE NO OF INPUTS")
n=int(n)
f=[]
for i in range (0,n):
    g=input("ENTER THE NO.")
    g=int(g)
    f.append(g)

for i in range (1,n):
    temp=f[i]
    j=i-1
    while (j>=0) and (f[j]>temp):
        f[j+1]=f[j]
        j=j-1
    f[j+1]=temp
print(f)




