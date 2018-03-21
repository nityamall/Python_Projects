sc=input("Enter your total charge")
sc=int(sc)
if sc<50:
    sc=sc+10
else:
    print("shipping free")
print("%d"%sc)