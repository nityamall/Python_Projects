n=input("Enter a no.")
n=int(n)
s=0
for i in range (1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("Perfect no.")
else:
    print("Not a perfect no.")