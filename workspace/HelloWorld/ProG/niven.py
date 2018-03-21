n=input("ENTER A NO.")
n=int(n)
l=n
s=0
while n>0:
    b=n%10
    s=b+s
    n=int(n/10)
if (l%s==0):
    print("niven")
else:
    print("not niven")
