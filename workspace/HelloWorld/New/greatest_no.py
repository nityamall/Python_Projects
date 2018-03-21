n=input("ENTER A NO.")
n=int(n)
g=[]
max=0
while n>0:
    b=n%10
    g.append(b)
    n=int(n/10)
l=len(g)
for i in range (0,l):
    if(g[i]>max):
        max=g[i]
print("%d max:-"%max)


