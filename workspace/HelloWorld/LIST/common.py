def cd (list1,list2):
    res='false'
    for i in list1:
        for j in list2:
            if (i==j):
                res='true'
                return res
    return res 
print(cd([5,6,7,8],[3,4,9,10]))