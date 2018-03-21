no=input("Fav no. -->")
no1=input("Worst no. -->")
no=int(no)
no1=int(no1)
a=5
if no==3 or no1==4:
    s=a+no-no1
elif no>3 or no1==5:
    s=a*no
elif no==0:
    s=100
else:
    s=a-no+no1
print("Result --> %d"%s)