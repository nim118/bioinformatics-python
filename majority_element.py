def findMajorityElement(arr):
	n = len(arr)
	maxCount = 0
	index = -1
	for i in range(n):
		count = 0
		for j in range(n):
			if(arr[i] == arr[j]):
				count += 1

		if (count > maxCount):
			maxCount = count
			index = i

	if (maxCount > n//2):
		return (arr[index])
	else :
		return -1
	





f = open("rosalind_maj.txt", "r")
fdata = f.readlines()
fdata.pop(0)
majority_elements = []

for line in fdata:
	numbers = line.strip()
	numbers = numbers.split(" ")
	majority_element = findMajorityElement(numbers)
	majority_elements.append(majority_element)

print (' ').join(str(e) for e in majority_elements)
	
exit();
