x=input("Enter the no of lines :> ")
x=int(x)
k = x+(x-2)
for i in range(0, x):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()