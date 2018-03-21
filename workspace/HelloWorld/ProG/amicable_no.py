n=input("Enter the 1st no.")
m=input("Enter the 2nd no.")
n=int(n)
m=int(m)
s=0
k=0
for i in range (1,n):
    if(n%i==0):
        s=s+i
for j in range (1,m):
    if(m%j==0):
        k=k+j
if(k==n and s==m):
    print("AMICABLE NO.")
else :
    print("NOT AMICABLE")

        
