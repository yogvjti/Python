class Arithmetic:
    Value = 0

    def __init__(self,Value1,Value2):
        self.i = Value1
        self.j = Value2

    def Accept(self):
        print("Accepted Numbers:",self.i,self.j)

    def Addition(self):
        print("Addition is:",self.i + self.j)

    def Subtraction(self):
        print("Sub is:",self.i - self.j)

    def Multiplication(self):
        print("Multi is:",self.i * self.j)

    def Division(self):
        print("Div is:", self.i / self.j)

def main():

    obj1 = Arithmetic(200,50);
    obj1.Accept();
    obj1.Addition();
    obj1.Subtraction();
    obj1.Multiplication();
    obj1.Division();

if __name__=="__main__":
    main()