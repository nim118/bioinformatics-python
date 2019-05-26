#Problem Url : http://rosalind.info/problems/mer/
f = open("merge_sorted_arrays_data.txt", "r")
fdata = f.readlines()

array_1_length = fdata.pop(0)
array_1 = fdata.pop(0).split(' ')
array_2_length = fdata.pop(0)
array_2 = fdata.pop(0).split(' ')

sorted_array = []

array_1 = [int(numeric_string) for numeric_string in array_1]
array_2 = [int(numeric_string) for numeric_string in array_2]

while (len(array_1) >= 1 and len(array_2) >= 1) :
	if(int(array_1[0]) > int(array_2[0])):
		sorted_array.append(int(array_2.pop(0)))
	else : 
		sorted_array.append(int(array_1.pop(0)))

if(len(array_1) >= 1):
	sorted_array += array_1
else :
	sorted_array += array_2

print " ".join(str(e) for e in sorted_array)