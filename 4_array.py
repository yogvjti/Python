print("||Shri Swami Samarth")
print("** Welcome to Yogesh Programming **")

import array as brr

b = brr.array('f',[1,2,3,4])
print("first term",b[0])
print("second term",b[1])
print("last term",b[-1])
print(b.typecode)

b.reverse()
for i in range(len(b)):
    print(b[i])

