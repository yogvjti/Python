print("|| Shri Swami Samarth ||")
print("** Wel-come to Yogesh Programming World **")

import sys

print("Maximum no of recursive call are {} in python".format(sys.getrecursionlimit()))

# changing recursion limit
sys.setrecursionlimit(1500)

print("Maximum no of recursive call are {} in python".format(sys.getrecursionlimit()))

#recursive function which goes into infinite recursive calls

def fun():
    print("Inaside fun")
    fun()
i = 1

#recursive function which performs recursive calls 10 times

def gun():
    global i
    if (i<10):
        print(i)
        i+=1
        gun()
gun()

def fact(no):
    if(no==0):
        return 1
    return no * fact(no-1)
value = 5
ret = fact(value)
print("Factorial of {} is {}".format(value,ret))

print("------")

x = int(input("Enter no:"))
def fact(n):
    if(n==0):
        return 1
    return n * fact(n-1)
ret = fact(x)
print("Factorial is",ret)
print("Factorial of {} is {}".format(x,ret))