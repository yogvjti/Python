print("||Shri Swami samarth||")
print("** Welcome to Yogesh Programmig World **")

College = "VJTI, Mumbai"
print(College)
print(type(College))
print(id(College))

College = 'VJTI, Mumbaip'
print(College)
print(type(College))
print(id(College))

print("First Term",College[0])
print("Last Term",College[-1])

print(College[0::2])
print(College[-1::-1])
print(College[:3])

print(College[1:])
print(College[:-1])



print(len(College))

name = "  Veermata Jijabai Technological Institute  "
print(name.strip())  # strip removes extra spaces

Sub = "FEA,SOM,Thermodynamics,FM,HT"
print(Sub.split(','))
