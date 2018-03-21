n=input("Enter a no.")
n=int(n)
b=0
s=0
h=n
while n>0:
    b=n%10
    s=s*10+b
    n=int(n/10)
for i in range (2,h):
    flag=1
    if(h%i==0):
        flag=0
        break
    else:
        flag=1
if (h==s and flag==1):
    print("PRIME PALINDROME")
else:
    print("NOT A PRIME PALINDROME NO.")