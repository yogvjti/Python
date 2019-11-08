print("First no is:")
a = int(input())

print("Second no is:")
b = int(input())

fptr = lambda a,b: (a*b)
ret = fptr(a,b)
print("Final Multiplication is: ",ret)