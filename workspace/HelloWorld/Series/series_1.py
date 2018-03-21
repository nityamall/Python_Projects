n=input("ENTER THE LIMIT")
n=int(n)
s=0
p=0
o=0
for i in range (1,n+1):
   s=i*(i-1)
   p=i+(i+i)
   o=s/p
   print("%f"%o,end=" ")
