n=input("ENTER A WORD")
l=len(n)
h=l-1
flag=0
for i in range (0,l):
    if(n[i]!=n[h]):
        flag=1
        break
    h=h-1
if(flag==0):
    print("palindrome")
else:
    print("not a palindrome word")
