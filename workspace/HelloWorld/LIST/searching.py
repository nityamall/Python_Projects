n=input("ENTER THE NO. OF NAMES")
n=int(n)
g=[]
flag=0
for i in range (n):
    x=input("ENTER THE NAME")
    g.append(x)
k=input("ENTER THE NAME THAT YOU ARE FINDING FOR")
for i in range (n):
    if(g[i]==k):
        flag=1 
        break       
if (flag==1):
    print ("Search successful !!!")
else:
    print ("Search not successful !!!")