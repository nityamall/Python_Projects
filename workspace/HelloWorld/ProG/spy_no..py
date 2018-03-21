n=input("ENTER A NO.")
n=int(n)
b=0
s=0
j=1
while n>0:
   b=n%10
   s=s+b
   j=j*b
   n=int(n/10)
if(s==j):
    print("SPY NO.")
else:
    print("NOT A SPY NO.")

