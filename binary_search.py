f = open("rosalind_bins.txt", "r")

file_data = f.readlines()

data_array_length = file_data[0].strip()

search_array_length = file_data[1].strip()

data_array = file_data[2].strip()
data_array = data_array.split(' ')

search_array = file_data[3].strip()
search_array = search_array.split(' ')

def binary_search(A, n, T):
	l = 0
	r = n - 1
	found = -1

	while l <= r:
		m = (l + r) / 2
		if int(A[m]) < T:
			l = m + 1
		elif int(A[m]) > T:
			r = m - 1
		else:  
			found = m + 1
			break

	return found

temp = ""
for search_variable in search_array:
	temp = temp + " " + str(binary_search(data_array, int(data_array_length), int(search_variable)))

print temp
