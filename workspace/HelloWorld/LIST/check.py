n=input("NO. OF NAMES")
n=int(n)
g=[]
for i in range(n):
    k=input("Enter the name")
    g.append(k)
g.sort()
for j in range(n):
    print(g[j])