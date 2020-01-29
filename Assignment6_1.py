class Demo:
    Value = 50
    def __init__(self,no1,no2):
        self.i= no1
        self.j= no2

    def fun(self):
        print(self.i,self.j)

    def gun(self):
        print(self.i,self.j)


def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    print("Fun:")
    obj1.fun()
    obj2.fun()

    print("Gun:")
    obj1.gun()
    obj2.gun()

    print("Done!")
if __name__=="__main__":
    main()
