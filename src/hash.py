import math

n = input("Enter string to hash\n")
num_array = []


for i in range(0, len(n)):
	if n[i] == " ":
		num_array.append(129)
	else:
		num_array.append(ord(n[i]))

def pHash_1(c_array):
	h = 0
	for i in range(0, len(c_array)):
		h = h + math.log(c_array[i])
	h1 = int((h + math.log(len(c_array))/len(c_array)+1) * 1000000000000000)
	pHash_2(h1)

def pHash_2(hash_1):
	h1_split = list(str(hash_1))
	h2 = 0
	for i in range(0, len(h1_split)):
		if int(h1_split[i]) == 0:
			h2 += 0
		else:
			h2 += math.log(int(h1_split[i]))
	print("Hash value is " + str(int(h2 * 100000000000000)))
	
pHash_1(num_array)
	

