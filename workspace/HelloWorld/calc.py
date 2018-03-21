n=1
def calculator ():
    s=0
    print("ENTER 1 TO ADD")
    print("ENTER 2 TO SUB")
    print("ENTER 3 TO MUL")
    print("ENTER 4 TO DIV")
    print("ENTER 0 TO EXIT")
    c1=input("ENTER YOUR CHOICE")
    c1=int(c1)
    if (c1>=1 and c1<=4):
        a=input("ENTER THE 1ST NO.")
        b=input("ENTER THE 2ND NO.")
        a=float(a)
        b=float(b)
        if (c1==0):
            exit(0)
        elif(c1==1):
            s=a+b
        elif(c1==2):
            s=a-b
        elif(c1==3):
            s=a*b
        else:
            s=a/b
        print("%f" % s)
    else:
        print("WRONG CHOICE !")
while (n !=0):
    calculator()