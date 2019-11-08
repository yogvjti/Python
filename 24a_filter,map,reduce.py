print("|| Shri Swami Samarth ||")
print("** Wel-come to Yogesh Programming World **")

#24b
print("----by normal functions----")
def Evenchk(no):
	return(no%2==0)

def Increase(n):
	return n+3

def ans(a,b):
	return a+b

arr = [8,17,20,21,94,92,93,16]
print("arr",arr)

brr = list(filter(Evenchk,arr))
print("Data after filter",brr)

crr = list(map(Increase,brr))
print("Data after map",crr)

import functools
ans = functools.reduce(ans,crr)
print("final answer",ans)

print("----by lambda functions----")

arr = [8,17,20,21,94,92,93,16]
print("arr",arr)

even = list(filter(lambda no:no%2==0,arr))
print("Data after Filter:",even)

modify = list(map(lambda n: n+5, even))
print("Data after Map:",modify)

import functools
ans = functools.reduce(lambda a,b:(a+b),modify)
print("Final Answer is:",ans)
