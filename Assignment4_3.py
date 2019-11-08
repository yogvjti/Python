def chknum(no):
    return(no>=70 and no<=90)

def mod(n):
    return(n+10)

def sum(a,b):
    return a*b

Arr = [4,34,36,76,68,24,89,23,86,90,45,70]
print("List is",Arr)

Brr = list(filter(chknum,Arr))
print("Data after Filter is",Brr)

Crr = list(map(mod,Brr))
print("Data after Map is",Crr)

import functools
ans = functools.reduce(sum,Crr)
print("Final Answer is",ans)

print("----End----")

Arr = [4,34,36,76,68,24,89,23,86,90,45,70]
print("List is",Arr)

brr= list(filter(lambda no:(no>=70 and no<=90),Arr))
print("Data After Filter is",brr)

crr = list(map(lambda n:(n+10),brr))
print("Data After Map",crr)

import functools
Ans = functools.reduce(lambda a,b:(a*b),crr)
print("Final Answer is",Ans)