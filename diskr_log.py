import random

def log_per(y: int, a:int, p:int):
    otvet = 'None'
    for i in range(p-1):
        if (y == (a**i)% p):
            otvet = i
            break    
    return otvet
            
def shag(y: int, a:int, p:int):
    otvet = 'None'
    while True:
        m = random.randint(1, int(p/2))
        k = random.randint(1, int(p/2))
        if m*k >p:
            break
    
    for i in range(1,k):
        for j in range(0,m-1):
            print (a**(i*m)%p,"  ",((a**j)*y)%p)
            if (a**(i*m))%p == ((a**j)*y)%p:
                otvet = i*m - j
                break
        if otvet != 'None':
            break
    print("m = ",m,"  k = ", k)
    print("i = ",i,"  j=",j)
    return otvet
        
