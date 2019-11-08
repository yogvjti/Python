def chknum(no):
    return(no%2==0)

def mod(n):
    return(n**2)

def sum(a,b):
    return a+b

Arr = [5,2,3,4,4,1,2,8,10]
print("List is",Arr)

Brr = list(filter(chknum,Arr))
print("Data after Filter is",Brr)

Crr = list(map(mod,Brr))
print("Data after Map is",Crr)

import functools
ans = functools.reduce(sum,Crr)
print("Final Answer is",ans)

print("----End----")

Arr = [5,2,3,4,4,1,2,8,10]
print("List is",Arr)

brr = list(filter(lambda no:(no%2==0),Arr))
print("Data after Filter is",brr)

crr= list(map(lambda n:(n**2),brr))
print("Data after Map is ",crr)

import functools
Ans = functools.reduce(lambda a,b:(a+b),crr)
print("Final Answer",Ans)