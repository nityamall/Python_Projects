n=input("ENTER THR STRING").upper()
k=input("ENTER THE WORD YOU ARE FINDING").upper()
n=n+' '
l=len(n)
g=[]
c=0
flag=0
for i in range (l):
    while(ord(n[i])!=32 and c<=l):
        g[c]=n[i]
        c=c+1
        if(n[i]==' '):
            break
    if(list(k)==list(g)):
        print("Found")
        flag=1
        break
    g=[]
    c=0
if(flag==0):
    print("Not Found")

        