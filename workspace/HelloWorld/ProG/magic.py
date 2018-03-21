m=input("Enter a no.")
m=int(m)
b=0
s=0
while m>9:
    while m>0:
        b=m%10
        s=s+b
        m=int(m/10)
    p=s
    m=s
    s=0
if (p==1):
    print("Magic no")
else:
    print("NOT A MAGIC NO. SORRY! ")

    