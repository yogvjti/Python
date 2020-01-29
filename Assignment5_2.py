i = 1
def yog():
    global i
    if(i<=5):
        print(i,end="  ")
        i+=1
        yog()
yog()
