c=0
def input1 ():
    n=input ("ENTER THE COSTUMER NAME ")
    m=input("ENTER THE COSTUMER NO.")
    e=input("ENTER THE ELECTRICITY UNITS ")
    e=int(e)
    return show(n,m,e)
def show(n,m,e):
     return billcalculate(e)
def billcalculate (u):
    if (u<100):
        c=100*1.20
    elif(u<300):
        c=(100*1.20)+((u-100)*2)
    elif(u>300):
        c=(100*1.20)+((u-100)*2)+((u-300)*3)
    return c
def display(c):
    print("Total bill is --> %f"%c)

input1()
show()
t=billcalculate()
display(t)