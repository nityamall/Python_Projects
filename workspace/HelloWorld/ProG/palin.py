n=input("Enter a no.")
n=int(n)
z=n
b=0
s=0
while n>0:
    b=n%10
    s=s*10+b
    n=int(n/10)
if (z==s):
    print ("Palindrome")
else:
    print ("Not palindrome")