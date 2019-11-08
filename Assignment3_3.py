List = []
Array = int(input("Enter NO of Elements in List: "))

for i in range(Array):
    i = int(input("Enter No: "))
    List.append(i)

print("Minimum No from List is:",min(List))

