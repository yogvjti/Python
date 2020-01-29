def down_rec(n):
    if n==1:
        print(n,end=" ")
    else:
        print(n,end=" ")
        down_rec(n-1)
print("Output:")
down_rec(5)