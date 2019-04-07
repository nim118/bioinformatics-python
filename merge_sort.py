# Python program for implementation of MergeSort
def mergeSort(arr):
	if (len(arr)) > 1:
		mid = len(arr)//2 #Finding the mid of the array
		L = arr[:mid]
		R = arr[mid:]

		#print L
		#print R
		mergeSort(L) #sorting the first half
		mergeSort(R) #sorting the second half

		i = j = k = 0

		# copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		#checking if any element is left
		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1
		print arr
			



arr = [20,19,35,-18,17,-20,20,1,4,4]

mergeSort(arr)

print arr