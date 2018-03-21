n=("ENTER A NO.")
n=int(n)
b=0
s=0
f=n
c=0
k=0
h=n*n
while n>0:
    b=n%10
    s=s*10+b
    n=int(n/10)
if(s==n):
    print("PALINDROME NO.")
else:
    while h>0:
        c=h%10
        k=c+k
        h=int(h/10)
    if (f==k):
        print("KAPREKAR NO.")
    else:
        print("THE NO IS NOT A KAPREKAR NO AS WELL AS NOT A PALINDROME NO")
    
    
    
