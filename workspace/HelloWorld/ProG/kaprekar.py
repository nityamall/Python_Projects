k=input("Enter a no.")
k=int(k)
b=0
s=0
s=k*k
r=0
while s>0:
    b=s%10
    r=b+r
    s=int (s/10)
if (r==k):
    print("KAPREKAR")
else:
    print("NOT KAPREKAR")

    

