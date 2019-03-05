import math

n = input("Enter string to hash\n")
num_array = []


for i in range(0, len(n)):
	if n[i] == " ":
		num_array.append(129)
	else:
		num_array.append(ord(n[i]))

def pHash(c_array):
	h = 0
	for i in range(0, len(c_array)):
		h = h + math.log(c_array[i])
	print(int((h + math.log(len(c_array))/len(c_array)+1) * 1000000000000000))

pHash(num_array)
	

