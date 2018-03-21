n=input("ENTER THE LAST TERM")
n=int(n)
p=1
s=0
for i in range(1,n+1):
    for j in range (1,i+1):
        p=p*j
    s=s+p
    p=1
print("%d"%s)



