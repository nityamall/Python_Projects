n=input("ENTER A WORD")
l=len(n)
l=int(l)
if (n[0]==n[l-1]):
    print("special word")
else:
    print("not a special word")