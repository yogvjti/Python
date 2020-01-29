def fact(n):
	if(n==0):
		return 1
	return n*fact(n-1)
val = int(input("Enter n: "))
ret = fact(val)
print("Factorial is:",ret)

print("---------OR----------")

def fact(no):
    if(no==0):
        return 1
    return no*fact(no-1)
value = 5
ret = fact(value)
print("Factorial of {} is {}".format(value,ret))
