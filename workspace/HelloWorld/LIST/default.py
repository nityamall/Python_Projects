def gender(sex='unknown'):
    if sex=='m':
        print("male")
    elif sex=='f':
        print("female")
    print(sex)

    

n=10325
def nitya():
    print(n)

def nitya2():
    print(n)
nitya()
nitya2()


def church(name='Bucky',action='eat',article='the',item='pizza'):
    print(name,action,item)
church(action='play',name='Nitya',item='tennis')


def add(*rex):
    tot=0
    for a in rex:
        tot+=a
    print(tot)
add(4,5,12,15,17,90,998,776,564,678)
        
        