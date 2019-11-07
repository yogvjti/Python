print("|| Shri Swami Samarth ||")
print("** Welcome to Yogesh Programming **")

# Function which accepts nothing and return nothing 
def yog():
	print("Inside yog")

# Function which accepts value and return nothing
def yog1(value):
	print("Inside yog1")
	print("Accepted value",value)

# Function which accepts value and return value
def yog2(value):
	print("Inside yog2")
	print("Accepted value is",value)
	return value+1

# Function which accepts multiple values and return multiple values
def yog3(v1,v2):
	print("Inside yog3")
	add = v1 + v2
	sub = v1 - v2
	return add, sub

# Function which calls another function which is defined outside it
def yog4():
	print("Inside yog4")
	yog()

# Function which contains another nested function defined in it
def yog5():
	print("Inside yog5")
	def innerfun():
		print("Inside inner fun")
	innerfun()

# Function calls for above functions
n= 21
yog()
yog1(n)
ret = yog2(n)
print("Return Value",ret)

yog4()

ret1,ret2 = yog3(10,4)
print("Addition is",ret1)
print("Subtraction is",ret2)




