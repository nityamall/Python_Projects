y=input("ENTER A YR")
y=int(y)
if(y%4==0 and y%100!=0):
    print("A LEAP YR")
elif(y%100==0):
    print("NOT A LEAP YEAR")
elif(y%400==0):
    print("A LEAP YR")
else:
    print("NOT A LEAP YEAR")