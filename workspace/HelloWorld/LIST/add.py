n=input("ENTER THE NO OF DIGITS")
n=int(n)
g=[]
s=0
for i in range (n):
    v=input("ENTER THE NO. YOU WANT")
    v=int(v)
    g.append(v)
for i in range (n):
    s=g[i]+s
print("%d"%s)