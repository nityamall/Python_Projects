n=input("ENTER YOUR TRANSACTION")
n=int (n)
s=0
b=0
v=0
l=0
c=0
i=0
r=0
k=0
j=0
a=0
s=n/2000
n=n%2000
print("2000 = %d"%s)
b=n/500
n=n%500
print("500 = %d"%b)
v=n/100
n=n%100
print("100 = %d"%v)
l=n/50
n=n%50
print("50 = %d"%l)
c=n/20
n=n%20
print("20 = %d"%c)
i=n/10
n=n%10
print("10 = %d"%i)
r=n/5
n=n%5
print("5 = %d"%r)
k=n/2
n=n%2
print("2 = %d"%k)
j=n/1
print("1 = %d"%j)
a=s+b+v+l+c+i+r+k+j
print("TOTAL NO. OF NOTES WITHDRAWN = %d"%a)







