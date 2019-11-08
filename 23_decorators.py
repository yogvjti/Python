print("|| Shri Swami Samarth ||")
print("** Wel-come to Yogeh Programming World **")

def sub(no1,no2):
	return (no1-no2)

def Decorator(OriginalFunction):
	def Updator(a,b):
		if(a<b):
			a,b=b,a
		return OriginalFunction(a,b)
	return Updator

newsub = Decorator(sub)

print("Subtraction is",newsub(10,7))
print("Subtraction is",newsub(2,9))
