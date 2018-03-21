j=1
while j>0: 
    n=input("Enter a no.")
    n=int(n)
    b=0
    f=0
    m=0
    h=n
    while n>0:
        b=n%10
        f=b*b*b
        m=m+f
        n=int(n/10)
    if (m==h):
        print ("armstrong no.")
    else:
        print ("not an armstrong no.")