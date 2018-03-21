n=input("Enter a no.")
n=int(n)
b=0
c=0
while n > 0 :
    b=n%10
    c=c+1
    n=int(n/10)
print("%d"%c)