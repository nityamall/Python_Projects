n=input("Enter a no.")
n=int(n)
b=0
sum=0
while n>0:
    b=n%10
    sum=sum+b
    n=int(n/10)
print ("%d"%sum)
    