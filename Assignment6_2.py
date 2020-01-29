class Circle:
    PI = 3.14;

    def __init__(self,radius):
        self.R = radius

    def Accept(self):
        print(self.R)
        #print("Radius is:"self.R)

    def area(self):
        print(self.R**2*3.14)

    def circum(self):
        print(2*self.R*3.14)

    @classmethod
    def DisplayPI(cls):
        print(cls.PI)

#obj = Circle(3)

R = int(input("Enter radius of circle: "))
obj = Circle(R)

print("Radius is:")
obj.Accept()

print("Area is:")
obj.area()

print("Circumference is: ")
obj.circum()

print("Value of PI: ")
obj.DisplayPI()


print("-----------------------------")

class Circle:
    PI = 3.14;

    def __init__(self,radius):
        self.R = radius

    def Accept(self):
        print("Radius is: ",self.R)
        print(self.R)

    def area(self):
        print("Area is: ",self.R**2*3.14)

    def circum(self):
        print("Circumference is: ",2*self.R*3.14)

    @classmethod
    def DisplayPI(cls):
        print("Value of PI:",cls.PI)

def main():

    Newcircle = Circle(3)
    print(Newcircle.Accept())
    print(Newcircle.area())
    print(Newcircle.circum())
    print(Newcircle.DisplayPI())

    print("Done!")

if __name__=="__main__":
    main()