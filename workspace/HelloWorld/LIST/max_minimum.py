n=input("Enter the no. of numbers u want to enter")
n=int(n)
g=[]
for i in range (n):
    d=input("Enter the no.")
    d=int(d)
    g.append(d)
max1=-99999999
min1=99999999
for i in range (n):
    if(g[i]>max1):
        max1=g[i]
    if(g[i]<min1):
        min1=g[i]
print("Maximum no.--> %d"%max1)
print("Minimum no.--> %d"%min1)