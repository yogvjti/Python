def digitAdd(num):
    sum = 0
    while(num>0):
        d = num%10
        num = num//10
        sum = sum + d
    return(sum)
a = 5012
print("No:",a)
print("Output:",digitAdd(a))