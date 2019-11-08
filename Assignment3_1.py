List = []
Arr = int(input("No of Elements in List: "))

for i in range(Arr):
	i = int(input("Enter No: "))
	List.append(i)

print("Sum of Elements in List is: ",sum(List))
