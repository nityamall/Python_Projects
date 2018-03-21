n=[]
m=[]
r=[]
l=input("ENTER THE NO.OF INPUTS ")
l=int(l)
for i in range (0,l):
    b=input("ENTER THE DIGITS")
    b=int(b)
    n.append(b)
for n1 in n :
    print("%d"%n1)
for j in range (0,l):
    h=input("ENTER THE DIGITS")
    h=int(h)
    m.append(h)
for m1 in m:
    print("%d"%m1)
print("RESULT")
for k in range(0,l):
    for s in range(0,l):
        if(n[k]==m[s]):
            r.append(n[k])
for r1 in r:
    print("%d"%r1)








