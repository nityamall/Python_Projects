import math
n=input("Enter a no.")
n=int(n)
b=0
s=0
while n>9:
    while n>0:
        b=n%10
        s=s+math.pow(b,2)
        n=int(n/10)
    n=s
    p=s
    s=0
if(p==1):
    print("IT IS A HAPPY NO.")
else:
    print("IT IS NOT A HAPPY NO.")