
def prime(num):
    for i in range(2,num):
        return(num % i != 0)
def mod(n):
    return (n*2)

def Ans(a,b):
    return (a>b)

Arr = [2,70,11,10,17,23,31,77]
print("Arr",Arr)

Brr = list(filter(prime,Arr))
print("Data after filter: ",Brr)

crr = list(map(mod,Brr))
print("Data after Map:",crr)

import functools
Ans = functools.reduce(Ans,crr)
print("Maximum No is",Ans)