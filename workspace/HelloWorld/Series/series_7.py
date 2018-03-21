n=input("ENTER THE RANGE")
n=int(n)
l=n
k=0
h=0
for i in range (1,n+1):
    k=l-i
    h = h + k
    l=l-1
print("%d"%h)