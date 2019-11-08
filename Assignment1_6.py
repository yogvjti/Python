n = int(input("Enter any No:"))

if (n>0):
	print("Positive")

elif (n<0):
	print("Negative")

else:
	print("Zero")

print("------")

def yog1(n):
	#print("Inside yog1")
	print("Accepted value",n)
	if(n>0):
		print("Positive")
	elif(n<0):
		print("Negative")
	else:
		print("Zero")

n= 0
yog1(n)
ret = yog1(n)
print("Return Value",ret)

print("-----END-----")

def yog1(n):
	print("Accepted no",n)
	if(n>0):
		print("No is Positive")
	elif(n<0):
		print("No is Negative")
	else:
		print("No is Zero")

n= 10
yog1(n)
n=- 21
yog1(n)
n= 0
yog1(n)

print("--------")

