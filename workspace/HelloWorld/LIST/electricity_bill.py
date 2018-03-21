n=""
units=0
bill=0.0
n=input("ENTER THE NAME OF THE CUSTOMER")
units=input("ENTER THE UNITS CONSUMED")
units=int(units)
if(units<=100):
    bill=2*units
elif(units<=300):
    bill=100*2+(units-100)*3
elif(units>300):
    bill=100*2+200*3+(units-300)*5
    bill=bill+2.5/100*bill
print(n)
print("units consumed :- %d"%units)
print ("total amt :- %f"%bill)