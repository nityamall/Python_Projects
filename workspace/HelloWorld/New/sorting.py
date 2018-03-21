n=input("ENTER A NO.")
n=int(n)
g=[]
while n>0:
    b=n%10
    g.append(b)
    n=int(n/10)
l=len(g)
for i in range(0,l):
    for j in range (0,l-i-1):
        if(g[j]<g[j+1]):
            temp=g[j+1]
            g[j+1]=g[j]
            g[j]=temp
print(g)


