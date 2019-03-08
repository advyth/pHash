import math

"""

	pHash level 1:
	
	*Input to this level is the array 'c_array' which contains the ASCII values for the input string. 
	*Take each ASCII value x and add it to log(x) to obtain H.
	*Take log(length(c_array)) and add it to H to obtain Z. Divide Z by length(c_array) then multiply by 10^14 for normalization.
	*The output of this level is h1 which will then be carried over to pHash level 2.

"""

def pHash_1(c_array):
	h = 0
	for i in range(0, len(c_array)):
		h = h + math.log(c_array[i])
	h1 = int((h + math.log(len(c_array))/len(c_array)+1) * 1000000000000000)
	return h1
"""
	
	pHash level 2:
	
	*Input to this level is the value h1, which is obtained after performing pHash level 1.
	*The variable h1_split is obtained by spliting the multidigit integer h1 into an array with a single digit as each element.
	*Now take log of each digit of the array h1_split and add it to a new variable h2.(if the digit is 0, we add 0 to h2 as log(0) is
	undefined.
	*Finally we multiply h2 with 10^13 for normalization.
	*The value obtained is the hash value for the input string.
	
"""

def pHash_2(hash_1):
	h1_split = list(str(hash_1))
	h2 = 0
	for i in range(0, len(h1_split)):
		if int(h1_split[i]) == 0:
			h2 += 0
		else:
			h2 += math.log(int(h1_split[i]))
	return str(int(h2 * 100000000000000))

def hash(n):
	num_array = [] #Initialize array of size x .
	for i in range(0, len(n)): #Obtain ASCII value of each character from the string and append it to the array.
		if n[i] == " ":	#If space is encountered, append 129 which is a default value.
			num_array.append(129)
		else:
			num_array.append(ord(n[i])) #if normal ASCII character, append the value itself.
	return pHash_2(pHash_1(num_array))


	

