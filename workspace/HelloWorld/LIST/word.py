def word (list1,n):
    list1=list1+" "
    str1=list1.split(" ")
    g=[]
    for i in str1:
        if len(i)>n:
            g.append(i)
    return g
list2=input("ENTER THE STRING\n")
m=input("ENTER THE NO.->")
m=int(m)
h=word (list2 ,m)
print(h) 