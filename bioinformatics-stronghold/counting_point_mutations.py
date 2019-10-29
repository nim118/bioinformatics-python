#Problem Url : http://rosalind.info/problems/hamm/
f = open("rosalind_hamm.txt", "r")


file_data = f.readlines()

f.close()


s = file_data[0].strip()
t = file_data[1].strip()


hd = 0
count = 0

for char in s:
	if(char != t[count]):
		hd = hd + 1
	count = count + 1


print hd