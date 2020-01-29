def up_rec(n):
    if n==5:
        print(n,end=" ")
    else:
        print(n,end=" ")
        up_rec(n+1)
print("Output:")
up_rec(1)