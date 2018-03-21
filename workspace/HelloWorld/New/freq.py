n=input("ENTER A STRING")
k=input("ENTER A LETTER")
l=len(n)
c=0
for i in range(0,l):
    if (n[i]==k):
        c=c+1
print("%d"%c)
