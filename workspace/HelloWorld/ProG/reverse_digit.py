n=input("Enter a no.")
n=int(n)
b=0
s=0
while n>0:
    b=n%10
    s=s*10+b
    n=int(n/10)
print ("%d"%s)
