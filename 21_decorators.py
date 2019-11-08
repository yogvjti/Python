print("|| Shri Swami Samarth ||")
print("** Wel-come to Yogesh Programming World  **")

def sub(a,b):
    print(a-b)
sub(2,7)

def Smartsub(fptr):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fptr(a,b)
    return inner
sub = Smartsub(sub)

print("Subtraction of 7 & 2 is")
sub(7,2)
print("Subtraction of 2 & 7 is")
sub(2,7)

print("-----END-----")

def Mul(n1,n2):
    print(n1*n2)
Mul(-7,2)

def Multiplication(fptr):
    def inner(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return fptr(n1,n2)
    return inner

Mul = Multiplication(Mul)

print("Multiplication is")
Mul(-7,2)




