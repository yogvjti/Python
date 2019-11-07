print("|| Shri Swami Samarth ||")
print("** Wel-come to Yogesh Programming World **")

print("Position arguments")

def stud(name,no):
    print("Student Name is",name)
    print("Student Roll no is",no)
print("Sudent Information")

stud('Kiran',1)
stud('Yogesh',2)
stud('Aarav',3)
stud('21',4)
print("----end----")

print("Keyword arguments")
def stud(name,dob):
    print("student name is",name)
    print("student DoB is",dob)
print("Student Information")

stud(dob = 8, name = "Savita")
stud(name = 'Roshni', dob = 17)
print("----end----")

print("default arguments")
def stud(Surname,id=100):
    print("Surname is",Surname)
    print("ID is", id)
print("Details")

stud("Pakhale",101)
stud(id=102, Surname="Chaudhhari")
stud(Surname="Gahiwal")
stud("Patil")
print('-----END-----')

print("varible no of arguments")

def Sub(*no):
    ans = 0
    for i in no:
        ans = ans - i
    return ans

ret = Sub(10,20,30,40,50)
print("Subtraction is",ret)

ret = Sub(25,30,35,40)
print("Addition is",ret)

print("-----END-----")

print("Keyword Variable number of arguments")
def StudentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

#StudentInfo(age=28, address=“Sinhagad Road”, mobile=7588945488, company="Marvellous")

