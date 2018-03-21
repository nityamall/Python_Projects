n=input("ENTER THE NO OF LINES ")
n=int(n)
l=65
for i in range (1,n+1):
    o=l
    for j in range (1,i+1):
        k=chr(o)
        print(k ,end=" ")
        o=o+1
    l=l+1
    print()
