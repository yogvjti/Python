import threading

def Even(no):
    print("")
    print("Even list:")
    for num in range(no):
        # checking condition
        if (num % 2 ==0):

            print(num, end=" ")
            #print(" ")

def Odd(no):
    print("")
    print("Odd list:")
    for num in range(no):
        # checking condition
        if (num % 2 != 0):

            print(num, end=" ")
            #print(" ")

if __name__=="__main__":
    print("Input list:")
    no = 20
    for num in range(1,no+1):
        print(num, end="  ")
        #print(" ")
    #start = int(input("Enter the start of range: "))
    #end = int(input("Enter the end of range: "))

    #print("Even List:")

    t1 = threading.Thread(target=Even,args=(no,))
    t2 = threading.Thread(target=Odd,args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("")
    print("Done!")







