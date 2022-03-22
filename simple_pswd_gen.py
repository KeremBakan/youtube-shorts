import random
arr = []
for i in range(16):
	letter = chr(random.randrange(33, 122))
	arr.append(letter)
	#print(arr[i])
print(''.join(arr))