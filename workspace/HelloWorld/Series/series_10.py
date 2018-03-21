n=input ("ENTER THE LIMIT")
v=input ("ENTER A NO.")
n=int(n)
v=int(v)
l=0
for i in range (1,n+1):
    if (i%2==0):
        l=l-(v/i)
    else:
        l=l+(v/i)
print("%d"%l)


