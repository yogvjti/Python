def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
a = 5
print("No:",a)
print("Factorial:",factorial(a))