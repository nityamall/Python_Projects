range1=input("Input the lower range ")
range2=input("Input the higher range")
range1=int(range1)
range2=int(range2)
print ("NOS. DIVISIDLE BY 7 :")
for i in range (range1,range2+1):
    if (i%7==0):
        print("%d"%i)
print ("NOS. NOT DIVISIBLE BY 7 :")
for i in range (range1,range2+1):
    if (i%7!= 0):
        print ("%d"%i)      



