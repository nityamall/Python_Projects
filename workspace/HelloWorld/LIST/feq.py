g="I LOVE CHOCOLATES"
c=0
l=len(g)
for i in range(65,90+1):
    for j in range(l):
        if(i==ord (g[j])):
            c=c+1
    if c>0:
        print(chr(i)+" :%d"%c)
    c=0