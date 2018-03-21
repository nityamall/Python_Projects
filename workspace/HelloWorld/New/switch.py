n=input("ENTER A NAME")
print("enter 1 to print complete name")
print("enter 2 to print the initial for the middle name")
print("enter 3 to print the initial for the 1st and the middle name")
print("enter 4 to print the initials for the full name")
print("enter 0 to exit")
c=input("enter your choice")
c=int(c)
if  (c<=4 and c>=0):
    if(c==0):
        exit (0)
    elif (c==1):
        print(n)
    elif (c==2):
        res=""
        n1=n
        g=""
        str1 = n1.split (" ")
        l=len(str1)-1
        for i in range (0,l):
            if(i==1):
                word=str1[i]
                word=word[0].upper()
                g=g+word

        res=res+str1[0]+"."
        res=res+g+"."
        res=res+str1[l]
        print(res)
    if (c==3):
        res = ""
        n1 = n
        g=""
        str1 = n1.split(" ")
        l = len(str1) - 1
        for i in range(0, l):
            word = str1[i]
            word = word[0].upper()
            g = g+word+"."
        res = res + g
        res = res + str1[l]
        print(res)
    elif (c==4):
        res = ""
        n1 = n
        g = ""
        str1 = n1.split(" ")
        l = len(str1)
        for i in range(0, l):
            word = str1[i]
            word = word[0].upper()
            g = g + word + "."
        res = res + g
        print(res)
    else:
        print("wrong choice")