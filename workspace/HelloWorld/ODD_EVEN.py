low=input("Input the lower range")
high=input("Input the higher range")
low=int(low)
high=int(high)
print(" EVEN : ")
for i in range (low,high+1):
    if (i%2==0):
        print ("%d"%i)
print ("ODD : ")
for i in range (low,high+1):
    if (i%2==1):
        print ("%d"%i)