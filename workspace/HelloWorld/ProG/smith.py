n=input("Enter a no.")
n=int(n)
b=0
s=0
k=0
z=0
c=0
while n>0:
    b=n%10
    s=b+s
    n=int(n/10)
for i in range (2,n):
    if(n%i==0):
        k=k+i
while k>0:
    c=k%10
    z=c+z
    k=int(k/10)
if(z==s):
    print("SMITH NO.")
else :
    print(" NOT A SMITH NO.")