print("|| Shri Swami samarth ||")
print("** Wel-come to Yogesh Programming World **")

print('----By Normal Function----')

def EvenChk(no):
    return(no%2==0)

def Increase(no):
    return(no+10)

def Add(a,b):
    return a+b

arr = [1,2,3,4,5,6,7,8,9]

evenarr = list(filter(EvenChk,arr))
print("Data after Filter is",evenarr)

incr = list(map(Increase,evenarr))
print("Data after Map is",incr)

import functools
ans = functools.reduce(Add,incr)
print("Final Answer is",ans)

print("-----END-----")

def yog(n):
    return(n%5==0)

def kir(m):
    return(m)

def Ans(n1,n2):
    return n1*n2

prr = [5,7,18,20,25,35,46]

qrr = list(filter(yog,prr))
print("No divisible by 5 is",qrr)

rrr = list(map(kir,qrr))
print("Divisible no",rrr)

import functools
ans = functools.reduce(Ans,rrr)
print("Final answer is",ans)

print("-----By Lambda function-----")

pqr = [1,2,3,4,5,6,7,8]
Even = list(filter(lambda no:(no%2==0),pqr))
print("After filter",Even)

Modify = list(map(lambda n:(n+5),Even))
print("After map",Modify)

import functools
Ans = functools.reduce(lambda a,b:(a+b),Modify)
print("Final Answer",Ans)
