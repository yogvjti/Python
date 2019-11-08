print("|| Shri Swami Samrth ||")
print("** Wel-come to Yogesh Programming World **")

from functools import *

def AcceptData():
	size = int(input("Enter No of Elements:"))
	arr = list()
	print("Enter Elements")
	for i in range(0,size,1):
		print("Enter no:", i+1)
		no = int(input())
		arr.append(no)
	return arr

def main():
	RawData = AcceptData()
	print("Accepted data is:",RawData)
	print(RawData)

	FilterData = list(filter(lambda no:(not(no%2)),RawData))
	print("Filtered Data is:",FilterData)
	print(FilterData)


	ModifyData = list(map(lambda no:(no+2),FilterData))
	print("Modified Data is:",ModifyData)
	print(ModifyData)

	if(len(ModifyData)>0):
		result = reduce(lambda n1,n2:(n1+n2),ModifyData)
		print("Final Result is",result)
	else:
		print("No Result")

if __name__=="__main__":
	main()