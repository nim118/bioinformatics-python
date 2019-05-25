# Problem Url : http://rosalind.info/problems/ins/
def insertionSort(arr, n):
	count = 0
 	for i in xrange(1,n):
 		print arr[i-1] + "-" + arr[i]
 		k = i
 		while int(arr[k-1]) > int(arr[k]) and k >= 1:
 			temp = arr[k-1]
 			arr[k-1] = arr[k]
 			arr[k] = temp
 			count = count + 1
 			k = k-1
 		print arr

 	print arr
 	print count	





f = open("insertion_sort.txt", "r")
fdata = f.readlines()

n = fdata[0].strip()
numbers = fdata[1].strip()

numbers = numbers.split(" ")
print numbers
insertionSort(numbers, int(n))