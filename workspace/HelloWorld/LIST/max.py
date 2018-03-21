n=input("ENTER A NO.")
n=int(n)
b=0
max2=-99999
min2=99999
while n>0:
    b=n%10
    n=int(n/10)
    if(b>max2):
        max2=b
    if(b<min2):
        min2=b
print("%d"%max2)
print("%d"%min2)