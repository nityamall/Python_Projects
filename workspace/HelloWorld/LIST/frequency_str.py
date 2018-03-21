n=input("ENTER THE STRING").upper()
l=len(n)
c=0
for i in range(65,90+1):
    for j in range (l):
        if(i==ord (n[j])):
            c=c+1
    if c>0:
        print(chr(i)+" = %d"%c)
    c=0